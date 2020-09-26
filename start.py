import requests


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


show_currencies(data)
save_to_currency_file(data)
