import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="iDEX Live Intelligence", page_icon="📡", layout="wide")

# 2. Advanced CSS for Real-Time "Pulse" and Aesthetic Light Mode
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #F8FAFC; }

    /* Blinking Pulse Effect for 'Live' feel */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.3; }
        100% { opacity: 1; }
    }
    .live-indicator {
        color: #ef4444;
        font-weight: bold;
        animation: pulse 1.5s infinite;
    }

    /* Metric Card Enhancements */
    div[data-testid="column"] {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC DATA SIMULATION ---
# Current time for the "Last Updated" feel
now = datetime.now().strftime("%d %b %Y | %H:%M:%S")

growth_data = pd.DataFrame({
    'Year': [2021, 2022, 2023, 2024, 2025, 2026],
    'Contracts': [102, 150, 260, 350, 430, 435],
    'Value': [150, 400, 900, 1500, 2100, 2400]
})

# --- 4. HEADER WITH LIVE INDICATOR ---
col_title, col_status = st.columns([3, 1])
with col_title:
    st.title("📡 iDEX Real-Time Impact Command")
    st.markdown(f"**Strategic Dashboard** | February 2026 Deployment")

with col_status:
    st.markdown(f"""
        <div style="text-align: right; padding-top: 20px;">
            <span class="live-indicator">● LIVE FEED</span><br>
            <span style="color: #64748B; font-size: 0.8rem;">Last Sync: {now}</span>
        </div>
    """, unsafe_allow_html=True)

st.write("##")

# --- 5. REAL-TIME METRICS ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Active Startups", "619", "↑ 4 New today")
c2.metric("Procurement Pipeline", "₹2,400 Cr", "Direct AoN")
c3.metric("ADITI Grants", "14 Active", "Strategic Deep-Tech")
c4.metric("Success Rate", "94%", "Prototype to Trial")

st.divider()

# --- 6. INTERACTIVE VISUALS ---
left, right = st.columns([2, 1])

with left:
    st.subheader("📈 Contractual Momentum (Cumulative)")
    # Aesthetic Spline Chart
    fig = px.area(growth_data, x='Year', y='Value',
                  title="Value Flow (₹ Crores)",
                  color_discrete_sequence=['#2563EB'])
    fig.update_layout(
        hovermode="x unified",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=True, gridcolor='#F1F5F9'),
        xaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("🎯 Problem Domains")
    domain_df = pd.DataFrame({
        "Domain": ["AI/ML", "Unmanned", "Space", "Cyber"],
        "Count": [35, 28, 15, 22]
    })
    fig_pie = px.pie(domain_df, values='Count', names='Domain', hole=0.7,
                     color_discrete_sequence=px.colors.sequential.Blues_r)
    fig_pie.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig_pie, use_container_width=True)

# --- 7. "LIVE" PROJECT TRACKER ---
st.subheader("🛡️ Recent Contractual Activity")

# Creating an "Aesthetic" project table
projects = [
    {"Project": "Quantum Key Distribution", "Startup": "QuNu Labs", "Force": "Army", "Status": "✅ Contract Signed"},
    {"Project": "Mini-Satellite Payload", "Startup": "SpacePixxel", "Force": "Air Force", "Status": "⏳ In Testing"},
    {"Project": "Underwater Swarm", "Startup": "SubSea Tech", "Force": "Navy", "Status": "🚀 Field Trials"},
    {"Project": "Fire-Fighting Robot", "Startup": "Milbotix", "Force": "Army", "Status": "📦 Procurement Ready"}
]
st.table(pd.DataFrame(projects))

# --- 8. FOOTER ---
st.info(
    "💡 **Insight:** iDEX just reached its **350th milestone** contract with SpacePixxel for miniaturized satellite development.")