# Event Sourcing Prototype

A skeleton of an event sourcing system for building prototypes on.

To get Redpanda up:

```bash
docker compose up -d
```

Run the producer:

```bash
python producer.py
```

In another window, run the consumer:

```bash
python consumer.py
```
