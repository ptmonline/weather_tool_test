import requests
import smtplib

def get_emails():
    emails = {}
    try:
        email_file = open('email.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)
    return emails

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    return schedule

    
def get_weather_forecast():
    api_key_config = open('config.txt', 'r')
    API_KEY = api_key_config.read()
    api_key_load = {'appid' : API_KEY.strip()}
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Barcelona,spain'
    weather_request = requests.get(url, params=api_key_load)
    weather_json = weather_request.json()
    description = weather_json['weather'][0]['description']
    temp_max = weather_json['main']['temp_max']
    temp_min = weather_json['main']['temp_min']

    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of '+ str(int(temp_min))

    return forecast

def send_emails(emails, schedule, forecast):
    #Add your email and password 
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()
    from_email = input("What is your email? : ')
    password = input("What is your password? :")
    server.login(from_email, password)
    message = 'Subject: Welcome to the circus\n'
    message += forecast
    print(message)
    server.sendmail(from_email, from_email, forecast)
    server.quit()
    
def main():
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    forecast = get_weather_forecast()
    print(forecast)
    send_emails(emails, schedule, forecast)
    
main()
