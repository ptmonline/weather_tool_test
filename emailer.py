import requests
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
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Barcelona,spain&appid='
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    print(weather_json)
    
def main():
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    get_weather_forecast()
main()
