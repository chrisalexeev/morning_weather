from . import weatherdata
from . import graphing
from . import dataAnalysis
# import getForms
from . import mailTest
from . import personal
from .personal import mailing_list

def main():
    for d in mailing_list:
        weatherdata.getWeather(d['zipcode'])
        graphing.graphs()
        analytics,interpretation,analyticsHTML,interpretationHTML = dataAnalysis.weatherStats()
        name = d['first_name']
        date = personal.getDate()
        mailTest.makeMessage(name,date,analytics,interpretation,analyticsHTML,interpretationHTML,d['email'])