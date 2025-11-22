import google.generativeai as genai
from agentic_automator.config.settings import settings
import time
from typing import Optional

class LLMClient:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.MODEL_NAME)

    def generate(self, prompt: str, system_instruction: Optional[str] = None) -> str:
        """
        Generates text from the LLM with retries.
        """
        full_prompt = prompt
        if system_instruction:
            full_prompt = f"System Instruction: {system_instruction}\n\nUser: {prompt}"

        for attempt in range(settings.MAX_RETRIES):
            try:
                response = self.model.generate_content(full_prompt)
                return response.text
            except Exception as e:
                print(f"Error generating content (Attempt {attempt+1}/{settings.MAX_RETRIES}): {e}")
                time.sleep(2 ** attempt) # Exponential backoff
        
        raise Exception("Failed to generate content after max retries")

llm_client = LLMClient()