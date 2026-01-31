# ☀️ SolarVision - AI-Powered Solar Calculator# ☀️ SolarVision - Advanced Solar Potential Calculator for UAE



<div align="center"><p align="center">

  <img src="src/Images/SolarPV%20System%20Overview.jpg" alt="SolarVision Banner" width="100%">

![SolarVision Banner](https://img.shields.io/badge/☀️_SolarVision-AI_Powered_Solar_Calculator-FACC15?style=for-the-badge&labelColor=0F172A)</p>



**Professional Solar Energy Calculator for UAE | 2026 NASA POWER Data**<div align="center">



[![NASA POWER](https://img.shields.io/badge/NASA-POWER_Data-0B3D91?style=flat-square&logo=nasa)](https://power.larc.nasa.gov/)<h1 align="center">☀️ SolarVision</h1>

[![AI Powered](https://img.shields.io/badge/AI-Groq_LLaMA_3.3-FACC15?style=flat-square)](https://groq.com/)

[![Leaflet.js](https://img.shields.io/badge/Maps-Leaflet.js-199900?style=flat-square&logo=leaflet)](https://leafletjs.com/)<p align="center">

[![License](https://img.shields.io/badge/License-MIT-10B981?style=flat-square)](LICENSE)  <strong>AI-Powered Solar Panel Calculator using NASA Satellite Data</strong>

</p>

[🚀 Features](#-features) • [📦 Installation](#-installation) • [🎯 Usage](#-usage) • [🔧 API Setup](#-api-setup) • [🤝 Contributing](#-contributing)

<p align="center">

</div>  <img src="https://img.shields.io/badge/NASA-POWER_Data-0B3D91?style=flat-square&logo=nasa">

  <img src="https://img.shields.io/badge/AI-Groq_Powered-EAB308?style=flat-square">

---  <img src="https://img.shields.io/badge/Maps-Leaflet.js-199900?style=flat-square&logo=leaflet">

  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square">

## 🌟 Overview</p>



**SolarVision** is a cutting-edge web application that calculates solar energy potential for rooftops in the **United Arab Emirates**. By combining **real NASA satellite data**, **AI-powered analysis**, and **interactive mapping**, it provides accurate solar production estimates, financial projections, and environmental impact assessments.[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Keys](#-api-keys-setup) • [Contributing](#-contributing)



### Why SolarVision?</div>



- 🛰️ **Real Data**: Uses NASA POWER satellite irradiation data (2020-2026)---

- 🤖 **AI-Optimized**: LLaMA 3.3 70B provides intelligent recommendations

- 🏢 **Smart Detection**: Auto-detects buildings from OpenStreetMap## 📖 Overview

- 📊 **Complete Analysis**: Energy, financial, and environmental insights

- 🌙 **Modern UI**: Beautiful dark mode with glassmorphism design**SolarVision** is a modern web-based solar energy calculator designed for the **UAE region**. It combines real **NASA POWER satellite irradiation data** with **AI-powered optimization** to accurately estimate rooftop solar energy production and financial returns.

- ⚡ **Real-Time**: Live weather data and instant calculations

Unlike basic calculators, SolarVision accounts for **cloud cover, heat losses, dust, degradation**, and **local UAE electricity pricing**.

---

---

## ✨ Features

## ✨ Key Features

### 🎯 Core Capabilities

| Feature | Description |

| Feature | Description ||---------|-------------|

|---------|-------------|| 🛰️ **NASA POWER Data** | Real satellite solar irradiation data (2020-2025) |

| **NASA POWER Integration** | Real satellite solar irradiation data covering 2020-2026 || 🤖 **AI Analysis** | Groq LLaMA 3.3 powered recommendations |

| **AI Analysis** | Groq LLaMA 3.3 70B provides personalized recommendations || 🗺️ **Interactive Map** | Draw/auto-detect roof areas with Leaflet.js |

| **Interactive Maps** | Draw or auto-detect roof areas with Leaflet.js || 🏢 **Smart Building Detect** | Auto-detects buildings from OpenStreetMap with multi-select capability |

| **Smart Building Detection** | Automatically detect buildings from OpenStreetMap || 📊 **Financial Analysis** | ROI, payback period, 25-year projections |

| **Multi-Building Selection** | Select multiple buildings for complex installations || ☀️ **Panel Visualization** | See panels rendered on your actual roof |

| **Automatic Panel Optimization** | AI calculates optimal panel rotation (20-40% more panels) || 🌙 **Dark Mode** | Eye-friendly dark theme support |

| **Solar Panel Visualization** | See panels rendered on your actual roof in real-time |

| **Financial Projections** | 25-year ROI, payback period, and savings analysis |---

| **Weather Integration** | Real-time weather data from Open-Meteo API |

| **Environmental Impact** | CO₂ reduction and tree planting equivalents |## 🎯 What Can It Do?

| **PDF Export** | Professional reports with all data and visualizations |

| **Dark Mode** | Eye-friendly dark theme with glowing effects |- ✅ Estimate monthly and annual solar energy production

- ✅ AI-optimized panel orientation and layout

### 📊 What You Get- ✅ Roof detection via OpenStreetMap buildings

- ✅ **Multi-building selection** for complex installations

- ✅ Monthly and annual energy production estimates- ✅ Installation cost, ROI, and payback period calculation

- ✅ Installation costs and financial ROI- ✅ Interactive map-based workflow

- ✅ Payback period calculation- ✅ Environmental impact (CO₂ reduction, trees equivalent)

- ✅ 25-year financial projections

- ✅ Environmental impact metrics---

- ✅ AI-powered optimization suggestions

- ✅ Interactive roof visualization## 🚀 Quick Start

- ✅ Exportable PDF reports

### How to Use:

---

1. Open the app at `http://localhost:8000/solar_advanced.html`

## 🚀 Quick Start2. Search for your UAE location

3. Click **🧠 Smart Building Detect** to auto-detect buildings

### Prerequisites4. **Single-Select Mode (Default)**: Click any building to select it

5. **Multi-Select Mode**: 

- Python 3.9 or higher   - Click **Multi-Select: OFF** to enable multi-select

- A Groq API key (free at [groq.com](https://groq.com/))   - Click multiple buildings to combine them

- Modern web browser (Chrome, Firefox, Safari, Edge)   - Click **Apply Selected** when ready

6. Adjust panel count with the slider if needed

### Installation7. Click **Calculate Solar Potential** for complete analysis



1. **Clone the repository**---

   ```bash

   git clone https://github.com/Hamdan772/SolarVision.git## 🏢 Smart Building Detection Features

   cd SolarVision

   ```### Single-Select Mode (Default)

- Click any detected building

2. **Create virtual environment**- Automatically applies as roof outline

   ```bash- Instant panel calculation

   python3 -m venv .venv

   source .venv/bin/activate  # On Windows: .venv\Scripts\activate### Multi-Select Mode (NEW!)

   ```- Enable with **Multi-Select: OFF** button

- Click multiple buildings to combine

3. **Install dependencies**- Selected buildings turn **green**

   ```bash- Click again to deselect

   pip install -r src/requirements.txt- Click **Apply Selected (X)** to merge all selected buildings

   ```- Perfect for:

  - Commercial complexes with multiple roofs

4. **Set up environment variables**  - Industrial facilities

   ```bash  - Residential compounds

   cp .env.example .env  - Adjacent building combinations

   # Edit .env and add your Groq API key:

   # GROQ_API_KEY=your_api_key_here### Visual Feedback

   ```- **Yellow buildings**: Available to select

- **Green buildings**: Currently selected (multi-select mode)

5. **Run the server**- **Numbered markers**: Easy building identification

   ```bash- **Tooltips**: Show area, type, and name on hover

   python3 server_local.py

   ```---



6. **Open in browser**## 🛠️ Tech Stack

   ```

   http://localhost:8000/solar_advanced.html| Category | Technology |

   ```|----------|------------|

| **Frontend** | HTML5, CSS3, JavaScript ES6+ |

---| **Mapping** | Leaflet.js 1.9.4, OpenStreetMap, Turf.js 7.1.0 |

| **Charts** | Chart.js 4.4.0 |

## 🎯 Usage Guide| **AI** | Groq API (LLaMA 3.3 70B) |

| **Data** | NASA POWER API, Open-Meteo |

### Basic Workflow| **Backend** | Python 3.9+, Flask |



1. **Search Location**---

   - Enter a UAE address or landmark

   - Map will zoom to your location## 📦 Installation



2. **Select Roof Area**### Prerequisites

   - **Option A**: Click "🧠 Smart Building Detect" to auto-detect buildings

   - **Option B**: Click "Draw Roof" and trace your roof manually- **Python 3.9+** (for backend server)

   - **Option C**: Enable "Multi-Select" to combine multiple buildings- **Modern Web Browser** (Chrome, Firefox, Safari, Edge)

- **Git** (for cloning repository)

3. **Review Panel Configuration**- **Groq API Key** (optional, for AI features)

   - System automatically optimizes panel rotation

   - Adjust panel count with slider if needed### Setup Steps

   - See instant visual feedback on the map

1. **Clone the Repository**

4. **Calculate**   ```bash

   - Click "Calculate Solar Potential"   git clone https://github.com/Hamdan772/SolarVision.git

   - View results in organized tabs:   cd SolarVision

     - 📊 **Quick Summary**: Key metrics at a glance   ```

     - 🌤️ **Weather Data**: Real-time conditions and forecasts

     - 🤖 **AI Analysis**: Personalized recommendations2. **Install Dependencies**

   ```bash

5. **Export Report**   pip install -r src/requirements.txt

   - Click "Download PDF Report"   ```

   - Get a professional document with all data   

   Required packages:

### Advanced Features   - `flask` - Web server

   - `requests` - HTTP requests

#### Multi-Building Selection   - `python-dotenv` - Environment variable management

Perfect for commercial properties or adjacent buildings:

3. **Set Up API Key (Optional)**

1. Click **"Multi-Select: OFF"** to enable multi-select mode   

2. Click multiple buildings on the map (they turn green)   For AI features, get a free Groq API key from [console.groq.com](https://console.groq.com)

3. Click **"Apply Selected (X)"** to combine them   

4. System calculates total roof area and optimal panel layout   ```bash

   # Option 1: Environment variable (temporary)

#### Manual Drawing Tools   export GROQ_API_KEY='your_key_here'

- **Draw Polygon**: Trace complex roof shapes   

- **Draw Rectangle**: Quick rectangular selections   # Option 2: .env file (permanent)

- **Edit Shapes**: Modify existing selections   echo 'GROQ_API_KEY=your_key_here' > .env

- **Delete Shapes**: Remove unwanted areas   ```



---4. **Start the Server**

   ```bash

## 🔧 API Setup   python3 server_local.py

   ```

### Groq API Key (Required)

5. **Open in Browser**

SolarVision uses Groq's AI for intelligent analysis:   ```

   http://localhost:8000/solar_advanced.html

1. Visit [console.groq.com](https://console.groq.com/)   ```

2. Sign up for a free account

3. Generate an API keyThat's it! 🎉

4. Add to `.env` file:

   ```---

   GROQ_API_KEY=gsk_your_actual_key_here

   ```## 📖 User Guide



### Other APIs (Automatic)### Basic Workflow



These work out of the box:1. **Search Location**: Enter a UAE address or location name

- **NASA POWER**: No key required (public data)2. **Detect Buildings**: Click "🧠 Smart Building Detect"

- **Open-Meteo**: No key required (free weather API)3. **Select Buildings**:

- **OpenStreetMap**: No key required (open data)   - **Single building**: Click any building

   - **Multiple buildings**: Enable Multi-Select, click buildings, then Apply

---4. **Adjust Panels**: Use slider to fine-tune panel count

5. **Calculate**: Click "Calculate Solar Potential" for full analysis

## 🏗️ Project Structure6. **Review**: See monthly production, financial projections, and ROI



```### Multi-Building Selection Tips

SolarVision/

├── solar_advanced.html      # Main calculator application- Perfect for commercial complexes or adjacent properties

├── index.html               # Landing page- Select up to 10+ buildings at once

├── server_local.py          # Local development server- Green highlighting shows selected buildings

├── vercel.json             # Production deployment config- Click selected buildings again to deselect

├── api/- All selected buildings merge into one analysis

│   ├── groq.py            # Groq AI API endpoint

│   └── overpass.py        # OpenStreetMap building detection### Drawing Custom Roof Shapes

├── data/

│   └── Weather Data/      # NASA POWER CSV data (2020-2026)If buildings aren't detected:

└── src/1. Use the drawing tools on the left side of the map

    ├── requirements.txt   # Python dependencies2. Click the polygon tool

    ├── server.py         # Production server3. Click points around your roof

    └── SolarPV/          # Legacy solar calculation modules4. Double-click to complete the shape

```

---

---

## 🔑 API Keys Setup

## 🎨 Technology Stack

### Groq API (Required for AI Features)

### Frontend

- **HTML5/CSS3**: Modern, responsive design**SolarVision uses Groq AI for intelligent recommendations.**

- **JavaScript ES6+**: Interactive functionality

- **Leaflet.js 1.9.4**: Interactive maps#### Get Your Free API Key

- **Turf.js 7.1.0**: Geospatial calculations

- **Chart.js 4.4**: Data visualization1. Visit [console.groq.com](https://console.groq.com)

- **jsPDF**: PDF report generation2. Sign up for a free account

3. Navigate to API Keys section

### Backend4. Create a new API key (starts with `gsk_`)

- **Python 3.9+**: Server runtime5. Copy the key

- **Flask 3.0**: Web framework

- **Pandas**: Data processing#### Set the Environment Variable

- **Requests**: API communication

**Option 1: Temporary (current session)**

### APIs & Data```bash

- **NASA POWER**: Solar irradiation dataexport GROQ_API_KEY='your_key_here'

- **Groq (LLaMA 3.3 70B)**: AI analysis```

- **Open-Meteo**: Weather forecasts

- **OpenStreetMap Overpass**: Building detection**Option 2: Permanent (add to shell profile)**

```bash

---# For zsh (macOS default)

echo 'export GROQ_API_KEY="your_key_here"' >> ~/.zshrc

## 🌍 Features Deep Divesource ~/.zshrc



### Automatic Panel Optimization# For bash

echo 'export GROQ_API_KEY="your_key_here"' >> ~/.bashrc

SolarVision's intelligent algorithm tests multiple panel orientations to maximize roof coverage:source ~/.bashrc

```

- Tests 7 rotation angles (0°, 15°, 30°, 45°, 60°, 75°, 90°)

- Calculates optimal spacing and layout**Option 3: .env file**

- Accounts for roof geometry and constraints```bash

- Typically achieves **20-40% more panels** than manual placementecho 'GROQ_API_KEY=your_key_here' > .env

```

### Financial Calculations

---

Accurate cost analysis based on UAE market rates:

## 📁 Project Structure

- Installation cost: **AED 4,500 per kW**

- Electricity savings: **0.42 AED per kWh**```

- 25-year projection with degradation (0.5% annually)SolarVision/

- ROI calculation with payback period├── index.html              # Landing page

- Net savings after system lifespan├── solar_advanced.html     # Main calculator app

├── server_local.py         # Local development server

### Environmental Impact├── vercel.json             # Vercel deployment config

├── README.md               # Documentation

Every kilowatt-hour counts:│

├── api/                    # Serverless API endpoints

- **CO₂ Reduction**: 0.5 kg per kWh saved│   ├── groq.py             # AI analysis endpoint

- **Tree Equivalent**: 1 tree absorbs ~22 kg CO₂/year│   └── overpass.py         # Building data endpoint

- Lifetime environmental benefit calculations│

- Visual representation of impact├── data/

│   └── Weather Data/       # NASA POWER CSV datasets

### AI Recommendations│

└── src/

LLaMA 3.3 analyzes your specific situation:    ├── server.py           # Production server

    ├── requirements.txt    # Python dependencies

- Location-specific sun exposure patterns    ├── LICENSE             # MIT License

- Optimal system sizing suggestions    ├── Docs/               # Additional documentation

- Maintenance and cleaning recommendations    ├── Images/             # Project images

- ROI optimization strategies    └── SolarPV/            # Solar PV calculation modules

- Seasonal production variations```



------



## 🎯 Use Cases## 🌍 Geographic Coverage



### Residential**Current Support: UAE Only**

- Single-family homes

- Villas and townhouses- Latitude: 22.5°N - 26.5°N

- Apartment buildings (rooftop installations)- Longitude: 51.5°E - 56.5°E

- Includes all seven emirates

### Commercial- Optimized for UAE climate and sun angles

- Office buildings

- Retail centers---

- Warehouses and industrial facilities

- Parking structures## 💰 Cost Calculations



### Industrial### System Pricing (UAE Market Rates)

- Manufacturing plants

- Storage facilities- **Installation Cost**: AED 2,380 per kW

- Logistics centers- **Electricity Rate**: AED 0.38 per kWh (DEWA residential)

- Agricultural facilities- **Panel Specifications**: 550W high-efficiency panels

- **Panel Dimensions**: 1.0m × 1.7m with 2cm gap

---- **Conversion Efficiency**: 21.8%



## 📱 Browser Support### Financial Projections Include



| Browser | Minimum Version |- Initial system cost

|---------|----------------|- Monthly electricity savings

| Chrome | 90+ |- Annual production estimates

| Firefox | 88+ |- Payback period (typically 5-7 years)

| Safari | 14+ |- 25-year ROI projection

| Edge | 90+ |- CO₂ reduction (tons)

- Equivalent trees planted

---

---

## 🔒 Privacy & Data

## 🧪 Testing

- **No user data stored**: All calculations happen in your browser

- **No tracking**: No analytics or cookies### Manual Testing Checklist

- **Secure API calls**: All external requests use HTTPS

- **Local processing**: Weather and map data cached locally- [ ] Search for UAE location works

- [ ] Smart Building Detect finds buildings

---- [ ] Single-select mode selects building

- [ ] Multi-select mode allows multiple selections

## 🐛 Troubleshooting- [ ] Apply Selected combines buildings

- [ ] Panel count slider adjusts panels

### Server won't start- [ ] Calculate Solar Potential shows results

```bash- [ ] Financial analysis displays correctly

# Check Python version- [ ] Charts render properly

python3 --version  # Should be 3.9+- [ ] Dark mode toggles correctly



# Reinstall dependencies### Test Locations

pip install -r src/requirements.txt --upgrade

Try these UAE locations for testing:

# Check port availability- Dubai Marina

lsof -i :8000  # Kill process if port is in use- Abu Dhabi Corniche

```- Sharjah University City

- Ajman Industrial Area

### API errors- Ras Al Khaimah Downtown

- Verify `.env` file exists with valid `GROQ_API_KEY`

- Check internet connection---

- Ensure firewall allows outbound HTTPS

## 🐛 Known Limitations

### Building detection not working

- Zoom in closer to your location- Roof detection depends on OpenStreetMap data quality

- Try drawing manually if building data is incomplete- AI features require Groq API key

- Some rural areas may have limited OpenStreetMap coverage- Solar estimates are calculations, not guarantees

- Financial model assumes stable electricity rates

### Calculations seem incorrect- Panel degradation simplified to linear model

- Verify location is within UAE- No real-time shading analysis yet

- Check roof area is reasonable (>20 m²)

- Ensure panel count slider is set appropriately---



---## 🚀 Deployment



## 🚀 Deployment### Local Development



### Local Development```bash

```bashpython3 server_local.py

python3 server_local.py```

```

### Production (Vercel)

### Production (Vercel)

```bashThe project is configured for Vercel deployment:

vercel --prod

```1. Push to GitHub

2. Import project in Vercel

The app is configured for Vercel with Python serverless functions. All API routes are automatically handled.3. Add environment variable: `GROQ_API_KEY`

4. Deploy

---

API endpoints are serverless functions in `/api` folder.

## 🤝 Contributing

---

Contributions are welcome! Here's how:

## 🤝 Contributing

1. Fork the repository

2. Create a feature branch: `git checkout -b feature/amazing-feature`Contributions are welcome! Please follow these steps:

3. Commit changes: `git commit -m 'Add amazing feature'`

4. Push to branch: `git push origin feature/amazing-feature`1. Fork the repository

5. Open a Pull Request2. Create a feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

### Development Guidelines4. Push to the branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

- Follow existing code style

- Test all changes locally### Development Guidelines

- Update documentation as needed

- Keep commits focused and descriptive- Follow existing code style

- Test thoroughly before submitting

---- Update documentation for new features

- Add comments for complex logic

## 📄 License- Keep commits focused and atomic



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.---



---## 📜 License



## 🙏 AcknowledgmentsMIT License — see [LICENSE](src/LICENSE)



- **NASA POWER Project**: For providing free satellite solar data---

- **Groq**: For AI inference infrastructure

- **OpenStreetMap**: For building footprint data## 👨‍💻 Contributors

- **Open-Meteo**: For weather forecast data

- **Leaflet.js**: For beautiful interactive maps- **Hamdan Nishad** - [GitHub](https://github.com/Hamdan772)



------



## 📧 Contact & Support## 🙏 Acknowledgments



- **GitHub Issues**: [Report bugs or request features](https://github.com/Hamdan772/SolarVision/issues)- **NASA POWER** - Solar irradiation data

- **GitHub**: [@Hamdan772](https://github.com/Hamdan772)- **OpenStreetMap** - Building footprint data

- **Groq** - AI-powered analysis

---- **Leaflet.js** - Interactive mapping

- **Chart.js** - Data visualization

## 🌟 Star History- **Turf.js** - Geospatial calculations



If you find SolarVision useful, please consider giving it a star on GitHub! ⭐---



---## 📧 Contact



<div align="center">For questions, suggestions, or support:



**Made with ☀️ for the UAE Solar Future**- GitHub Issues: [SolarVision Issues](https://github.com/Hamdan772/SolarVision/issues)

- Repository: [github.com/Hamdan772/SolarVision](https://github.com/Hamdan772/SolarVision)

[⬆ Back to Top](#️-solarvision---ai-powered-solar-calculator)

---

</div>

<div align="center">

**Made with ☀️ for a sustainable future**

⭐ Star this repo if you find it helpful!

</div>
