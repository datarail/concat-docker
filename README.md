# Example Docker image build and usage with docker-compose

## Dockerfile

This file specifies how the Docker image is to be built. This will generally be
created the application developer who will then push the built Docker image to
Dockerhub for public consumption.

An example of building a docker image labelled `datarail/concat:latest` using
this Dockerfile.

```bash
docker build -t datarail/concat .
```

## Dockerhub

Repository for this example:

It is possible to push an image to a (preconfigured) Dockerhub resource once
authenticated to Dockerhub:

```bash
docker login
docker push datarail/concat:latest
```

As a convenience we usually make use of GitHub web-hooks to trigger a build on
Dockerhub when a tag or master branch is pushed to GitHub.

## docker-compose.yml

This file is a template provided by the application develop which details how
the application is to be run. This will be customised by the user of the
application according to their specific needs.

For example, the user will likely wish to configure the location at which their
input data exists and the location to which outputs should be written. For
example, if a user (`bob`) has some data in a subdirectory
(`/Users/bob/myproject/input_data/`) of his home directory on a mac. He also may
wish to have the output written into an (existing) directory
(`/Users/bob/myproject/concatenated_data/`) created for this purpose.

```yaml
...
  volumes:
   - /Users/bob/myproject/input_data/:/mnt/input:ro
   - /Users/bob/myproject/concatenated_data/:/mnt/output
...
```

Running a containerised application configured with docker-compose is achieved
by calling `docker-compose run <app>` where `<app>` is the name of the service
in the docker-compose file. The `--rm` informs docker that the container used to
run the application should be deleted upon completion which is generally
desirable unless debugging a failure using intermediate state.

```bash
docker-compose run --rm concat
```

## Application configuration

It is expected that each application written that conforms roughly to this
template will have a configuration file that the user will provider specifying
the parameters to use when running the application on the given data. This
should be found in the directory used as input and named according to the
specification of the application for which it is intended. In this example, the
configuration file is expected to be called `concat_config.yml`.

## Data

Example data for running the `concat` application. Includes the required
`concat_config.yml` config file and two files to be concatenated. The Docker
compose file currently references this directory relative to the location of the
`docker-compose.yml` as the input directory.

## Standard Docker Layout

All Dockerised applications are expected to have (at minimum):

 - A volume mounted into the container at `/mnt/input` for input data
 - A volume mounted into the container at `/mnt/output` for output data
 - A configuration file specific to the application within the volume mounted at
  `/mnt/input`
 - An optional ability to accept environment variables
