from kafka import KafkaConsumer, KafkaProducer

from util.actuator import Actuator
from util.arguments import get_kafka_brokers, get_channel_destinations, get_env_info

print(get_env_info())

Actuator.start(port=8080, info=get_env_info())

consumer = KafkaConsumer('orders', bootstrap_servers=[get_kafka_brokers()],
                         auto_offset_reset='earliest', enable_auto_commit=False)

# consumer = KafkaConsumer(get_channel_destinations('timestamp'), bootstrap_servers=[get_kafka_brokers()],
#                          enable_auto_commit=True, client_id='python-client', max_poll_interval_ms=3000,
#                          request_timeout_ms=4000)

producer = KafkaProducer(bootstrap_servers=[get_kafka_brokers()])


def is_even(value):
    return int(value[-1:]) % 2 == 0


while True:
    for message in consumer:
        # Convert the byte array payload into string
        timestamp = message.value.decode("utf-8")
        print(timestamp)
        if timestamp is not None:
            if is_even(timestamp):
                print(get_channel_destinations('hot.drink')[0])
                futureEven = producer.send('hotDrink', timestamp)
            else:
                print(get_channel_destinations('cold.drink')[0])
                futureOdd = producer.send('coldDrink', timestamp)
