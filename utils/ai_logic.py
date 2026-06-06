import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image


#1. Load Configuration
load_dotenv()

#the api connection
api_key= os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_boring_response(message, level="Corporate Drone"):
  """Handles text only Frizzing"""

  try:
      
      model = genai.GenerativeModel("gemini-flash-1.5")

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
  """Handles image-based Frizzing"""

  try:
      img = Image.open(image_file)

      model = genai.GenerativeModel("gemini-1.5-flash")

      system_instruction = f"""
You are Frizz AI. Analyze this  chat screenshot carefully. 
    1. Identify the last incoming message sent by other person. 
    2. Convert it into a dry, formal, conversation-ending reply.
    3. If that message is in Nepali,respond in formal 'Sarkari' Nepali (if Nepali).
    4. If it is English, use bureaucratic English.
    5. Match boredom level: {level}.
    6. Provide only the direct-response.
    """
      
      response = model.generate_content([system_instruction,img])
      return response.text.strip()
  
  except Exception as e:
      return f"System Error: Unable to complete vision processing. Details: {str(e)}"


  


  if not API_URL:
      return"Error:API_URL not found in .env"
  
  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":"application/json"
  }

  

  data = {
    "model":"gpt-4o",
    "messages": [
      {"role":"system","content": system_instruction},
      {"role":"user","content": message}
    ]
  }

  response = requests.post(API_URL, headers=headers, json=data, timeout=60)
  return _extract_reply(response)




  #Convert the image to a string the API can read
  encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
  mime_type = getattr(image_file,"type","image/jpg")

  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type":"application/json" 
  }

#3. The "Personality" Logic
  

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

