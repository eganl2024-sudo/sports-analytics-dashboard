import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# ==========================================
# 1. CONFIG & STYLING
# ==========================================
st.set_page_config(page_title="League Predictions ⚽", layout="wide", page_icon="⚽")

st.markdown("""
<style>
    .metric-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-left: 5px solid #4bbf73;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .metric-box-red {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-left: 5px solid #ff4b4b;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .metric-label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { font-size: 22px; font-weight: bold; color: #333; margin-top: 5px; }
    .metric-sub { font-size: 14px; color: #888; }
    
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; background-color: #f0f2f6; border-radius: 4px 4px 0px 0px; padding-top: 10px; }
    .stTabs [aria-selected="true"] { background-color: #ffffff; border-top: 2px solid #4bbf73; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOCAL DATA & ASSET LOADING
# ==========================================
LEAGUE_MAP = {
    'ENG-Premier League': '(ENG) Premier League',
    'ESP-La Liga': '(ESP) La Liga',
    'GER-Bundesliga': '(GER) Bundesliga',
    'FRA-Ligue 1': '(FRA) Ligue 1',
    'ITA-Serie A': '(ITA) Serie A'
}

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('Final_App_Data.csv')
    except FileNotFoundError:
        return pd.DataFrame() 

    df['league'] = df['league'].map(LEAGUE_MAP).fillna(df['league'])
    
    # Force 1-based Integer Ranks
    df['rank_super'] = df.groupby('league')['ensemble_projected'].rank(ascending=False, method='min').astype(int)
    df['rank_elo'] = df.groupby('league')['projected_pts'].rank(ascending=False, method='min').astype(int)
    return df

df = load_data()

if df.empty:
    st.error("⚠️ Data file 'Final_App_Data.csv' not found. Please run the deployment script.")
    st.stop()

# ==========================================
# FIXED LOGO FUNCTION - ADAPTIVE SIZING
# ==========================================
def get_content_bounds(img):
    """
    Calculate the bounding box of non-transparent pixels.
    Returns the effective size of the logo content.
    """
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Get alpha channel
    alpha = img.split()[3]
    bbox = alpha.getbbox()
    
    if bbox:
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        return max(width, height)  # Use the larger dimension
    
    return max(img.size)  # Fallback to image size

def get_logo(name, ax, target_size_px=22):
    """
    FIXED: Adaptive logo sizing based on content bounds.
    
    Args:
        name: Team name (matches filename without .png)
        ax: Matplotlib axis object
        target_size_px: Desired logo size in pixels on the plot (default: 22px)
    
    Returns:
        AnnotationBbox or None
    """
    filename = f"logos/{name}.png"
    
    if not os.path.exists(filename):
        return None
    
    try:
        img = Image.open(filename)
    except:
        return None
    
    # Calculate adaptive zoom based on content size
    content_size = get_content_bounds(img)
    
    # Calculate zoom to achieve target size
    # zoom = target_size / content_size
    if content_size > 0:
        zoom = target_size_px / content_size
    else:
        zoom = 0.05  # Fallback to original zoom
    
    # Clamp zoom to reasonable range to prevent extreme sizes
    zoom = max(0.02, min(0.15, zoom))
    
    ib = OffsetImage(img, zoom=zoom)
    ib.image.axes = ax
    
    return AnnotationBbox(
        ib, (0, 0), 
        xybox=(0, 0), 
        xycoords='data', 
        boxcoords="offset points", 
        frameon=False
    )

def get_relegation_text(league, subset_df):
    bottom_table = subset_df.sort_values('ensemble_projected', ascending=True)
    if "(GER)" in league or "(FRA)" in league:
        auto = bottom_table.iloc[0:2]['team'].tolist() 
        playoff = bottom_table.iloc[2]['team']
        return f"{', '.join(auto)} (Auto)<br><span style='color:#f39c12'>{playoff} (Playoff)</span>"
    else:
        auto = bottom_table.iloc[0:3]['team'].tolist()
        return f"{', '.join(auto)}"

def plot_super_slope(league_df):
    """FIXED VERSION - Sequential spacing to prevent cramping"""
    fig, ax = plt.subplots(figsize=(11, 14), facecolor='white')
    ax.set_facecolor('white')
    
    # Sort by rank_super and reset index for sequential numbering
    L = league_df.sort_values('rank_super').reset_index(drop=True)
    
    # CRITICAL: Use row number (idx) for visual position, NOT rank
    for idx, row in L.iterrows():
        team = row['team']
        r_elo = int(row['rank_elo'])
        r_super = int(row['rank_super'])
        
        # THIS IS THE KEY: visual_pos is sequential (0,1,2,3...) + 1
        visual_pos = idx + 1  # Will be: 1, 2, 3, 4, 5... (NEVER cramped!)
        
        # Color logic
        color = '#4bbf73' if r_super < r_elo else ('#ff4b4b' if r_super > r_elo else '#e0e0e0')
        alpha = 0.9 if color != '#e0e0e0' else 0.3
        width = 2.5 if color != '#e0e0e0' else 1
        
        # Draw line from left (r_elo) to right (visual_pos)
        ax.plot([0, 1], [r_elo, visual_pos], color=color, alpha=alpha, linewidth=width, marker='o')
        
        # Left side text
        ax.text(-0.05, r_elo, f"{r_elo} {team}", ha='right', va='center', fontsize=11, color='#555')
        
        # Right side text - SHOWS ACTUAL RANK but positioned at visual_pos
        fontweight = 'bold' if color == '#4bbf73' else 'normal'
        p5, p95 = int(row['p5']), int(row['p95'])
        label = f"{team} {r_super} | {row['ensemble_projected']:.1f} pts [{p5}-{p95}]"
        ax.text(1.05, visual_pos, label, ha='left', va='center', fontweight=fontweight, fontsize=11)
        
        # Logo at visual position
        ab = get_logo(team, ax, target_size_px=22)
        if ab:
            ab.xy = (1, visual_pos)
            ab.xybox = (250, 0)
            ax.add_artist(ab)
    
    # Set limits based on number of teams (not max rank)
    max_visual = len(L)
    ax.set_ylim(max_visual + 1, 0) 
    ax.set_xlim(-0.5, 2.2)
    ax.axis('off')
    
    # Headers
    ax.text(0, 0, "Feb 12, 2026 Standings", ha='center', fontsize=14, fontweight='bold', color='#888')
    ax.text(1, 0, "Final Projected Standings", ha='center', fontsize=14, fontweight='bold', color='#000')
    
    return fig

# ==========================================
# 3. UI LAYOUT
# ==========================================
tab1, tab2 = st.tabs(["🏆 League Predictions", "📘 Project Documentation"])

with tab1:
    with st.sidebar:
        st.header("⚙️ League Selector")
        custom_order = ['(ENG) Premier League', '(ESP) La Liga', '(GER) Bundesliga', '(FRA) Ligue 1', '(ITA) Serie A']
        available = [L for L in custom_order if L in df['league'].unique()]
        league = st.selectbox("Choose Competition", available)
        
        st.markdown("---")
        st.info("**Context:** Comparing Elo Baseline vs. Context-Aware Ensemble.")

    subset = df[df['league'] == league].copy()
    winner = subset.loc[subset['rank_super'].idxmin()]
    value_pick = subset.loc[subset['diff_vs_elo'].idxmax()]
    fade_pick = subset.loc[subset['diff_vs_elo'].idxmin()]
    relegation_text = get_relegation_text(league, subset)

    st.title(f"{league} Projections")

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f"<div class='metric-box'><div class='metric-label'>🏆 Champion</div><div class='metric-value'>{winner['team']}</div><div class='metric-sub'>{winner['ensemble_projected']:.1f} Pts</div></div>", unsafe_allow_html=True)
    with c2: st.markdown(f"<div class='metric-box'><div class='metric-label'>✅ Value Pick</div><div class='metric-value'>{value_pick['team']}</div><div class='metric-sub' style='color:#4bbf73'>+{value_pick['diff_vs_elo']:.1f} vs Elo</div></div>", unsafe_allow_html=True)
    with c3: st.markdown(f"<div class='metric-box-red'><div class='metric-label'>⚠️ Fade</div><div class='metric-value'>{fade_pick['team']}</div><div class='metric-sub' style='color:#ff4b4b'>{fade_pick['diff_vs_elo']:.1f} vs Elo</div></div>", unsafe_allow_html=True)
    with c4: st.markdown(f"<div class='metric-box-red'><div class='metric-label'>📉 Relegation</div><div class='metric-value' style='font-size:16px; line-height:1.4'>{relegation_text}</div></div>", unsafe_allow_html=True)

    st.write("")
    col_chart, col_data = st.columns([2, 1])

    with col_chart:
        st.subheader("Trajectory Divergence")
        st.pyplot(plot_super_slope(subset))

    with col_data:
        st.subheader("Detailed Projections")
        disp_df = subset[['team', 'ensemble_projected', 'projected_pts', 'diff_vs_elo']].copy()
        disp_df = disp_df.sort_values('ensemble_projected', ascending=False)
        disp_df.columns = ['Team', 'Model Pts', 'Elo Pts', 'Diff']
        
        # Clean Index (Start at 1)
        disp_df = disp_df.reset_index(drop=True)
        disp_df.index = disp_df.index + 1

        st.dataframe(
            disp_df.style.format({'Model Pts': '{:.1f}', 'Elo Pts': '{:.1f}', 'Diff': '{:+.1f}'})
            .background_gradient(subset=['Diff'], cmap='RdYlGn', vmin=-5, vmax=5), 
            height=800
        )

with tab2:
    st.markdown("""
    # 📘 Project Documentation
    
    ### **Objective**
    The goal of this project was to determine if a **Context-Aware Machine Learning Model** could outperform the traditional **Elo Rating System** in predicting the final standings of the 2025/2026 European Soccer Season.
    
    ---
    
    ### **1. The Data Pipeline**
    We engineered a robust pipeline to prevent data leakage and ensure historical accuracy.
    * **History (Train):** 10 years of match data (2015–2025).
    * **Banked (Current):** All matches played up to Feb 12, 2026.
    * **Future (Test):** The remaining fixtures for the season.
    
    ### **2. The "Skeptic" Architecture**
    Unlike Elo, which relies solely on past results, our model incorporates **Contextual Features**:
    1.  **Strength of Schedule:** Did the team beat a giant or a minnow? (Rolling Opponent Elo).
    2.  **Finishing Efficiency:** Is the team "lucky" (scoring more than xG) or "clinical"?
    3.  **Fatigue:** Days of rest between matches.
    
    ### **3. The Ensemble Engine**
    We used a "Stacking" approach to combine three algorithms:
    * **Random Forest:** Captures non-linear patterns and interactions.
    * **XGBoost:** Reduces bias and handles edge cases.
    * **Logistic Regression:** Provides a stable linear baseline.
    
    ### **4. Validation & Calibration**
    * **Simulation:** We ran **10,000 Monte Carlo simulations** for the remaining games.
    * **Calibration:** We verified that when our model predicts a 70% win probability, the team actually wins ~70% of the time (Brier Score analysis).
    
    ---
    
    ### **How to Read the Charts**
    * **Green Line:** The Model predicts this team will finish **higher** than their current Elo ranking implies. (Undervalued).
    * **Red Line:** The Model predicts this team will finish **lower** than their current Elo ranking implies. (Overvalued).
    * **[Low-High]:** The 90% Confidence Interval. We are 90% sure the team's final points will fall in this range.
    """)
