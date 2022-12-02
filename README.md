# Сервис сбора гистограмм 
Сервис подключается к брокеру сообщений rabbitMQ, получает данные в формате protobuf, накапливает их и сохраняет в hadoop хранилище в формате parquet

### Требования
1. Apache Spark https://spark.apache.org/downloads.html
2. Apache Hadoop https://hadoop.apache.org/releases.html


### Компиляция protobuf
```
protoc -I=. --python_out=. format.proto 
```

### Библиотеки
```
pip install pyspark
pip install pika
```

### Параметры конфигурационного файла (histogramm.conf)
**[hdfs]** - Раздел относящийся к hadoop кластеру

**host** - ip адрес или днс имя сервера на котором запущен hadoop

**port** - порт который слушает  hadoop

**file_dir** - директория где будут храниться parquet файлы 

**[rabbitMq]** - Раздел относящийся к брокеру сообщений RabbitMQ

**host** - ip адрес или днс имя сервера на котором запущен RabbitMQ

**port** - порт который слушает RabbitMQ

**queue** - название очереди

**exchange** - название обменника

**[logs]**

**log_parh** - директория для хранения логов 

**log_file_name** - имя файла логов (незабываем выставлять права)


