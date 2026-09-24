# 📊 WhatsApp Chat Analyzer

An end-to-end Python project that takes a raw exported WhatsApp chat (`.txt`), parses it into a structured dataset and surfaces interactive statistics and visualizations through a Streamlit web app — including message/word/media/link counts, activity timelines, busiest days & months, an activity heatmap, most active users, a word cloud, top used words and emoji usage.

## 💬 About

WhatsApp lets you export any chat (individual or group) as a `.txt` file. This project turns that unstructured text export into a clean, analyzable dataset and then builds a dashboard on top of it so you can explore chat activity — overall or for any individual participant.

## ✨ Features

- **Top Statistics** — total messages, total words, media shared, and links shared
- **Message Timeline** — monthly message volume over the lifetime of the chat
- **Activity Map** — busiest day of the week and busiest month
- **Period Activity Heatmap** — message activity by day-of-week × hour-of-day
- **Most Busy Users** (group chats) — top participants by message count and their share of total messages
- **Word Cloud** — most frequently used words, with stopwords removed
- **Top 20 Used Words** — bar chart of the most common words
- **Emoji Analysis** — most frequently used emojis
- User-level filtering — run any analysis for the whole group or for a single participant

## 📸 Screenshots

**Top Statistics**
![Top Statistics](images/1.%20Top%20statistics.jpg)

**Message Timeline**
![Monthly Timeline](images/2.%20Monthly%20timeline.jpg)

**Activity Map**
![Activity Map](images/3%20Activity%20map.jpg)

**Period Activity Heatmap**
![Heatmap](images/4%20Heatmap.jpg)

**Most Busy Users**
![Most Busy Users](images/6.%20Most%20busy%20users.jpg)

**Word Cloud**
![Word Cloud](images/7.%20Word%20Cloud.jpg)

**Top 20 Used Words**
![Top 20 Words](images/8.%20Top%2020%20words.jpg)

**Emoji Analysis**
![Most Emoji Used](images/5.%20Most%20emoji%20used.jpg)

## 🛠️ Tech Stack

| Component        | Tool/Library                     |
|-------------------|-----------------------------------|
| Language          | Python                            |
| Web App           | Streamlit                         |
| Data Wrangling    | pandas, re (regex)                |
| Visualization     | Matplotlib, Seaborn, WordCloud    |
| Text Processing   | emoji, urlextract                 |
| Prototyping       | Jupyter Notebook                  |

## 📁 Project Structure

```
WhatsApp-Chat-Analyzer/
│
├── app.py                      # Streamlit web app
├── preprocessor.py             # Raw chat text → structured DataFrame
├── helper.py                   # All analysis/stat functions used by app.py
├── stop_hinglish.txt           # Stopword list (English + Hindi) for word cloud/top words
├── README.md
│
├── images/
│   ├── 1. Top statistics.jpg
│   ├── 2. Monthly timeline.jpg
│   ├── 3 Activity map.jpg
│   ├── 4 Heatmap.jpg
│   ├── 5. Most emoji used.jpg
│   ├── 6. Most busy users.jpg
│   ├── 7. Word Cloud.jpg
│   └── 8. Top 20 words.jpg
│
└── notebook/
    └── Whatsapp_Chat_Analysis.ipynb   # EDA / prototyping notebook
```

## 🧩 What's Done in This Project

- **`preprocessor.py`** parses a raw WhatsApp `.txt` export into a structured pandas DataFrame (sender, message, date, year, month, day, hour, etc.) using regex.
- **`helper.py`** computes all the stats and visualizations above, per user or overall, using that DataFrame.
- **`app.py`** is the Streamlit dashboard that ties it together — upload a chat, pick a user, click a button, see the results.
- **`notebooks/`** holds the original exploratory notebook used to build and test the parsing/analysis logic.

## 🚀 How to Run

1. Clone the repo and install dependencies (`streamlit`, `pandas`, `matplotlib`, `seaborn`, `wordcloud`, `emoji`, `urlextract`)
2. Make sure `preprocessor.py` and `helper.py` are in the same folder as `app.py`, then run `streamlit run app.py`
3. Upload a WhatsApp chat export (**Chat → More → Export Chat → Without Media**), select a user and click **Show Analysis**


---

## 👨‍💻 About the Author

**Surajkumar Bevnale**
Data Analyst | SQL • Excel • Power BI • Python
B.Tech, Engineering Physics, IIT Ropar (2023–2027)

- 📫 Reach me at: surajk.b168@gmail.com
- 🔗 LinekdIn: [Surajkumar B](https://www.linkedin.com/in/skb168/)
---
