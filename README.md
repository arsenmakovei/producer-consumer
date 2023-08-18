# Producer - Consumer 

The Producer - Consumer project is a simple microservice implemented 
on the basis of Django, PostgreSQL, and Celery technologies. 
Its main goal is to demonstrate the interaction between the producer 
and the consumer through asynchronous tasks. 
The project allows adding records to the "Order" model through Celery, 
randomly assigning them to users from the "Employee" model. 
Users can delete their records from the table through the browser, 
while receiving notifications

## Installation
Python3 must be already installed

1. Clone project and create virtual environment
```shell
git clone https://github.com/arsenmakovei/producer-consumer.git
cd producer_consumer
python -m venv venv
Windows: venv\Scripts\activate
Linux, Unix: source venv/bin/activate
pip install -r requirements.txt
```

2. Create .env file and set environment variables

```shell
DJANGO_SECRET_KEY=<your Django secret key>
POSTGRES_DB=<your Postgres db name>
POSTGRES_USER=<your Postgres db user>
POSTGRES_PASSWORD=<your Postgres db password>
POSTGRES_HOST=<your Postgres db host>
TELEGRAM_BOT_TOKEN=<your Telegram bot token>
TELEGRAM_CHAT_ID=<your Telegram chat id>
CELERY_BROKER_URL=<your Celery broker url>
CELERY_RESULT_BACKEND=<your Celer result backend url>
```

3. Make migrations and run server
```shell
python manage.py migrate
python manage.py runserver
```
4. When you delete order, you can see notification about it in [telegram chat](https://t.me/producer_consumer_chat).
5. Also you can create admin user using `python manage.py createsuperuser` and visit admin panel `/admin/`

6. Run a periodic task that adds a randomly generated order every minute using Celery.

* start Redis server
* In separate terminals, run commands: `celery -A producer_consumer worker -l INFO` and `celery -A producer_consumer beat -l INFO`

## Run with Docker

Docker should be installed and running

```shell
docker-compose up --build
```