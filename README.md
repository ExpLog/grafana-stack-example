# Grafana Labs

## Setup

First we have to install the Loki docker driver. This allows applications in our docker-compose to ship their logs to Loki.

```shell
docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```

Then, we need to start our stack:

```shell
docker-compose up -d
```