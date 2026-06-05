import streamlit as st
from utils.storage_manager import log_neutralized_rizz
from utils.ai_logic import generate_boring_response, process_screenshot
import json
import os

#page configuration
st.set_page_config(page_title="Frizz_AI",page_icon="📉")

#helper function to read logs
def load_archive_history():
    """Read the JSON log file to display permanently in UI sidebar."""
    log_file = "frizz_history.json"
    if os.path.exists(log_file):
        with open(log_file,"r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return[]
    return[]

st.title("📉Frizz_AI")
st.write("Stop the Frizz, Embrace the Rizz")

#Side bar for archives
with st.sidebar:
    st.header("📂Frizz Archives")

    db_history = load_archive_history()

    if not db_history:
        st.write("No records found")
    else:

        for i,record in enumerate(reversed(db_history)):
            st.info(f"Entry {len(db_history) - i} | 📅 {record['timestamp']}")
            st.markdown(f"**Cringe Input:** {record['input_text']}")
            st.markdown(f"**Defense Deployed:**")
            st.code(record['ai_response'])
            st.divider()

#Main input tabs
tab1, tab2 = st.tabs(["Text Mode","Screenshot Mode"])

with tab1:
    user_msg = st.text_area("Paste the message")
    if st.button("Frizz Text"):
        if user_msg:
            import requests
            
            # 1. Isolate the unstable network operation in the try-except block
            try:
                res = generate_boring_response(user_msg)
                network_success = True
            except requests.exceptions.ConnectionError:
                network_success = False
                st.error("📡 Network Connectivity Error: Unable to resolve connection to backend AI server. Please check your internet connection and try again.")
            
            # 2. If the network call succeeded safely, proceed with UI and Storage
            if network_success:
                st.code(res)
                
                # Call your storage layer safely outside the exception check
                log_neutralized_rizz(
                    sender_text=user_msg,
                    generated_defense=res,
                    boredom_score="Severe"
                )
                
                st.rerun()

with tab2:
    img = st.file_uploader("Upload Screenshot",type = ["png","jpg","jpeg"])
    if img and st.button("Frizz Screenshot"):
        res = process_screenshot(img)
        st.code(res)

        log_neutralized_rizz(
            sender_text="[Image Screenshot Uploaded]",
            generated_defense=res,
            boredom_score="Critical"
        )

        st.rerun()
