#!/bin/bash
clear
printf "You are about to download the dataset of sport activities tracked by a Garmin watch.\n"
printf "Gps points close to some given specific location have been removed. The owner of these data grant full use.\n"
printf "Confirm you intend to download the data and that you have read the LICENSE.txt document by typing: download ...\n"
printf "\n"

read download
if [ "$download" == "download" ]; then
    cd ./data/processed-data
    wget https://be-active.s3.eu-west-2.amazonaws.com/activities.tar.gz
    tar -xzvf activities.tar.gz && rm activities.tar.gz
    cd -
fi