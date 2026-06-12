import streamlit as st
import json
from openai import OpenAI

# API Key management
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Sales-Gen AI SaaS", layout="wide")
st.title("🚀 Sales-Driven Marketing Engine")

product_desc = st.text_area("Product ya Offer ka details yahan likhein:")

if st.button("Generate Sales Assets"):
    with st.spinner('Generating content and visuals...'):
        prompt = f"Act as an elite marketer. Create sales-driven strategy for: {product_desc}. Respond in valid JSON format with pinterest_strategy, instagram_facebook_strategy, and a 30-day sales roadmap."
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # JSON output handle karna
        output = response.choices[0].message.content
        st.subheader("Marketing Strategy (JSON)")
        st.json(output)
        
        # Image Generation
        st.subheader("Sales-Driven Visual")
        img_prompt = f"Professional ad design for {product_desc}, high conversion, clean, modern, clear CTA."
        img_response = client.images.generate(model="dall-e-3", prompt=img_prompt, n=1, size="1024x1024")
        
        # Fixed image line
        st.image(img_response.data[0].url)
