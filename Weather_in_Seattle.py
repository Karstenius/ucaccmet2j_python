# I could not commit this file when I wanted to because it did not show up in the Source Control under changes. 
# Part 1

import json

# Part 1.1: Find the station code for Seattle

with open('ucaccmet2j_python\stations.csv') as file_csv:
    file_csv.readline()
    stations = []
    for line in file_csv:
        location, state, station = line.strip().split(',')
        stations.append({'Location': location, 'State': state, 'Station': station})

code_Seattle = stations[1]['Station']

# print(code_Seattle)

# Part 1.2: Select all the measurements belonging to Seattle & 
# Part 1.3: Sum all the measurements for each month

with open('ucaccmet2j_python\precipitation.json') as file_json:
    rain_data = json.load(file_json)

rain_Seattle = []
count = [0] *12
m = 0
for measurement in rain_data:
    if measurement ['station'] == code_Seattle:
        for m in range(12):
            if (f'2010-{m+1:02d}') in measurement ['date']:
                rain_Seattle.append(measurement)
                count[m] += measurement ['value']

# Part 1.4: Save to a JSON file

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rain_month = dict(zip(count, months))

with open('rain_Seattle.json', 'w') as file:
    json.dump(rain_month, file, indent=4)


# Part 2.1: Sum of precipitation over the whole year

total_precip = sum(count)
print(f'The total precipitation in Seattle in 2010 was {total_precip} in tenths of ml.')

# Part 2.2: Relative percipitation per month

monthly_percent = []
for number in count:
    monthly_percent.append(number / total_precip * 100)

percantage_month = dict(zip(monthly_percent, months))

with open('rain_percentage_Seattle.json', 'w') as file:
    json.dump(percantage_month, file, indent=4)

