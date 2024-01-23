import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
from textblob import TextBlob  # Ensure to install this library

# Function to get sentiment score for a given text
def get_sentiment_score(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

API_KEY = 'CG-71WZpBDHuh3BQ8jHLKakxhRP'
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30'

headers = {
    'Content-Type': 'application/json',
    'X-CoinGecko-API-Key': API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Include sentiment analysis as a feature
    df['sentiment'] = df['timestamp'].apply(lambda x: get_sentiment_score(f"Bitcoin on {x}"))  # Example text, you may fetch relevant news/social media data

    X = df[['timestamp', 'sentiment']].copy()
    X['timestamp'] = X['timestamp'].apply(lambda x: x.toordinal())
    y = df['price'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict price for the next day
    next_day_timestamp = datetime.now().toordinal() + 1
    next_day_sentiment = get_sentiment_score(f"Bitcoin on {datetime.fromordinal(next_day_timestamp)}")
    next_day_price = model.predict([[next_day_timestamp, next_day_sentiment]])[0]

    print(f"Predicted Price for Next Day: ${round(next_day_price, 2)}")

else:
    print("Failed to retrieve data from the API.")
