# Producer - Consumer 

The Producer - Consumer project is a simple microservice implemented 
on the basis of Django, PostgreSQL, and Celery technologies. 
Its main goal is to demonstrate the interaction between the producer 
and the consumer through asynchronous tasks. 
The project allows adding records to the "Order" model through Celery, 
randomly assigning them to users from the "Employee" model. 
Users can delete their records from the table through the browser, 
while receiving notifications