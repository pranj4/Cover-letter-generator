from PyPDF2 import PdfReader
import docx
from prompts.job_extractor_prompt import job_extractor_prompt
from prompts.cover_letter_prompt import cover_letter_prompt
from groq import Groq
import requests

# --- Resume Parsing ---
def extract_resume_text(uploaded_file):
    """Extract text from PDF or DOCX uploaded via Streamlit."""
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text.strip()

# --- Fetch Raw HTML ---
def fetch_raw_html(url):
    """Fetch raw HTML content from a URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching URL: {e}"

# --- Groq API Call ---
def groq_api_call(prompt, api_key, model="llama3-8b-8192"):
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content


# --- HuggingFace model ---
def hf_api_call(prompt, api_key, model="google/flan-t5-base"):
    """
    Send prompt to Hugging Face Inference API and return response.
    """
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": prompt}

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{model}",
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code == 200:
        data = response.json()
        # HF returns list of dicts or generated_text key
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif "error" in data:
            return f"Error: {data['error']}"
        else:
            return str(data)
    else:
        return f"Error {response.status_code}: {response.text}"



# --- Unified Job Description Extraction ---
def extract_job_description(html_content, api_key, provider):
    """
    Extract job description from HTML using selected provider ('groq' or 'huggingface').
    """
    limited_html = html_content[:4000] if html_content else ""
    prompt = job_extractor_prompt(limited_html)
    if provider == "groq":
        return groq_api_call(prompt, api_key)
    elif provider == "huggingface":
        return hf_api_call(prompt, api_key)
    else:
        raise ValueError(f"Unknown provider: {provider}")

# --- Cover Letter Generation ---
def generate_cover_letter(resume_text, job_description, style, api_key):
    prompt = cover_letter_prompt(resume_text, job_description, style)
    return groq_api_call(prompt, api_key)
