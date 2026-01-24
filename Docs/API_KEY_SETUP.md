# 🔑 API Key Setup Guide

## Groq AI API Key

The AI SolarVision calculator uses Groq AI for intelligent panel layout optimization and building detection. You'll need a free Groq API key to use these features.

### Getting Your Groq API Key

1. **Visit Groq Console**
   - Go to: https://console.groq.com/keys
   - Sign up for a free account if you don't have one

2. **Create API Key**
   - Click "Create API Key"
   - Give it a name (e.g., "Solar Calculator")
   - Copy the API key (starts with `gsk_`)

3. **Add to Application**
   - Open `solar_advanced.html` in a text editor
   - Find line ~1358:
     ```javascript
     const GROQ_API_KEY = 'YOUR_GROQ_API_KEY_HERE';
     ```
   - Replace `YOUR_GROQ_API_KEY_HERE` with your actual API key
   - Save the file

### Example

```javascript
// Before
const GROQ_API_KEY = 'YOUR_GROQ_API_KEY_HERE';

// After (with your key)
const GROQ_API_KEY = 'gsk_abc123xyz789...';
```

### Features Requiring API Key

- ✅ AI Auto-Detect Building (automatic roof detection)
- ✅ AI Panel Layout Optimization (tests multiple orientations)
- ✅ Smart Panel Recommendations (personalized suggestions)

### Features Working Without API Key

- ✅ Manual roof drawing
- ✅ NASA POWER weather data
- ✅ Solar calculations
- ✅ Financial analysis
- ✅ Interactive map

### Rate Limits

Groq free tier includes:
- 30 requests per minute
- 14,400 requests per day
- More than enough for personal use

### Security Note

⚠️ **Never commit API keys to public repositories!**

For production deployment:
- Use environment variables
- Implement server-side API proxy
- Restrict API key to specific domains

### Troubleshooting

**Error: "API key invalid"**
- Make sure you copied the complete key
- Check for extra spaces or quotes
- Verify key is active in Groq console

**Error: "Rate limit exceeded"**
- Wait a minute and try again
- Free tier: 30 requests/minute
- Consider upgrading for higher limits

**No AI features working**
- Check browser console for errors
- Verify API key is set correctly
- Ensure internet connection is active

### Alternative: No API Key Mode

You can still use the calculator without AI features:
1. Leave `GROQ_API_KEY` as is
2. Use manual drawing tools instead of AI auto-detect
3. Manually adjust panel orientation
4. All calculations will still work perfectly!

---

**Questions?** Open an issue on GitHub: https://github.com/Hamdan772/SolarVision/issues
