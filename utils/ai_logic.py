import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HACKCLUB_API_KEY")
API_URL = os.getenv("HACKCLUB_API_URL")



from fastapi import requests


def process_screenshot(image_file, level = "Corporate Drone"):
  #Convert the image to base64
  encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":"application/json" 
  }

# Custom instruction based on the slider level
  system_instruction = f"""
    You are Frizz AI. Analyze the uploaded chat screenshot. 
    1. Identify the last message sent. 
    2. If the message is in Nepali, respond in formal 'Sarkari' Nepali. 
    3. If in English, use bureaucratic English.
    4. Match this boredom level: {level}.
    The goal is to be so dry and formal that the other person stops flirting or joking.
    """


  data ={
    "model":"gpt-4o",
    "messageS": [
      {
        "role":"user",
        "content":[
          {"type":"text","text": system_instruction},
          {"type":"image-url","image-url":{"url": f"data:image/jpeg;base64,{encoded_image}"}}
        ]            }
    ]
  }

  #Notice: No quotes around API_URL variable
  response = requests.post(API_URL, headers=headers, json=data)
  return response.json()['choices'][0]['message']['content']