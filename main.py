import streamlit as st
import google.generativeai as genai

# Gemini Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 Free Sales-Driven AI Engine")

product_url = st.text_input("Product Link:")

if st.button("Generate Free Strategy"):
    with st.spinner('Generating...'):
        prompt = f"Analyze {product_url} for sales. Provide SEO keywords, Pinterest/Insta/FB post ideas for high sales."
        response = model.generate_content(prompt)
        st.write(response.text)
