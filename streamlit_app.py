import streamlit as st

st.title("Disease Prediction using RandomForest Classifier")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import numpy as np
import joblib

# بارگذاری مدل
model = joblib.load('heart_disease_model.pkl')

st.title("پیش‌بینی بیماری قلبی")

# گرفتن ورودی از کاربر
age = st.slider("سن", 20, 80, 40)
height = st.slider("قد (cm)", 140, 200, 170)
weight = st.slider("وزن (kg)", 40, 150, 70)
bp = st.slider("فشار خون", 90, 200, 120)
glucose = st.slider("قند خون", 60, 300, 100)
cholesterol = st.slider("کلسترول", 100, 350, 180)
smoking = st.selectbox("آیا فرد سیگاری است؟", [0, 1])
exercise = st.selectbox("آیا فرد ورزش می‌کند؟", [0, 1])

# تبدیل به آرایه
sample = np.array([[age, height, weight, bp, glucose, cholesterol, smoking, exercise]])

# دکمه پیش‌بینی
if st.button("پیش‌بینی"):
    result = model.predict(sample)
    if result[0] == 1:
        st.error("❌ پیش‌بینی: این فرد بیمار قلبی است.")
    else:
        st.success("✅ پیش‌بینی: این فرد سالم است.")
