from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]      # If the selected user is not 'Overall' then we are changing the dataframe according to selected user

    # Count total number of messages
    num_messages = df.shape[0]

    # Count total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # Count total number of media shares
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]

    # Count total number of links shares
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    # This will return top 5 busy users
    user_messages_count = df['user'].value_counts().head()

    # This will return percent of total messages user wise
    new_df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns = {'count':'percent'})
    return user_messages_count, new_df


def create_wordcloud(selected_user, df):
    temp = df[df['user'] != 'Group Notification']
    temp = temp[temp['message'] != '<Media omitted>']
    if selected_user != 'Overall':
        temp = temp[temp['user'] == selected_user]

    file = open(r"C:\Users\suraj\OneDrive\Desktop\Projects\Whatsapp Chat Analysis\stop_hinglish.txt")
    stop_words = file.read()
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    temp['message'] = temp['message'].apply(remove_stop_words)
    wc = WordCloud(width = 500, height = 500, min_font_size = 10, background_color = 'white')
    wordcloud_df = wc.generate(temp['message'].str.cat(sep = ''))
    return wordcloud_df


def most_common_words(selected_user, df):
    temp = df[df['user'] != 'Group Notification']
    temp = temp[temp['message'] != '<Media omitted>']
    file = open(r"C:\Users\suraj\OneDrive\Desktop\Projects\Whatsapp Chat Analysis\stop_hinglish.txt")
    stop_words = file.read()
    if selected_user != 'Overall':
        temp = temp[temp['user'] == selected_user]
    words = []
    for message in temp['message']:
        for word in message.lower().split():
           if word not in stop_words:
               words.append(word)
    top_20_words_df = pd.DataFrame(Counter(words).most_common(20), columns = ['word', 'count'])
    return top_20_words_df




def emoji_count(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emoji_list = []
    for message in df['message']:
        for char in message:
            if emoji.is_emoji(char):
                emoji_list.append(char)
    emoji_df = pd.DataFrame(Counter(emoji_list).most_common(), columns = ['emoji', 'count'])
    return emoji_df



def message_timeline_history(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    message_timeline = pd.DataFrame(df.groupby(['year', 'month_num', 'month']).count()['message']).reset_index().sort_values(by=['year', 'month_num'])

    timeline = []
    for i in range(message_timeline.shape[0]):
        timeline.append(message_timeline['month'][i] + '-' + str(message_timeline['year'][i]))
    message_timeline['timeline'] = timeline

    return message_timeline



def day_message_count(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    most_busy_day = pd.DataFrame(df['day_name'].value_counts()).reset_index()
    return most_busy_day


def month_message_count(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    most_busy_month = pd.DataFrame(df['month'].value_counts()).reset_index()
    return most_busy_month


def period_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    activity_heatmap = df.pivot_table(index = 'day_name', columns = 'period', values = 'message', aggfunc = 'count').fillna(0)
    return activity_heatmap
