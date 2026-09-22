# Market Expansion Intelligence Engine

## Overview
The Market Expansion Intelligence Engine is a decision-support system designed to help strategy and operations teams prioritize international markets for expansion using structured, explainable analytics.

The project focuses on decision intelligence rather than black-box machine learning, making trade-offs and assumptions explicit and adjustable.

---

## Problem Statement
Organizations planning global expansion often face:
- Conflicting economic and regulatory indicators
- Overreliance on intuition or single metrics (e.g., GDP alone)
- Slow decision cycles due to manual analysis

This project addresses these challenges through a transparent, multi-factor scoring framework and interactive scenario analysis.

---

## Key Features
- Multi-dimensional market evaluation (economic, growth, readiness, risk)
- Explainable weighted scoring engine
- Strategy guardrails for feasibility filtering
- Scenario-based prioritization (manual sliders and preset strategies)
- Market archetype segmentation using clustering
- Interactive leadership-facing dashboard (Streamlit)

---

## Data Sources
- World Bank (World Development Indicators, 2022)
- EF English Proficiency Index (proxy)
- Numbeo Cost of Living Index (proxy)
- Governance indicators (World Bank proxies)

---

## Methodology
1. Data cleaning and normalization (Min–Max scaling)
2. Category-level scoring:
   - Economic Strength
   - Growth Momentum
   - Market Readiness
   - Risk & Stability
3. Weighted composite scoring with adjustable priorities
4. Strategy guardrails to remove non-viable markets
5. Market archetype clustering
6. Interactive visualization using Streamlit

---

## Outputs
- Ranked list of priority markets
- Market archetype classification
- Country-level insights
- Executive-style recommendations (Top markets + Watchlist)

---

## How to Run Locally
```bash
pip install streamlit pandas numpy scikit-learn
streamlit run app.py
