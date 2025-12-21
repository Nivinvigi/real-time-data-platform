import json
import time
import uuid
import random
from datetime import datetime, timezone

EVENT_TYPES = ["click", "view", "purchase"]
PAGES = ["/", "/products", "/pricing", "/checkout"]
DEVICES = ["mobile", "desktop"]
COUNTRIES = ["DE", "FR", "NL", "IN"]

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
        print(json.dumps(event))
        time.sleep(1)
