## Search a word (substring) function on S3 (Python)

The project source includes function code and supporting resources:

![alt text](https://github.com/FAROUG/aws-lambda/blob/feature/lambda_function_python_code/sample-lambda-python.png?raw=true)

* `function` - A Python function.
* template.yml - An AWS CloudFormation template that creates an application (later).
* 1-run-lambda-locally.sh, 2-deploy-lamdbda.sh, etc. - Shell scripts that use the AWS CLI to deploy and manage the application.

Use the following instructions to deploy the sample application.
## Description

This lambda is to search a word on all the txt objects within only one or all the s3 buckets.
and then will display all the occuance of that word, the line and in which object or bucket it founds.
as 
 ```
 String b'the' The word number is approximately 7 Found In Line 13 in file name PROD-SYSTEM-MANAGER-DEPLOYMENT-BACK_END.txt bucket  mytestversioningbucket
 ```
will also evaluate if the bucket name entered is correct and will display all the existing buckets in the case the value of the bucket name was not found.

The lambda code expect two variables (**bucket_name** and **string**) passed as environment variables and thier values.
### How to search?? 
## Locally
by using the -e option when executing the python-lambda-local command 
```
-e environment_variables.json
as in python-lambda-local -f lambda_handler lambda_function.py event.json -e environment_variables.json --timeout 30000
check the environment_variables.json file 
```
## AWS lambda resource
![alt text](https://github.com/FAROUG/aws-lambda/blob/feature/lambda_function_python_code/lambda-environment-configuration.png?raw=true)


## Requirements
* Python (3.7, 3.8, 3.9, or 3.10) --> Downlad Python from [here](https://www.python.org/downloads/)
* The Bash shell. For Linux and macOS, this is included by default. In Windows 10, you can install the Windows Subsystem for Linux to get a Windows-integrated version of Ubuntu and Bash.
* The AWS CLI v1.17 or newer --> Download AWS CLI from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

## Setup
Download or clone this repository.

```
git clone https://github.com/FAROUG/aws-lambda.git
cd aws-lambda/search-on-s3-word-txt-type-object/
```

### To install all the packages needed to run the code locally, run 1-run-lambda-locally.sh.
```
sh 1-run-lambda-locally.sh
```
Or Use
```
./1-run-lambda-locally.sh
```
and to locally invoke it 
```
python-lambda-local -f lambda_handler lambda_function.py event.json -e environment_variables.json --timeout 30000
```
In locally lambda invocation, (Optionally) pass the values of AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to the environment_variables.json file, otherwise, it will look for the default AWS credentials stored under the ~/.aws directory. 
check out [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) The order in which searches for credentials.
### Deploy The Python package on AWS Lambda
To deploy this python package (< few MB) on AWS Lambda with external libraries (like smart_open, …), you must put all these libs in the lambda folder you want to deploy. Then zip all the files it contains and finally deploy the zip file.
Let's pack the python and prepare it using the below script
```
sh 2-deploy-lamdbda.sh
or
./2-deploy-lamdbda.sh
```
then let's deploy it using the AWS CLI, Assuming that you have properly created an AWS lambda in AWS lambda console with the name **s3_lambda** and configured s3_lambda lambda function to access to the s3 buckets using role and policy
```
aws lambda update-function-code --function-name s3_lambda --zip-file fileb://lambda.zip
```