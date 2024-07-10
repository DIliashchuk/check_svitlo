import streamlit as st
import requests

def is_router_accessible(router_ip):
    try:
        response = requests.get(f'http://{router_ip}', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

st.title("Check Home Power Status")

router_ip = st.text_input("Enter the IP address of your router:", "192.168.0.1")

if st.button("Check Light"):
    if is_router_accessible(router_ip):
        st.success("Світло є вдома.")
    else:
        st.error("Світла немає вдома.")
