# ETL pipeline projects

A repository for personal data pipeline projects

# Author: 👤 Joshua Omolewa

## Requirement 

- python package manager : `uv`
- python-version: 3.12
- Aws account 

# Project 1

### DESCRIPTION
Creating a etl pipeline that extract data from csv and uploads it to aws s3

I created a python script [`project1.py`]('practice_project_etl/csv_to_s3_etl/etl_pipeline_projects/project_1.py') that extract a [csv file]('practice_project_etl/csv_to_s3_etl/etl_pipeline_projects/raw/customer_data.csv') and uploads to s3 (Amazon simple storage service) bucket.

**Note: csv file contains fake customer data.**

### ARCHITECTURE DIAGRAM


![alt text](<img/Animated  architecture.gif>)

  
  
### How to run project

- Ensure you have an aws account, aws cli installed and you have a valid aws session
- Ensure you have `uv` python package manager installed
- Ensure you already created the S3 bucket to upload the csv file to
- edit the [`project1.py`]('practice_project_etl/csv_to_s3_etl/etl_pipeline_projects/project_1.py') by adding the correct values for the variables below for the s3 bucket name, the csv path on your local machine and the file name (name of the the object in S3)

`BUCKET_NAME = "bronze-layer-csv"  # name of s3 bucket`

`FILE_NAME = "customer.csv"  # name of the file object in s3`

`RAW_CSV_FILE_PATH = "raw/customer_data.csv"  # local path of the csv file`

- execute the program by using the command below

```python
uv run python project_1.py 
```

- Once you execute the code the output should look like the image below in your terminal
![alt text](<img/Pythonscript execution.png>)
- You should  also see the file in S3 as seen in the image below
  ![alt text](<img/s3 file uploaded.jpg>)


# Follow Me On
  
* LinkedIn: [@omolewajoshua](https://www.linkedin.com/in/joshuaomolewa/)  
* Github: [@joshua-omolewa](https://github.com/Joshua-omolewa)


## Show your support

Give a ⭐️ if any of the projects helped you!