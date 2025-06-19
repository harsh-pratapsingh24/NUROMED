import streamlit as st
from PIL import Image
from ocr_utils import extract_text
from gemini_response import fetch_medicine_info

st.set_page_config(page_title="Nuromed – Medicine Info Scanner", layout="centered")

st.title("💊 Nuromed – AI-Powered Medicine Info Scanner")
st.markdown("OCR + Gemini AI powered tool to scan medicine labels and fetch usage, dosage & side effect information.")

tab1, tab2 = st.tabs(["📷 Upload Image", "📄 About"])

with tab1:
    uploaded_file = st.file_uploader("Upload a clear image of the medicine label", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        
        with st.spinner("🔍 Extracting text from image..."):
            image = Image.open(uploaded_file)
            extracted_text = extract_text(image)
            st.code(extracted_text, language='text')
        
        st.success("✅ Text extracted successfully!")

        with st.spinner("🤖 Fetching AI-generated medicine information..."):
            response = fetch_medicine_info(extracted_text)

        st.subheader("🧠 AI-Based Analysis")
        st.markdown(f"**Medicine Name:** `{response.get('Medicine', 'N/A')}`")
        st.markdown(f"**Dosage:** {response.get('Dosage', 'N/A')}")
        st.markdown(f"**Usage:** {response.get('Use', 'N/A')}")
        st.markdown(f"**Side Effects:** {response.get('Side Effects', 'N/A')}")
        
        if st.button("🔄 Run Again"):
            st.experimental_rerun()

with tab2:
    st.header("📄 About Nuromed")
    st.markdown("""
    **Nuromed** is a research-oriented mini application developed as a demonstration for AI-integrated healthcare tools.

    - Combines **OCR** and **Gemini AI** for smart parsing of medicine labels.
    - Useful for **patients**, **pharmacists**, and **researchers**.
    - Built using Python, Streamlit, and dummy AI responses to simulate real-world use cases.
    
    _Note: This project is part of an ongoing research and is not for medical use._
    """)

st.caption("© 2025 Harsh Pratap Singh | BML Munjal University")
