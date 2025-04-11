import streamlit as st
from scraper import scrape_leads
from lead_scorer import score_lead
from utils import export_to_csv

# Set page configuration
st.set_page_config(
    page_title="SmartLead Extractor 🚀",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS styling for colors and buttons
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stDownloadButton>button {
            background-color: #2196F3;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# UI Layout
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🤖 SmartLead Extractor")
st.subheader("📊 B2B Lead Generation & AI-like Scoring Tool")
st.write("Generate, score, and export leads in seconds. No API keys needed!")
st.markdown("</div>", unsafe_allow_html=True)

# Action Button
if st.button("✨ Extract and Score Leads"):
    with st.spinner("🔍 Scraping and scoring leads..."):
        leads = scrape_leads()

        for lead in leads:
            lead['score'] = score_lead(lead['name'], lead['title'], lead['description'])

    st.success("✅ Leads successfully scored!")
    st.markdown("### 🔍 Scored Leads Table")
    st.dataframe(leads)

    # Export
    csv = export_to_csv(leads)
    with open(csv, "rb") as file:
        st.download_button(
            label="📥 Download Scored Leads (CSV)",
            data=file,
            file_name="smart_leads.csv",
            mime="text/csv"
        )
