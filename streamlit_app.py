import streamlit as st
import pandas as pd

# اقرأ الداتا
df = pd.read_csv("cleaned_df.csv")

# واجهة المستخدم
st.title("📊 ChatBot بسيط لتحليل البيانات")
st.write("اسأل عن بياناتك بصيغة بسيطة، مثل:")
st.markdown("""
- عدد الصفوف
- ما هي الأعمدة؟
- ما هو متوسط عمود معين؟
- ما هي القيم الفريدة في عمود معين؟
""")

# مدخل المستخدم
user_input = st.text_input("✍️ اكتب سؤالك هنا")

# تحليل السؤال والرد
if user_input:
    user_input_lower = user_input.lower()

    if "عدد الصفوف" in user_input_lower:
        st.write(f"🔢 عدد الصفوف هو: {df.shape[0]}")

    elif "عدد الأعمدة" in user_input_lower:
        st.write(f"🔢 عدد الأعمدة هو: {df.shape[1]}")

    elif "الأعمدة" in user_input_lower:
        st.write("🧾 الأعمدة هي:")
        st.write(df.columns.tolist())

    elif "متوسط" in user_input_lower:
        for col in df.select_dtypes(include='number').columns:
            if col.lower() in user_input_lower:
                st.write(f"📉 متوسط العمود '{col}' هو: {df[col].mean():.2f}")
                break
        else:
            st.warning("❗ لم يتم التعرف على العمود. حاول كتابة اسمه كما هو بالضبط.")

    elif "أقصى" in user_input_lower or "أعلى" in user_input_lower:
        for col in df.select_dtypes(include='number').columns:
            if col.lower() in user_input_lower:
                st.write(f"📈 أعلى قيمة في العمود '{col}' هي: {df[col].max()}")
                break
        else:
            st.warning("❗ لم يتم التعرف على العمود.")

    elif "فريدة" in user_input_lower or "فريد" in user_input_lower:
        for col in df.columns:
            if col.lower() in user_input_lower:
                st.write(f"🧬 القيم الفريدة في العمود '{col}':")
                st.write(df[col].unique())
                break
        else:
            st.warning("❗ لم يتم التعرف على العمود.")

    else:
        st.warning("🤔 لم أفهم سؤالك. حاول استخدام نمط بسيط من الأسئلة.")
