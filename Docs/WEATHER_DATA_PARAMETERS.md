# NASA POWER Weather Data Parameters

## Complete Dataset Overview

The application uses **27 NASA POWER CSV files** with comprehensive solar and atmospheric data for the UAE region.

### Available Parameters

| File | Parameter | Description | Unit | Usage |
|------|-----------|-------------|------|-------|
| Main | `ALLSKY_SFC_SW_DWN` | All Sky Surface Shortwave Downward Irradiance | kW-hr/m²/day | **Primary calculation** |
| -2 | `CLRSKY_SFC_SW_DWN` | Clear Sky Surface Shortwave Downward Irradiance | kW-hr/m²/day | **Cloud derating** |
| -3 | `ALLSKY_SFC_SW_DNI` | All Sky Direct Normal Irradiance | kW-hr/m²/day | Tracking systems |
| -4 | `ALLSKY_SFC_SW_DIFF` | All Sky Surface Diffuse Irradiance | kW-hr/m²/day | Shading analysis |
| -5 | `ALLSKY_KT` | All Sky Insolation Clearness Index | dimensionless | Cloud coverage |
| -6 | `CLRSKY_KT` | Clear Sky Insolation Clearness Index | dimensionless | Ideal conditions |
| -7 | `ALLSKY_SRF_ALB` | All Sky Surface Albedo | dimensionless | Ground reflection |
| -8 | `TOA_SW_DWN` | Top-Of-Atmosphere Shortwave Downward | kW-hr/m²/day | Atmospheric loss |
| -9 | `T2M` | Temperature at 2 Meters | °C | **Temp derating** |
| -10 | `T2M_MAX` | Maximum Temperature at 2 Meters | °C | Peak conditions |
| -11 | `T2M_MIN` | Minimum Temperature at 2 Meters | °C | Minimum conditions |
| -12 | `T2M_RANGE` | Temperature Range at 2 Meters | °C | Daily variation |
| -13 | `TS` | Earth Skin Temperature | °C | Panel heating |
| -14 | `T2MDEW` | Dew/Frost Point at 2 Meters | °C | Condensation |
| -15 | `T2MWET` | Wet Bulb Temperature at 2 Meters | °C | Humidity effect |
| -16 | `RH2M` | Relative Humidity at 2 Meters | % | **Soiling rate** |
| -17 | `PRECTOTCORR` | Precipitation Corrected | mm/day | Cleaning effect |
| -18 | `WS2M` | Wind Speed at 2 Meters | m/s | **Cooling effect** |
| -19 | `WS10M` | Wind Speed at 10 Meters | m/s | Wind loading |
| -20 | `WS50M` | Wind Speed at 50 Meters | m/s | Utility scale |
| -21 | `WD2M` | Wind Direction at 2 Meters | Degrees | Orientation |
| -22 | `WD10M` | Wind Direction at 10 Meters | Degrees | Orientation |
| -23 | `WD50M` | Wind Direction at 50 Meters | Degrees | Utility scale |
| -24 | `PS` | Surface Pressure | kPa | Altitude correction |
| -25 | `CLOUD_AMT` | Cloud Amount | % | **Cloud coverage** |
| -26 | `CLRSKY_DAYS` | Clear Sky Days | days | Sunny days count |
| -27 | `SZA` | Solar Zenith Angle | Degrees | Panel angle optimization |

### Data Coverage
- **Region**: UAE (22.5-25.5°N, 51.5-56.5°E)
- **Resolution**: 0.5° × 0.625° grid
- **Period**: January 2020 - December 2025
- **Points**: ~150 locations per parameter

### Key Parameters for Solar Calculations

#### Primary Energy Calculation
1. **ALLSKY_SFC_SW_DWN**: Actual solar irradiation (with clouds)
2. **T2M**: Temperature for derating calculations
3. **WS2M**: Wind speed for cooling effects

#### Accuracy Improvements
4. **CLRSKY_SFC_SW_DWN**: Cloud derating factor calculation
5. **CLOUD_AMT**: Direct cloud coverage percentage
6. **RH2M**: Soiling and humidity effects

#### Advanced Features
7. **ALLSKY_SFC_SW_DNI**: For tracking systems (future)
8. **ALLSKY_SFC_SW_DIFF**: Diffuse radiation for shading
9. **SZA**: Optimal tilt angle calculations

## Implementation Priority

### Phase 1: ✅ Implemented
- All-sky irradiation
- Clear-sky irradiation
- Cloud derating factor

### Phase 2: 🔄 In Progress
- Temperature data (T2M)
- Wind speed (WS2M)
- Relative humidity (RH2M)
- Cloud amount (CLOUD_AMT)

### Phase 3: 📋 Planned
- All 27 parameters
- Advanced weather modeling
- Predictive maintenance
- Seasonal optimization
