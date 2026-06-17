import streamlit as st
import PyPDF2
import google.generativeai as genai

# Configure Gemini API
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Resume Analyzer")
st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

def extract_text(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

if uploaded_file is not None:

    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Extracted Successfully")

    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze the following resume and provide:

        1. Resume Score out of 100
        2. ATS Compatibility Score
        3. Technical Skills Found
        4. Strengths
        5. Weaknesses
        6. Missing Skills
        7. Suggestions for Improvement

        Resume:
        {resume_text}
        """

        response = model.generate_content(prompt)

        st.subheader("Analysis Report")
        st.write(response.text)