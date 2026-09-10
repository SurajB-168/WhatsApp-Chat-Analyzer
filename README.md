# WhatsApp Chat Analyzer

A Streamlit web app that analyzes exported WhatsApp chat logs and generates interactive statistics and visualizations — including message/word counts, activity timelines, busiest users, most common words, and emoji usage.

🔗 **Live Demo:** [Add your deployed link here]

---

## 📋 Overview

WhatsApp lets you export any chat as a `.txt` file. This app takes that raw export, parses it into structured data, and turns it into a rich analytics dashboard — helping you understand activity patterns, top contributors, and conversation trends at a glance.

You can analyze either the **overall group chat** or drill down into a **specific member's** activity.

---

## ✨ Features

**Top Statistics**
- Total messages
- Total words
- Media shared
- Links shared

**Timeline Analysis**
- Monthly activity timeline
- Daily activity timeline

**Activity Maps**
- Most active day of the week
- Most active month
- Weekly activity heatmap

**User Analysis**
- Most active users (bar chart, for group chats)
- Percentage contribution of each user

**Text & Emoji Analysis**
- Word cloud of most frequently used words
- Most common words (bar chart)
- Most frequently used emojis (with pie chart)

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Web Framework | Streamlit |
| Data Processing | Pandas |
| Visualization | Matplotlib, Seaborn |
| NLP / Text Utils | WordCloud, URLExtract, Emoji |

---

## 📂 Project Structure

```
whatsapp-chat-analyzer/
│
├── app.py               # Main Streamlit app (UI + workflow)
├── preprocessor.py       # Parses raw chat text into a structured DataFrame
├── helper.py             # Core analysis functions (stats, timelines, wordcloud, emojis, etc.)
├── stop_hinglish.txt      # Stopwords list (English + Hinglish) for cleaner word analysis
├── requirements.txt       # Python dependencies
└── README.md
```

---

## ⚙️ What This Project Does

- **Parses raw chat exports:** Uses regex-based preprocessing (`preprocessor.py`) to convert an unstructured WhatsApp `.txt` export into a clean, structured Pandas DataFrame containing dates, timestamps, senders, and messages.
- **Cleans and enriches the data:** Extracts additional fields such as year, month, day, hour, and day-of-week from timestamps to power time-based analysis, and filters out system notifications and deleted/media placeholders.
- **Computes core statistics:** Calculates total messages, total words, media messages shared, and links shared, for either the overall group or an individual user (`helper.py`).
- **Builds activity timelines:** Aggregates message counts by month and by day to visualize how activity has changed over time.
- **Generates activity maps:** Identifies the most active day of the week, the most active month, and builds a weekly activity heatmap (day vs. hour).
- **Ranks user activity:** Computes and visualizes the most active participants in a group chat along with their percentage share of total messages.
- **Analyzes text content:** Removes stopwords (including Hinglish stopwords via `stop_hinglish.txt`), generates a word cloud, and lists the most frequently used words.
- **Analyzes emoji usage:** Extracts emojis from messages using the `emoji` library and visualizes the most frequently used ones with a pie chart.
- **Ties it together in an interactive UI:** Uses Streamlit (`app.py`) to let the user upload a chat file, select a user (overall or specific member) from the sidebar, and instantly view all the above analyses on one dashboard.

---

## 🙋 Notes & Limitations

- Works best with chats exported in the standard WhatsApp date-time format; formatting can vary slightly by device/OS/app version.
- Group-level "most active users" analysis is only shown when analyzing "Overall" (not for 1:1 chats).
- Stopwords are tuned for English + Hinglish text; you can edit `stop_hinglish.txt` to customize word-cloud/common-word filtering for other languages.

---




## 🙌 Acknowledgements

Inspired by the original [WhatsApp Chat Analysis project by CampusX](https://github.com/campusx-official/whatsapp-chat-analysis).
