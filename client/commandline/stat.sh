#!/bin/bash

source config.sh

curl -X GET -H "Token: $TOKEN" http://localhost:8000/finance/q/generalstat
