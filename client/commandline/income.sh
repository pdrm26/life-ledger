#!/bin/bash

source config.sh

curl -X POST -H "Token: $TOKEN" --data "amount=$1&text=$2" http://localhost:8000/finance/submit/income
