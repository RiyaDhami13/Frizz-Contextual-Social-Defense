import json
import os
from datetime import datetime

def log_neutralized_rizz(sender_text, generated_defense, boredom_score):
  """
  Saves a transaction log of conversations to a permanent JSON file.
  Demonstrates file handling and dictionary data mapping.
  """
  log_file = "frizz_history.json"

  #the structured data entry
  log_entry = {
    "timestamp":datetime.now().strftime("%d-%m-%y %H:%M:%S"),
    "input_text":sender_text,
    "ai_response":generated_defense,
    "boredom_rating":boredom_score
  }

  #checking for the file
  if os.path.exists(log_file):
    with open(log_file,"r") as file:
      try:
        data= json.load(file)
      except json.JSONDecodeError:
        data = []
  
  else:
    data = []   

  #append the new entry and write it to the disk.
  data.append(log_entry)
  with open(log_file,"w") as file:
    json.dump(data,file,indent = 4)

    print("Success! Data securely commited to disk storage.")

#testing quickly
if __name__ == "__main__":
  #simulate a quick application run
  log_neutralized_rizz(
    sender_text = "Hey gorgeous, are you a Wi-Fi router? Because I'm feeling a connection.",
    generated_defense = "This terminal endpoint does not support unsolicited network protocols.Connection closed.",
    boredom_score = "Severe"
  )