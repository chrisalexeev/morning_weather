from bs4 import BeautifulSoup
import csv
import datetime as dt
# import pandas as pd
from selenium import webdriver

def getSoup(zipCode):
    driver = webdriver.Chrome()

    now = dt.datetime.now()
    add12Hours = dt.timedelta(hours=12)
    newTime = now + add12Hours
    newTime = str(newTime).replace('-','').replace(' ','')
    newTime = newTime[:10]

    url = 'https://www.weatherbug.com/weather-forecast/hourly/'+zipCode+'?hour='+newTime
    driver.get(url)

    site = driver.page_source

    soup = BeautifulSoup(str(site), 'html.parser')

    driver.close()

    return soup

def getWeather(zipCode):
    soup = getSoup(zipCode)
    hour_lst = []
    temperature_lst = []
    precip_lst = []

    # Hours
    hours = soup.findAll(class_='hour-card__desktop__title')
    for block in hours:
        eachHour = block.get_text().strip().split('\n')
        eachHour = eachHour[0][:8].strip() # [:-2].strip()
        hr24 = eachHour[:-2].strip()
        if ('pm' in eachHour) and (eachHour != '12:00 pm'):
            hour = eachHour.split(':')
            hour = str(int(hour[0])+12) + ':00'
            hr24 = hour
        elif eachHour == '12:00 am':
            hr24 = '00:00'
        if len(hr24) < 5:
            hr24 = '0' + hr24
        hour_lst.append(hr24)

    # Temperatures
    temps = soup.findAll(class_='temp')
    for block in temps:
        eachTemp = block.get_text().strip()
        eachTemp = eachTemp[:-1]
        temperature_lst.append(eachTemp)

    trueTempLst = []
    for i in range(len(temperature_lst)):
        if i % 2 == 0:
            trueTempLst.append(temperature_lst[i])
    temperature_lst = trueTempLst

    # Precip
    precipBlocks = soup.findAll(class_='precip')
    for block in precipBlocks:
        eachPrecip = block.find('span').get_text()
        eachPrecip = eachPrecip[:-1]
        precip_lst.append(eachPrecip)

    # Conditions
    """
    conds = soup.findAll(class_='hour-card__desktop__conditions__description')
    for block in conds:
        eachCond = block.get_text().strip()
        descrip_lst.append(eachCond)
    """

    csv_template = [['','Time', 'Temperature', 'Precipitation']]
    index = 0
    while index < len(hour_lst):
        #csv_template += item + ', ' + temperature_lst[hour_lst.index(item)] + '\n'
        row = [index+1,hour_lst[index], temperature_lst[index], precip_lst[index]]
        csv_template.append(row)
        index += 1

    print(csv_template)

    with open ('weatherbug_scrape.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for item in csv_template:
            csv_writer.writerow(item)

"""
def weatherStats():
    df = pd.read_csv('weatherbug_scrape.csv')
    print(df.head(3))
"""