# 🐦 Twitter Hashtag Tracker with Tweepy

This is a simple web-based tool that allows users to track tweets based on a specific hashtag using the Twitter API.  
It is built using **Flask** (for the backend) and **Tweepy** (for Twitter API access).

---

## 🔧 Features

- ✅ Search tweets by any hashtag (e.g. `#Python`, `#news`)
- ✅ User-defined number of tweets to fetch
- ✅ Displays tweet content and author
- ✅ Error handling for failed requests
- 
---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/kaanyagizkilinc/X-hashtag-Bot.git
cd X-hashtag-Bot
```

### Install Python dependencies
``` bash
  pip install tweepy python-dotenv
```

###Set up Twitter API credentials
Create a `.env`file in the project root directory and add:
```env
API_KEY=your_api_key
API_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_SECRET=your_access_secret
```
You can get your credentials from the Twitter Developer Portal.

##🛠️ Running the App
``` bash
  python startbot.py
```
---
##📌 Important Notes
  -The Twitter API requires authentication and is limited based on your access level.

  -If you're using the Free Tier, you may not be able to use advanced search endpoints.

  -Make sure your developer account has Elevated Access to use search_recent_tweets (if using API v2).

  -This project currently uses API v1.1 via Tweepy for search functionality.
  
 ---

