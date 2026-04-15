# 💰 Finance Analyzer Dashboard

An interactive **Data Science + Streamlit** project to analyze personal spending, visualize patterns, and generate smart insights.

---

## 📸 Project Preview
<img width="1919" height="852" alt="Screenshot 2026-04-15 050249" src="https://github.com/user-attachments/assets/f2e67752-540c-4613-8c15-cfc548a5a02e" />
<img width="1903" height="842" alt="Screenshot 2026-04-15 050313" src="https://github.com/user-attachments/assets/a7aa8855-df63-414d-aef0-3d75903626cc" />
<img width="1897" height="830" alt="Screenshot 2026-04-15 050339" src="https://github.com/user-attachments/assets/7830f71c-a7da-4bf2-ba74-3a90b948fb78" />
<img width="1905" height="842" alt="Screenshot 2026-04-15 050355" src="https://github.com/user-attachments/assets/353ae965-32b6-47d1-8a0a-bc611c9d71fa" />


> 💡 Tip: Upload your screenshot to GitHub (`assets/` folder) or use Imgur and paste the link here.

---

## 🚀 Features

* 📂 Upload CSV financial data
* 🔍 Filter by **category** and **date range**
* 📊 Key metrics:

  * Total Spending
  * Average Spending
  * Next Month Prediction
* 📈 Visualizations:

  * Category-wise spending (Bar Chart)
  * Monthly trends (Line Chart)
  * Spending heatmap
* 🧠 Smart insights:

  * Detect high spending categories
  * Weekend vs weekday analysis

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Data Processing**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn

---

## 📁 Project Structure

```
finance-analyzer/
│
├── app.py                  # Main Streamlit app
├── requirements.txt       # Dependencies
│
└── utils/
    ├── preprocess.py      # Data cleaning & transformation
    ├── analysis.py        # Business logic & insights
    └── visualization.py   # Charts & plots
```

---

## ⚙️ Installation & Run Locally

```bash
# Clone repo
git clone https://github.com/your-username/finance-analyzer.git

# Navigate
cd finance-analyzer

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 📊 Sample Dataset Format

Your CSV should include:

| date       | category | amount |
| ---------- | -------- | ------ |
| 2024-01-01 | food     | 500    |
| 2024-01-02 | travel   | 1200   |

---

## 🌐 Live Demo

👉https://finance-analyse.streamlit.app/

---

## 🧠 Insights Logic

* Flags if **food spending > 30%**
* Detects **weekend overspending**
* Predicts next month using **average trend**

---

## 📌 Future Improvements

* 🔮 Machine Learning prediction model
* 📥 Export reports (PDF/Excel)
* 🔐 User authentication
* 📱 Mobile-friendly UI

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork and improve.

---

## 📬 Contact

* GitHub: https://github.com/namal1230/finance-analyse.git
* LinkedIn: Add your profile here

---

⭐ If you like this project, give it a star!
