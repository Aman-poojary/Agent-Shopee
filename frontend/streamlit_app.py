import streamlit as st
import requests
import json
from datetime import datetime
import os

# FastAPI backend URL - can be overridden by environment variable
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def test_api_connection():
    """Test API connection and return detailed status"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        return {
            "connected": True,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "data": response.json() if response.status_code == 200 else None,
            "error": None
        }
    except requests.exceptions.ConnectionError as e:
        return {
            "connected": False,
            "status_code": None,
            "response_time": None,
            "data": None,
            "error": f"Connection Error: {str(e)}"
        }
    except requests.exceptions.Timeout as e:
        return {
            "connected": False,
            "status_code": None,
            "response_time": None,
            "data": None,
            "error": f"Timeout Error: {str(e)}"
        }
    except Exception as e:
        return {
            "connected": False,
            "status_code": None,
            "response_time": None,
            "data": None,
            "error": f"Unexpected Error: {str(e)}"
        }

def main():
    st.set_page_config(
        page_title="FastAPI + Streamlit App",
        page_icon="🚀",
        layout="wide"
    )
    
    st.title("🚀 FastAPI + Streamlit Application")
    st.markdown("---")
    
    # Debug information
    with st.expander("🔧 Debug Information"):
        st.write(f"**API Base URL:** {API_BASE_URL}")
        st.write(f"**Environment:** {os.getenv('API_BASE_URL', 'Not set')}")
        
        # Test connection
        connection_status = test_api_connection()
        st.write("**Connection Test:**")
        st.json(connection_status)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Dashboard", "Health Check", "User Management", "API Documentation"]
    )
    
    if page == "Dashboard":
        show_dashboard()
    elif page == "Health Check":
        show_health_check()
    elif page == "User Management":
        show_user_management()
    elif page == "API Documentation":
        show_api_docs()

def show_dashboard():
    st.header("📊 Dashboard")
    
    # API Status with detailed debugging
    st.subheader("API Status")
    
    connection_status = test_api_connection()
    
    if connection_status["connected"] and connection_status["status_code"] == 200:
        st.success("✅ API is running")
        if connection_status["data"]:
            st.json(connection_status["data"])
    else:
        st.error("❌ Cannot connect to API")
        if connection_status["error"]:
            st.error(f"**Error Details:** {connection_status['error']}")
    
    # Quick Stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        api_status = "Online" if connection_status["connected"] and connection_status["status_code"] == 200 else "Offline"
        st.metric("API Status", api_status)
    
    with col2:
        response_time = f"{connection_status['response_time']:.3f}s" if connection_status["response_time"] else "N/A"
        st.metric("Response Time", response_time)
    
    with col3:
        st.metric("Current Time", datetime.now().strftime("%H:%M:%S"))

def show_health_check():
    st.header("🏥 Health Check")
    
    if st.button("Check API Health"):
        with st.spinner("Checking API health..."):
            connection_status = test_api_connection()
            
            if connection_status["connected"] and connection_status["status_code"] == 200:
                st.success("✅ API is healthy!")
                st.json(connection_status["data"])
            else:
                st.error("❌ API is not healthy")
                if connection_status["error"]:
                    st.error(f"**Error:** {connection_status['error']}")
                if connection_status["status_code"]:
                    st.error(f"**Status Code:** {connection_status['status_code']}")

def show_user_management():
    st.header("👥 User Management")
    
    # Create new user
    st.subheader("Create New User")
    
    with st.form("create_user"):
        email = st.text_input("Email", placeholder="user@example.com")
        full_name = st.text_input("Full Name", placeholder="John Doe")
        password = st.text_input("Password", type="password")
        is_active = st.checkbox("Active", value=True)
        
        submitted = st.form_submit_button("Create User")
        
        if submitted:
            if email and full_name and password:
                user_data = {
                    "email": email,
                    "full_name": full_name,
                    "password": password,
                    "is_active": is_active
                }
                
                try:
                    response = requests.post(
                        f"{API_BASE_URL}/api/v1/users/",
                        json=user_data,
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        st.success("✅ User created successfully!")
                        st.json(response.json())
                    else:
                        st.error(f"❌ Error creating user: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Error connecting to API: {str(e)}")
            else:
                st.error("Please fill in all required fields")
    
    # View all users
    st.subheader("All Users")
    
    if st.button("Refresh Users"):
        try:
            response = requests.get(f"{API_BASE_URL}/api/v1/users/", timeout=10)
            if response.status_code == 200:
                users = response.json()
                if users:
                    for user in users:
                        with st.expander(f"User: {user['full_name']} ({user['email']})"):
                            st.json(user)
                else:
                    st.info("No users found")
            else:
                st.error(f"❌ Error fetching users: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error connecting to API: {str(e)}")

def show_api_docs():
    st.header("📚 API Documentation")
    
    st.markdown("""
    ### Available Endpoints
    
    #### Health Check
    - **GET** `/health` - Check API health status
    
    #### Users
    - **GET** `/api/v1/users/` - Get all users
    - **GET** `/api/v1/users/{id}` - Get specific user
    - **POST** `/api/v1/users/` - Create new user
    
    ### Interactive Documentation
    You can also access the interactive API documentation:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Open Swagger UI"):
            st.markdown(f"[Open Swagger UI]({API_BASE_URL}/docs)")
    
    with col2:
        if st.button("Open ReDoc"):
            st.markdown(f"[Open ReDoc]({API_BASE_URL}/redoc)")

if __name__ == "__main__":
    main() 