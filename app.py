import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Market Expansion Intelligence Engine",
    layout="wide"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🌍 Market Expansion Intelligence Engine")
st.caption("Decision-support tool for prioritizing international markets using explainable analytics")

# -------------------------------
# LOAD DATA (DECISION-READY)
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/scoring_data.csv")

df = load_data()

# -------------------------------
# SIDEBAR — STRATEGY INPUT
# -------------------------------
st.sidebar.header("🎯 Strategy Configuration")

mode = st.sidebar.radio(
    "Choose weight input mode",
    ["Manual (Sliders)", "Preset Scenario"]
)

# ---- DEFAULT WEIGHTS ----
w_economic = 0.25
w_growth = 0.15
w_readiness = 0.30
w_risk = 0.30

# ---- MANUAL MODE ----
if mode == "Manual (Sliders)":
    st.sidebar.subheader("Manual Weights")

    w_economic = st.sidebar.slider("Economic Strength", 0.0, 1.0, w_economic)
    w_growth = st.sidebar.slider("Growth Momentum", 0.0, 1.0, w_growth)
    w_readiness = st.sidebar.slider("Market Readiness", 0.0, 1.0, w_readiness)
    w_risk = st.sidebar.slider("Risk & Stability", 0.0, 1.0, w_risk)

# ---- PRESET MODE ----
else:
    st.sidebar.subheader("Scenario Presets")

    scenario = st.sidebar.selectbox(
        "Select scenario",
        [
            "Baseline",
            "Growth First",
            "Risk Conservative",
            "Execution Ready"
        ]
    )

    if scenario == "Growth First":
        w_economic, w_growth, w_readiness, w_risk = 0.20, 0.40, 0.20, 0.20
    elif scenario == "Risk Conservative":
        w_economic, w_growth, w_readiness, w_risk = 0.20, 0.10, 0.30, 0.40
    elif scenario == "Execution Ready":
        w_economic, w_growth, w_readiness, w_risk = 0.25, 0.10, 0.45, 0.20
    # Baseline keeps defaults

total_weight = w_economic + w_growth + w_readiness + w_risk
st.sidebar.write(f"**Total Weight:** {round(total_weight, 2)}")

if total_weight == 0:
    st.warning("Total weight cannot be zero.")

# -------------------------------
# DYNAMIC SCORING
# -------------------------------
df["dynamic_score"] = (
    w_economic * df["economic_score"] +
    w_growth * df["growth_score"] +
    w_readiness * df["readiness_score"] +
    w_risk * df["risk_score"]
)

df["dynamic_rank"] = df["dynamic_score"].rank(ascending=False)
df_view = df.sort_values("dynamic_rank")

# -------------------------------
# MARKET RANKING TABLE
# -------------------------------
st.subheader("📊 Market Ranking")

display_cols = [
    "dynamic_rank",
    "country",
    "dynamic_score",
    "economic_score",
    "growth_score",
    "readiness_score",
    "risk_score"
]

# Add optional columns safely
optional_cols = ["market_archetype"]
for col in optional_cols:
    if col in df_view.columns:
        display_cols.append(col)

st.dataframe(
    df_view[display_cols].round(3),
    use_container_width=True
)

# -------------------------------
# AI INSIGHTS PANEL
# -------------------------------
st.subheader("🧠 Market Insight")

selected_country = st.selectbox(
    "Select a country",
    df_view["country"].values
)

row = df_view[df_view["country"] == selected_country].iloc[0]

st.markdown(f"**Final Rank:** {int(row['dynamic_rank'])}")
st.markdown(f"**Composite Score:** {round(row['dynamic_score'], 3)}")

if "market_archetype" in row:
    st.markdown(f"**Market Archetype:** {row['market_archetype']}")

if "ai_insight" in row:
    st.markdown(f"**Insight:** {row['ai_insight']}")

# -------------------------------
# EXECUTIVE SUMMARY
# -------------------------------
st.subheader("🏆 Executive Recommendation")

top_markets = df_view.head(3)["country"].tolist()
watchlist = df_view.iloc[3:5]["country"].tolist()

st.markdown(f"**Top Priority Markets:** {', '.join(top_markets)}")
st.markdown(f"**Watchlist Markets:** {', '.join(watchlist)}")
