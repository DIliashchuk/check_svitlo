import streamlit as st
import socket

def check_router(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # Встановлюємо таймаут на 2 секунди

    try:
        sock.connect((ip_address, port))
        return f"Роутер {ip_address} доступний на порті {port}."
    except socket.error:
        return f"Роутер {ip_address} не доступний на порті {port}."
    finally:
        sock.close()

def main():
    st.title('Перевірка доступності роутера через Socket')

    ip_address = st.text_input('Введіть IP-адресу роутера:')
    port = 443  # Порт HTTP (змініть на потрібний)

    if st.button('Перевірити'):
        if ip_address:
            result = check_router(ip_address, port)
            st.write(result)
        else:
            st.warning('Будь ласка, введіть IP-адресу роутера.')

if __name__ == '__main__':
    main()
