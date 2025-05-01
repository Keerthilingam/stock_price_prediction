# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Data load cheyyadam
data = pd.read_csv('../data/stock_data.csv')  # Data ni read chestundi

# Step 2: Basic preprocessing
data = data.dropna()  # Missing values remove

# Step 3: Exploratory Data Analysis (EDA)
sns.pairplot(data)
plt.show()

# Step 4: Features and Target define cheyyadam
X = data[['Open', 'High', 'Low', 'Volume']]  # Features
y = data['Close']  # Target price

# Step 5: Train-Test Split

# New line: test_size 0.5 cheyyadam valla 50% data test ki vasthundi → R2 calculate cheyyachu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)


# Step 6: Model build cheyyadam
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Prediction
predictions = model.predict(X_test)

# Step 8: Evaluation
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")

# Optional: Output results file lo save cheyyachu
with open('../output/results.txt', 'w') as f:
    f.write(f'MSE: {mse}\nR2 Score: {r2}\n')
