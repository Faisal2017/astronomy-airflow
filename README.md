To get started, you need installed:
- Docker
- Astro cli

Astro uses docker containers for each component - Web server, scheduler, triggerer and metadata store (database)


CLI commands used throughout the Astronomy Airflow tutorial.

<details>
<summary>Useful CLI commands</summary>

Astro cli:

`astro dev init` - initialize a new Airflow project

`astro dev start` - create the containers and run Airflow locally

`astro dev restart` - to update containers with any changes you've made i.e. install a provider like AWS

`astro dev parse` - test DAGs for syntax or import errors

`astro dev pytest` - run tests

`astro dev run dags list` - check DAG list on metadata store (if not shown, could be issue with scheduler not picking up new DAGs)

`astro dev logs scheduler` - print scheduler logs

`astro dev bash` - access Docker container to be able to run Airflow commands directly

Airflow cli:

`airflow version` - get version rnuning

`airflow info` - show information about current Airflow and environment (i.e. what providers installed)

`airflow config list` - get in-depth Airflow settings

`airflow cheat-sheet` - list all available airflow commands

`airflow dags backfill --start-date START_DATE --end-date END_DATE dag_id` - command to backfill

</details>


## NOTE - the below was created automatically by Astro cli


## Overview

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.


## Project Contents

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes two example DAGs:
    - `example_dag_basic`: This DAG shows a simple ETL data pipeline example with three TaskFlow API tasks that run daily.
    - `example_dag_advanced`: This advanced DAG showcases a variety of Airflow features like branching, Jinja templates, task groups and several Airflow operators.
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.


## Deploy Your Project Locally

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://docs.astronomer.io/astro/test-and-troubleshoot-locally#ports-are-not-available).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.


## Deploy Your Project to Astronomer

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://docs.astronomer.io/cloud/deploy-code/


## Contact

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.
