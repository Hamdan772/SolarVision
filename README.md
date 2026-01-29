<p align="center">
  <img src="src/Images/SolarPV%20System%20Overview.jpg" alt="SolarVision Banner" width="100%">
</p>

<h1 align="center">☀️ SolarVision</h1>

<p align="center">
  <strong>AI-Powered Solar Panel Calculator using NASA Satellite Data</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/NASA-POWER_Data-0B3D91?style=flat-square&logo=nasa">
  <img src="https://img.shields.io/badge/AI-Groq_Powered-EAB308?style=flat-square">
  <img src="https://img.shields.io/badge/Maps-Leaflet.js-199900?style=flat-square&logo=leaflet">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">
</p>

---

## 🚀 What is SolarVision?

**SolarVision** is a modern web-based solar energy calculator designed for the **UAE region**. It combines real **NASA POWER satellite irradiation data** with **AI-powered optimization** to accurately estimate rooftop solar energy production and financial returns.

Unlike basic calculators, SolarVision accounts for **cloud cover, heat losses, dust, degradation**, and **local UAE electricity pricing**.


---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🛰️ **NASA POWER Data** | Real satellite solar irradiation data (2020-2025) |
| 🤖 **AI Analysis** | Groq LLaMA 3.3 powered recommendations |
| 🗺️ **Interactive Map** | Draw/auto-detect roof areas with Leaflet.js |
| 📊 **Financial Analysis** | ROI, payback period, 25-year projections |
| ☀️ **Panel Visualization** | See panels rendered on your actual roof |
| 🌙 **Dark Mode** | Eye-friendly dark theme support |

---

## 🎯 What Can It Do?

- ✅ Estimate monthly and annual solar energy production
- ✅ AI-optimized panel orientation and layout
- ✅ Roof detection via OpenStreetMap buildings
- ✅ Installation cost, ROI, and payback period calculation
- ✅ Interactive map-based workflow
- ✅ Environmental impact (CO₂ reduction, trees equivalent)

---


### Quick Start:
1. Open the app and go to Calculator
2. Search for your UAE location
3. Click **AI Auto-Detect Building**
4. Adjust panel count if needed
5. Click **Calculate Solar Potential**

---

## � Recent updates (2026-01-26)
- ⚠️ **Panel rendering update reverted**: A planned center-out spiral placement was briefly implemented but reverted on **2026-01-26** by request. The repository now contains the original grid-based placement (see `src/Docs/FIXES_COMPLETE.md`).

## �🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Mapping** | Leaflet.js, OpenStreetMap, Turf.js |
| **Charts** | Chart.js |
| **AI** | Groq API (LLaMA 3.3 70B) |
| **Data** | NASA POWER API |
| **Backend** | Python |

---

# add GROQ_API_KEY for production
vercel env add GROQ_API_KEY production
```

If `GROQ_API_KEY` is not set, `/api/groq` will return `{"error": "GROQ_API_KEY not configured"}`. Sensitive keys should never be checked into Git.

Environment variables can also be set for `preview` and `development` scopes using `vercel env add <NAME> preview` or `vercel env add <NAME> development`.

---

If you want, I can add a short `DEPLOYMENT.md` with step-by-step instructions, including how to add secrets and enable Git integrations.

---

## ⚙️ Local Development

### Prerequisites
- Python 3.7+
- Modern web browser
- (Optional) Groq API key for AI features

### Setup

```bash
# Clone the repository
git clone https://github.com/Hamdan772/SolarVision.git
cd SolarVision

# Install dependencies
pip install -r src/requirements.txt

# Start the server
python src/server.py
```

Then open: **http://localhost:8000**

### Environment Variables (Optional)
Create a `.env` file for AI features:
```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📁 Project Structure

```
SolarVision/
├── index.html              # Landing page
├── solar_advanced.html     # Main calculator app
├── vercel.json             # Vercel deployment config
├── README.md               # Documentation
│
├── api/                    # Serverless API endpoints
│   ├── groq.py             # AI analysis endpoint
│   └── overpass.py         # Building data endpoint
│
├── data/
│   └── Weather Data/       # NASA POWER CSV datasets
│
└── src/
    ├── server.py           # Local development server
    ├── requirements.txt    # Python dependencies
    ├── Docs/               # Additional documentation
    ├── Images/             # Project images
    └── SolarPV/            # Solar PV calculation modules
```

---

## 🌍 Current Limitations

> Known constraints the team is actively addressing:

- Roof detection depends on OpenStreetMap; buildings must exist in OSM (no AI rooftop segmentation yet)
- Solar output is an estimation; irradiance data is UAE-only and less accurate elsewhere
- Financial model is simplified; maintenance, labor, tariffs, and panel degradation are excluded
- AI panel recommendation is not fully trained; may not match real-world specs or availability
- Limited to individual houses; multi-building or community analysis unsupported
- No shading/obstacle handling; trees, AC units, tanks ignored, which can overestimate output
- No export/report workflow for installers; cannot generate contractor-ready reports
- Geographic defaults are UAE-focused (data, assumptions, currency)
- No validation against real installed systems
- Currently a tool answering “Can I install solar?” rather than a broader platform for change

---

## 🛠️ Planned Improvements / Changes

**Functionality & AI**
- Fix panel rendering when selecting large areas
- Make panel rotation work: rotate panels, remove if they do not fit, re-add if they do
- Auto-set panel rotation to maximize panel count
- Add optimal panel tilt for better efficiency

**UI / UX**
- Remove sign-in button; simplify onboarding
- Remove Twitter and LinkedIn buttons; ensure GitHub button works
- Add dark mode to the landing page and improve dark-mode readability (e.g., AI insights)
- Shift the color theme to yellow for consistency
- Elevate layout, spacing, and overall modern look; improve the landing page first impression

**Code & Structure**
- Organize files into folders (except README); delete unused files
- Remove fallbacks in code; ensure clean console with no errors or broken functionality

**Documentation**
- Improve README with clearer explanation, setup instructions, tech stack, and demo links

---

## 📜 License

MIT License — see [LICENSE](src/LICENSE)

---

## 👨‍💻 Developers

<p align="center">
  <strong>Hamdan Nishad</strong><br/>
  <a href="https://github.com/Hamdan772">
    <img src="https://img.shields.io/badge/GitHub-@Hamdan772-181717?style=flat-square&logo=github" alt="GitHub Hamdan772">
  </a>
</p>

<p align="center">
  <strong>Rishi Rahul</strong><br/>
  <a href="https://github.com/RishiSomanIsASomosa">
    <img src="https://img.shields.io/badge/GitHub-@RishiSomanIsASomosa-181717?style=flat-square&logo=github" alt="GitHub Rishi">
  </a>
</p>


<p align="center">
  <strong>Built with 💖 in the UAE</strong><br>
  Powered by NASA POWER & Groq AI
</p>
