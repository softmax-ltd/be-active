# Introduction

In 2020 we have all experienced a deeply transformational period. The pandemic changed the life of all of us and it has be tough for many. It is, however, a change to improve the world and ourselves.

At [Softmax Ltd](https://softmaxltd.com/) we believe that it is important to stay active to keep the physically and mentally healty. Practising sports is a great way to achieve that.

We love sport and we encourage you to get invoved into it, if you don't already.

# Garmin gps and activity tracking data

This repository contains Python code that can be used for parsing gps and activity tracking data from Garmin Connect.

This code makes use of the following other works and repository to:

-   parse the data from Garmin Connect: https://github.com/pe-st/garmin-connect-export.git
-   to convert files to csv: https://github.com/dtcooper/python-fitparse

Together with the code, we make available a series of dataset containing datapoints that were collected during 2020 with a Garmin 645 watch.

## Data

The activity and tracking data is made available under the Creative Common License v3. You are welcome to conduct your analysis if you wish.

It includes mostly runs, trail runs and hikes, but also some cyling, swimming and other cardio activities.

The data is made available freely in the form of csv files. For the respect of the privacy of the owner, some gps coordinate have been removed. Should you notice that this removal was not adequate, please let us know at <privacy@softmaxltd.com>.

Please refer to [Softmax Ltd privacy](https://softmaxltd.com/privacy-policy/) policy for further details.

Most of these data are also available in Strava for [this](https://www.strava.com/athletes/giovanni_doni) profile.

### Raw data

If you have an account on Garmin Connect, just add your creadentials to the `config.sh` file and by using the (lightwieght) container, you will be able to fetch and covert into more convenient csv format.

You just need to have docker install, create and run the container as follow.

```docker build . -t run:latest
docker run -it -v $(pwd)/data/raw-data/:/app/raw-data `docker images run:latest --format {{.ID}}`
```

### Processed data

The activity and gps tracking data can be downloaded from an S3 bucket by running the `download-process-data.sh` scripts.

The code used to process the data from the raw data is contained in found in `data/process-data.py`.
