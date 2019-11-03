import re
from statistics import mean
import numpy as np

def fatality(text):
    text = str(text)
    text = text.strip()
    if re.search('[Nn]', text):
        return 'N'
    if re.search('[Yn]', text):
        return 'Y'
    else:
        return 'UNKNOWN'

def clean_countries(text):
    text = str(text)
    text = text.strip()
    text = text.upper()
    if re.search('UNITED ARAB EMIRATES (UAE)', text):
        return 'UNITED ARAB EMIRATES'
    if re.search('ASIA\?', text):
        return 'UNKNOWN'
    if re.search ('SUDAN\?', text):
        return 'SUDAN'
    if re.search('Yemen ', text):
        return 'YEMEN'
    if re.search('INDIAN OCEAN?', text):
        return 'INDIAN OCEAN'
    if re.search('MEDITERRANEAN SEA?', text):
        return 'MEDITERRANEAN SEA'
    else:
        return text

def countries(text):
    landl = ['BOLIVIA', 'PARAGUAY', 'ANDORRA', 'AUSTRIA', 'BELARUS', 'CZECH REPUBLIC', 'HUNGARY', 'LIECHTENSTEIN', 'LUXEMBOURG', 'MACEDONIA', 'MOLDOVA', 'SAN MARINO', 'SERBIA', 'SLOVAKIA', 'SWITZERLAND', 'VATICAN CITY', 'BOTSWANA', 'BURUNDI', 'BURKINA FASO', 'CENTRAL AFRICAN REPUBLIC', 'CHAD', 'ETHIOPIA', 'LESOTHO', 'MALAWI', 'MALI', 'NIGER', 'RWANDA', 'SOUTH SUDAN', 'SWAZILAND', 'UGANDA', 'ZAMBIA', 'ZIMBABWE', 'LESOTHO', 'AFGHANISTAN', 'ARMENIA', 'AZERBAIJAN', 'BHUTAN', 'LAOS', 'KAZAKHSTAN', 'KYRGYZSTAN', 'MONGOLIA', 'NEPAL', 'TAJIKISTAN', 'TURKMENISTAN', 'UZBEKISTAN']
    
    for e in landl:
        if e == text:
            return e
        else:
            np.nan

def clean_year(text):  
    if text > 1940 : 
        return text
    else:
        return np.nan
