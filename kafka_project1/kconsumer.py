from kafka import KafkaConsumer
import json


if __name__ == "__main__":
    consumer = KafkaConsumer('userInfo', group_id='usergroup1',
                             bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest')

    for msg in consumer:
        # print(msg)
        print(json.loads(msg.value))
        
