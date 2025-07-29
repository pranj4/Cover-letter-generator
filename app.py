import streamlit as st
from utils import (
    extract_resume_text,
    fetch_raw_html,
    extract_job_description,
    generate_cover_letter,
)

st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="centered"
, initial_sidebar_state="expanded")

st.title("AI Cover Letter Generator")

st.write("Welcome to the AI Cover Letter Generator! This app will help you create a personalized cover letter for your job applications.")

st.sidebar.header("Model and API settings")

st.sidebar.write("You can select the model you want to use for generating your cover letter. The available options are:")

model = st.sidebar.selectbox(
    "Select a free LLM model",
    ["Groq (LLaMA 3)", "HuggingFace (Mistral-7B-Instruct-v0.3)"],
)

st.sidebar.write("Make sure to enter a valid API key for the selected model.")

api_key = st.sidebar.text_input(
    "Enter your API key",
    type="password"
)

#main content

st.subheader("1.Upload your resume")
resume_file = st.file_uploader("Upload your resume (PDF, DOCX)", type=["pdf", "docx"])

st.subheader("2.Enter job description please")
job_url = st.text_input("Enter the job description URL")
job_description = st.text_area("Or paste the job description here if you are facing issues with job url")

st.subheader("3. Select the style of the cover letter")
style = st.radio(
    "Select the style of the cover letter",
    ["Formal", "Casual", "Creative"]
)

#Generate cover letter button
if st.button("Generate Cover Letter"):
    if not api_key:
        st.error("Please enter your API key.")
    elif not resume_file:
        st.error("Please upload your resume.")
    elif not job_description and not job_url:
        st.error("Please enter the job description or job url.")
    elif not style:
        st.error("Please select the style of the cover letter.")
    else:
        st.success("Generating cover letter...")

        resume_text = extract_resume_text(resume_file)
        job_desc = job_description.strip()
        model_choice = model
        if model_choice.startswith("Groq"):
            provider = "groq"
        elif model_choice.startswith("HuggingFace"):
            provider = "huggingface"
        else:
            provider = "groq"  # Default fallback

        if job_url:
            html_content = fetch_raw_html(job_url)
            job_description = extract_job_description(html_content, api_key, provider)
        else:
            job_description = job_desc

        cover_letter = generate_cover_letter(resume_text, job_description, style, api_key)

        st.subheader("Generated Cover Letter")
        st.text_area("Copy to clipboard:", cover_letter, height=200)