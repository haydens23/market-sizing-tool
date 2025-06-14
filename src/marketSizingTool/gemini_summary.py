import google.generativeai as genai
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt
import os

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

@retry(
    wait=wait_exponential(multiplier=1, min=4, max=10),
    stop=stop_after_attempt(3)
)
def generate_summary(business_summary, geography, trend, traits):
    prompt = (
        f"Business Idea: {business_summary}\n"
        f"Geography: {geography}\n"
        f"Market Trend: {trend}\n"
        f"Traits: {traits}\n\n"
        "Provide a detailed market size analysis with the following sections:\n\n"
        "1. KEY ASSUMPTIONS:\n"
        "List 3-5 key assumptions for the market sizing calculation.\n\n"
        "2. CALCULATION METHODOLOGY:\n"
        "Explain your step-by-step calculation approach.\n\n"
        "3. TOTAL ADDRESSABLE MARKET:\n"
        "State the final TAM estimate in USD with a brief explanation.\n\n"
        "Format each section with clear headers as shown above."
    )

    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40
        }
        response = model.generate_content(prompt, generation_config=generation_config)
        
        if not response.text:
            print("Error: Empty response from Gemini")
            return None
            
        # Split response into sections
        text = response.text
        sections = text.split('\n\n')
        
        # Parse sections into dictionary
        summary = {
            'assumptions': '',
            'methodology': '',
            'TAM': ''
        }
        
        current_section = None
        for section in sections:
            if 'KEY ASSUMPTIONS' in section:
                current_section = 'assumptions'
                summary[current_section] = section.replace('1. KEY ASSUMPTIONS:', '').strip()
            elif 'CALCULATION METHODOLOGY' in section:
                current_section = 'methodology'
                summary[current_section] = section.replace('2. CALCULATION METHODOLOGY:', '').strip()
            elif 'TOTAL ADDRESSABLE MARKET' in section:
                current_section = 'TAM'
                summary[current_section] = section.replace('3. TOTAL ADDRESSABLE MARKET:', '').strip()
            elif current_section:
                summary[current_section] += '\n' + section.strip()
        
        return summary
        
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None



