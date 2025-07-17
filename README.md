# 📊 Cryptocurrency Price Prediction Model

![Bitcoin Price Prediction Banner](https://img.shields.io/badge/Bitcoin-Price%20Prediction-orange?style=for-the-badge&logo=bitcoin)

## 📝 Overview
This project implements advanced machine learning models to predict Bitcoin prices based on historical data. The models analyze Bitcoin price data from the past 30 days and forecast the price for the next day with visualizations and comparative analysis.

---

## ✨ Features

### 🔍 Data Collection & Processing
- Real-time data retrieval from CoinGecko API
- Automatic data preprocessing and cleaning
- Time series formatting for prediction models

### 🤖 Machine Learning Models
- **Linear Regression**: Simple trending analysis
- **Decision Tree**: Complex pattern recognition 
- **Random Forest**: Ensemble learning with multiple decision trees
- **Support Vector Regressor (SVR)**: Non-linear relationships mapping
- **Gradient Boosting**: Sequential error-correction model

### 📈 Visualization
- Interactive time-series plots of Bitcoin prices
- Model comparison charts
- Prediction vs. actual price visualization
- Trend analysis graphs

![Model Comparison](https://img.shields.io/badge/Visualizations-Interactive%20Plots-blue?style=flat-square&logo=chart.js)

---

## 🛠️ Requirements
- Python 3.x
- Required libraries:
```
pandas >= 1.3.0
numpy >= 1.20.0
scikit-learn >= 0.24.2
matplotlib >= 3.4.2
requests >= 2.25.1
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YooshaMirza/CRYPTO-PRICE-PREDICTION-MODEL.git
cd CRYPTO-PRICE-PREDICTION-MODEL
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. API Configuration
Get a CoinGecko API key from [CoinGecko](https://www.coingecko.com/en/api) and update the API key in the notebook:
```python
API_KEY = 'your_api_key_here'
```

---

## 📊 Visual Outputs

The project generates several visual outputs to help understand the Bitcoin price predictions:

### Sample Visualizations:

1. **Linear Regression Model**
   - Blue scatter points show actual Bitcoin prices
   - Red dashed line shows the model's fit to historical data
   - Green dashed horizontal line indicates the next day's predicted price

2. **Decision Tree Model**
   - Shows the non-linear fit of the Decision Tree to Bitcoin price data
   - Highlights how the model captures price fluctuations

3. **Random Forest Model**
   - Demonstrates the ensemble approach's prediction capability
   - Combines multiple decision trees for improved accuracy

4. **SVR Model**
   - Shows how SVR maps complex patterns in the price data
   - Often provides different predictions from tree-based models

5. **Model Comparison**
   - Side-by-side visualization of all models' predictions
   - Helps identify which model may be more reliable

![Visualization Preview](https://img.shields.io/badge/Interactive-Charts-green?style=flat-square&logo=plotly)

---

## 📈 Model Performance

### Prediction Results
| Model | Next Day Price Prediction ($) | Confidence Level |
|-------|-------------------------------|------------------|
| Linear Regression | varies | Medium |
| Decision Tree | ~76,031 | Medium-High |
| Random Forest | ~76,031 | High |
| SVR | ~67,911 | Medium |
| Gradient Boosting | varies | High |

> Note: Actual prediction values will vary based on the most recent 30 days of data when the model is run.

---

## 📋 Usage Instructions

### Running the Notebook
1. Open the Jupyter notebook `crypto price prediction pynb file.ipynb`
2. Run all cells sequentially to:
   - Fetch the latest Bitcoin price data
   - Train all prediction models
   - Generate visualization charts
   - Compare model performances
   - Get next-day price predictions

### Customizing the Analysis
- Change the cryptocurrency by modifying the API endpoint
- Adjust the historical data period by changing the `days` parameter
- Tune model hyperparameters for potentially improved accuracy

---

## ⚠️ Limitations
- Relies solely on historical price patterns without external factors
- Limited to 30 days of training data
- Does not account for sudden market events or regulatory changes
- Cryptocurrency markets are highly volatile and unpredictable

---

## 🚀 Future Improvements
- [ ] Add sentiment analysis from social media and news
- [ ] Implement deep learning models (LSTM, Transformers)
- [ ] Include market indicators (RSI, MACD, Bollinger Bands)
- [ ] Develop multi-day forecasting capability
- [ ] Create automated daily prediction reports
- [ ] Add portfolio optimization suggestions

---

## 👨‍💻 Contributors
- [Yoosha Mirza](https://github.com/YooshaMirza)

---

## 📄 License
MIT License

## 🙏 Acknowledgments
- CoinGecko for providing comprehensive cryptocurrency market data
- scikit-learn for the robust machine learning toolkit
- The open-source community for continuous inspiration and support

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
