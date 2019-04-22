# -*- coding: utf-8 -*-
"""
Print the current stock value for ESTC
"""
import os
import requests

url = "https://www.alphavantage.co/query"
params = {"function": "GLOBAL_QUOTE", "symbol": "ESTC", "apikey": os.environ.get("STOCKS_API_KEY")}


class Py3status:
    def stock_status(self):
        resp = requests.get(url, params=params)
        if not resp.ok:
            resp.raise_for_stats()

        output = resp.json()
        try:
            symbol = output["Global Quote"]["01. symbol"]
        except KeyError:
            return {"full_text": resp.text}

        price = float(output["Global Quote"]["05. price"])
        change = float(output["Global Quote"]["09. change"])
        if change < 0:
            color = "#FF0000"
        else:
            color = "#32CD32"
                
        change_percent = output["Global Quote"]["10. change percent"]
        percent = float(change_percent.replace("%", ""))
        return {
            "composite": [
                {"full_text": f"{symbol} ${price:.2f}"},
                {"full_text": f" ${change:.2f} ({percent:.2f}%)", "color": color},
            ]
        }
