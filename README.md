<p align="center">
  <img src="Images/SolarPV%20System%20Overview.jpg" alt="SolarVision Banner" width="100%"/>
</p>

<h1 align="center">☀️ SolarVision</h1>

<p align="center">
  <strong>AI-Powered Solar Panel Calculator with NASA Satellite Data</strong>
</p>

<p align="center">
  <a href="https://solarvision-app.vercel.app">
    <img src="https://img.shields.io/badge/🌐_Live_Demo-Visit_Site-0891B2?style=for-the-badge" alt="Live Demo"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/NASA-POWER_Data-0B3D91?style=flat-square&logo=nasa" alt="NASA POWER"/>
  <img src="https://img.shields.io/badge/AI-Groq_Powered-F97316?style=flat-square" alt="Groq AI"/>
  <img src="https://img.shields.io/badge/Maps-Leaflet.js-199900?style=flat-square&logo=leaflet" alt="Leaflet"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"/>
</p>

---

## 🎯 Overview

**SolarVision** is a professional-grade solar panel calculator that combines NASA satellite irradiation data with AI-powered optimization to provide accurate solar energy projections for the UAE region.

Calculate your solar potential with precision using real satellite measurements, AI-optimized panel layouts, and detailed financial analysis tailored for the UAE market.

### 🌐 Live Demo

**[➡️ Launch SolarVision](https://solarvision-app.vercel.app)**

---

## ✨ Key Features

### 🛰️ NASA POWER Integration
| Feature | Description |
|---------|-------------|
| **Real Satellite Data** | Uses NASA POWER satellite measurements for UAE region |
| **All-Sky Irradiation** | Accounts for actual cloud coverage patterns |
| **Clear-Sky Reference** | Calculates accurate cloud derating factors |
| **Historical Data** | Based on 5+ years of measurements (2020-2025) |
| **Offline Mode** | Works 100% offline after initial data load |

### 🤖 AI-Powered Intelligence
- **Auto Panel Layout** — AI optimizes panel orientation (0°, 45°, 90°, 135°)
- **Building Detection** — Automatic roof outline detection from satellite imagery
- **Smart Recommendations** — AI-powered panel selection based on your needs
- **Maximum Efficiency** — Tests multiple configurations to maximize output

### 📊 Accurate Calculations
- Scientific cloud derating using all-sky vs clear-sky ratios
- Temperature compensation for UAE's hot climate
- Performance ratio accounting for dust, degradation, and system losses
- Monthly and annual production breakdowns

### 💰 UAE Market Specific
- **Currency**: AED pricing with DEWA electricity rates
- **Local Costs**: UAE market panel prices (AED 8.08/W installed)
- **Net Metering**: Export rate calculations for UAE
- **Financial Analysis**: ROI, payback period, 25-year profit projections

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+ (for local development)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Groq API key (optional - for AI features)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Hamdan772/SolarVision.git
cd SolarVision

# 2. Install dependencies (optional for local server)
pip install -r requirements.txt

# 3. Start local server
python server.py

# 4. Open in browser
# Navigate to: http://localhost:8000
```

### Adding Groq API Key (Optional)

To enable AI auto-detection features:

1. Get a free API key from [Groq Console](https://console.groq.com/)
2. Open `solar_advanced.html`
3. Find the line: `const groqApiKey = '';`
4. Add your key: `const groqApiKey = 'gsk_...';`

See [Docs/API_KEY_SETUP.md](Docs/API_KEY_SETUP.md) for detailed instructions.

### Or Visit Live Demo
No installation needed — just visit **[solarvision-app.vercel.app](https://solarvision-app.vercel.app)**

---

## 📖 How to Use

### Method 1: AI Auto-Detect (Recommended)
1. Navigate to the **Calculator** from the landing page
2. Search for your address or click on the map
3. Click **"AI Auto-Detect Building"**
4. AI automatically detects your roof outline
5. Adjust panel count using the slider
6. Click **"Calculate Solar Potential"**

### Method 2: Manual Drawing
1. Click **"Draw Roof Polygon"** in the toolbar
2. Click points around your roof to trace the outline
3. Double-click to complete the shape
4. Adjust settings and calculate

---

## 🔬 Technical Specifications

### Data Sources

| Source | Purpose |
|--------|---------|
| **NASA POWER** | Solar irradiation data (all-sky & clear-sky) |
| **OpenStreetMap** | Building footprints via Overpass API |
| **Groq AI** | LLaMA 3.1 70B for layout optimization |
| **Leaflet.js** | Interactive mapping |

### Calculation Method

```
Annual Energy = System Size × Daily Irradiation × 365 × Efficiency × Deratings

Cloud Derating = All-Sky Irradiation / Clear-Sky Irradiation
```

### System Parameters (2026)

| Parameter | Value |
|-----------|-------|
| Panel Efficiency | 21% |
| Panel Size | 2m × 1m |
| System Efficiency | 85% |
| Performance Ratio | 80% |
| Installation Cost | AED 8.08/W |
| Electricity Rate | AED 0.38/kWh |

### Coverage Area

**UAE Region:**
- Dubai, Abu Dhabi, Sharjah, Ajman, Fujairah, RAK, UAQ
- Latitude: 22.5°N to 25.5°N
- Longitude: 51.5°E to 56.5°E
- Average Irradiation: 5.8-6.4 kWh/m²/day

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white" alt="Leaflet"/>
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js"/>
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel"/>
</p>

---

## 📁 Project Structure

```
SolarVision/
├── index.html              # Landing page
├── solar_advanced.html     # Main calculator application
├── server.py               # Local development server
├── data/
│   └── Weather Data/       # NASA POWER regional data (CSV)
├── Docs/                   # Documentation
├── Images/                 # Assets and screenshots
└── SolarPV/                # Python solar calculation modules
```

---

## 🙏 Acknowledgments

- **[NASA POWER](https://power.larc.nasa.gov/)** — Solar irradiation satellite data
- **[Groq](https://groq.com/)** — Ultra-fast AI inference
- **[OpenStreetMap](https://www.openstreetmap.org/)** — Building footprint data
- **[Leaflet](https://leafletjs.com/)** — Interactive mapping library
- **[Chart.js](https://www.chartjs.org/)** — Data visualization

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developers

<p align="center">
  <strong>Hamdan Nishad</strong><br/>
  <a href="https://github.com/Hamdan772">
    <img src="https://img.shields.io/badge/GitHub-@Hamdan772-181717?style=flat-square&logo=github" alt="GitHub"/>
  </a>
</p>

<p align="center">
  <strong>Rishi</strong><br/>
  <a href="https://github.com/RishiSomanIsASomosa">
    <img src="https://img.shields.io/badge/GitHub-@RishiSomanIsASomosa-181717?style=flat-square&logo=github" alt="GitHub"/>
  </a>
</p>

---

<p align="center">
  <strong>Made with ☀️ in UAE</strong><br/>
  <sub>Powered by NASA POWER + Groq AI</sub>
</p>
