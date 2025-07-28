# 📊 AmLaw 200 Dashboard & Database Project

A comprehensive data analysis pipeline for AmLaw 200 law firm rankings (2019–2024) with intelligent column matching, data cleaning, and interactive visualization.

## 🚀 **What This Project Does**

Transforms 6 years of messy AmLaw data into a clean, analyzable dataset with **16 comprehensive metrics** across **1,000+ law firm records**.

### **Key Features:**
- **🧹 Intelligent Data Cleaning**: Handles inconsistent headers, line breaks, parentheses, and naming variations
- **🔗 Smart Column Matching**: Finds common columns across years despite formatting differences  
- **📊 Rich Dataset**: 16 financial, structural, and performance metrics per firm
- **💻 Interactive Dashboard**: Streamlit-powered visualization and analysis
- **🗄️ Database Integration**: PostgreSQL storage with easy querying

---

## 🎯 **Final Dataset Overview**

After processing, you get **16 core metrics** for law firm analysis:

### **💰 Financial Performance**
- **Gross Revenue** - Total firm revenue
- **Net Operating Income** - Operating profit  
- **Profit Margin** - Profitability percentage
- **Profitability Index** - Overall profitability measure

### **👥 Partnership Structure** 
- **Number of Lawyers** - Total attorneys
- **Number of Partners** - All partners (equity + non-equity)
- **Number of Equity Partners** - Partners with ownership
- **Number of Non-Equity Partners** - Salaried partners
- **Leverage** - Associate-to-partner ratio

### **💵 Compensation & Efficiency**
- **Profits Per Lawyer** - Average profit per attorney
- **Profits Per Equity Partner** - Profit per equity partner
- **Revenue per Lawyer** - Revenue efficiency per attorney
- **Value per Lawyer** - Value generated per attorney
- **Compensation Average, All Partners** - Average partner compensation
- **Compensation Non-Equity Partners** - Non-equity partner pay

### **📈 Time Series**
- **Year** - 2019-2024 data for trend analysis
- **Firm Name** - For firm-specific tracking

---

## 🔧 **Tech Stack**

- **Python** (Pandas, regex for data processing)
- **PostgreSQL** for database storage
- **Streamlit** for interactive dashboards
- **Virtual Environment** (.venv) for dependency management

---

## 📁 **Project Structure**

```
AmLaw_200_Dashboard_Database/
├── AmLaw Yearly Data/           # Raw CSV files (2019–2024)
│   ├── Amlaw 2019.csv
│   ├── Amlaw 2020.csv
│   ├── Amlaw 2021.csv
│   ├── Amlaw 2022.csv
│   ├── Amlaw 2023.csv
│   └── Amlaw 2024.csv
├── scripts/
│   ├── combine_data.py          # ⭐ Enhanced data cleaning & combination
│   └── upload_to_postgres.py    # Database upload utility
├── dashboard/
│   └── streamlit_app.py         # Interactive dashboard
├── combined_amlaw.csv           # Final cleaned dataset
├── .env                         # Database connection (not committed)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🚀 **Quick Start**

### **1. Setup Virtual Environment (.venv)**
```bash
# Create your isolated Python environment
python3 -m venv .venv

# Activate it (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**🎓 Why .venv?** Think of it as your own private coding space - keeps this project's tools separate from your system's Python, preventing conflicts!

### **2. Process the Data**
```bash
# Run the enhanced data combination script
python3 scripts/combine_data.py
```

**What happens:** The script intelligently cleans headers, matches columns across years, and creates `combined_amlaw.csv` with 16 comprehensive metrics.

### **3. Launch Dashboard**
```bash
# Start the interactive dashboard
streamlit run dashboard/streamlit_app.py
```

### **4. (Optional) Database Setup**
```bash
# Upload to PostgreSQL (requires .env setup)
python3 scripts/upload_to_postgres.py
```

---

## 🧹 **Data Cleaning Magic**

Our enhanced cleaning algorithm handles:

### **Header Inconsistencies:**
- `"Revenue (millions)"` → `"Revenue"`
- `"Net Operating\nIncome"` → `"Net Operating Income"`  
- `"Total Number of Lawyers"` → `"Number of Lawyers"`
- `"Revenue per Lawyer (RPL)"` → `"Revenue per Lawyer"`

### **Naming Variations:**
- `"CAP divided by number of Lawyers (VPL)"` → `"Value per Lawyer"`
- `"Compensation of Non-Equity Partners"` → `"Compensation Non-Equity Partners"`
- `"Total Partners"` → `"Number of Partners"`

### **Formatting Issues:**
- Removes parentheses and contents: `(millions)`, `(RPL)`, `(FY:2019)`
- Normalizes line breaks and extra spaces
- Handles "Total" prefix variations
- Standardizes measurement terminology

---

## 📊 **Example Analysis Possibilities**

With this rich dataset, you can analyze:

- **📈 Growth Trends**: Revenue and profit changes 2019-2024
- **🏢 Firm Size Evolution**: How lawyer counts changed over time  
- **💰 Compensation Patterns**: Partner pay trends across years
- **⚖️ Efficiency Metrics**: Revenue/profit per lawyer benchmarking
- **🤝 Partnership Structure**: Equity vs non-equity partner ratios
- **🏆 Performance Comparison**: Firm-to-firm competitive analysis

---

## 🔧 **Technical Details**

### **Column Matching Algorithm:**
1. **Clean** all headers using comprehensive normalization
2. **Find** intersection of columns present in ALL 6 years
3. **Combine** data using only consistently available metrics
4. **Standardize** final column names (lowercase, underscores)

### **Data Quality:**
- **1,000 total records** (law firms across 6 years)
- **16 core metrics** consistently available
- **No missing data** in final dataset (only complete columns included)
- **Standardized formatting** for analysis

---

## 📝 **Dependencies**

Core requirements:
- `pandas` - Data manipulation and analysis
- `streamlit` - Dashboard framework  
- `psycopg2-binary` - PostgreSQL connectivity
- `python-dotenv` - Environment variable management
- `sqlalchemy` - Database ORM

---

## 🤝 **Contributing**

1. **Data Issues**: Found inconsistencies in source files? Update the cleaning logic in `scripts/combine_data.py`
2. **Dashboard Features**: Enhance visualizations in `dashboard/streamlit_app.py`  
3. **Database**: Improve database schema or queries in `scripts/upload_to_postgres.py`

---

## 📈 **Next Steps**

- [ ] Add more sophisticated analytics (firm clustering, growth predictions)
- [ ] Implement real-time data updates
- [ ] Add geographic analysis capabilities
- [ ] Create executive summary reports
- [ ] Build API endpoints for data access

---

**🎯 Ready to analyze law firm performance like never before!**