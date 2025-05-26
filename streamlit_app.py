import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import os

# واجهة المستخدم
st.title("🤖 Chatbot ذكي لفهم بياناتك باستخدام PandasAI")
st.write("اسأل أي سؤال عن البيانات بلغة طبيعية!")

# رفع الملف
uploaded_file = st.file_uploader("📁 حمّل ملف CSV", type="csv")

# إدخال الـ API Key
api_key = st.text_input("🔐 أدخل OpenAI API Key", type="password")

# استكمال الكود عند توفر الملف والمفتاح
if uploaded_file and api_key:
    df = pd.read_csv(uploaded_file)
    st.write("✅ بياناتك:")
    st.dataframe(df.head())

    # نموذج PandasAI
    llm = OpenAI(api_token=api_key)
    sdf = SmartDataframe(df, config={"llm": llm})

    # سؤال المستخدم
    user_question = st.text_input("❓ اسأل عن البيانات")

    if user_question:
        try:
            answer = sdf.chat(user_question)
            st.success("📌 الإجابة:")
            st.write(answer)
        except Exception as e:
            st.error(f"❗ حدث خطأ أثناء المعالجة: {e}")
