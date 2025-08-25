#!/bin/bash

source .env

az webapp up\
        --sku F1\
        --name $DASH_APP_NAME\
        --resource-group $RESOURCE_GROUP\
        --runtime "PYTHON:3.12"\
        --location $LOCATION\
        -p $APP_PLAN

