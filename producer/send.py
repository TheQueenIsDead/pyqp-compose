#!/usr/bin/env python
import sys

import pika

def send_message(m):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=m)
    print(f" [x] Sent {m}'")
    connection.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        message = sys.argv[1]
        send_message(message)
    else:
        print("Sorry, you must include a message on the cli, invalid args (Forgot quotes?)")
