import streamlit as st
import requests

def is_router_accessible(public_ip):
    try:
        response = requests.get(f'https://{public_ip}', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

st.title("Check Home Power Status")

public_ip = st.text_input("Enter the public IP address of your router:", "YOUR_PUBLIC_IP")

if st.button("Check Light"):
    if is_router_accessible(public_ip):
        st.success("Світло є вдома.")
    else:
        st.error("Світла немає вдома.")
