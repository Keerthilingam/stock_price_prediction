# stock-price-prediction
Mini project using Linear Regression
📈 Stock Price Prediction using Linear Regression
🔍 Project Overview
This is a mini project where I built a simple stock price prediction model using Linear Regression. The goal was to predict the closing price of a stock based on features like Open, High, Low, and Volume using historical stock data.

📚 What I Learned
How to load and clean real-world stock data using pandas.

How to perform Exploratory Data Analysis (EDA) using matplotlib and seaborn.

How to split data using train_test_split with a 50% test size for better model validation.

How to train and evaluate a Linear Regression model using sklearn.

How to interpret metrics like Mean Squared Error (MSE) and R² Score.

🛠️ Technologies Used
Python

pandas

seaborn

matplotlib

scikit-learn

🧪 Model Performance
Test Size: 50% (for more reliable validation)

Mean Squared Error (MSE): 1.02

R² Score: 0.97 (Very good fit)

🔄 Project Process
Load the dataset: Used historical stock data stored in a CSV file.

Data Cleaning: Removed missing/null values using dropna().

EDA: Visualized the relationships using pairplot.

Feature Selection: Used Open, High, Low, and Volume to predict Close.

Train-Test Split: 50% for training and 50% for testing.

Model Building: Trained using Linear Regression.

Evaluation: Measured with MSE and R² score.

Result Storage: Saved output metrics to a text file.

💡 How This Project Helped Me
Helped me understand the basics of machine learning workflow.

Improved my Python skills, especially with real data handling.

Gave confidence in building a working model from scratch.

Showed how simple models like Linear Regression can give high accuracy with well-prepared data.

🚀 Future Scope and Real-World Use
This mini project is just the beginning. In the future, this model can be extended by:

Using more advanced models like Random Forest, XGBoost, or LSTM (for time series).

Adding more financial indicators like Moving Averages, RSI, MACD, etc.

Creating a real-time stock predictor using live APIs.

Deploying the model using Flask or Streamlit for a web interface.

📂 Folder Structure
bash
Copy code
stock_price_prediction/
│
├── data/
│   └── stock_data.csv
│
├── output/
│   └── results.txt
│
├── stock_predictor.py  # Main Python file
├── README.md
## How to Use
To run this project:
1. Clone the repository.
2. Install the required libraries:
Run the script:

bash
Copy code
python stock_prediction.py
Libraries Used
pandas

matplotlib

seaborn

scikit-learn
3. Save the file.
