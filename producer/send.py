#!/usr/bin/env python
import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(sys.argv)
    else:
        print("Sorry, you must include a message on the cli, invalid args (Forgot quotes?)")
