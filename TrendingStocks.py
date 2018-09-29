import requests
import json
import pandas as pd
from datetime import datetime
import time


def get_data():
    # Retrieve list of 30 trending equities
    r = requests.get('https://api.stocktwits.com/api/2/trending/symbols/equities.json')
    ans = json.loads(r.text)

    df = pd.read_excel('data.xlsx')
    writer = pd.ExcelWriter('data.xlsx')
    stock_list = []
    for i in range(30):
        print(ans['symbols'][i]['symbol'])
        stock_list.append(ans['symbols'][i]['symbol'])

    df[datetime.now()] = stock_list
    df.to_excel(writer)
    writer.save()
    writer.close()

if __name__ == '__main__':
    start_time = time.time()
    cnt = 0
    while True:
        get_data()
        time.sleep(300.0-((time.time() - start_time) % 300.0))
        cnt += 1
        if cnt == 10:
            break
