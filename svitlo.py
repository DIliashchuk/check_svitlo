import streamlit as st
from pythonping import ping


def icmp_ping(host):
    try:
        response_list = ping(host, count=4)
        if response_list.success():
            avg_rtt = sum([r.time_elapsed_ms for r in response_list]) / len(response_list)
            return f"Урааа іди включай сімс: {avg_rtt:.2f} ms"
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
