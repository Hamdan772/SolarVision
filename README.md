<p align="center">
  <img src="src/Images/SolarPV%20System%20Overview.jpg" alt="SolarVision Banner" width="100%">
</p>

<h1 align="center">☀️ SolarVision</h1>

<p align="center">
  <strong>AI-Powered Solar Panel Calculator using NASA Satellite Data</strong>
</p>

<p align="center">
  <a href="https://solarvision-app.vercel.app">
    <img src="https://img.shields.io/badge/🌐_Live_Demo-Visit_Site-EAB308?style=for-the-badge" alt="Live Demo">
  </a>
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

👉 **Live App:** [https://solarvision-app.vercel.app](https://solarvision-app.vercel.app)

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

## 🖥️ Demo

🔗 **[Launch Live Demo](https://solarvision-app.vercel.app)** — No installation required!

### Quick Start:
1. Open the app and go to Calculator
2. Search for your UAE location
3. Click **AI Auto-Detect Building**
4. Adjust panel count if needed
5. Click **Calculate Solar Potential**

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Mapping** | Leaflet.js, OpenStreetMap, Turf.js |
| **Charts** | Chart.js |
| **AI** | Groq API (LLaMA 3.3 70B) |
| **Data** | NASA POWER API |
| **Backend** | Python (Flask) |
| **Deployment** | Vercel |

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

> These are known limitations we're actively working to improve:

- **UAE-Focused**: Optimized for UAE region; global support coming soon
- **OSM Dependency**: Roof detection requires buildings in OpenStreetMap
- **Simplified Financial Model**: Doesn't include maintenance, labor, or panel degradation
- **No Shading Analysis**: Trees, AC units, water tanks not factored in
- **Individual Houses Only**: Multi-building/community analysis not yet supported

---

## 🗺️ Roadmap

- [ ] Global location support with region-specific data
- [ ] AI-based rooftop segmentation (satellite image analysis)
- [ ] Shading/obstacle detection
- [ ] Export PDF reports for installers
- [ ] Community/multi-building analysis
- [ ] Real installation validation

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
  <strong>Rishi</strong><br/>
  <a href="https://github.com/RishiSomanIsASomosa">
    <img src="https://img.shields.io/badge/GitHub-@RishiSomanIsASomosa-181717?style=flat-square&logo=github" alt="GitHub Rishi">
  </a>
</p>

---

<p align="center">
  <strong>Built with ☀️ in the UAE</strong><br>
  Powered by NASA POWER & Groq AI
</p>
