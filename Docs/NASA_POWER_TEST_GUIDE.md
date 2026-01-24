# Quick Test Guide - NASA POWER Integration

## What to Check

### 1. Open Browser Console
Press `F12` or `Cmd+Option+I` to open Developer Console

### 2. Expected Console Messages

When you click "Calculate Solar Potential", you should see:

```
✅ NASA POWER data loaded successfully
All-Sky records: 150
Clear-Sky records: 150

NASA POWER Data for (24.50, 55.50):
  All-Sky: 6.20 kW-hr/m²/day
  Clear-Sky: 6.50 kW-hr/m²/day
  Cloud Derating Factor: 0.954
  Avg Cloud Cover: 4.6%

✅ NASA POWER Weather Data loaded: {
  avgCloudCover: 4.6,
  sunnyDays: 25,
  partlyCloudyDays: 3,
  cloudyDays: 2,
  cloudDeratingFactor: 0.954,
  condition: "Clear",
  dataSource: "NASA POWER"
}

Cloud Derating Factor: 0.954
```

### 3. Weather Card Should Show
- **Condition**: Clear / Partly Cloudy / Mostly Cloudy / Overcast
- **Temperature**: 25-45°C (varies by month)
- **Cloud Coverage**: Usually 5-15% for UAE
- **Data Source**: "NASA POWER" at bottom of card

### 4. What NOT to See ❌
- ❌ "Open-Meteo API error"
- ❌ "CORS proxy failed"
- ❌ "Using fallback UAE data"
- ❌ "Weather API failed, using defaults"
- ❌ Any mention of "corsproxy.io"

## Test Locations

Try these UAE coordinates:

| Location | Lat | Lon | Expected Cloud Cover |
|----------|-----|-----|---------------------|
| Dubai | 25.2 | 55.3 | 5-10% |
| Abu Dhabi | 24.5 | 54.4 | 5-10% |
| Sharjah | 25.3 | 55.5 | 5-10% |
| Fujairah | 25.1 | 56.3 | 10-15% (coastal) |
| Al Ain | 24.2 | 55.7 | 5-10% |

## Expected Values

### Cloud Derating Factor
- **Dubai/Abu Dhabi**: 0.92 - 0.98 (excellent conditions)
- **Coastal Areas**: 0.88 - 0.95 (slightly more clouds)
- **UAE Average**: 0.90 - 0.96 (world-class solar conditions)

### Monthly Irradiation (All-Sky)
- **Winter (Dec-Feb)**: 4.5 - 5.5 kW-hr/m²/day
- **Spring (Mar-May)**: 6.0 - 7.5 kW-hr/m²/day
- **Summer (Jun-Aug)**: 7.0 - 8.0 kW-hr/m²/day
- **Fall (Sep-Nov)**: 5.5 - 7.0 kW-hr/m²/day

## Troubleshooting

### If NASA POWER data doesn't load:

1. **Check CSV files exist**:
   ```bash
   ls -la "Weather Data/"
   ```
   Should show:
   - POWER_Regional_Monthly_2020_2025.csv
   - POWER_Regional_Monthly_2020_2025-2.csv

2. **Check browser console for errors**:
   - File path issues?
   - CSV parsing errors?

3. **Check server is running**:
   ```bash
   curl http://localhost:8000/
   ```
   Should return HTML

### If PVGIS fails:

1. **Check local server**:
   ```bash
   curl "http://localhost:8000/api/pvgis?lat=25.2&lon=55.3"
   ```

2. **Check internet connection** (for direct PVGIS call)

3. **Console should show**:
   - "✅ PVGIS data loaded successfully"
   - NOT "PVGIS API error" (no fallbacks now!)

## Performance Benchmarks

Expected loading times:

| Operation | Before (Open-Meteo) | After (NASA POWER) |
|-----------|--------------------|--------------------|
| First load | 2-5 seconds | 0.5-1 second |
| Subsequent | 2-5 seconds | <0.1 second (cached) |
| Offline | ❌ Fails | ✅ Works |

## Success Criteria ✅

You're good if you see:
1. ✅ Console shows "NASA POWER data loaded successfully"
2. ✅ Weather card shows "NASA POWER" as data source
3. ✅ Cloud derating factor between 0.88-0.98
4. ✅ No API error messages in console
5. ✅ Weather data loads instantly (<1 second)
6. ✅ Works without internet connection (after first page load)

## Common Issues

### "Failed to load NASA POWER weather data"
**Cause**: CSV files not found or wrong path
**Fix**: Check files are in `/Weather Data/` folder

### "No NASA POWER data found for location"
**Cause**: Location outside UAE coverage (22.5-25.5°N, 51.5-56.5°E)
**Fix**: Select a location within UAE

### "PVGIS API error"
**Cause**: PVGIS server down or internet issue
**Note**: This is expected now - no fallback provided
**Fix**: 
- Check internet connection
- Try local proxy: make sure `server.py` is running
- Wait and retry (PVGIS might be temporarily down)

---

**Quick Test**: Click any UAE location → Draw roof → Calculate
**Expected**: See NASA POWER messages in console, weather card shows data
**Time**: < 2 seconds total
