import time
from bot import track_hashtag, send_tweet

def write(text, color="white"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, colors['white'])}{text}{colors['reset']}")

# 🚀 Start
write("[BOT] Twitter Hashtag Bot is starting...", "yellow")
time.sleep(1)

# 🧾 Get hashtag
hashtag = input("Enter the hashtag to track (e.g. #Unity or 'Q' to quit): ")
if hashtag.lower().strip() == "q":
    write("[×] Operation cancelled by user.", "red")
    exit()

# 🔢 Get tweet count
count = input("How many tweets should be processed? (e.g. 5 or 'Q'): ").strip()
if count.lower() == "q":
    write("[×] Operation cancelled.", "red")
    exit()

try:
    count = int(count)
except:
    write("[X] Invalid number input!", "red")
    exit()

# 🔌 Simulate API connection
write("[✓] API connection successful.", "green")
time.sleep(0.5)

# 🔍 Process hashtag
track_hashtag(hashtag, count)

# 💬 Get tweet message
tweet_message = input("Enter the message to tweet ('Q' to cancel): ")
if tweet_message.lower() == "q":
    write("[×] Tweet sending cancelled.", "red")
else:
    send_tweet(tweet_message)
    write(f"[✓] Tweet sent successfully: {tweet_message}", "green")
