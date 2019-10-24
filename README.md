# Playground

This repository is here to satisfy an idle curiosity,
haven't had the chance to play with stock AMQP in Python outside of Django.

Dont have too many ideas on how to develop this further without meaningful
application messages, but we'll see how it goes!

## Interesting notes

* The docker image for Rabbit MQ is lacklustre in the sense that the
ready state does not accurately reflect when the service is ready, hence the
`sleep 10` at the beginning of the Dockerfile CMD's

After more reading this can be explained by the [Official Docker stance on 
controlling startup times](https://docs.docker.com/compose/startup-order/),
which is the [stance the rabbitmq guys take](https://github.com/docker-library/rabbitmq/pull/174#issuecomment-452002696)
, you are in charge of the timing of your deployments and you can implement healthchecks to buy into the
docker-compose way of doing things, or build resilient consumers that handle
failure / connection drops.
