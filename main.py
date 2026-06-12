import streamlit as st
import google.generativeai as genai

# API Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# App UI
st.title("🚀 Sales-Driven Marketing Engine")
product_url = st.text_input("Product ka link yahan daalein:")

if st.button("Generate Strategy"):
    if product_url:
        with st.spinner('AI Marketing strategy bana raha hai...'):
            # Prompt ko aur behter banaya taake wo sales par focus kare
            prompt = f"""
            Aap ek professional digital marketer hain. Is product link ko analyze karein: {product_url}.
            Mujhe in teeno cheezon ke liye sales-focused plan dein:
            1. Pinterest: 3 Pin titles aur descriptions (SEO tags ke saath).
            2. Instagram: 3 engaging posts aur hashtags.
            3. Facebook: Ek sales-driving ad copy.
            """
            response = model.generate_content(prompt)
            st.markdown(response.text)
    else:
        st.warning("Please link enter karein!")
