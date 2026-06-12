import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Sales-Driven Marketing Engine", layout="wide")
st.title("🚀 Sales-Driven Marketing Engine")

# API Configuration
# Yaad rakhein: GEMINI_API_KEY aapke Streamlit Secrets mein hona chahiye
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Naya model update: gemini-pro
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error("API Key ya Configuration mein error hai. Settings > Secrets check karein.")
    st.stop()

# User Input
product_url = st.text_input("Promote karne ke liye Product ya Website ka Link dein:")

if st.button("Generate Full Sales Strategy"):
    if not product_url:
        st.warning("Please link provide karein!")
    else:
        with st.spinner('Generating SEO & Social Media Plan...'):
            prompt = f"""
            Aap ek expert digital marketer hain. Is link ko analyze karein: {product_url}.
            Mujhe sales badhane ke liye ek detailed plan dein:
            1. SEO Package: Keywords, Meta Description, aur Title.
            2. Pinterest: 3 Pin titles/descriptions (SEO optimized).
            3. Instagram: 3 engaging carousel post ideas with viral hashtags.
            4. Facebook: Sales-driving ad copy.
            
            Sab kuch point-wise likhein.
            """
            
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("📋 Marketing Strategy Output")
                st.write(response.text)
                st.success("Strategy ready hai!")
            except Exception as e:
                st.error(f"Error generating content: {e}")
