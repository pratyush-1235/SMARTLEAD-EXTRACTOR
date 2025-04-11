# 🚀 SmartLead Extractor

**AI-Ready Lead Generation Tool** built by **Pratyush Paradarshi Patra** for Caprae Capital’s AI-Readiness Pre-Screening Challenge.

---

## 🧠 What It Does

SmartLead Extractor is a simple yet powerful tool that helps investment and sales teams instantly identify high-quality B2B leads.

It scrapes business contact information (simulated in this demo), assigns a score based on title and description, and allows you to export the results — all from a user-friendly Streamlit interface.

---

## 🔧 Features

- 🔍 Simulated Lead Scraping (mock data that can be replaced with Crunchbase or LinkedIn scraping)
- 🤖 Rule-Based Lead Scoring (e.g., CEO = High, Marketing = Medium, Others = Low)
- 🧪 Streamlit UI for interactive lead filtering
- 📤 CSV Export for CRM or outreach
- 💡 Modular and ready to integrate with GPT-4 or Claude for real AI scoring

---

## 🛠 Tech Stack

- Python 3.9+
- Streamlit
- pandas
- (Optional: OpenAI GPT-4 via API)

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/smartlead-extractor.git
cd smartlead-extractor
pip install -r requirements.txt
streamlit run app.py
