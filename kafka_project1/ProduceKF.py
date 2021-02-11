from kafka import KafkaProducer
import json
import time
## write message to particular partition



producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for i in range(100):
    res = 'value is {} '.format(i)

    # data = producer.send('userInfo', value=res.encode('utf-8'), partition=1)
    print(res)
    data = producer.send('userInfo', res.encode('utf-8'), partition=1)
    # producer.send('userInfo', res.encode('utf-8'), partition=1)
# print(producer.metrics())
    

    


