from kafka import KafkaAdminClient
from kafka.admin import NewPartitions


admin_client=KafkaAdminClient(bootstrap_servers=['localhost:9092'])

topic_partitions = {'userInfo': NewPartitions(total_count=4)}
admin_client.create_partitions(topic_partitions)

