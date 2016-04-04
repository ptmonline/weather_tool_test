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
    api_key_config = open('config.txt', 'r')
    API_KEY = api_key_config.read()
    API_KEY = API_KEY.strip()
    api_key_load = {'appid' : API_KEY}
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Barcelona,spain'
    weather_request = requests.get(url, params=api_key_load)
    weather_json = weather_request.json()

    print(weather_json)
    
def main():
    emails = get_emails()
    print(emails)
    schedule = get_schedule()
    print(schedule)
    get_weather_forecast()
    
main()
