# A Producer and Consumer With Redpanda in the Middle

A skeleton of an event sourcing system for building prototypes on.

To get Redpanda up:

```bash
docker compose up -d
```

Redpanda console:

<http://localhost:8080/overview>

Run the producer:

```bash
python producer.py
```

In another window, run the consumer:

```bash
python consumer.py
```
