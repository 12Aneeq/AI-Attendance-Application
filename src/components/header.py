import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/FqzFRrm6/ai-attendance-logo.png"

    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center;"><img src="{logo_url}" style="height:180px; margin-bottom:-40px;" />
        <h1 style="
            text-align:center;
            color:#FFFFFF;
            font-size:60px;
            font-weight:600;white-space: nowrap;">SNAP VOICE
        </h1>
        <h2 style="
            text-align:center;
            color:#FFFFFF;
            font-size:5px;
            font-weight:10;white-space: nowrap;">AI Powered Attendance marking app
        </h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def header_dashboard():

    logo_url = "https://i.ibb.co/FqzFRrm6/ai-attendance-logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>SNAP<br/>VOICE</h2>
        </div>   
                
                """, unsafe_allow_html=True)