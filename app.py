# The streamlit front end
import streamlit as st
import time

import streamlit_funcs
from nielsen_daily import create_nielsen_reports

st.set_page_config(
        page_title="Nielsen Reports App",
)

st.subheader('Upload Nielsen Data Here:', help= "These files should be able to be dragged straight from your inbox.")
col1, col2 = st.columns(2)
with col1:
    daily_15min_file = st.file_uploader("Upload raw daily 15min file here.")
with col2: 
    daily_dayparts_file = st.file_uploader("Upload raw daily dayparts file here.")

st.write('Current Benchmark Data: **:blue[April]**')

# No html functionality for now
#create_html = st.toggle('Generate HTML Files?', value = False)

email_to = st.selectbox(
    'To whom would you like to send the reports?', 
    ('Keelan.Gallagher@charter.com', 'jack.driscoll@charter.com', 'nathan.hess@charter.com')
)

st.write(' If you are ready, you can generate the report with the button. It will generate the reports and email them, should take a little less than a minute.')

if st.button('Generate Report', type='primary', use_container_width=True):
    with st.spinner('Running Report...'):
        create_nielsen_reports(daily_15min_file, daily_dayparts_file, email_to, generate_html= False)
        time.sleep(1)
        # if create_html: 
        #     st.write('HTML outputs:')
        #     streamlit_funcs.download_html_file('resources/html_exports/file1.html', 'file 1.')
        #     streamlit_funcs.download_html_file('resources/html_exports/file2.html', 'file 2.')
        # else: 
        #     st.write('No html files created.')
        
    st.write('Report Generated! Check your inbox (should come in the next minute or so).')