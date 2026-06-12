import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Sales-Gen Pro", layout="wide")
st.title("🚀 Sales-Driven Marketing Engine Pro")

product_url = st.text_input("Promote karne ke liye Product ya Website ka Link dein:")

if st.button("Generate Full Sales Strategy"):
    if not product_url:
        st.warning("Link provide karein!")
    else:
        with st.spinner('Generating SEO & Social Assets for all platforms...'):
            
            # Marketing Logic
            prompt = f"""
            Analyze {product_url} for high-conversion sales. Provide:
            1. PINTEREST: 3 Pin titles/descriptions (SEO optimized), 3 specific DALL-E image prompts for pins.
            2. INSTAGRAM: SEO keyword set, 3 Carousel post contents with viral hashtags, 3 DALL-E image prompts.
            3. FACEBOOK: Sales-copy post, SEO-optimized headline, 3 DALL-E image prompts.
            """
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            
            strategy = response.choices[0].message.content
            st.markdown(strategy)
            
            # Automated Image Generation per platform
            platforms = ["Pinterest Ad", "Instagram Post", "Facebook Ad"]
            for platform in platforms:
                st.subheader(f"Generating Image for: {platform}")
                img_prompt = f"High conversion {platform} for {product_url}, professional design, clear CTA, sales focused."
                img_res = client.images.generate(model="dall-e-3", prompt=img_prompt, n=1, size="1024x1024")
                st.image(img_res.data[0].url, caption=f"Visual for {platform}")

st.success("Strategy aur Creative Assets ready hain!")
