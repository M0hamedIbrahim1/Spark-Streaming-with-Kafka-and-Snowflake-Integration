# !pip install confluent_kafka
# !pip install confluent-kafka configparser

from confluent_kafka import Producer, KafkaError
import json

# Kafka broker address
bootstrap_servers = 'pkc-w8nyg.me-central1.gcp.confluent.cloud:9092'
security_protocol = 'SASL_SSL'
sasl_mechanisms = 'PLAIN'
sasl_username = '7PVG3JMXVJM7G6BE'
sasl_password = ''

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'security.protocol': security_protocol,
    'sasl.mechanisms': sasl_mechanisms,
    'sasl.username': sasl_username,
    'sasl.password': sasl_password,
}

# Kafka topic
topic = 'Transactions'
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


for data in json_data:
    json_str = json.dumps(data)
    producer.produce(topic, key=str(data["TransactionNo"]), value=json_str, callback=delivery_report)

producer.flush()

