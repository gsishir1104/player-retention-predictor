import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Generate fake player data
np.random.seed(42)

data_size = 500

data = pd.DataFrame({
    "session_length": np.random.randint(5, 120, data_size),
    "levels_completed": np.random.randint(1, 50, data_size),
    "deaths": np.random.randint(0, 30, data_size),
    "purchases": np.random.randint(0, 5, data_size),
})

# Retention rule (fake logic)
data["retained"] = (
    (data["session_length"] > 40) &
    (data["levels_completed"] > 10)
).astype(int)

# Features and labels
X = data[[
    "session_length",
    "levels_completed",
    "deaths",
    "purchases"
]]

y = data["retained"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Graph
plt.hist(data["session_length"])
plt.title("Player Session Length")
plt.xlabel("Minutes")
plt.ylabel("Players")

plt.show()