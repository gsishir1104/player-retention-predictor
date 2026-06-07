import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Generate fake player data
np.random.seed(42)

data_size = 500

data = pd.DataFrame({
    "session_length": np.random.randint(5, 120, data_size),
    "levels_completed": np.random.randint(1, 50, data_size),
    "deaths": np.random.randint(0, 30, data_size),
    "purchases": np.random.randint(0, 5, data_size),
})

# Retention logic
data["retained"] = (
    (data["session_length"] +
     data["levels_completed"] * 2 -
     data["deaths"]) > 50
).astype(int)

# Features
X = data[[
    "session_length",
    "levels_completed",
    "deaths",
    "purchases"
]]

y = data["retained"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Streamlit UI
st.title("Player Retention Predictor")

st.write("Predict whether a player will continue playing the game.")

session_length = st.slider("Session Length", 5, 120, 60)
levels_completed = st.slider("Levels Completed", 1, 50, 10)
deaths = st.slider("Deaths", 0, 30, 5)
purchases = st.slider("Purchases", 0, 5, 1)

# Predict
prediction = model.predict([[
    session_length,
    levels_completed,
    deaths,
    purchases
]])

if prediction[0] == 1:
    st.success("Player likely to stay!")
else:
    st.error("Player likely to quit.")