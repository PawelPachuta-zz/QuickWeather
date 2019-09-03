#! python3
# quickWeather.py

import json, requests, sys

if len(sys.argv) < 2:  # if number of args is smaller than 2...
    print('Use: quickWeather.py localization')  # print this sentence
    sys.exit()  # return to python's console
location = ''.join(sys.argv[1:])  # join all args except 1st(0)- name of module

# download data in json format from API OpenWeatherMap.org
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()  # check the status

# placing Json data in Python variable
weatherData = json.loads(response.text)  # scrapped text is located in response.text
# show weather
w = weatherData['list']
print('Actual weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('2morrow: ')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after 2morrow: ')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

