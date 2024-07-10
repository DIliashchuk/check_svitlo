import streamlit as st
import ping3


def icmp_ping(host):
    try:
        result = ping3.ping(host)
        if result is not None:
            return f"Урааа іди включай сімс: {result:.2f} ms"
        else:
            return f"От блєт, читай книжечку і чекай. Could not reach '{host}'"
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    st.title('Перевірка інтернетику')

    host = st.text_input('Пиши IP:')

    if st.button('Ping'):
        if host:
            st.write(f'Pinging {host}...')
            result = icmp_ping(host)
            st.write(result)


if __name__ == '__main__':
    main()
