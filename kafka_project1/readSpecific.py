from kafka import KafkaConsumer
from kafka.structs import TopicPartition


consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest'
                             )

consumer.assign([TopicPartition('userInfo',1)])
print("from readSpecific ")

for msg in consumer:
    print(msg.value.decode('utf-8'))
