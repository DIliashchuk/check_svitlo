import streamlit as st
import requests
import subprocess


def is_router_accessible(public_ip):
    try:
        response = requests.get(f'https://{public_ip}', timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False


def ping_ip_address(ip_address):
    try:
        subprocess.check_call(["ping", "-c", "1", ip_address])
        return True
    except subprocess.CalledProcessError:
        return False


st.title("Check Home Power Status")

public_ip = st.text_input("Enter the public IP address of your router:", "YOUR_PUBLIC_IP")
ip_to_ping = st.text_input("Enter the IP address to ping:", "8.8.8.8")  # Default to Google's DNS server

if st.button("Check Light"):
    router_accessible = is_router_accessible(public_ip)
    if router_accessible:
        st.success("Світло є вдома.")
    else:
        st.error("Світла немає вдома.")

    ip_pingable = ping_ip_address(ip_to_ping)
    if ip_pingable:
        st.success(f"Ping to {ip_to_ping} successful.")
    else:
        st.error(f"Ping to {ip_to_ping} unsuccessful.")
