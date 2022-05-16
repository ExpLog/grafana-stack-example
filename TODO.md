# TODO

- [ ] Add git, .gitignore, and push to Github.
- [x] Add Loki to the `docker-compose.yml`.
- [x] Make Loki and Tempo work together correlating logs and traces.
- [ ] Build a sample API in Python that can use everything from the Grafana + Prometheus stack.
- [ ] Build a sample consumer (maybe consuming events produced by the API), then integrate it.
- [ ] Learn how to make good dashboards in Grafana, querying all the tools available (Prometheus, Loki, Tempo)
- [x] Learn how to configure everything, including auto-discovery from `docker`.'
  - Using the Loki driver for `docker-compose`.

## Questions
* Can we use something like `keycloak.x` to secure all these tools?
* Can we backup Grafana dashboards, etc?
  * https://github.com/esnet/gdg
  * https://github.com/ysde/grafana-backup-tool