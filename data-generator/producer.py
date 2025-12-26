import json
import time
import uuid
import random
from datetime import datetime, timezone
from kafka import KafkaProducer

EVENT_TYPES = ["click", "view", "purchase"]
PAGES = ["/", "/products", "/pricing", "/checkout"]
DEVICES = ["mobile", "desktop"]
COUNTRIES = ["DE", "FR", "NL", "IN"]

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": random.randint(1, 1000),
        "event_type": random.choice(EVENT_TYPES),
        "event_timestamp": datetime.now(timezone.utc).isoformat(),
        "page": random.choice(PAGES),
        "device": random.choice(DEVICES),
        "country": random.choice(COUNTRIES),
    }

if __name__ == "__main__":
    while True:
        event = generate_event()
        producer.send("user-events", event)
        print(f"Sent: {event}")
        time.sleep(1)
