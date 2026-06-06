import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# 1. Load Configuration
load_dotenv()

# The API connection configuration
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_boring_response(message, level="Corporate Drone"):
    """Handles text-only Frizzing using the native Gemini SDK"""
    try:
        # FIX: Changed 'gemini-flash-1.5' to 'gemini-1.5-flash'
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        
        system_instruction = f"""
        You are Frizz AI.
        Convert the user's message into a dry, formal, conversation-ending reply.
        If the message is in Nepali, respond in formal 'Sarkari' Nepali.
        If it is in English, use bureaucratic English.
        Match this boredom level: {level}.
        Do not explain yourself or add conversational filler. Provide only the direct reply.
        """
        
        full_prompt = f"{system_instruction}\n\nUser Message: {message}"
        
        response = model.generate_content(full_prompt)
        return response.text.strip()
        
    except Exception as e:
        return f"System Error: Unable to complete text AI generation. Details: {str(e)}"


def process_screenshot(image_file, level="Corporate Drone"):
    """Handles image-based Frizzing natively with Gemini Vision capabilities"""
    try:
        img = Image.open(image_file)
        
        # FIX: Changed 'gemini-flash-1.5' to 'gemini-1.5-flash'
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        
        system_instruction = f"""
        You are Frizz AI. Analyze this chat screenshot carefully.
        1. Identify the last incoming message sent by the other person.
        2. Convert it into a dry, formal, conversation-ending reply.
        3. If that message is in Nepali, respond in formal 'Sarkari' Nepali.
        4. If it is in English, use bureaucratic English.
        5. Match this boredom level: {level}.
        Provide only the direct response text.
        """
        
        response = model.generate_content([system_instruction, img])
        return response.text.strip()
        
    except Exception as e:
        return f"System Error: Unable to complete image vision processing. Details: {str(e)}"