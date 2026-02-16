import streamlit as st
import pandas as pd
import time
import os
import plotly.express as px

st.set_page_config(page_title="AI-IDS", layout="wide")


st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #00ffcc; }
    [data-testid="stMetricValue"] { color: #00ffcc; font-family: 'Courier New'; }
    </style>
    """, unsafe_allow_html=True)

st.title("AI-IDS: BEHAVIORAL ANALYSIS")

def load_data():
    if not os.path.exists("logs.csv") or os.path.getsize("logs.csv") < 60:
        return pd.DataFrame()
    try:
        df = pd.read_csv("logs.csv", engine='python', on_bad_lines='skip')
        df.columns = [c.strip() for c in df.columns]
        return df
    except:
        return pd.DataFrame()

container = st.empty()

while True:
    df = load_data()
    with container.container():
        if df.empty:
            st.info("📡 Scanning network interfaces... Start an attack to see results.")
        else:
            m_df = df[df["prediction"] == "MALICIOUS"]
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Packets Processed", len(df))
            c2.metric("Threats Found", len(m_df))
            c3.metric("Status", "ALARM" if len(m_df) > 5 else "SAFE", delta_color="inverse")

            col1, col2 = st.columns(2)
            with col1:
                fig = px.pie(df, names='prediction', hole=0.5, color='prediction',
                             color_discrete_map={'BENIGN':'#00cc99','MALICIOUS':'#ff4b4b'})
                
                st.plotly_chart(fig, width='stretch', key=f"chart_{time.time()}")
            
            with col2:
                if not m_df.empty:
                    st.subheader("Top Threat Sources")
                    
                    st.bar_chart(m_df['src_ip'].value_counts(), width='stretch')
            
            st.subheader("Live Packet Stream")
            
            st.dataframe(df.tail(10), width='stretch')

    time.sleep(1)