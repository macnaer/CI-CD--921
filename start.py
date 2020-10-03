import requests
from boto3.session import Session
import boto3


FILENAME = "currency.txt"
URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

responce = requests.get(URL)
data = responce.json()


def save_to_currency_file(data):
    with open(FILENAME, "w") as file:
        for item in data:
            file.write(item["ccy"] + " " + item["base_ccy"] +
                       " " + item["buy"] + " " + item["sale"] + "\n")


def show_currencies(data):
    print("Inside show_Ccurrency")
    for item in data:
        print(item["ccy"] + " " + item["base_ccy"] +
              " " + item["buy"] + " | " + item["sale"])


def save_to_s3():
    bucketname = "currency-u"
    s3 = boto3.client('s3')
    s3.upload_file(FILENAME, bucketname, FILENAME)


show_currencies(data)
save_to_currency_file(data)
save_to_s3()
