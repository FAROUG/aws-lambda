## Search a word (substring) function on S3 (Python)

## Description

This lambda is to search a word on all the txt objects within only one or all the s3 buckets.
and then will display all the occuance of that word, the line and in which object or bucket it founds.
as 
 ```
 String b'the' The word number is approximately 7 Found In Line 13 in file name PROD-SYSTEM-MANAGER-DEPLOYMENT-BACK_END.txt bucket  mytestversioningbucket
 ```
## how to use it
The lambda code expect two variables (**bucket_name** and **string**) passed as environment variables and thier values
***Locally** 
```
```
***AWS lambda resource** 
![alt text](https://github.com/FAROUG/aws-lambda/blob/feature/lambda_function_python_code/image.jpg?raw=true)

* `function` - A Python function.
* template.yml - An AWS CloudFormation template that creates an application (later).
* 1.run-lambda-locally.sh, 2.deploy-lamdbda.sh, etc. - Shell scripts that use the AWS CLI to deploy and manage the application.

Use the following instructions to deploy the sample application.

## Requirements
* Python (3.7, 3.8, 3.9, or 3.10)
* The Bash shell. For Linux and macOS, this is included by default. In Windows 10, you can install the Windows Subsystem for Linux to get a Windows-integrated version of Ubuntu and Bash.
* The AWS CLI v1.17 or newer.

## Setup
Download or clone this repository.

```
git clone git@github.com:FAROUG/aws-lambda.git
cd aws-lambda.git
```
To invoke the lambda locally ensure that the default aws credentials is 
