import os
import base64
import requests
from dotenv import load_dotenv


#1. Load Configuration

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("HACKCLUB_API_KEY")
API_URL = os.getenv("HACKCLUB_API_URL")


def _extract_reply(response):
  """Helper to cleanup the API response"""
  if response.status_code == 200:
    return response.json()["choices"][0]["message"]["content"]
  
  return f"Error: API returned {response.status_code}-{response.text}"


def generate_boring_response(message, level="Corporate Drone"):
  """Handles text only Frizzing"""

  if not API_URL:
      return"Error:API_URL not found in .env"
  
  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":"application/json"
  }

  system_instruction = f"""
    You are Frizz AI.
    Convert the user's message into a dry, formal, conversation-ending reply.
    If the message is in Nepali, respond in formal 'Sarkari' Nepali.
    If it is in English, use bureaucratic English.
    Match this boredom level: {level}.
    """

  data = {
    "model":"gpt-4o",
    "messages": [
      {"role":"system","content": system_instruction},
      {"role":"user","content": message}
    ]
  }

  response = requests.post(API_URL, headers=headers, json=data, timeout=60)
  return _extract_reply(response)


def process_screenshot(image_file, level="Corporate Drone"):
  """Handles image-based Frizzing"""

  #Convert the image to a string the API can read
  encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
  mime_type = getattr(image_file,"type","image/jpg")

  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":"application/json" 
  }

#3. The "Personality" Logic
  system_instruction = f"""
You are Frizz AI. Analyze the chat screenshot. 
    1. Identify the last message sent. 
    2. Respond in formal 'Sarkari' Nepali (if Nepali) or Bureaucratic English.
    3. Match boredom level: {level}.
    """

#4. Construct the Request(Note:'messages' is lowercase)
  data ={
    "model":"gpt-4o",
    "messages": [
      {
        "role":"user",
        "content":[
          {"type":"text","text": system_instruction},
          {"type":"image_url","image_url":{"url": f"data:{mime_type};base64,{encoded_image}"}}
        ]            }
    ]
  }

#5. Send to Hack Club API
  response = requests.post(API_URL, headers=headers, json=data, timeout=60)
  return _extract_reply(response)

