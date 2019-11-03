import re
from statistics import mean
import numpy as np
def edad(text):
    text = str(text)
    text.strip()
    if re.match('month', text):
        return "1"
    if re.search('(\d{1,2})\s(.+)\s(\d{1,2})', text):
        return str(round(mean([int(s) for s in re.findall('(\d{1,2})', text)]), 0))
    if re.search('\d{1,2}', text):
        return re.findall('\d{1,2}', text)[0]
    if re.match('[Tt]een', text):
        return "16"
    if re.search('[aA]dult', text):
        return "40"
    if re.search('[Yy]oung', text):
        return "30"
    else:
        return np.NaN

def fatality(text):
    text = str(text)
    text.strip()
    if re.search('[Nn]', text):
        return 'N'
    if re.search('[Yn]', text):
        return 'Y'
    else:
        return 'UNKNOWN'

landl = ['BOLIVIA', 'PARAGUAY', 'ANDORRA', 'AUSTRIA', 'BELARUS', 'CZECH REPUBLIC', 'HUNGARY', 'LIECHTENSTEIN', 'LUXEMBOURG', 'MACEDONIA', 'MOLDOVA', 'SAN MARINO', 'SERBIA', 'SLOVAKIA', 'SWITZERLAND', 'VATICAN CITY', 'BOTSWANA', 'BURUNDI', 'BURKINA FASO', 'CENTRAL AFRICAN REPUBLIC', 'CHAD', 'ETHIOPIA', 'LESOTHO', 'MALAWI', 'MALI', 'NIGER', 'RWANDA', 'SOUTH SUDAN', 'SWAZILAND', 'UGANDA', 'ZAMBIA', 'ZIMBABWE', 'LESOTHO', 'AFGHANISTAN', 'ARMENIA', 'AZERBAIJAN', 'BHUTAN', 'LAOS', 'KAZAKHSTAN', 'KYRGYZSTAN', 'MONGOLIA', 'NEPAL', 'TAJIKISTAN', 'TURKMENISTAN', 'UZBEKISTAN']

def countries(text):
    text = str(text)
    text.strip()
    text.upper()
    for e in landl:
        if e == text:
            return e

