# https://docs.astronomer.io/astro/runtime-release-notes
# can update the runtime by changing here
FROM quay.io/astronomer/astro-runtime:10.5.0


# add -base if want full control over docker build process
# i.e. what to install or configure
# FROM quay.io/astronomer/astro-runtime:10.5.0-base

# use Dockerfile to export variables to Astro cloud
# locally can use .env, .dev or .prod files and command:
# `astro dev start --env .prod`
# ENV AIRFLOW__WEBSERVER__INSTANCE_NAME="DevEnv"