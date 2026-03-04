# 🧠 DataMind

DataMind is an AI-Powered Data Quality & Storytelling System.

## 📖 Overview

DataMind automates the entire data intelligence pipeline — from messy CSVs to clean insights, AI narratives, and professional reports. The application provides a seamless, step-by-step interactive workflow powered by Streamlit, featuring a modern UI with glassmorphism card styles and custom gradients.

## ✨ Key Features

- **Upload:** Upload custom CSV files or begin instantly with a built-in sample dataset.
- **Quality Analysis:** Automatically scan datasets to identify missing values, duplicate rows, and data type distributions, visualized via Plotly charts.
- **Intelligent Data Cleaning:** Offers basic and advanced data cleaning strategies, including IQR-based outlier removal and smart missing value imputation.
- **Deep-Dive Analysis:** Explore relationships with correlation heatmaps, analyze variables using distribution explorers, and detect high-risk data points using a Machine Learning-based Isolation Forest anomaly detector.
- **AI-Generated Stories:** Utilizes the OpenAI API (GPT-3.5-turbo) to digest the data quality report and automatically write a 3-paragraph executive summary explaining the data health, critical issues, and next steps.
- **Professional Report Export:** Compiles the AI story, quality metrics, and anomaly detection results into a polished, downloadable PDF report built with ReportLab. Users can also download the cleaned CSV data.

## 🛠️ Tech Stack

- **Frontend/Framework:** Streamlit, Streamlit-Lottie
- **Data Processing & ML:** Pandas, NumPy, SciPy, Scikit-Learn
- **Visualization:** Plotly
- **AI Integration:** OpenAI API, Python-dotenv
- **PDF Generation:** ReportLab

## 🚀 Installation & Setup

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd datamind

```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

3. **Install dependencies:**

```bash
pip install -r requirements.txt

```

4. **Set up Environment Variables:**

- Create a `.env` file in the root directory.
- Add your OpenAI API key to enable AI story generation:

```env
OPENAI_API_KEY=your_api_key_here

```

- _Note: The application will warn you if the API key is missing but will still run the other pipeline steps._

5. **Run the Application:**

```bash
streamlit run app.py

```

## 📁 Project Structure

The application is modularized to separate UI logic from data processing:

- `app.py`: The main entry point and global session state initializer.
- `pages/`: Contains the sequential Streamlit pages defining the pipeline (Upload, Quality, Clean, Analysis, Story, Reports).
- `modules/`: Contains the core logic scripts (`advanced_cleaner.py`, `anomaly_detector.py`, `data_cleaner.py`, `pattern_analyzer.py`, `quality_analyzer.py`, `report_generator.py`, `story_generator.py`, `ui_components.py`).
- `.streamlit/config.toml`: Custom Streamlit theme configuration ensuring a cohesive dark-mode design.
