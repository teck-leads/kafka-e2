from kafka import KafkaProducer
import json
import time
from data import user_details
# pip install kafka-python
def jsonSerializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=jsonSerializer)

if __name__ == "__main__":

    for i in range(100):
        userInfo = user_details()
        print(userInfo)
        producer.send('userInfo', userInfo)
        time.sleep(5)
       
