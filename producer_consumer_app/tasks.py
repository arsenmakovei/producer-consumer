import random
import uuid

from celery import shared_task
from faker import Faker

from producer_consumer_app.models import Order, Employee


@shared_task
def add_order():
    employees = Employee.objects.all()

    if employees:
        random_employee = random.choice(employees)

        faker = Faker()
        random_text = faker.text(max_nb_chars=255)

        order = Order.objects.create(
            task_id=str(uuid.uuid4())[:8],
            name="Text record",
            description=random_text,
            employee=random_employee,
        )

        print(order)
