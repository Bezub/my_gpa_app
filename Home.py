import streamlit as st
from database import supabase, apply_custom_design

apply_custom_design()

st.set_page_config(page_title="Bezub's Academic Portal", layout="wide")

# AUTHENTICATION STATE
if "username" not in st.session_state:
    st.session_state.username = None

def handle_auth():
    st.title("🔐 Academic Portal")
    choice = st.radio("Select Action:", ["Login", "Register"])
    user = st.text_input("Username").lower().strip()
    pwd = st.text_input("Password", type="password")

    if choice == "Register":
        if st.button("Create Account"):
            check = supabase.table("users").select("*").eq("username", user).execute()
            if check.data:
                st.error("Username already taken!")
            elif len(user) < 4 or len(pwd) < 4:
                st.error("Username and Password must be at least 4 characters.")
            else:
                supabase.table("users").insert({"username": user, "password": pwd}).execute()
                st.success("Account created! You can now switch to Login.")
    else:
        if st.button("Login"):
            res = supabase.table("users").select("*").eq("username", user).eq("password", pwd).execute()
            if res.data:
                st.session_state.username = user
                st.rerun()
            else:
                st.error("Invalid username or password.")

# 3. THE GATEKEEPER
if not st.session_state.username:
    handle_auth()
    st.stop()

# 4. SIDEBAR & LOGOUT
with st.sidebar:
    st.success(f"👤 Logged in: **{st.session_state.username}**")
    if st.button("Logout"):
        st.session_state.username = None
        st.rerun()

# 5. LOGGED-IN CONTENT
st.title("🎓 GPA Management System")
st.markdown("> *“The beautiful thing about learning is that no one can take it away from you.”* – B.B. King")

col1, col2 = st.columns(2)
with col1:
    st.info("### 1. Calculate & Save\nHead to the **GPA Calculator** to input your semester grades.")
with col2:
    st.success("### 2. View Progress\nUse the **Transcript** page to see your cumulative GPA.")