# 🛒 Retail Price Optimization using Machine Learning

This project demonstrates how to use **Machine Learning** to optimize retail product pricing by analyzing historical data, exploring pricing trends, comparing with competitors, and predicting ideal prices to **maximize profit and maintain competitiveness**.

> 🚀 **This project is deployed and live!**  
> Access the interactive dashboard here: [Live App](https://retail-price-optimization-using-python-and-ml-jszjbazyblfvu2re.streamlit.app/)

---

## 📌 Objective

The goal is to identify optimal selling prices based on multiple factors such as product quantity, competitor pricing, customer behavior, and product scores to maximize **revenue and profit** while staying competitive in the retail market.

---

## 📂 Dataset

The dataset used contains:
- Product identifiers and categories
- Pricing metrics: `unit_price`, `total_price`, `freight_price`, `comp_1`, `comp_2`, `comp_3`
- Product attributes: `score`, `weight`, `photo count`, etc.
- Time data: `month_year`, `weekday`, `holiday`
- Customer data: number of buyers, ratings, etc.

> 📁 File: [`retail_price.csv`](https://github.com/arn897/RetailPriceApp/blob/main/retail_price.csv)  
> ✅ No missing values.

---

## 🧪 Technologies Used

- **Python**
- **Pandas** for data manipulation
- **Plotly Express & Graph Objects** for interactive visualizations
- **Scikit-learn** for modeling and evaluation
- **Streamlit** for deployment

---

## 🔗 Links

- **GitHub Repo:** [RetailPriceApp](https://github.com/arn897/RetailPriceApp)  
- **Notebook:** [Retail Price Optimization Notebook](https://github.com/arn897/RetailPriceApp/blob/main/Retail%20price%20optimization%20using%20python%20and%20ML.ipynb)

---

## 🔍 Exploratory Data Analysis (EDA)

Visualizations include:
- Distribution of total and unit prices
- Scatter plot of `qty` vs `total_price` (linear trend)
- Box plots by `weekday` and `holiday`
- Correlation heatmap of numerical features
- Average competitor price difference by category

---

## 🧠 Machine Learning Model

We trained a **Decision Tree Regressor** using key features:

### 📈 Features:
- `qty`
- `unit_price`
- `comp_1`
- `product_score`
- `comp_price_diff` (engineered)

### 🎯 Target:
- `total_price`

### 📊 Evaluation:
Predicted vs Actual prices plotted, along with an ideal prediction line.

---

## 📌 Project Highlights
- Cleaned and explored 676 rows x 30 columns retail dataset
- Engineered features to capture competitor pricing dynamics
- Visualized key pricing behaviors and trends
- Built an ML model to predict optimized retail prices
- **Deployed live on Streamlit for interactive exploration**  

---

## 📊 Future Work
- Try other ML models like Random Forest, XGBoost, or Linear Regression
- Add hyperparameter tuning using GridSearchCV
- Expand Streamlit app to allow manual input for predictions
- Simulate pricing scenarios to estimate profit gain
