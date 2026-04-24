import streamlit as st

# 1. Define the pages
# (Make sure the filenames match exactly what you named them in your folder)
home_page = st.Page("home.py", title="Home", icon="🏠", default=True)
calc_page = st.Page("pages/gpa_calculator.py", title="GPA Calculator", icon="🧮")
trans_page = st.Page("pages/transcript_and_cgpa.py", title="Transcript", icon="📜")
admin_page = st.Page("admin_portal.py", title="Admin Panel", icon="🛡️")

# 2. Start with the pages everyone can see
my_pages = [home_page, calc_page, trans_page]

# 3. THE SECRET CHECK
# Replace "your_username" with your actual login username
if st.session_state.get("username") == "your_username":
    my_pages.append(admin_page)

# 4. Run the navigation
pg = st.navigation(my_pages)
pg.run()