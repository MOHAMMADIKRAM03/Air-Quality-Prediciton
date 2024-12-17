
import os
import time
import requests
import sys


def retrieve_html():
    for year in range(2013, 2019):
        for month in range(1, 13):
            month_str = f"0{month}" if month < 10 else str(month)
            url = f'http://en.tutiempo.net/climate/{month_str}-{year}/ws-421820.html'

            try:
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful

                text_utf = response.text.encode('utf-8')

                # Create directory if it doesn't exist
                os.makedirs(f"Data/Html_Data/{year}", exist_ok=True)

                with open(f"Data/Html_Data/{year}/{month}.html", "wb") as output:
                    output.write(text_utf)

            except requests.exceptions.RequestException as e:
                print(f"Error retrieving data from {url}: {e}")

        sys.stdout.flush()


if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))


