# Setup Instructions for Local Development

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hamdan772/SolarVision.git
   cd SolarVision
   ```

2. **Set up Groq API Key (Optional - for AI features)**
   - Get your free API key from [Groq Console](https://console.groq.com/keys)
   - Copy `.env.example` to `.env`
   - Add your API key to `.env`:
     ```
     GROQ_API_KEY=gsk_your_actual_key_here
     ```
   - **OR** set it in your terminal:
     ```bash
     # Windows PowerShell
     $env:GROQ_API_KEY="gsk_your_actual_key_here"
     
     # Windows CMD
     set GROQ_API_KEY=gsk_your_actual_key_here
     
     # Linux/Mac
     export GROQ_API_KEY=gsk_your_actual_key_here
     ```

3. **Run the local server**
   ```bash
   python server_local.py
   ```

4. **Open in browser**
   Navigate to: `http://localhost:8000/solar_advanced.html`

## Features

- ✅ Real-time solar panel visualization
- ✅ NASA POWER weather data integration
- ✅ Advanced financial calculations (ROI, NPV, Payback)
- ✅ AI-powered investment analysis (with Groq API key)
- ✅ Auto-rotation optimization
- ✅ Building detection via Overpass API

## Notes

- The application works without an API key, but AI features will use fallback analysis
- All weather data and calculations work offline using included NASA POWER CSV files
- Server includes CORS proxies for Overpass API and Groq AI

## Production Deployment

For Vercel deployment, add the environment variable in Vercel dashboard:
```
GROQ_API_KEY=gsk_your_actual_key_here
```
