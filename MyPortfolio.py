import requests
import json
from tkinter import *

pycrypto= Tk()
pycrypto.title("My Crypto portfolio")
pycrypto.iconbitmap('icon.ico')

def font_color(amount):
    if amount>=0:
        return "green"
    else:
        return "red"

def my_portfolio():
    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=c0c4d24a-2526-4119-8ad1-b88afb43e935")
    api=json.loads(api_request.content)

    coins=[
        {
            "symbol":"BTC",
            "amount_owned":2,
            "price_per_coin":3000
        },
        {
            "symbol":"USDT",
            "amount_owned":100,
            "price_per_coin":5
        },
        {
            "symbol": "ETH",
            "amount_owned": 40,
            "price_per_coin": 30
        },
        {
            "symbol": "XRP",
            "amount_owned": 1000,
            "price_per_coin": 6
        }
    ]

    total_pl = 0
    coin_row=1
    total_current_value=0

    for i in range(0, 5):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]

                total_pl = total_pl + total_pl_coin
                total_current_value=total_current_value+current_value

                name = Label(pycrypto, text=api["data"][i]["symbol"], bg="white", fg="black",font="Helvetica 10", padx="5",pady="5",relief="groove")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="black",font="Helvetica 10", padx="5",pady="5",relief="groove")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                No_coins = Label(pycrypto, text=coin["amount_owned"], bg="white", fg="black",font="Helvetica 10", padx="5",pady="5",relief="groove")
                No_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text="${0:.2f}".format(total_paid), bg="white", fg="black",font="Helvetica 10", padx="5",pady="5",relief="groove")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="white", fg="black",font="Helvetica 10", padx="5",pady="5",relief="groove")
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(pycrypto, text="${0:.2f}".format(pl_percoin), bg="white", fg=font_color(float("{0:.2f}".format(pl_percoin))),font="Helvetica 10", padx="5",pady="5",relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="white", fg=font_color(float("{0:.2f}".format(total_pl_coin))),font="Helvetica 10", padx="5",pady="5",relief="groove")
                totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row=coin_row+1

    totalcv = Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="white", fg="black", font="Helvetica 10",padx="5",pady="5", relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N + S + E + W)

    totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="white", fg=font_color(float("{0:.2f}".format(total_pl))), font="Helvetica 10",padx="5", pady="5", relief="groove")
    totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)

    api=""

    update = Button(pycrypto, text="Update", bg="gray",command=my_portfolio,fg="white", font="helvetica 10 bold", padx="5", pady="5",relief="groove")
    update.grid(row=coin_row+1, column=6, sticky=N + S + E + W)



name= Label(pycrypto,text="Coin Name",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
name.grid(row=0,column=0,sticky=N+S+E+W)

price= Label(pycrypto,text="Price",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
price.grid(row=0,column=1,sticky=N+S+E+W)

No_coins= Label(pycrypto,text="Coins Owned",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
No_coins.grid(row=0,column=2,sticky=N+S+E+W)

amount_paid= Label(pycrypto,text="Total Amount paid",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
amount_paid.grid(row=0,column=3,sticky=N+S+E+W)

current_val= Label(pycrypto,text="Current Value",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
current_val.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin= Label(pycrypto,text="P/L per coin",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
pl_coin.grid(row=0,column=5,sticky=N+S+E+W)

totalpl= Label(pycrypto,text="Total P/L with coin",bg="#43C6DB",fg="black",font="Helvetica 12 bold", padx="5",pady="5",relief="groove")
totalpl.grid(row=0,column=6,sticky=N+S+E+W)

my_portfolio()
pycrypto.mainloop()