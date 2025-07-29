
# AI Cover Letter Generator

## 1. Introduction

The AI Cover Letter Generator is a web application designed to help job seekers quickly create personalized cover letters. By leveraging advanced Large Language Models (LLMs), the app can analyze your resume and a job description to generate a tailored cover letter in seconds. This tool is ideal for anyone who wants to save time and improve the quality of their job applications.

## 2. LLMs Powered by Groq and Hugging Face

This project uses free-tier LLMs provided by Groq and Hugging Face. These platforms offer powerful models such as LLaMA 3 (Groq) and Mistral 7B (Hugging Face) that are accessible via API. By using these free providers, users can generate high-quality cover letters without incurring any cost or needing specialized hardware.

**Why Groq and Hugging Face?**

- Both offer free access to state-of-the-art LLMs for text generation.
- No need for local GPU or cloud compute resources.
- Easy API integration and fast response times.

## 3. Steps to Use the App

Upload Resume:
Users can upload their resume in PDF format. The application extracts the text from the PDF using the pypdf2 library for further processing.

Input Job Listing:
Users may provide either a job listing URL or enter the job description directly as text. The app uses an LLM-powered scraper to extract relevant job and company details from the provided URL.
Note: If a website is difficult to scrape, please use the text input option to manually enter the job description.

Style Selector:
Users can choose the desired style for their cover letter, which determines the prompt used for generation.

The Classic style produces a traditional cover letter with a formal tone and standard length.
The Modern style creates a concise, more casual cover letter.
Generate Cover Letter:
Based on the selected style, resume, and job listing, the app generates a personalized cover letter. The result is displayed in the interface and can be easily copied to the clipboard.
5. **Follow the on-screen instructions:**
   - Enter your API key for Groq or Hugging Face
   - Upload your resume (PDF or DOCX)
   - Enter the job description or provide a job URL
   - Select the style and model
   - Click "Generate Cover Letter"

## 4. Getting API Keys

### Groq API Key

1. Go to the [Groq Console](https://console.groq.com/keys)
2. Sign up or log in to your Groq account
3. Click "Create API Key" and give it a name
4. Copy the generated key
5. Paste the key into the sidebar field in the app

### Hugging Face API Key

1. Go to [Hugging Face Tokens](https://huggingface.co/settings/tokens)
2. Log in or create a Hugging Face account
3. Click "New token" and select "read" access
4. Copy the token
5. Paste the token into the sidebar field in the app

## 5. Deployment


- https://coverletterllm.pranj.dev/



## 6. Screenshots

Below are example screenshots of the app in action:

**Home Page:**

<img width="1911" height="971" alt="image" src="https://github.com/user-attachments/assets/1e59c18c-cb61-44ba-8c82-9cc5687d0c9a" />


**Generated Cover Letter:**

<img width="1018" height="515" alt="image" src="https://github.com/user-attachments/assets/3a6a05ad-24a5-4c24-a965-0226abaacd99" />



---


