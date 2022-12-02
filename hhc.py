#!/bin/python
import time
from pandas import array
from pyspark.sql.types import *
from pyspark.sql import SparkSession
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
LevelType["PKTLEN"] = 11
LevelType["L3_SRC"] = 31
LevelType["L3_DST"] = 32
LevelType["L4_SRC"] = 41
LevelType["L4_DST"] = 42


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
spark.sparkContext.setLogLevel('ERROR')   

Globalschema = StructType([
        StructField("timestamp", IntegerType(), True),
        StructField("subagent_id", IntegerType(), True),
        StructField("num_protocol", IntegerType(), True),
        StructField("CountPkt", IntegerType(), True),
        StructField("type_proto", IntegerType(), True),
        StructField("dst_ip", LongType(), True)
    ])
file_dir = f"/{hdfs_file_dir}/"


#***************************************************************************************************************
sc = spark.sparkContext
URI           = sc._gateway.jvm.java.net.URI
Path          = sc._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem    = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration
fs = FileSystem.get(URI("hdfs://"+str(hdfs_host)+":"+str(hdfs_port)), Configuration())


#***************************************************************************************************************
def dataToParquet (data, file_prefix):
    today = date.today()
    print(f"Save data ....")
    cur_date = int(datetime.strptime(today.strftime("%d/%m/%Y"), "%d/%m/%Y").timestamp())
    file_name = file_prefix + str(int(cur_date))

    ts = int(time.time())
    round_hour = int(ts/3600) * 3600
    file_name = file_prefix + str(round_hour)

    rdd = spark.sparkContext.parallelize(data)    
    Data = spark.createDataFrame(rdd, Globalschema)
    try:
        print("Append File")
        Data.write.mode('append').parquet(f"hdfs://{hdfs_host}:{hdfs_port}{file_dir}{file_name}")            
        print(f"INFO: Append to  file  {file_name} block {len(data)}")
        logging.info(f"INFO: Append to  file  {file_name} block {len(data)}")
    except BaseException as e:
        print("Create File", e)
        Data.write.parquet(f"hdfs://{hdfs_host}:{hdfs_port}{file_dir}{file_name}")    
        print(f"INFO: CRATE FILE {file_name}")
        logging.info(f"INFO: CRATE FILE {file_name}")

def disassemblyProto(proto):
    proto_name, proto_data, probe_time, mashine_id,dst_ip_addr = proto
    for i in range(len(proto_data)):
        if proto_data[i] > 0:
            LevelArrayToParquet.append((probe_time,mashine_id,i,proto_data[i],LevelType[proto_name],dst_ip_addr))


#***************************************************************************************************************            
def histogramReciver(ch, method, properties, body):
    start = time.perf_counter()
    pb_data = histogram.HistogramFamily.FromString(body)
    try:    
        ip_address = getattr(pb_data, pb_data.WhichOneof("dst_ip_addr"))
    except:
        ip_address = 0
   
    data_arr =[
        ("PKTLEN",list(pb_data.pck_len), pb_data.probe_time.seconds, pb_data.mashine_id,ip_address),
        ("L4_SRC",list(pb_data.L4_SRC), pb_data.probe_time.seconds, pb_data.mashine_id,ip_address),
        ("L4_DST",list(pb_data.L4_DST), pb_data.probe_time.seconds, pb_data.mashine_id,ip_address),
        ("L3_SRC",list(pb_data.L3_SRC), pb_data.probe_time.seconds, pb_data.mashine_id,ip_address),
        ("L3_DST",list(pb_data.L3_DST), pb_data.probe_time.seconds, pb_data.mashine_id,ip_address)
    ]
    with Pool(6) as p:
        p.map(disassemblyProto, data_arr )    
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)}', len(LevelArrayToParquet)) 
    if len(LevelArrayToParquet) > 100:  
        dataToParquet(LevelArrayToParquet, "level_")
        LevelArrayToParquet[:] = []


#***************************************************************************************************************
if __name__ == "__main__":
    pktLenData_to_save = []
    manager = Manager()
    LevelArrayToParquet = manager.list()

    try:
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(rmq_host,rmq_port,'/',credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
         try:
             channel.exchange_declare(exchange=rmq_queue, exchange_type="fanout", passive=False)
         except:
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
            sys.exit(0)
