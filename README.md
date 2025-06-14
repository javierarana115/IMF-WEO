# IMF Python and Power BI Assessment

## Project Overview
This project provides automated access to IMF economic data with analysis and visualization capabilities.

Key features:
- Retrieve GDP growth and inflation data directly from IMF's World Economic Outlook (WEO) API
- Process and clean raw data using pandas
- Generate analytical outputs including:
  - Summary statistics table
  - Visualizations
  - Excel report generation

## Data Specifications

### Indicators
- **GDP growth**: constant prices, percent change
- **Inflation**: Average consumer prices, percent change

### Country Coverage
- United States
- Germany
- Brazil
- India
- South Africa

### Time Period
2015-2024 (10-year analysis)

## Installation

1. **Clone the repository**:
```
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. **Install dependencies (recommended in a virtual environment)**:
```
pip install -r requirements.txt
```
3. **Run the project**:
```
python main.py
```
