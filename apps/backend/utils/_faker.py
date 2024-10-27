from faker import Faker
import random
from datetime import datetime, timedelta, time

fake = Faker()

def generate_fake_center():
    center_id = fake.name()  # Generate a random UUID for center ID
    date_last_updated = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d %H:%M:%S")  # Convert to string format
    location_lat = float(fake.latitude())  # Generate a random latitude
    location_long = float(fake.longitude())  # Generate a random longitude
    eta_hours = random.randint(0, 23)
    eta_minutes = random.randint(0, 59)
    eta_seconds = random.randint(0, 59)
    eta = time(eta_hours, eta_minutes, eta_seconds).strftime("%H:%M:%S")  # Convert to string format
    in_schedule = fake.boolean()  # Generate a random boolean value for in_schedule

    # Assuming you have a list of driver IDs to choose from
    driver_id = random.choice(['driver1', 'driver2', 'driver3'])

    return {
        "center_id": center_id,
        "date_last_updated": date_last_updated,
        "location_lat": location_lat,
        "location_long": location_long,
        "ETA": eta,
        "in_schedule": in_schedule,
        "driver_id": driver_id
    }

# Example usage:
fake_center = generate_fake_center()
print(fake_center)
