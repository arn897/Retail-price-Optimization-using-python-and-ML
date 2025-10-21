import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

st.title("Retail Price Optimization Dashboard")

# -----------------------------
# Step 1: Upload CSV
# -----------------------------
uploaded_file = st.file_uploader("Upload your retail CSV file", type=["csv"])
model_trained = False

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(data.head())

    # -----------------------------
    # Step 2: Visualizations
    # -----------------------------
    st.subheader("Distribution of Total Price")
    fig = px.histogram(data, x='total_price', nbins=20)
    st.plotly_chart(fig)

    st.subheader("Box plot of Unit Price")
    fig = px.box(data, y='unit_price')
    st.plotly_chart(fig)

    st.subheader("Quantity vs Total Price")
    fig = px.scatter(data, x='qty', y='total_price', trendline='ols')
    st.plotly_chart(fig)

    st.subheader("Average Competitor Price Difference by Category")
    data['comp_price_diff'] = data['unit_price'] - data['comp_1']
    avg_price_diff_by_category = data.groupby('product_category_name')['comp_price_diff'].mean().reset_index()
    fig = px.bar(avg_price_diff_by_category, x='product_category_name', y='comp_price_diff')
    st.plotly_chart(fig)

    # -----------------------------
    # Step 3: Train Decision Tree
    # -----------------------------
    st.subheader("Train Decision Tree Model")
    features = ['qty', 'unit_price', 'comp_1', 'product_score', 'comp_price_diff']
    X = data[features]
    y = data['total_price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    st.write(f"Model trained! Mean Squared Error on test set: {mse:.2f}")
    model_trained = True

    # Plot Predicted vs Actual
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_test, y=y_pred, mode='markers', name='Predicted vs Actual'))
    fig.add_trace(go.Scatter(x=[min(y_test), max(y_test)], y=[min(y_test), max(y_test)], mode='lines', name='Ideal Prediction'))
    st.plotly_chart(fig)

# -----------------------------
# Step 4: User Input Prediction
# -----------------------------
st.subheader("Predict Total Price for a New Product")

# Only allow prediction if model is trained
if model_trained:
    qty = st.number_input("Quantity", min_value=1, value=10)
    unit_price = st.number_input("Unit Price", min_value=0.0, value=100.0)
    comp_1 = st.number_input("Competitor Price", min_value=0.0, value=90.0)
    product_score = st.number_input("Product Score", min_value=0, value=5)
    comp_price_diff = unit_price - comp_1

    if st.button("Predict"):
        new_data = pd.DataFrame([[qty, unit_price, comp_1, product_score, comp_price_diff]],
                                columns=['qty','unit_price','comp_1','product_score','comp_price_diff'])
        predicted_price = model.predict(new_data)[0]
        st.success(f"Predicted Total Price: {predicted_price:.2f}")
else:
    st.info("Upload a CSV first to train the model and enable predictions.")
