# 📋 Project Manifest — European Football Season Predictor

> **MSBA Sports Analytics Project**
> *Predicting league outcomes across Europe's Top 5 leagues using ML ensemble modeling*

---

## 📂 1. Data Engineering

| Phase | File | Purpose |
|-------|------|---------|
| **1** | `01_Data_Extraction.ipynb` | Raw data ETL from FBRef, ClubElo, and local sources |
| **2** | `02_Data_Cleaning_Pipeline.ipynb` | Entity resolution, team name mapping, merge pipeline |
| **3** | `03_Current_Season_Prep.ipynb` | Trichotomy split: banked results / future fixtures / training history |

---

## 🧠 2. Modeling Pipeline

| Phase | File | Purpose |
|-------|------|---------|
| **4** | `04_Baseline_Elo_Simulation.ipynb` | Elo-only Monte Carlo simulation (10,000 runs) — the **control group** |
| **5** | `05_Feature_Engineering.ipynb` | Rolling form, finishing efficiency, rest days, Elo diff |
| **6** | `06_ML_Random_Forest.ipynb` | Single Random Forest model + Monte Carlo simulation |
| **7** | `07_Final_Visualization.ipynb` | Master comparison: RF vs Elo across all 96 teams |
| **8** | `08_League_Dashboards.ipynb` | High-resolution slope charts with team logos (5 leagues × 300 DPI) |
| **9** | `09_Ensemble_Modeling.ipynb` | Soft-vote ensemble (LR + RF + GB) — the "Super Model" |
| **9.5** | `09_5_Context_and_Calibration.ipynb` | **The Masterpiece**: Schedule Strength + Calibration Curve + Context-Aware Ensemble |

---

## 🎨 3. Visualization & Product

| File | Purpose |
|------|---------|
| `app.py` | **Interactive Streamlit Dashboard** — "The War Room" |
| `deploy_context_model.py` | Deployment pipeline: swaps data engine from Phase 9 → 9.5 |
| `data_merge.py` | Original merge script (superseded by `deploy_context_model.py`) |

---

## 📄 4. Key Data Outputs

| File | Source | Description |
|------|--------|-------------|
| `data/results/Final_App_Data.csv` | `deploy_context_model.py` | **The brain of the app** — merged context-aware projections + Elo + RF |
| `data/results/Ensemble_Context_Projection.csv` | Phase 9.5 | Context-aware ensemble projections (with SOS) |
| `data/results/Ensemble_Projection.csv` | Phase 9 | Vanilla ensemble projections (without SOS) |
| `data/results/Baseline_Elo_Projection.csv` | Phase 4 | Elo-only baseline projections |
| `data/results/ML_vs_Elo_Comparison.csv` | Phase 6 | Single RF projections |

---

## 📊 5. Report Assets

| File | Description |
|------|-------------|
| `Report_Assets/Calibration_Curve.png` | 3-panel "BS Detector" — model trustworthiness |
| `Report_Assets/Feature_Importance_Context.png` | Feature importance with SOS highlighted |
| `Report_Assets/Ensemble_vs_RF_Comparison.png` | Super Model vs Random Forest divergence |
| `Report_Assets/Model_Accuracy_Comparison.png` | Accuracy comparison across model iterations |
| `Report_Assets/EPL_Dashboard.png` | Premier League slope chart (300 DPI) |
| `Report_Assets/LaLiga_Dashboard.png` | La Liga slope chart |
| `Report_Assets/Bundesliga_Dashboard.png` | Bundesliga slope chart |
| `Report_Assets/SerieA_Dashboard.png` | Serie A slope chart |
| `Report_Assets/Ligue1_Dashboard.png` | Ligue 1 slope chart |
| `Report_Assets/logos/` | 96 cached team logos |

---

## 🏃 How to Run

```bash
# 1. Deploy the context-aware model (creates Final_App_Data.csv)
python deploy_context_model.py

# 2. Launch the dashboard
python -m streamlit run app.py
```

---

## 🏗️ Architecture

```
Raw Data (FBRef, ClubElo)
    ↓
Data Cleaning + Entity Resolution
    ↓
Trichotomy Split (Train / Banked / Future)
    ↓
Feature Engineering (11 features incl. SOS)
    ↓
┌─────────────────────────────────────────┐
│  Context-Aware Ensemble (Phase 9.5)     │
│  ├── Logistic Regression (scaled)       │
│  ├── Random Forest (raw)                │
│  └── Gradient Boosting (raw)            │
│  → Manual Soft-Vote → Calibrated Probs  │
└─────────────────────────────────────────┘
    ↓
Monte Carlo Simulation (10,000 runs)
    ↓
deploy_context_model.py → Final_App_Data.csv
    ↓
app.py → "The War Room" Dashboard
```

---

## 📈 Model Evolution

| Version | Features | Accuracy | Key Innovation |
|---------|----------|----------|----------------|
| Elo Baseline | 1 (Elo diff only) | ~45% | Control group |
| Single RF (Phase 6) | 7 | ~48% | ML uplift over Elo |
| Vanilla Ensemble (Phase 9) | 9 | ~49% | Soft-vote LR+RF+GB |
| **Context-Aware (Phase 9.5)** | **11** | **~50%** | **Schedule Strength + Calibration** |

---

*Generated: Feb 14, 2026*
