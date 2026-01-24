# 🤝 Contributing to SolarVision

Thank you for your interest in contributing to SolarVision! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/SolarVision.git
   cd SolarVision
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 💻 Development Setup

### Prerequisites
- Python 3.7+
- Modern web browser
- Text editor or IDE (VS Code recommended)
- Git

### Installation

```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the development server
python server.py

# Open http://localhost:8000 in your browser
```

## 📁 Project Structure

```
SolarVision/
├── index.html              # Landing page
├── solar_advanced.html     # Main calculator app
├── server.py               # Local development server
├── data/
│   └── Weather Data/       # NASA POWER CSV data
├── Docs/                   # Documentation files
├── SolarPV/                # Python solar calculation modules
└── api/                    # API endpoints (Vercel)
```

## 🔨 Making Changes

### Types of Contributions

- 🐛 **Bug Fixes**: Fix issues or errors
- ✨ **New Features**: Add new functionality
- 📝 **Documentation**: Improve docs or comments
- 🎨 **UI/UX**: Enhance user interface
- ⚡ **Performance**: Optimize code
- 🧪 **Tests**: Add or improve tests

### Before You Start

1. **Check existing issues** to avoid duplicates
2. **Open an issue** to discuss major changes
3. **Keep changes focused** - one feature/fix per PR

### Development Guidelines

#### HTML/CSS/JavaScript
- Use semantic HTML5 elements
- Follow existing code style (indentation, naming)
- Comment complex logic
- Ensure responsive design (test on mobile)
- Use CSS variables from `:root` for theming

#### Python
- Follow PEP 8 style guide
- Add docstrings to functions/classes
- Use type hints where appropriate
- Keep functions focused and small

#### NASA POWER Data
- Data files are in `data/Weather Data/`
- Don't modify CSV structure
- Coordinate changes with project maintainers

## 📤 Submitting Changes

### Commit Messages

Use clear, descriptive commit messages:

```bash
# Good ✅
git commit -m "Fix: Correct solar panel efficiency calculation"
git commit -m "Feature: Add monthly energy breakdown chart"
git commit -m "Docs: Update API setup instructions"

# Bad ❌
git commit -m "fixes"
git commit -m "update"
git commit -m "changes"
```

### Creating a Pull Request

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what was changed and why
   - Screenshots (for UI changes)
   - Reference to related issues

3. **Wait for review** - maintainers will review and provide feedback

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Changes are tested and working
- [ ] Documentation is updated (if needed)
- [ ] Commit messages are clear
- [ ] No unnecessary files included
- [ ] PR description explains the changes

## 🎨 Code Style Guidelines

### JavaScript

```javascript
// Use const/let, not var
const panelEfficiency = 0.21;
let totalEnergy = 0;

// Use descriptive variable names
const annualEnergyProduction = calculateEnergy();

// Add comments for complex calculations
// Calculate cloud derating factor using all-sky vs clear-sky ratio
const cloudDerating = allSkyIrradiation / clearSkyIrradiation;

// Use template literals
console.log(`Total energy: ${totalEnergy} kWh`);
```

### CSS

```css
/* Use CSS variables */
.button {
    background: var(--primary);
    color: var(--bg);
}

/* Group related properties */
.card {
    /* Layout */
    display: flex;
    flex-direction: column;
    
    /* Sizing */
    width: 100%;
    height: auto;
    
    /* Styling */
    background: var(--bg-card);
    border-radius: 12px;
    box-shadow: var(--shadow-md);
}
```

### Python

```python
def calculate_solar_potential(
    system_size: float,
    irradiation: float,
    efficiency: float = 0.85
) -> float:
    """
    Calculate annual solar energy production.
    
    Args:
        system_size: Solar system size in kW
        irradiation: Daily solar irradiation in kWh/m²
        efficiency: System efficiency (default: 0.85)
    
    Returns:
        Annual energy production in kWh
    """
    annual_energy = system_size * irradiation * 365 * efficiency
    return annual_energy
```

## 🧪 Testing

### Manual Testing

Before submitting:

1. **Test all features** you modified
2. **Check on different browsers** (Chrome, Firefox, Safari)
3. **Test responsive design** (mobile, tablet, desktop)
4. **Verify calculations** with known values
5. **Check console** for errors

### Test Scenarios

- Search for locations and verify map updates
- Draw roof polygons and calculate energy
- Use AI auto-detect feature
- Adjust sliders and verify updates
- Check export functionality
- Test with/without API key

## 🐛 Reporting Bugs

When reporting bugs, include:

- **Description**: What happened vs what should happen
- **Steps to reproduce**: Detailed steps to recreate the bug
- **Environment**: Browser, OS, screen size
- **Screenshots**: Visual bugs or errors
- **Console errors**: JavaScript errors (F12 → Console)

## 💡 Feature Requests

For feature requests:

- **Describe the feature** clearly
- **Explain the use case** - why is it needed?
- **Provide examples** or mockups if possible
- **Consider alternatives** - are there other solutions?

## 📞 Questions?

- **Open an issue** for questions or discussion
- **Check existing docs** in the `Docs/` folder
- **Review closed issues** - your question may be answered

## 📜 Code of Conduct

- Be respectful and constructive
- Welcome newcomers and help others learn
- Focus on what's best for the project
- Accept feedback gracefully
- Give credit where it's due

## 🙏 Thank You!

Your contributions make SolarVision better for everyone. Whether you're fixing a typo or adding a major feature, every contribution is valued!

---

<p align="center">
  <strong>Happy Coding! ☀️</strong>
</p>
