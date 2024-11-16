import sys
from time import sleep
from json import dumps

# Hack while we wait for https://github.com/dpkp/kafka-python/issues/2412 to be resolved
import six
sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:19092'], value_serializer=lambda v: dumps(v).encode('utf-8'))

for e in range(1000):
    event = {'number': e}
    producer.send("events", value=event)
    print(event)
    sleep(5)
