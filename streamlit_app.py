import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.huggingface import HuggingFaceLLM

st.set_page_config(page_title="🤖 Data Chatbot", layout="centered")
st.title("🧠 Chat مع بياناتك (Hugging Face + PandasAI)")

# ======== الخطوة 1: رفع ملف البيانات ========
uploaded_file = st.file_uploader("📁 حمّل ملف CSV الخاص بك", type="csv")

# ======== الخطوة 2: إدخال مفتاح Hugging Face والنموذج ========
hf_token = st.text_input("🔐 أدخل Hugging Face API Token", type="password")
model_name = st.text_input("🧠 اسم نموذج اللغة (مثال: google/flan-t5-large)", value="google/flan-t5-large")

# ======== الخطوة 3: عرض البيانات وتشغيل الشات ========
if uploaded_file and hf_token and model_name:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 البيانات المحملة (أول 5 صفوف)")
    st.dataframe(df.head())

    # إعداد نموذج اللغة الذكي
    llm = HuggingFaceLLM(api_token=hf_token, model=model_name)
    sdf = SmartDataframe(df, config={"llm": llm})

    # ======== الشات ========
    st.subheader("💬 اسأل أي سؤال عن البيانات")
    user_input = st.text_input("❓ اكتب سؤالك هنا")

    if user_input:
        with st.spinner("⏳ جاري المعالجة..."):
            try:
                response = sdf.chat(user_input)
                st.success("✅ الإجابة:")
                st.write(response)
            except Exception as e:
                st.error(f"❗ حصل خطأ: {e}")
