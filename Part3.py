import json

with open('ucaccmet2j_python\stations.csv') as file_csv:
    file_csv.readline()
    stations = []
    for line in file_csv:
        location, state, station = line.strip().split(',')
        stations.append({'Location': location, 'State': state, 'Station': station})

code_Cincinnati = stations[0]['Station']
code_Seattle = stations[1]['Station']
code_Maui = stations[2]['Station']
code_San_Diego = stations[3]['Station']

with open('ucaccmet2j_python\precipitation.json') as file_json:
    rain_data = json.load(file_json)

# rain_City = []
# count = [0] *12
# m = 0
# i = 0
# for measurement in rain_data:
#     for i in range(4):
#         if stations[{i}] in measurement ['station']:
#             for m in range(12):
#                 if (f'2010-{m+1:02d}') in measurement ['date']:
#                     rain_City.append(measurement)
#                     count[m] += measurement ['value']

# Seattle
rain_Seattle = []
count_S = [0] *12
m_S = 0
for measurement_S in rain_data:
    if measurement_S ['station'] == code_Seattle:
        for m_S in range(12):
            if (f'2010-{m_S+1:02d}') in measurement_S ['date']:
                rain_Seattle.append(measurement_S)
                count_S[m_S] += measurement_S ['value']

# Cincinnati
rain_Cincinnati = []
count_C = [0] *12
m_C = 0
for measurement_C in rain_data:
    if measurement_C ['station'] == code_Cincinnati:
        for m_C in range(12):
            if (f'2010-{m_C+1:02d}') in measurement_C ['date']:
                rain_Cincinnati.append(measurement_C)
                count_C[m_C] += measurement_C ['value']

# Maui
rain_Maui = []
count_M = [0] *12
m_M = 0
for measurement_M in rain_data:
    if measurement_M ['station'] == code_Maui:
        for m_M in range(12):
            if (f'2010-{m_M+1:02d}') in measurement_M ['date']:
                rain_Maui.append(measurement_M)
                count_M[m_M] += measurement_M ['value']

# San Diego
rain_San_Diego = []
count_D = [0] *12
m_D = 0
for measurement_D in rain_data:
    if measurement_D ['station'] == code_San_Diego:
        for m_D in range(12):
            if (f'2010-{m_D+1:02d}') in measurement_D ['date']:
                rain_San_Diego.append(measurement_D)
                count_D[m_D] += measurement_D ['value']

total_precip_C = sum(count_C)
total_precip_D = sum(count_D)
total_precip_M = sum(count_M)
total_precip_S = sum(count_S)

precip = [total_precip_C, total_precip_S, total_precip_D, total_precip_M]
total_precip = sum(precip)

print(f'The total precipitation in the four cities (Seattle, Cincinnati, Maui, and San Diego) in 2010 was {total_precip} in tenths of ml.')

# Relative of Seattle compared to other cities

percentage_Seattle = total_precip_S / total_precip * 100

print(f'{percentage_Seattle} per cent of the rain in the four cities fell in Seattle.')