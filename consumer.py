import sys
from json import loads

# Hack while we wait for https://github.com/dpkp/kafka-python/issues/2412 to be resolved
import six

sys.modules["kafka.vendor.six.moves"] = six.moves

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "events",
    bootstrap_servers=["localhost:19092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="events",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
)

for message in consumer:
    print(f"Received message: {message.value}")
