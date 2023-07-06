import requests
from bs4 import BeautifulSoup

http_text = requests.get("https://weather.com/weather/tenday/l/63f4de10a8c7b229661a9674a3d0915b9740827451d381e82b730ca1b96bbbf5").text
#print(http_text)

soup = BeautifulSoup(http_text, 'lxml')

weather_data = soup.find_all('div', class_="DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF" )

#print(len(weather_data))
with open('ELEC390_Lab2.txt','a') as f:
    for day in weather_data:
        date = day.find('h3', class_="DetailsSummary--daypartName--kbngc").text
        # print(date)
        temp_section = day.find('div', class_="DetailsSummary--temperature--1kVVp")
        span_tags = temp_section.find_all('span')
        max_temp = span_tags[0].text
        min_temp = span_tags[1].span.text
        # print(max_temp)
        # print(min_temp)
        weather_condition = day.find('div', class_="DetailsSummary--condition--2JmHb").span.text
        # print(weather_condition)
        chance = day.find('div', class_="DetailsSummary--precip--1a98O").span.text
        # print(chance)
        wind_section = day.find('div', class_="DetailsSummary--wind--1tv7t").span.text
        # print(wind_section)
        wind_separated = wind_section.split()
        # print(wind_separated)
        wind_direction = wind_separated[0]
        # print(wind_direction)
        wind_speed = wind_separated[1]
        # print(wind_speed)
        final_data = (date, max_temp, min_temp, weather_condition, chance, wind_direction, wind_speed)
        print(final_data,file=f)
