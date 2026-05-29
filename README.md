# How to Guard Karl-Anthony Towns

A scouting dashboard for exploring how Karl-Anthony Towns' scoring, rebounding, and playmaking patterns change across opponents, seasons, pace environments, and shot-zone profiles.

## Overview

This project analyzes Karl-Anthony Towns' historical game logs and opponent context to provide insight into potentially effective defensive strategies.

The dashboard lets users explore whether Towns' biggest scoring, rebounding, and assist games are associated with changes in variables such as minutes, region-specific shots, and other statistics.

## Features
- Interactive Streamlit dashboard
- Multi-season Karl-Anthony Towns game log database
- Opponent pace data by season
- Opponent shot-zone profile data by season
- Custom graph builder for comparing any numeric variables
Defensive objective analysis:
- - Stop him from scoring
- - Keep him off the glass
- - Limit his playmaking
- Top-game comparison tables
- Opponent matchup summaries
- Downloadable dataset

## Data

The dataset is built using NBA API data and includes:

- KAT box score game logs
- Opponent abbreviations
- Home/away indicator
- Opponent pace
- Opponent shot-zone field goal attempts, makes, and percentages
Derived features such as:
- - Offensive volume
- - Three-point attempt rate
- - Free throw attempt rate
- - Points per minute
- - Rebounds per minute
- - Assists per minute

## Tech Stack
Python
pandas
nba_api
Streamlit
Plotly

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```
Run the dashboard:

```bash
streamlit run MODEL/app.py
```

## Dashboard Sections

### Custom Analysis Workspace

Users can select any numeric variables for the x-axis and y-axis, color by season or opponent, and explore relationships across Towns' historical games.

### Defensive Objective Analysis

Users can choose a scouting goal:

- Stop him from scoring
- Keep him off the glass
- Limit his playmaking

The dashboard then compares Towns' top games for that category against his normal profile to identify the largest statistical differences.

### Opponent Matchup Summary

The dashboard groups games by opponent to show how Towns has historically performed against each team.

## Key Takeaway

This project is intended as a scouting and exploratory analytics tool. The modeling experiments suggested that low-frequency props like blocks are difficult to predict using only box-score and team-level opponent features. 