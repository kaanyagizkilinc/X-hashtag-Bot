# 🐦 Twitter Hashtag Tracker with Tweepy

This is a simple web-based tool that allows users to track tweets based on a specific hashtag using the Twitter API. It is built using **Flask** for the backend and **Tweepy** for Twitter API access.

## 🔧 Features

- 🔍 Search tweets by any hashtag (e.g. #Python, #news)
- 🧮 Custom number of tweets to fetch
- 🧑‍💬 Displays tweet content and author
- 🛡️ Error handling for failed requests

## 🚀 Getting Started

### 1. Clone this repository
```bash
git clone https://github.com/kaanyagizkilinc/X-hashtag-Bot.git
cd X-hashtag-Bot
```
### 2. Install dependencies
pip install tweepy python-dotenv flask

### 3. Set up Twitter API credentials

Create a `.env` file in the project root directory and add the following:
```env
API_KEY=your_api_key  
API_SECRET=your_api_secret  
ACCESS_TOKEN=your_access_token  
ACCESS_SECRET=your_access_secret
```
You can get your credentials from the Twitter Developer Portal: https://developer.twitter.com/

## 🛠️ Running the App

```bash
python startbot.py
```

## 📌 Important Notes

- The Twitter API requires authentication and has limitations based on your access level.
- Free Tier users might not have access to advanced search endpoints.
- Make sure your developer account has **Elevated Access** to use `search_recent_tweets` (if using API v2).
- This project currently uses Twitter API v1.1 via Tweepy for hashtag search functionality.

## 📁 Project Structure

X-hashtag-Bot/
├── startbot.py         # Bot starter
├── bot.py              # Tweet scraping logic  
├── .env                # Twitter credentials (you create this)
└── README.md           # This file

Made with ❤️ by @kaanyagizkilinc
