# 💰 Finance Analyzer Dashboard

An interactive **Data Science + Machine Learning powered Streamlit application** to analyze personal spending, uncover patterns, and generate intelligent financial insights.

---

## 📸 Project Preview

<img width="1187" height="1772" alt="Screenshot 2026-04-25 194930" src="https://github.com/user-attachments/assets/27b1afe3-2ebe-44ca-985a-f21c916fca2c" />
<img width="1180" height="1762" alt="Screenshot 2026-04-25 194953" src="https://github.com/user-attachments/assets/abb3719f-34fd-46fa-b5c5-99f9c8b2ab5d" />
<img width="1172" height="1766" alt="Screenshot 2026-04-25 195009" src="https://github.com/user-attachments/assets/524fa652-c6de-4d87-82f9-7e584eb587ae" />

---

## 🚀 Features

### 📂 Data Handling

* Upload custom **CSV financial datasets**
* Automatic data cleaning & preprocessing
* Supports flexible real-world data formats

---

### 📊 Analytics Dashboard

* 💸 Total Spending
* 📉 Average Spending
* 🔮 Next Month Forecast (ARIMA)
* 📈 Monthly Growth Analysis
* 📊 Moving Average Trends

---

### 📈 Visualizations

* Category-wise spending (Bar Chart)
* Monthly trends (Time Series)
* Spending distribution (Histogram)
* Heatmaps for pattern detection
* Outlier visualization

---

### 🤖 Machine Learning & AI

* 🔮 **ARIMA Forecasting** for future spending
* 🧠 **KMeans Clustering** for spending segmentation
* 🎯 **Overspending Classifier** (Random Forest)
* 🚨 **Outlier Detection** (Z-score)

---

### 💡 Smart Recommendations

* Detect high-risk spending behavior
* Identify category imbalance (e.g., entertainment vs food)
* Highlight unusual transactions
* Provide actionable financial advice

---

### 📥 Export

* Download processed financial reports as CSV

---

## 🛠️ Tech Stack

| Layer            | Technology          |
| ---------------- | ------------------- |
| Frontend         | Streamlit           |
| Data Processing  | Pandas, NumPy       |
| Visualization    | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn        |
| Forecasting      | Statsmodels (ARIMA) |

---

## 📁 Project Structure

```
finance-analyzer/
│
├── app.py                  # Main Streamlit application
├── requirements.txt       # Dependencies
│
└── utils/
    ├── preprocess.py      # Data cleaning & loading
    ├── analysis.py        # Business logic & metrics
    ├── visualization.py   # Charts & plots
    └── ml_model.py        # ML models (ARIMA, KMeans, RF)
```

---

## ⚙️ Installation & Run Locally

```bash
# Clone repository
git clone https://github.com/namal1230/finance-analyse.git

# Navigate into project
cd finance-analyse

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 📊 Sample Dataset Format

Ensure your CSV includes:

| date       | category | amount | description |
| ---------- | -------- | ------ | ----------- |
| 2024-01-01 | food     | 500    | lunch       |
| 2024-01-02 | travel   | 1200   | bus         |

---

## 🌐 Live Demo

👉 [https://finance-analyse.streamlit.app/](https://finance-analyse.streamlit.app/)

---

## 🧠 Insights Logic

* Flags **high spending categories**
* Detects **abnormal transactions**
* Tracks **monthly growth trends**
* Forecasts future spending using **time series modeling**
* Classifies transactions into **normal vs overspending**

---

## 📌 Future Improvements

* 📄 Export reports as PDF/Excel
* 📊 Advanced forecasting models (Prophet / LSTM)
* 🔐 User authentication system
* 🌍 Multi-currency support
* 📱 Fully responsive mobile UI
* 🤖 AI chatbot for financial advice

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📬 Contact

* GitHub: [https://github.com/namal1230/finance-analyse](https://github.com/namal1230/finance-analyse)
* LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful:

👉 Give it a **star ⭐**
👉 Share it with others

---

## 🧠 Author Note

This project demonstrates practical integration of:

* Data Analysis
* Machine Learning
* Real-world financial insights
* Interactive dashboards
