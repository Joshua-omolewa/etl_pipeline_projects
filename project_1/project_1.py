# Uploading csv file to s3
# Author: Joshua Omolewa
import boto3
import logging

# open the file and write to s3

fmt_str = "%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(level=logging.INFO, format=fmt_str, datefmt=date_format)

BUCKET_NAME = "bronze-layer-csv"  # name of s3 bucket
FILE_NAME = "customer.csv"  # name of the file object in s3
RAW_CSV_FILE_PATH = "project_1/raw/customer_data.csv"  # local path of the csv file


def s3_client() -> boto3.client:
    "returns an s3 client object to enable us interact with s3"
    logging.info("providing new s3 client")
    return boto3.client("s3")


def main() -> None:
    with open(
        RAW_CSV_FILE_PATH, mode="br"
    ) as csv_file:  # create a csv file object in binary mode

        logging.info(f"Uploading {RAW_CSV_FILE_PATH } file to s3")

        s3_client_new = s3_client()

        try:
            s3_client_new.upload_fileobj(csv_file, BUCKET_NAME, FILE_NAME)
        except Exception as e:
            logging.error(f"Encounter an issue when trying to upload file to s3: {e}")
            raise e

        logging.info(f"Uploaded {FILE_NAME} to s3")


if __name__ == "__main__":
    main()
