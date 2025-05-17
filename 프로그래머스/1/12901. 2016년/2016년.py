import datetime

def solution(a, b):
    year = 2016
    date = datetime.date(year, a, b)
    
    days = date.strftime('%a')
    
    days_upper = days.upper()
    
    return days_upper
    
    
    