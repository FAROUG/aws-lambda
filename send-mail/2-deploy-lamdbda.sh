#!/bin/bash

virtualenv env
source env/bin/activate
pip3 install smart_open
pip3 install boto3
pip3 freeze > requirements.txt

cd env/lib/python*/sit*
zip -r9 ${OLDPWD}/lambda.zip .
cd $OLDPWD
zip -g lambda.zip lambda_function.py 