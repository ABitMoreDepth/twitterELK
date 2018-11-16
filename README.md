# Tweet analysis with ELK #


This repo provides a complete system for pulling tweets from twitter based on #hashtags, ingressing that data into elasticsearch, and visualising that data with Kibana.

The core idea is reasonably simple, tweets from twitter contain geocode information alongside the tweets content.  We can pull that data into elasticsearch, where we can then visualise that data using Kibana.

Kibana supports regional visualisations out of the box, so all we really need to do is ensure that we use the correct mapping when pulling tweets into ES.

## Project Dependencies ##
The project is built within docker containers and is orchestrated using docker-compose.  This makes setting up and getting running reasonably simple.

First off, ensure you have both docker and docker-compose:
```
# get docker:
curl https://get.docker.com | sudo sh

# Get docker-compose
pipsi install docker-compose
```

See here about getting pipsi, but those familiar with python environments should be able to get the docker-compose tooling setup on their machine without too much additional effort.


## Bringing everything up ##
The first thing you need to do is setup the environment file, which will provide some of the key settings needed for the logstash pipeline.  The file should contain a key value pair per line, per the [docker env file docs](https://docs.docker.com/compose/env-file/).

An example of such a file that you can use as a template looks like this:
```
CONSUMER_KEY=123abc
CONSUMER_SECRET=123abc
OAUTH_KEY=123abc
OAUTH_SECRET=123abc
HASHTAGS=hashtag1,hashtag2,hashtag3
```

The file should be save in the repo root as `.env`.

Please note that you will need to retrieve the `CONSUMER_KEY` and token, along with the `OATH_TOKEN` and secret by registering a developer account on twitter and using that account to create an app.  After the various data scandals and spurious bot usage etc. apparently twitter will now manually vet applications for a developer account, so if you want to test this, it may be with getting in touch with Sam Martin to borrow his credentials, or just view the system running from his machine.

Bringing up the project once you have configured the env file is straightforward: `docker-compose up -d` will pull in the Elasticsearch & Kibana images, build the ingress image and launch the containers.  You can follow the logs for the Kibana container to check when the container has spun up its web interface, at which point it will be available at http://localhost:5601.

## Importing Kibana Visualisations and Dashboard ##
Until we have automated the deployment of the kibana dashboard, the user will either need to step through and create their own visualisations on system start up.  But for brevity the user can also import the `kibana_dashboard.json` file in order to load in a set of visualisations which should work out of the gate.
