from langchain_ollama import OllamaLLM
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

def analyze_website(summary_text):
    # Connect to Ollama local model
    llm = Ollama(model="mistral")

    prompt = PromptTemplate(
        input_variables=["summary"],
        template="""
You are a website conversion optimization expert.

Analyze the following website summary and identify:
1. Key issues that may reduce conversion rate
2. Explain why each issue affects user behavior

Website Summary:
{summary}

Give clear bullet-point output.
"""
    )

    # Format prompt
    formatted_prompt = prompt.format(summary=summary_text)

    # Call the model directly
    response = llm.invoke(formatted_prompt)

    return response
def improve_website(summary_text):
    llm = Ollama(model="mistral")

    prompt = PromptTemplate(
        input_variables=["summary"],
        template="""
You are a website conversion optimization expert.

Based on the following website summary, generate an improved version of the website content that will increase conversion rate.

You must:
1. Suggest a better headline
2. Improve or rewrite the call-to-action (CTA)
3. Add a trust-building section (testimonials, contact, security, etc.)
4. Keep the content clear and concise

Website Summary:
{summary}

Output the improved website content in a clean, structured format.
"""
    )

    formatted_prompt = prompt.format(summary=summary_text)
    response = llm.invoke(formatted_prompt)

    return response

