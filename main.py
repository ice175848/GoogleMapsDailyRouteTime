import googlemaps
import csv
from datetime import datetime
import time

API_KEY = '' #input your Google maps API key
gmaps = googlemaps.Client(key=API_KEY)

origin = '' #input your start position
destination = '' #input your destination


def collect_travel_time():
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode="driving",
                                         departure_time=now)
    duration = directions_result[0]['legs'][0]['duration_in_traffic']['text']
    return now, duration


# 每天收集一次數據
def main():
    with open('travel_times.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Duration'])

        while True:
            timestamp, duration = collect_travel_time()
            print(f"At {timestamp}, travel duration is {duration}.")
            writer.writerow([timestamp, duration])
            # 等待一天
            time.sleep(86400)


if __name__ == "__main__":
    main()
