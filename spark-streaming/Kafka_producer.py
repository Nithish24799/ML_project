#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import requests
from kakfa import KafkaProducer
from time import sleep


# In[ ]:


producer=KafkaProducer(bootstrap_server=["localhost:9092"],
                      value_serializer=lambda x: json.dumps(x).encode("utf-8"))


# In[ ]:


for i in range(50):
    res=requests.get("http://api.open.notify.org/iss-now.json")
    data=json.loads(res.content.decode("utf-8"))
    producer.send("TestTopics",value=data)
    sleep(2)
    producer.flush()

