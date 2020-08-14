Airflow Development Starter
===

About
---

In this folder you will find a docker-compose file and related files that will assist with set-up of a local instance of
Airflow for development purposes. It will run a standard Airflow server with no add-ons or special configuration. This
is not meant for production deployment or to emulate a specific deployment of Airflow , rather to make it easier to
develop new Airflow DAGS outside of any special considerations for specific Airflow deployments.

What is this for?
---

#### It should help:
- Simplify local development and testing of Airflow dags
- Allow a user to run an instance of Airflow without add-ons

#### It does not:
- Emulate any particular Airflow deployment
- Allow development using non-standard libraries

Pre-requisites
---

1. Install `docker`
2. Install `docker-compose`
3. Install python
4. Install python package `cryptography`

Setup
---

1. Copy [.env.template](.env.template) to [.env](.env)
2. In [.env](.env), fill in values for the fernet key and postgres password:
      - POSTGRES_PASSWORD can be any valid password
      - FERNET_KEY must be a valid fernet key. See [these instructions](https://bcb.github.io/airflow/fernet-key)
        to generate a valid fernet key
3. Create a folder to contain your new dags (you can use [example-dags](example-dags) to get started)

Execution
---

In [this directory](.), run the container using docker-compose (note: it might be necessary to `sudo` the docker-compose
command:

```bash
DAGS_FOLDER=./example-dags/ docker-compose up -d
```

Note: DAGS_FOLDER must begin with `.` or `/` or else it will be interpreted as the name of a docker volume.

You can supply a dags folder of your choosing.

Outcome
---

Airflow should be accessible at `localhost:8080`. Airflow data should be stored in a postgres database accessible at
`localhost:5433`.

Additional Configuration
---

Any configuration parameter can be applied to your instance of Airflow simply by adding an extra line to [.env](.env).
Refer to Airflow documentation for information about Airflow configuration parameters.
