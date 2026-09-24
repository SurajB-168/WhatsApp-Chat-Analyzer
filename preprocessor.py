import re
import pandas as pd

def preprocessing(data):
    split_pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s?[AP]M\s-\s'
    date_pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s?[AP]M'


    messages = re.split(split_pattern, data.replace('\u202f', ''))[1:]
    dates = re.findall(date_pattern, data.replace('\u202f', ''))

    df = pd.DataFrame({'user_messages': messages, 'date': dates})
    df['user_messages'] = df['user_messages'].str.replace('\n', '').str.strip()
    df['date'] = df['date'].str.replace(',', '').str.strip()

    user = []
    messages = []
    for message in df['user_messages']:
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if entry[1:]:
            user.append(entry[1])
            messages.append(entry[2])
        else:
            user.append('Group Notification')
            messages.append(entry[0])

    df['user'] = user
    df['message'] = messages
    df.drop(columns=['user_messages'])

    df['date'] = pd.to_datetime(df['date'], format='mixed')
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour


    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(str(hour) + '-' + str('00'))
        elif hour == 0:
            period.append(str('00')+ '-' + str(hour + 1))
        else:
            period.append(str(hour) + '-' + str(hour + 1))

    df['period'] = period

    df = df[['date', 'user', 'message', 'year', 'month_num', 'month', 'day', 'day_name', 'hour', 'period']]

    return df
