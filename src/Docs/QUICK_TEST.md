# Testing Guide - AI SolarVision

## Quick Test Checklist

### ✅ Step 1: Open Application
- Server running: http://localhost:8000
- Open: http://localhost:8000/solar_advanced.html
- Check console for errors (F12 → Console)

### ✅ Step 2: Test Weather API (Open-Meteo)
1. Click "📍 Locate Me" or search for "Dubai"
2. Wait for location to load
3. **Expected Result:**
   - Weather card appears in sidebar
   - Shows current temperature and condition
   - Shows 7-day forecast with sunny/cloudy days
   - No API key errors in console

### ✅ Step 3: Test PVGIS API
1. Draw a roof area on the map (or use AI auto-detect)
2. Click "Calculate Solar Potential"
3. **Expected Result:**
   - Loading message: "Fetching PVGIS solar data..."
   - Monthly production chart appears
   - No CORS errors
   - Server console shows: "📡 Proxying PVGIS request"

### ✅ Step 4: Test Building Detection (Overpass)
1. Center map on a building
2. Zoom in close (level 19+)
3. Click "🤖 AI Auto-Detect"
4. **Expected Result:**
   - Status: "🔍 Detecting building at map center..."
   - Building outline appears in blue
   - Roof area calculated
   - Server console shows: "📡 Proxying Overpass request"

### ✅ Step 5: Test AI Insights (Groq)
1. After calculating solar (Step 3)
2. Switch to "AI Insights" tab
3. **Expected Result:**
   - AI analysis appears
   - Cost-benefit analysis shows
   - Panel recommendations display

---

## 🔍 Common Issues & Solutions

### Issue: Weather doesn't load
- **Solution:** Check internet connection
- Open-Meteo API: https://api.open-meteo.com
- Should work without any API key

### Issue: PVGIS returns error
- **Check:** Server is running on port 8000
- **Check:** Terminal shows PVGIS proxy request
- **Try:** Different location (some remote areas not covered)

### Issue: Building detection fails
- **Solution:** Zoom in more (level 19-20)
- **Solution:** Center building exactly in map center
- **Note:** Only works for buildings in OpenStreetMap

---

## 🌍 Test Locations

Good test locations in UAE:

1. **Dubai Mall**
   - Coordinates: 25.1972, 55.2744
   
2. **Burj Khalifa Area**
   - Coordinates: 25.1963, 55.2744

3. **Abu Dhabi**
   - Coordinates: 24.4539, 54.3773

---

**Test Status:** All APIs working ✅
**Last Verified:** January 23, 2026
