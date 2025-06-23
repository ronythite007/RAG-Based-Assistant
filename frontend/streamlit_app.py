import streamlit as st
import requests
from enum import Enum

class Role(str, Enum):
    FINANCE = "finance"
    MARKETING = "marketing"
    HR = "hr"
    ENGINEERING = "engineering"
    CEO = "ceo"
    EMPLOYEE = "employee"

st.set_page_config(page_title="RAG Chatbot", layout="wide")

# Title
st.title("📊RAG Chatbot")
st.markdown("#### Role-Based Access Control System\n")

# Initialize session state
if "auth_token" not in st.session_state:
    st.session_state.auth_token = None
    st.session_state.user_role = None
    st.session_state.messages = []

# Login form
if not st.session_state.auth_token:
    with st.form("login_form", clear_on_submit=True):
        st.write("### 🔐 Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            try:
                res = requests.post(
                    "http://localhost:8000/login",
                    json={"username": username, "password": password}
                )
                if res.status_code == 200:
                    token = res.json()["access_token"]
                    st.session_state.auth_token = token
                    st.session_state.user_role = username.split('_')[0] if username != "ceo_user" else "ceo"
                    st.success("Login successful.")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            except Exception as e:
                st.error(f"Login error: {str(e)}")

# Logged-in view
else:
    st.markdown(f"✅ **Logged in as:** `{st.session_state.user_role.upper()}`")
    if st.button("Logout"):
        st.session_state.auth_token = None
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    # Chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                st.caption("Sources: " + ", ".join(msg["sources"]))

    # Chat input
    if prompt := st.chat_input("Type your question here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            res = requests.post(
                "http://localhost:8000/query",
                json={"text": prompt},
                headers={"Authorization": f"Bearer {st.session_state.auth_token}"}
            )
            if res.status_code == 200:
                data = res.json()
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": data["answer"],
                    "sources": data["sources"]
                })
                with st.chat_message("assistant"):
                    st.markdown(data["answer"])
                    if data["sources"]:
                        st.caption("Sources: " + ", ".join(data["sources"]))
            else:
                st.error(f"Error {res.status_code}: {res.text}")
        except Exception as e:
            st.error(f"Request failed: {str(e)}")
