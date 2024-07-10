import streamlit as st
from scapy.all import *


def icmp_ping(host):
    try:
        # Виконання пінгу за допомогою ICMP пакетів з допомогою scapy
        packet = IP(dst=host) / ICMP()
        reply = sr1(packet, timeout=2, verbose=False)

        if reply:
            return f"Урааа іди включай сімс: {host} доступний!"
        else:
            return f"От блєт, читай книжечку і чекай. Could not reach '{host}'"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    st.title('ICMP Ping Checker')

    host = st.text_input('Пиши IP:')

    if st.button('Ping'):
        if host:
            st.write(f'Pinging {host}...')
            result = icmp_ping(host)
            st.write(result)


if __name__ == '__main__':
    main()
