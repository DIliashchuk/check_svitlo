import streamlit as st
import subprocess


def icmp_ping(host):
    try:

        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)

        if result.returncode == 0:

            return f"Урааа іди включай сімс:\n{result.stdout}"
        else:
            return f"От блєт, читай книжечку і чекай. Could not reach '{host}':\n{result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    st.title('Перевірка Світла')

    host = st.text_input('Пиши IP:')

    if st.button('Ping'):
        if host:
            st.write(f'Pinging {host}...')
            result = icmp_ping(host)
            st.write(result)


if __name__ == '__main__':
    main()

    host = st.text_input('Пиши IP:')

    if st.button('Ping'):
        if host:
            st.write(f'Pinging {host}...')
            result = icmp_ping(host)
            st.write(result)

if __name__ == '__main__':
    main()
