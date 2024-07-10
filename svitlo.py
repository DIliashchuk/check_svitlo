import streamlit as st
import requests
import socket

def is_router_accessible(public_ip):
    try:
        response = requests.get(f'https://{public_ip}', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def check_ip_connectivity(ip_address):
    try:
        socket.create_connection((ip_address, 80), timeout=5)
        return True
    except OSError:
        return False

st.title("Check Home Power Status")

public_ip = st.text_input("Enter the public IP address of your router:", "YOUR_PUBLIC_IP")

if st.button("Check Light"):
    router_accessible = is_router_accessible(public_ip)
    if router_accessible:
        st.success("Світло є вдома.")
    else:
        st.error("Світла немає вдома.")
    
    ip_to_check = "8.8.8.8"  # Default to Google's DNS server for connectivity check
    ip_pingable = check_ip_connectivity(ip_to_check)
    if ip_pingable:
        st.success(f"Connection to {ip_to_check} successful.")
    else:
        st.error(f"Connection to {ip_to_check} unsuccessful.")
