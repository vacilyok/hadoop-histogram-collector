#!/bin/python
import time
from pandas import array
from pyspark.sql.types import *
from pyspark.sql import SparkSession, Row
from array import array
from pb import format_pb2 as histogram
import pika
import os
import datetime
from datetime import date, datetime
import configparser
import sys
from multiprocessing import Pool,Manager,Process
from time import gmtime, strftime
import pytz
import logging
# hadoop fs -rm -R /histogramm/level_1645995600 -- command delete file from hadoop

logging.basicConfig(filename='hhc.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
os.environ["HADOOP_USER_NAME"] = "hadoop"
os.environ["ARROW_LIBHDFS_DIR"] = "/usr/local/hadoop/lib/native"
tz = pytz.timezone('Europe/Moscow')
moscow_now = datetime.now(tz)




LevelType = {}
LevelType["PKTLEN"] = 0
LevelType["L3_SRC"] = 1
LevelType["L3_DST"] = 2
LevelType["L4_SRC"] = 3
LevelType["L4_DST"] = 4


# *******************************************************************************************************
# Read config
# *******************************************************************************************************
dir_path = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
params = config.read(f"{dir_path}/histogramm.conf")
if len(params) == 0:
    logging.error('Error: Not found config file histogramm.conf. Stop programm.')
    sys.exit(0)
hdfs_host = config.get('hdfs','host')
hdfs_port = config.get('hdfs','port')
hdfs_file_dir = config.get('hdfs','file_dir')
rmq_host = config.get('rabbitMq','host')
rmq_port = config.get('rabbitMq','port')
rmq_queue = config.get('rabbitMq','queue')
rmq_exchange = config.get('rabbitMq','exchange')

log_parh = config.get('logs','log_parh')
log_file_name = config.get('logs','log_file_name')

# *******************************************************************************************************
spark = SparkSession.builder\
   .master('spark://10.10.16.15:7077')\
   .appName('Python Spark histogramm collector')\
   .config('spark.executor.memory', '4gb')\
   .config("spark.cores.max", "4")\
   .getOrCreate()
sc = spark.sparkContext

file_dir = f"/{hdfs_file_dir}/"


#***************************************************************************************************************
sc = spark.sparkContext
URI           = sc._gateway.jvm.java.net.URI
Path          = sc._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem    = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration
fs = FileSystem.get(URI("hdfs://"+str(hdfs_host)+":"+str(hdfs_port)), Configuration())


#***************************************************************************************************************
def dataToParquet (data,file_prefix):
    schema = StructType([
        StructField("timestamp", IntegerType(), False),
        StructField("mashine_id", IntegerType(), False),
        StructField("dst_ip", IntegerType(), False),
        StructField("data", ArrayType(IntegerType()), False)
    ])

    today = date.today()
    print(f"Save data ....")
    cur_date = int(datetime.strptime(today.strftime("%d/%m/%Y"), "%d/%m/%Y").timestamp())
    file_name = file_prefix + str(int(cur_date))
    rdd = spark.sparkContext.parallelize(data,numSlices=28) 
    # rdd = spark.sparkContext.parallelize(data) 
    Data = spark.createDataFrame(rdd, schema)   
    try:
        print(f"INFO: Append to  file  {file_name} block {len(data)}")
        Data.write.mode('append').parquet(f"hdfs://{hdfs_host}:{hdfs_port}{file_dir}{file_name}")            
        logging.info(f"INFO: Append to  file  {file_name} block {len(data)}")
    except:
        print(f"INFO: CRATE FILE {file_name}")
        Data.write.parquet(f"hdfs://{hdfs_host}:{hdfs_port}{file_dir}{file_name}")    
        logging.info(f"INFO: CRATE FILE {file_name}")


#***************************************************************************************************************            
def histogramReciver(ch, method, properties, body):
    pb_data = histogram.HistogramFamily.FromString(body)
    try:    
        ip_address = getattr(pb_data, pb_data.WhichOneof("dst_ip_addr"))
    except:
        ip_address = 0
   
    
    pcktlen.append(Row(timestamp=pb_data.probe_time.seconds,mashine_id=pb_data.mashine_id,dst_ip=ip_address,data=list(pb_data.pck_len)))
    l4src.append(Row(timestamp=pb_data.probe_time.seconds,mashine_id=pb_data.mashine_id,dst_ip=ip_address,data=list(pb_data.L4_SRC)))
    l4dst.append(Row(timestamp=pb_data.probe_time.seconds,mashine_id=pb_data.mashine_id,dst_ip=ip_address,data=list(pb_data.L4_DST)))
    l3src.append(Row(timestamp=pb_data.probe_time.seconds,mashine_id=pb_data.mashine_id,dst_ip=ip_address,data=list(pb_data.L3_SRC)))
    l3dst.append(Row(timestamp=pb_data.probe_time.seconds,mashine_id=pb_data.mashine_id,dst_ip=ip_address,data=list(pb_data.L3_DST)))
    
    
    
    if len(pcktlen) > 200:  
        dataToParquet(pcktlen, "pcktlen_")
        dataToParquet(l4src, "l4src_")        
        dataToParquet(l4dst, "l4dst_")
        dataToParquet(l3src, "l3src_")
        dataToParquet(l3dst, "l3dst_")
        pcktlen[:] = []
        l4src[:] = []
        l4dst[:] = []
        l3src[:] = []
        l3dst[:] = []


#***************************************************************************************************************
if __name__ == "__main__":
    
    manager = Manager()
    pcktlen = manager.list()
    l3src = manager.list()
    l3dst = manager.list()
    l4src = manager.list()
    l4dst = manager.list()


    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(rmq_host,rmq_port,'/',credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=rmq_queue, durable=True)
        try:
            channel.queue_bind(exchange=rmq_exchange,queue=rmq_queue)
        except:
            logging.error(f"Error: Exchange with name '{rmq_queue}' not found. Stop programm")

        channel.basic_consume(rmq_queue,histogramReciver, auto_ack=True)
        cur_time = strftime("%Y-%m-%d %H:%M:%S", gmtime() )
        logging.info("Start consuming")
        channel.start_consuming()
    except BaseException as e:
            print(e.args[0])
            logging.error(e.args[0])
            sys.exit(0)
