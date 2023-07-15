import time

import account
import robin_stocks.robinhood as rh

NUMBER_OF_WORKERS = 1
TICKER_SYMBOLS = ["CSHI"]

def start():
    login = account.login_user(account.LOCAL_PATH, account.FILE_NAME)
    start_worker()

def start_worker():
    while True:
        quotes = rh.get_quotes(TICKER_SYMBOLS)
        print(quotes[0].get("ask_price"))
        time.sleep(1)



