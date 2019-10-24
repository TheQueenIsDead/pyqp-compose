#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

def callback(ch, method, properties, body):
    print(" [x] Received: {}".format(body))


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print("Listener started, waiting for messages")
channel.start_consuming()