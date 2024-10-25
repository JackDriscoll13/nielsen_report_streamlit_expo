import streamlit as st

def download_html_file(filepath, name):
    with open(filepath, "rb") as file:
        btn = st.download_button(
                label=f"Download {name}",
                data=file,
                file_name = 'nielsen_report.html',
                mime = 'html'
            )