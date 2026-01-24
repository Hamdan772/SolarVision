# Testing Guide - Solar Calculator v2.0

## 🧪 Quick Test Procedure

### Step 1: Start Server
```bash
cd /Users/hamdannishad/Downloads/SolarPV-Simulator-master
python3 server.py
```
Server will start on `http://localhost:8000`

### Step 2: Open Application
Navigate to: `http://localhost:8000/solar_advanced.html`

### Step 3: Test Features

#### ✅ Test AI Panel Recommendations
1. Search for a location (e.g., "Dubai Marina")
2. Draw a roof polygon (rectangular shape works best)
3. Click "Calculate Solar Potential"
4. Wait for calculations (shows status updates)
5. Go to **System** tab
6. Verify:
   - ✅ "Recommended Solar Panels" section appears
   - ✅ Shows AI-recommended panel with green border
   - ✅ Shows alternative panel option
   - ✅ Displays specs: Power, Efficiency, Price, Total Cost
   - ✅ Shows feature tags
   - ✅ Includes AI reasoning text

#### ✅ Test Weather Integration
1. After calculation completes
2. Check **System** tab
3. Look for "Cloud Impact" row at bottom of System Overview card
4. Verify:
   - ✅ Shows sunny/partly cloudy/cloudy day counts
   - ✅ Shows "last 30 days" text
   - ✅ Data appears reasonable for UAE

#### ✅ Test Enhanced Charts
**Monthly Production Chart (Production Tab):**
1. Go to **Production** tab
2. Verify:
   - ✅ Bars have gradient fill (orange shades)
   - ✅ Hover shows tooltip with production data
   - ✅ Tooltip shows daily average
   - ✅ Smooth animation on load
   - ✅ Grid lines visible but subtle

**Savings Chart (Financial Tab):**
1. Go to **Financial** tab
2. Verify:
   - ✅ Line chart with gradient fill under curve
   - ✅ Green line for cumulative savings
   - ✅ Red dashed line for break-even
   - ✅ Hover shows "Investment:" or "Profit:" with AED amounts
   - ✅ Break-even year indicator in tooltip
   - ✅ Smooth animation (2 seconds)

#### ✅ Test Improved AI Insights
1. Go to **Impact** tab
2. Scroll to "AI-Powered Insights" section
3. Verify:
   - ✅ Shows "Analyzing comprehensive data with AI..." initially
   - ✅ Analysis appears after ~3-5 seconds
   - ✅ Has 4 numbered points
   - ✅ Bold headers are colored orange
   - ✅ Numbered points are colored green
   - ✅ Mentions weather/cloud impact
   - ✅ Provides actionable recommendations

### Step 4: Check Console
Open browser DevTools (F12) → Console tab

**Look for these logs:**
- ✅ `Weather Data:` (object with cloud data)
- ✅ `Cloud Derating Factor:` (number between 0.7-1.0)
- ✅ `Base Annual Production:` vs `Cloud-adjusted Production:`
- ✅ No red errors related to AI or weather APIs

### Step 5: Test Error Handling

#### Weather API Failure:
- Calculations should still work
- Should show "⚠️ Weather data unavailable" message
- Energy production uses standard 100% factor

#### Panel Recommendation Failure:
- System tab should still show specs
- Panel recommendation section hidden
- No errors in console

#### AI Insights Failure:
- Should show friendly error message
- Mentions "temporarily unavailable"
- Calculations remain valid

## 🎯 Expected Results

### Performance Metrics:
- **Page Load**: < 2 seconds
- **PVGIS Data Fetch**: 2-4 seconds
- **Weather Data Fetch**: 1-2 seconds
- **Panel Recommendation**: 2-3 seconds
- **AI Insights**: 3-5 seconds
- **Total Calculation Time**: ~10-15 seconds

### Data Validation:
- **Panel Count**: Should fit within drawn polygon
- **Rotation**: 0-180° in 5° increments
- **System Size**: Correct based on panel count × 400W
- **Cloud Factor**: Between 0.70 (very cloudy) and 1.00 (clear)
- **Panel Prices**: AED 520-580 per panel
- **Payback**: Typically 4-8 years for UAE

## 🐛 Common Issues & Fixes

### Issue: AI Insights not appearing
**Fix**: Check Groq API key is valid
```javascript
const GROQ_API_KEY = 'YOUR_GROQ_API_KEY_HERE';
```

### Issue: Weather data not loading
**Fix**: Check WeatherAPI key is valid
```javascript
const WEATHER_API_KEY = '4f40250da04d4a2199f181904252201';
```

### Issue: PVGIS data fails
**Fix**: Ensure proxy server is running on port 8000

### Issue: Panel recommendations not showing
**Fix**: 
1. Check console for JSON parse errors
2. AI might return invalid JSON - already has retry logic
3. Check internet connection

### Issue: Charts not rendering
**Fix**: 
1. Ensure Chart.js is loaded (check Network tab)
2. Clear browser cache
3. Check for JavaScript errors

## 📊 Test Data Examples

### Good Test Locations:
- **Dubai Marina**: `25.0772, 55.1397`
- **Abu Dhabi**: `24.4539, 54.3773`
- **Sharjah**: `25.3573, 55.3914`
- **Ajman**: `25.4052, 55.5136`

### Expected Outputs (Dubai Marina, 100m² roof):
- **System Size**: ~3.5 kW (35 panels)
- **Annual Production**: ~5,800-6,200 kWh
- **Peak Sun Hours**: 5.5-6.0 hrs/day
- **Payback**: 5-7 years
- **Cloud Factor**: 0.85-0.95 (mostly sunny)

## ✅ Sign-off Checklist
- [ ] Panel recommendations appear correctly
- [ ] Weather data integrated into calculations
- [ ] Monthly chart has gradient and smooth animations
- [ ] Savings chart shows break-even point
- [ ] AI insights formatted with colors
- [ ] All currency displays show "AED"
- [ ] No console errors during normal operation
- [ ] Panel specifications accurate
- [ ] Weather impact visible in System tab
- [ ] All 5 solar panels in database

---
**Test Date**: January 23, 2026  
**Tester**: _______________  
**Status**: PASS / FAIL  
**Notes**: _______________
