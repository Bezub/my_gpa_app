import streamlit as st

home_page = st.Page("Home.py", title="Home", default=True)
calc_page = st.Page("pages/gpa_calculator.py", title="GPA Calculator")
trans_page = st.Page("pages/transcript_and_cgpa.py", title="Transcript")
admin_page = st.Page("admin_portal.py", title="Admin Panel")

my_pages = [home_page, calc_page, trans_page]

if st.session_state.get("username") == "mememe":
    my_pages.append(admin_page)

pg = st.navigation(my_pages)
pg.run()
