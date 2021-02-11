from kafka import KafkaConsumer

from kafka import KafkaAdminClient
import json


if __name__ == "__main__":
    consumer = KafkaConsumer('userInfo', group_id='usergroup1',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')


partition = consumer.partitions_for_topic('userInfo')
print(partition)
        
