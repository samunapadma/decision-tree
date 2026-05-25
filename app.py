import streamlit as st
import pickle

# Model load பண்ணு
with open("decision_tree_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Pass / Fail Predictor")
st.write("மாணவர் தகவல் கொடுத்து result பாருங்க!")

# Input fields
hours = st.slider("Hours Studied", 1, 10, 5)
attendance = st.slider("Attendance (%)", 50, 100, 75)
assignments = st.slider("Assignments (%)", 40, 100, 70)

# Predict button
if st.button("Predict"):
    result = model.predict([[hours, attendance, assignments]])
    if result == 1:
        st.success("✅ Pass!")
    else:
        st.error("❌ Fail!")
