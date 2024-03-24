from faker import Faker
import random

fake = Faker('en_IN')  # 'en_IN' for Indian English locale


def generate_job_seekers(num_records):
    job_seekers = []
    for _ in range(num_records):
        full_name = fake.name()
        email_id = fake.email()
        contact = fake.phone_number()
        city = fake.city()
        address = fake.address()

        # Ensure that the city is in Maharashtra
        while not city or city.lower() not in ['mumbai', 'pune', 'nagpur', 'nashik', 'aurangabad', 'solapur', 'amravati', 'kolhapur', 'thane']:
            city = fake.city()

        job_seekers.append({
            'full_name': full_name,
            'email_id': email_id,
            'contact': contact,
            'city': city,
            'address': address
        })

    return job_seekers


if __name__ == '__main__':
    num_records = 10
    job_seekers = generate_job_seekers(num_records)

    # Print the generated job seekers
    for idx, job_seeker in enumerate(job_seekers, start=1):
        print(f"Job Seeker {idx}:")
        print(f"Full Name: {job_seeker['full_name']}")
        print(f"Email ID: {job_seeker['email_id']}")
        print(f"Contact: {job_seeker['contact']}")
        print(f"City: {job_seeker['city']}")
        print(f"Address: {job_seeker['address']}")
        print()

