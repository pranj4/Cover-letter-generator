# Configuration file for the Cover Letter Generator

# OpenAI Settings
DEFAULT_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 1000
TEMPERATURE = 0.7

# App Settings
APP_TITLE = "AI Cover Letter Generator"
APP_ICON = "📝"

# Prompt Templates
SYSTEM_PROMPT = "You are a professional career counselor and expert writer specializing in creating compelling cover letters."

COVER_LETTER_PROMPT = """
Generate a professional cover letter based on the following information:

Job Title: {job_title}
Company Name: {company_name}
Job Description: {job_description}

Candidate's Resume/Background: {resume_text}

Please create a personalized, professional cover letter that:
1. Shows enthusiasm for the specific role and company
2. Highlights relevant experience from the resume that matches the job requirements
3. Demonstrates knowledge of the company/role
4. Maintains a professional yet engaging tone
5. Is concise and well-structured
6. Includes a strong opening and closing

Format the cover letter with proper business letter structure including date, company address placeholder, salutation, body paragraphs, and professional closing.
"""
