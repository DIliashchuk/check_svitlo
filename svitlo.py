import streamlit as st
from ping3 import ping, verbose_ping

def icmp_ping(host):
    try:
        result = ping(host, unit='ms')
        if result is not None:
            return f"Ping successful. Round-trip time: {result:.2f} ms"
        else:
            return f"Ping failed. Could not reach '{host}'"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title('ICMP Ping Checker')
    
    host = st.text_input('Enter IP address or hostname:')
    
    if st.button('Ping'):
        if host:
            st.write(f'Pinging {host}...')
            result = icmp_ping(host)
            st.write(result)

if __name__ == '__main__':
    main()
