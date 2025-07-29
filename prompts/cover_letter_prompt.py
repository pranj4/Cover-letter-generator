def cover_letter_prompt(resume_text: str, job_description: str, style: str) -> str:
    """
    Prompt to generate cover letter based on resume, job description, and chosen style.
    """
    return f"""
You are a professional career writer specializing in creating tailored cover letters.

STYLE: {style}

TASK:
Write a {style.lower()} cover letter for the following job using details from the resume.
Ensure the tone is professional, personalized, and highlights key skills matching the role.

Resume:
{resume_text}

Job Description:
{job_description}
"""
