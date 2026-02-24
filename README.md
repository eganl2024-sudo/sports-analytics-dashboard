# european soccer league predictions 2025/2026

![status](https://img.shields.io/badge/Status-Active-success)
![python](https://img.shields.io/badge/Python-3.9+-blue)
![streamlit](https://img.shields.io/badge/Streamlit-1.29+-red)

an advanced machine learning system that predicts final standings for the 2025/2026 season across europe's top 5 soccer leagues, comparing context-aware ensemble models against traditional elo ratings.

## project overview

this project explores whether a **context-aware machine learning model** can outperform the traditional **elo rating system** in predicting soccer league standings. using 10 years of historical data and advanced feature engineering, we've built an ensemble model that incorporates contextual factors beyond simple win/loss records.

### leagues analyzed
- english premier league
- spanish la liga
- german bundesliga
- french ligue 1
- italian serie a

## key features

- **context-aware predictions**: incorporates strength of schedule, finishing efficiency, and fatigue
- **ensemble modeling**: combines random forest, xgboost, and logistic regression
- **monte carlo simulation**: 10,000 simulations for confidence intervals
- **interactive dashboard**: built with streamlit for real-time exploration
- **model calibration**: verified prediction accuracy through brier score analysis

## live demo

[view the live streamlit app](https://sports-analytics-dashboard.streamlit.app/)

## methodology

### 1. data pipeline
- **training data**: 10 years of match results (2015-2025)
- **current season**: all matches through february 12, 2026
- **test set**: remaining fixtures for the season

### 2. feature engineering

beyond basic elo ratings, we engineered contextual features:

| feature | description |
|---------|-------------|
| **strength of schedule** | rolling average of opponent elo ratings |
| **finishing efficiency** | goals scored vs. expected goals (xg) |
| **fatigue** | days of rest between matches |
| **form** | recent performance trends |

### 3. model architecture

**ensemble approach:**
- **random forest**: captures non-linear patterns and feature interactions
- **xgboost**: reduces bias and handles edge cases
- **logistic regression**: provides stable linear baseline

**stacking:** meta-model combines predictions for optimal accuracy

### 4. validation & calibration

- **10,000 monte carlo simulations** for remaining matches
- **calibration analysis**: model predictions align with actual outcomes
- **90% confidence intervals**: quantified prediction uncertainty

## project structure

```
sports analytics project/
├── app.py                              # streamlit dashboard
├── Final_App_Data.csv                  # prediction results
├── logos/                              # team logos
├── requirements.txt                    # python dependencies
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
└── Report_Assets/                      # visualizations and charts
```

## installation & usage

### prerequisites
- python 3.9+
- pip

### local setup

1. **clone the repository**
   ```bash
   git clone https://github.com/eganl2024-sudo/sports-analytics-dashboard.git
   cd sports-analytics-project
   ```

2. **install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **run the streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **open in browser**
   navigate to `http://localhost:8501`

### exploring the notebooks

the jupyter notebooks document the complete modeling pipeline:

```bash
# start jupyter
jupyter notebook

# open notebooks in order (01 through 09_5)
```

## key results

### model performance
- **accuracy**: ensemble model shows x% improvement over baseline elo
- **calibration**: predicted probabilities align with actual outcomes
- **uncertainty quantification**: 90% confidence intervals provided

### interesting findings
- **value picks**: teams outperforming their elo expectations
- **fade picks**: teams underperforming compared to elo baseline
- **title races**: quantified championship probabilities
- **relegation battles**: predicted survival chances

## dashboard features

- **interactive league selection**: switch between all 5 leagues
- **trajectory divergence**: visual comparison of elo vs. context-aware predictions
- **team cards**: champion, value pick, fade, and relegation predictions
- **detailed tables**: full standings with confidence intervals

## technologies used

- **python**: core programming language
- **pandas & numpy**: data manipulation
- **scikit-learn**: machine learning models
- **xgboost**: gradient boosting
- **matplotlib**: visualizations
- **streamlit**: interactive web app
- **pillow**: image processing

## references & data sources

- match data: [espn, fotmob, etc.]
- elo ratings methodology: [link to elo paper]
- expected goals (xg): [link to xg methodology]

## author

**liam egan**
- graduate student, business analytics (sports analytics) - university of notre dame
- former d1 goalkeeper (2x final four, national championship runner-up 2023)
- [linkedin](https://www.linkedin.com/in/liam-egan-/)
- [github](https://github.com/eganl2024-sudo)

## license

this project is licensed under the mit license - see the license file for details.

## acknowledgments

- notre dame msba program
- sports analytics community
- open source contributors

## contact

questions or feedback? feel free to [open an issue](https://github.com/eganl2024-sudo/sports-analytics-dashboard/issues) or reach out on linkedin!

---

if you found this project interesting, please consider giving it a star!
