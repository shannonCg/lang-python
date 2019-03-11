import json, datetime


with open('significant_week.geojson', 'r') as file:
    earthquakes = json.load(file)

print("過去7天全球發生重大的地震資訊:")
for earthquake in earthquakes['features']:
    print("地點:{}".format(earthquake['properties']['place']))
    print("震度:{}".format(earthquake['properties']['mag']))

    time = float(earthquake['properties']['time']) / 1000 #because the value unit of earthquake['properties']['time'] is million second
    date_time = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    print("時間:{}".format(date_time))
    print()