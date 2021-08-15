# Crypto_Trendalyzer

## Prerequisites
1. [Python 3.6+](https://www.python.org/downloads/)
2. [Git](https://git-scm.com/downloads)
3. [News API Key](https://newsapi.org/)

## Setup
1. Clone the git repository.
```
git clone https://github.com/Saqifur-Rahman/Crypto_Trendalyzer.git
```

2. Inside the cloned repo, make a virtual environment. (This MUST be done for authentication to function properly)
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

2. Install the dependencies.
```
pip install -r requirements.txt
```

3. Generate key on News API, and update `main.py`
```
API_KEY = "YOUR_NEWS_API_KEY"
```

4. Run the server.
```
python main.py
```

## Specifications
- Framework: Flask (Python)
- Frontend: HTML, CSS, JavaScript, JQuery, Bootstrap 4
- APIs used:
  1. [CoinGecko](https://www.coingecko.com/en/api) - Cryptocurrency API
  2. [Chart.js](https://www.chartjs.org/) - For producing charts
  3. [News API](https://newsapi.org/) - News related to cryptocurrencies

## Key Featues

### News & Events
- Latest and Trending news, events related to cryptocurrencies.
- Route: `./`
- This section contains two parts:
  1. **News**: Fetch latest news related to cryptocurrencies using NewsAPI.
  ```
  GET : newsapi.org/v2/everything?q=cryptocurrencies&apiKey={API_KEY}
  ```
  2. **Events**: Fetch current events related to cryptocurrencies using CoinGecko API.
  ```
  GET : api.coingecko.com/api/v3/events
  ```

### Authentication
- Authenticate users for making transcations and view portfolio using Firebase Authentication.
- Signup Route: `./signup`
- Signin Route: `./signin`
- Logout: `./logout`
- Firebase Authentication stores and uses email and hashed password for authenticate users.
- Session is generated after successful authentication and session is destroyed after logout. Session stores email portfolio_id of the user.

### Coins
- List of coins with live prices, percentage change, market cap etc. with search and sort features.
- Route: `./crypto/`
- Fetch list of coins and all related details using CoinGecko API.
```
GET : api.coingecko.com/api/v3/coins/markets
Parameters: 
  vs_currency - usd
  order - market_cap_desc
  per_page - 200
```
- Search and Sort coins implemented using JQuery.
- List of coins is refreshed every 7.5 seconds using JQuery.

### Coin Page
- Performance of coin in intervals of a day, week, month, year, alltime, options to buy and sell coins.
- Route: `./crypto/coin` | Parameters: `id = {coin_id}`
- This section contains two parts:
  1. **Coin Performance**: Fetch detials of coin using CoinGecko API and performance graph generated using Chart.js
  ```
  GET : api.coingecko.com/api/v3/coins/markets
  Parameters: 
    vs_currency - usd
    ids - {coin_id}
    order - market_cap_desc
    per_page - 200
  ```
  2. **Buy/Sell Coin**: If authenticted, allows user to buy/sell coin in terms of USD or coin units, making and validating transactions using  Firebase Realtime Database.

### Portfolio
- Dedicated section for all the transcations, current distribution of coins with profit/loss.
- Route: `./portfolio/`
- This section contains two parts:
  1. **Portfolio Details**: Display portfolio value, margin(profit/loss) made, distribution of coins in the portfolio where coin details fetched using CoinGecko API and portfolio details from Firebase Realtime Database.
  2. **Transactions**: Display transcations with details fetched from Firebase Realtime Database.
