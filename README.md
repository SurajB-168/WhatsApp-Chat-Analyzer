#📊 WhatsApp Chat Analyzer

An end-to-end Python project that takes a raw exported WhatsApp chat (`.txt`), parses it into a structured dataset and surfaces interactive statistics and visualizations through a Streamlit web app — including message/word/media/link counts, activity timelines, busiest days & months, an activity heatmap, most active users, a word cloud, top used words and emoji usage.

##💬 About

WhatsApp lets you export any chat (individual or group) as a `.txt` file. This project turns that unstructured text export into a clean, analyzable dataset and then builds a dashboard on top of it so you can explore chat activity — overall or for any individual participant.

## Features

- **Top Statistics** — total messages, total words, media shared, and links shared
- **Message Timeline** — monthly message volume over the lifetime of the chat
- **Activity Map** — busiest day of the week and busiest month
- **Period Activity Heatmap** — message activity by day-of-week × hour-of-day
- **Most Busy Users** (group chats) — top participants by message count and their share of total messages
- **Word Cloud** — most frequently used words, with stopwords removed
- **Top 20 Used Words** — bar chart of the most common words
- **Emoji Analysis** — most frequently used emojis
- User-level filtering — run any analysis for the whole group or for a single participant

##🛠️ Tech Stack

| Component        | Tool/Library                     |
|-------------------|-----------------------------------|
| Language          | Python                            |
| Web App           | Streamlit                         |
| Data Wrangling    | pandas, re (regex)                |
| Visualization     | Matplotlib, Seaborn, WordCloud    |
| Text Processing   | emoji, urlextract                 |
| Prototyping       | Jupyter Notebook                  |

##📁 Project Structure

```
WhatsApp-Chat-Analyzer/
│
├── app.py                      # Streamlit web app
├── preprocessor.py             # Raw chat text → structured DataFrame
├── helper.py                   # All analysis/stat functions used by app.py
├── stop_hinglish.txt           # Stopword list (English + Hindi) for word cloud/top words
├── README.md
│
├── notebooks/
│   └── Whatsapp_Chat_Analysis.ipynb   # EDA / prototyping notebook
│
└── assets/
    └── demo.png                # Screenshot(s) of the running app
```

##🧩 What's Done in This Project

- **`preprocessor.py`** parses a raw WhatsApp `.txt` export into a structured pandas DataFrame (sender, message, date, year, month, day, hour, etc.) using regex.
- **`helper.py`** computes all the stats and visualizations above, per user or overall, using that DataFrame.
- **`app.py`** is the Streamlit dashboard that ties it together — upload a chat, pick a user, click a button, see the results.
- **`notebooks/`** holds the original exploratory notebook used to build and test the parsing/analysis logic.

##🚀 How to Run

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
