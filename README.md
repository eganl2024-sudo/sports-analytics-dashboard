#  European Soccer League Predictions 2025/2026

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red)

An advanced machine learning system that predicts final standings for the 2025/2026 season across Europe's top 5 soccer leagues, comparing context-aware ensemble models against traditional Elo ratings.

##  Project Overview

This project explores whether a **Context-Aware Machine Learning Model** can outperform the traditional **Elo Rating System** in predicting soccer league standings. Using 10 years of historical data and advanced feature engineering, we've built an ensemble model that incorporates contextual factors beyond simple win/loss records.

### Leagues Analyzed
- English Premier League
- Spanish La Liga
- German Bundesliga
- French Ligue 1
- Italian Serie A

## Key Features

- **Context-Aware Predictions**: Incorporates strength of schedule, finishing efficiency, and fatigue
- **Ensemble Modeling**: Combines Random Forest, XGBoost, and Logistic Regression
- **Monte Carlo Simulation**: 10,000 simulations for confidence intervals
- **Interactive Dashboard**: Built with Streamlit for real-time exploration
- **Model Calibration**: Verified prediction accuracy through Brier Score analysis

## Live Demo

[View the live Streamlit app](https://sports-analytics-dashboard.streamlit.app/)

## Methodology

### 1. Data Pipeline
- **Training Data**: 10 years of match results (2015-2025)
- **Current Season**: All matches through February 12, 2026
- **Test Set**: Remaining fixtures for the season

### 2. Feature Engineering

Beyond basic Elo ratings, we engineered contextual features:

| Feature | Description |
|---------|-------------|
| **Strength of Schedule** | Rolling average of opponent Elo ratings |
| **Finishing Efficiency** | Goals scored vs. expected goals (xG) |
| **Fatigue** | Days of rest between matches |
| **Form** | Recent performance trends |

### 3. Model Architecture

**Ensemble Approach:**
- **Random Forest**: Captures non-linear patterns and feature interactions
- **XGBoost**: Reduces bias and handles edge cases
- **Logistic Regression**: Provides stable linear baseline

**Stacking:** Meta-model combines predictions for optimal accuracy

### 4. Validation & Calibration

- **10,000 Monte Carlo simulations** for remaining matches
- **Calibration analysis**: Model predictions align with actual outcomes
- **90% Confidence Intervals**: Quantified prediction uncertainty

## Project Structure

```
Sports Analytics Project/
├── app.py                              # Streamlit dashboard
├── Final_App_Data.csv                  # Prediction results
├── logos/                              # Team logos
├── requirements.txt                    # Python dependencies
│
├── Notebooks/
│   ├── 01_Data_Extraction_Pipeline.ipynb
│   ├── 02_Data_Cleaning_Pipeline.ipynb
│   ├── 03_Current_Season_Prep.ipynb
│   ├── 04_Baseline_Simulation.ipynb
│   ├── 05_Feature_Engineering.ipynb
│   ├── 06_ML_Simulation.ipynb
│   ├── 07_Final_Visualization.ipynb
│   ├── 08_League_Dashboards.ipynb
│   ├── 09_Ensemble_Modeling.ipynb
│   └── 09_5_Context_and_Calibration.ipynb
│
└── Report_Assets/                      # Visualizations and charts
```

##  Installation & Usage

### Prerequisites
- Python 3.9+
- pip

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sports-analytics-project.git
   cd sports-analytics-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:8501`

### Exploring the Notebooks

The Jupyter notebooks document the complete modeling pipeline:

```bash
# Start Jupyter
jupyter notebook

# Open notebooks in order (01 through 09_5)
```

## Key Results

### Model Performance
- **Accuracy**: Ensemble model shows X% improvement over baseline Elo
- **Calibration**: Predicted probabilities align with actual outcomes
- **Uncertainty Quantification**: 90% confidence intervals provided

### Interesting Findings
- **Value Picks**: Teams outperforming their Elo expectations
- **Fade Picks**: Teams underperforming compared to Elo baseline
- **Title Races**: Quantified championship probabilities
- **Relegation Battles**: Predicted survival chances

## Dashboard Features

- **Interactive League Selection**: Switch between all 5 leagues
- **Trajectory Divergence**: Visual comparison of Elo vs. Context-Aware predictions
- **Team Cards**: Champion, Value Pick, Fade, and Relegation predictions
- **Detailed Tables**: Full standings with confidence intervals

## Technologies Used

- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: Machine learning models
- **XGBoost**: Gradient boosting
- **Matplotlib**: Visualizations
- **Streamlit**: Interactive web app
- **Pillow**: Image processing

## References & Data Sources

- Match data: [ESPN, FotMob, etc.]

## Author

**Liam Egan**
- Graduate Student, Business Analytics (Sports Analytics) - University of Notre Dame
- Former D1 Goalkeeper (2x Final Four, National Championship Runner-up 2023)
- [LinkedIn](https://www.linkedin.com/in/liam-egan-/)
- [GitHub](https://github.com/eganl2024-sudo)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Notre Dame MSBA Program
- Sports Analytics Community
- Open source contributors

## Contact

Questions or feedback? Feel free to [open an issue](YOUR_REPO/issues) or reach out on LinkedIn!

---

 If you found this project interesting, please consider giving it a star!
