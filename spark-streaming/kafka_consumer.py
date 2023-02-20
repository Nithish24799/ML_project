#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import findspark
findspark.init()
import pymongo
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
import json
import time


# In[ ]:


client = pymongo.MongoClient("<Your DB Connection>")
db = client.International_space_station
col= db.Data


# In[ ]:


if __name__=="__main__":
    spark=SparkSession.builder.master("local".appName("kafka spark demo").getOrCreate())
    sc=spark.SparkContext
    ssc=StreamingContext(sc,20)
    msg=KafkaUtils.createDirectStream(ssc,topics=["TestTopics"],kafkaParams={"metadata.broker.list":"localhost:9092"})
    data=msg.map(lambda x:x[1])
    def functordd(rdd):
        try:
            rdd1=rdd.map(lambda x: json.loads(x))
            df=spark.read.json(rdd1)
            df.CreateOrReplaceTempView("Test")
            df1=spark.sql("slect iss_position.latitude,iss_position.longitude,message,timestap from Test")
            col.insert_one(df1)
        except:
            pass


# In[ ]:


data.ForeachRDD(functordd)
scc.start()
ssc.awaitTermination()

