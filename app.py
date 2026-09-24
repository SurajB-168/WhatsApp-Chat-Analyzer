import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor, helper



st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

# Create a sidebar for title and to create some other options
st.sidebar.title('WhatsApp Chat Analyzer')


# This is how you allow user to upload files
uploaded_file = st.sidebar.file_uploader('Choose a file')
if uploaded_file is not None:
    byte_data = uploaded_file.getvalue()  # This takes the data in bytes
    data = byte_data.decode('utf-8')      # This converts that byte data into strings by decoding the utf-8

    df = preprocessor.preprocessing(data)

    # Now we will fetch unique users from the dataframe so that we can do individual analysis
    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.remove('Group Notification')
    user_list.remove('+91 99993 50941')
    user_list.remove('+91 94129 37033')
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox('Analyze with respect to', user_list)
    num_messages, num_words, num_media_messages, num_links_shared = helper.fetch_stats(selected_user, df)

    # Add a button "Show Analysis", when clicked it will show analysis wrt to selected user
    if st.sidebar.button("Show Analysis"):
        st.title('Top Statistics')
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header('Total Messages')
            st.title(num_messages)
        with col2:
            st.header('Total Words')
            st.title(num_words)
        with col3:
            st.header('Total Media')
            st.title(num_media_messages)
        with col4:
            st.header('Total Links Shared')
            st.title(num_links_shared)




        # Message Timeline (Monthly)
        message_timeline = helper.message_timeline_history(selected_user, df)
        st.title('Message Timeline')
        fig, ax = plt.subplots()
        ax.plot(message_timeline['timeline'], message_timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


        # Which day of the week is busiest
        most_busy_day = helper.day_message_count(selected_user, df)
        most_busy_month = helper.month_message_count(selected_user, df)

        st.title('Activity Map')
        col1, col2 = st.columns(2)
        with col1:
            st.header('Most Busy Day')
            fig, ax = plt.subplots()
            ax.bar(most_busy_day['day_name'], most_busy_day['count'], color = 'orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header('Most Busy Month')
            fig, ax = plt.subplots()
            ax.bar(most_busy_month['month'], most_busy_month['count'], color = 'yellow')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Period Activity Heatmap
        st.title('Period Activity Heatmap')
        activity_heatmap = helper.period_heatmap(selected_user, df)
        fig, ax = plt.subplots(figsize = (20, 6))
        plt.yticks(rotation='horizontal')
        ax = sns.heatmap(activity_heatmap)
        st.pyplot(fig)





        user_messages_count, new_df = helper.most_busy_users(df)
        if selected_user == 'Overall':
            st.title('Most Busy Users')


            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            # This will create and display bar chart for top 5 busy users
            with col1:
                ax.bar(user_messages_count.index, user_messages_count.values, color = 'purple')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            # This will return the percent of total messages user wise
            with col2:
                st.dataframe(new_df)

        # Word Cloud
        st.title('Word Cloud')
        wordcloud_df = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud_df)
        st.pyplot(fig)


        # Top 20 words
        st.title('Top 20 Used Words')
        top_20_words_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(top_20_words_df['word'], top_20_words_df['count'])
        st.pyplot(fig)


        # Emoji Analysis
        emoji_df = helper.emoji_count(selected_user, df)
        st.title('Most Used Emoji')
        st.dataframe(emoji_df)






    else:
        st.title('Select the user and click "Show Analysis"')


