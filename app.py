import streamlit as st
from utilis.ai_logic import generate_boring_response, process
from utils.ai_logic import process_screenshot screenshot
st.set_page_config(page_title="Frizz_AI",page_icon="📉")

#--1.Session state
if 'frizz_history' not in st.session_state:
    st.session_state.frizz_history = []

st.title("📉Frizz_AI")
st.write("Stop the Rizz, Embrace the Frizz!")

#--2.Sidebar for archives
with st.sidebar:
    st.header("📂Frizz Archives")
    if not st.session_state.frizz_history:
        st.write("No records found")
for i, record in enumerate(reversed(st.session_state.frizz_history)):
    st.info(f"Entry{len(st.session_state.frizz_history)-i}")
    st.write(record)
    st.divider()

#--3.Main Input tabs
tab1,tab2 = st.tab(["Text Mode","Screenshot Mode"])

with tab1:
    user_msg = st.text_area("Paste the message")
    if st.button("Frizz Text"):
        if user_msg:
            res = generate_boring_response(user_msg)
            st.code(res)
            st.session_state.frizz_history.append(res)
            st.rerun()


with tab2:
    img = st.file_uploader("Upload screenshot",type=["png","jpg","jpeg"])
    if img and st.button("Frizz Screenshot"):
        res = process_screenshot(img)
        st.code(res)
        st.session_state.frizz_history.append(res)
        st.rerun()
