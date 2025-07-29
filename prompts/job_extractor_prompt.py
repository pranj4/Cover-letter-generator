def job_extractor_prompt(html_content: str) -> str:
    """
    Prompt to extract job description (role, responsibilities, skills) from raw HTML.
    """
    return f"""
You are an expert at extracting structured information from unstructured web pages.

TASK:
Extract ONLY the relevant job description details — role, responsibilities, required skills, and qualifications.
Ignore headers, navigation menus, ads, or unrelated content. Output plain clean text.

HTML Content:
{html_content}
"""
