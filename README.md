# Playground

This repository is here to satisfy an idle curiosity,
haven't had the chance to play with stock AMQP in Python outside of Django.

Dont have too many ideas on how to develop this further without meaningful
application messages, but we'll see how it goes!

## Interesting notes

* The docker image for Rabbit MQ is lacklustre in the sense that the
ready state does not accurately reflect when the service is ready, hence the
`sleep 10` at the beginning of the Dockerfile CMD's
