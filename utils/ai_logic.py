import base64
import requests
import os
from dotenv import load_dotenv


#1. Load Configuration
load_dotenv()
API_KEY = os.getenv("HACKCLUB_API_KEY")
API_URL = os.getenv("HACKCLUB_API_URL")


def _extract_reply(response):
  if response.status_code == 200:
    return response.json()["choices"][0]["message"]["content"]

  return f"Error: API returned {response.status_code}-{response.text}"


def generate_boring_response(message, level="Corporate Drone"):
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
  #Convert the image to a string the API can read
  encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":"application/json" 
  }

#3. The "Personality" Logic
  system_instruction = f"""
    You are Frizz AI. Analyze the uploaded chat screenshot. 
    1. Identify the last message sent. 
    2. If the message is in Nepali, respond in formal 'Sarkari' Nepali. 
    3. If in English, use bureaucratic English.
    4. Match this boredom level: {level}.
    The goal is to be so dry and formal that the other person stops flirting or joking.
    """

#4. Construct the Request(Note:'messages' is lowercase)
  mime_type = getattr(image_file, "type", "image/jpeg")
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

# 6. Safety check: Did it work?
  if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
  else:
        return f"Error: API returned {response.status_code} - {response.text}"






def generate_boring_response(text_input, level="Corporate Drone"):
    """Handles text-only Frizzing"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    system_instruction = f"You are Frizz AI. Transform this text into {level} speak. Be boring. Use Sarkari Nepali if the input is Nepali."

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": [{"type":"text", "text":f"{system_instruction}\n\nInput: {text_input}"}]}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    return f"Error: {response.status_code}"