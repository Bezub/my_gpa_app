import streamlit as st
from supabase import create_client

URL = st.secrets["SUPABASE_URL"]
KEY = st.secrets["SUPABASE_KEY"]

@st.cache_resource
def init_connection():
    return create_client(URL, KEY)

supabase = init_connection()

def check_auth():
    if "username" not in st.session_state or st.session_state.username is None:
        st.warning("⚠️ Access Denied. Please log in on the Home page.")
        st.stop()


def apply_custom_design():
    st.markdown("""
    <style>
    /* THE MAIN BACKGROUND - Soft Off-White Lavender */
    .stApp {
        background-color: #F8F4FF !important;
    }

    /* THE SIDEBAR - Light Lavender */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
        background-color: #F3EAFD !important;
        border-right: 1px solid #E1D5F5 !important;
    }

    div[data-testid="stExpander"] {
        background-color: white !important;
        border: 1px solid #E1D5F5 !important;
        border-radius: 12px !important;
    }

    .streamlit-expanderHeader {
        background-color: white !important;
        color: #4A148C !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="input"], .stNumberInput div, .stTextInput div {
        background-color: #F8F4FF !important;
        border-radius: 8px !important;
        border: none !important;
    }

    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #F8F4FF !important;
        color: #4A148C !important;
        border: 1px solid #E1D5F5 !important;
        border-radius: 8px !important;
    }

    /* TEXT COLOR - Force Deep Purple for everything */
    label, p, h1, h2, h3, .stMarkdown {
        color: #4A148C !important;
    }

    /* BUTTONS - Soft Purple buttons with Dark Purple text */
    div.stButton > button:first-child {
        background-color: #E1D5F5 !important; 
        color: #4A148C !important;
        border: 1px solid #D1B3FF !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }

    /* WIDGET ICONS */
    button[pagemediastyle="true"], [data-testid="stIcon"] {
        color: #4A148C !important;
    }
    
    
    .stDeployButton {
        display: none !important;
    }

    #MainMenu {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
        color: #4A148C !important;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)
