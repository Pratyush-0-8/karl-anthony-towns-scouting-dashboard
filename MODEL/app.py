import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="How to Guard KAT",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"], .stApp {
    font-family: "Times New Roman", Times, serif !important;
}

.stApp {
    background-color: #f4f1ea;
    color: #111827;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background-color: #fbfaf7;
    border-right: 1px solid #d6d3cc;
}

.big-title {
    font-size: 3rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.25rem;
}

.subtitle {
    font-size: 1.05rem;
    color: #4b5563;
    margin-bottom: 1.5rem;
    max-width: 900px;
}

.section-title {
    font-size: 1.45rem;
    font-weight: 700;
    color: #111827;
    margin-top: 2rem;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid #c9c3b8;
    padding-bottom: 0.35rem;
}

div[data-testid="stMetric"] {
    background-color: #fbfaf7;
    border: 1px solid #d6d3cc;
    border-radius: 6px;
    padding: 1rem;
}

footer, #MainMenu {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">How to Guard Karl-Anthony Towns</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">A scouting dashboard analyzing Towns’ scoring, rebounding, and playmaking patterns using NBA game logs, opponent pace, and shot-zone profiles.</div>',
    unsafe_allow_html=True
)
# -----------------------
# Load data
# -----------------------
df = pd.read_csv("../NBADATA/NBADATA/kkat_df.csv")
df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])
df = df.sort_values("GAME_DATE").reset_index(drop=True)

st.sidebar.download_button(
    label="Download KAT Dataset",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="kkat_df.csv",
    mime="text/csv"
)

# -----------------------
# Sidebar filters
# -----------------------
st.sidebar.header("Filters")

season_options = sorted(df["SEASON"].dropna().unique())
selected_seasons = st.sidebar.multiselect(
    "Season",
    season_options,
    default=season_options
)

season_type_options = sorted(df["SEASON_TYPE"].dropna().unique())
selected_season_types = st.sidebar.multiselect(
    "Season Type",
    season_type_options,
    default=season_type_options
)

opp_options = sorted(df["OPP"].dropna().unique())
selected_opps = st.sidebar.multiselect(
    "Opponent",
    opp_options,
    default=opp_options
)

filtered = df[
    (df["SEASON"].isin(selected_seasons)) &
    (df["SEASON_TYPE"].isin(selected_season_types)) &
    (df["OPP"].isin(selected_opps))
].copy()

st.write(f"Showing **{len(filtered)} games**")

# -----------------------
# Main metric cards
# -----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg PTS", round(filtered["PTS"].mean(), 1))
col2.metric("Avg REB", round(filtered["REB"].mean(), 1))
col3.metric("Avg AST", round(filtered["AST"].mean(), 1))
col4.metric("Avg MIN", round(filtered["MIN"].mean(), 1))

# -----------------------
# Custom graph builder
# -----------------------
st.subheader("Custom Graph Builder")

numeric_cols = filtered.select_dtypes(include=["number"]).columns.tolist()

bad_cols = ["SEASON_ID", "Player_ID", "Game_ID", "VIDEO_AVAILABLE"]
numeric_cols = [col for col in numeric_cols if col not in bad_cols]

c1, c2, c3, c4 = st.columns(4)

with c1:
    x_col = st.selectbox("X-axis", ["GAME_DATE"] + numeric_cols, index=0)

with c2:
    default_y = numeric_cols.index("PTS") if "PTS" in numeric_cols else 0
    y_col = st.selectbox("Y-axis", numeric_cols, index=default_y)

with c3:
    color_col = st.selectbox(
        "Color by",
        ["None", "SEASON", "SEASON_TYPE", "OPP", "HOME"],
        index=1
    )

with c4:
    size_col = st.selectbox(
        "Size by",
        ["None"] + numeric_cols,
        index=0
    )

chart_type = st.radio(
    "Chart type",
    ["Scatter", "Line", "Bar"],
    horizontal=True
)

color_arg = None if color_col == "None" else color_col
size_arg = None if size_col == "None" else size_col

hover_cols = [
    "GAME_DATE", "OPP", "SEASON", "SEASON_TYPE",
    "MIN", "PTS", "REB", "AST", "BLK",
    "FGA", "FG3A", "FTA"
]

hover_cols = [col for col in hover_cols if col in filtered.columns]

if chart_type == "Scatter":
    fig = px.scatter(
        filtered,
        x=x_col,
        y=y_col,
        color=color_arg,
        size=size_arg,
        hover_data=hover_cols,
        title=f"{y_col} vs {x_col}"
    )
elif chart_type == "Line":
    fig = px.line(
        filtered,
        x=x_col,
        y=y_col,
        color=color_arg,
        hover_data=hover_cols,
        title=f"{y_col} over {x_col}"
    )
else:
    fig = px.bar(
        filtered,
        x=x_col,
        y=y_col,
        color=color_arg,
        hover_data=hover_cols,
        title=f"{y_col} by {x_col}"
    )

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Rolling trend overlay
# -----------------------
st.subheader("Trend Overlay")

overlay_col = st.selectbox(
    "Choose stat to overlay with rolling average",
    ["PTS", "REB", "AST", "BLK", "MIN", "FGA", "FG3A", "FTA"],
    index=0
)

window = st.slider("Rolling average window", 3, 20, 5)

trend_df = filtered.sort_values("GAME_DATE").copy()
trend_df[f"{overlay_col}_ROLLING_{window}"] = trend_df[overlay_col].rolling(window).mean()

fig_trend = px.line(
    trend_df,
    x="GAME_DATE",
    y=[overlay_col, f"{overlay_col}_ROLLING_{window}"],
    hover_data=hover_cols,
    title=f"{overlay_col} with {window}-game rolling average"
)

st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------
# How to Guard KAT section
# -----------------------
st.subheader("How Do You Want to Guard KAT?")

goal = st.selectbox(
    "Defensive goal",
    ["Stop him from scoring", "Keep him off the glass", "Limit his playmaking"]
)

top_n = st.slider("Analyze top N games", 5, 75, 25)

if goal == "Stop him from scoring":
    target = "PTS"
    supporting_cols = [
        "MIN", "FGA", "FG3A", "FTA",
        "FG_PCT", "FG3_PCT", "FT_PCT",
        "USAGE_PROXY", "FG3A_RATE", "FTA_RATE",
        "OPP_PACE"
    ]

elif goal == "Keep him off the glass":
    target = "REB"
    supporting_cols = [
        "MIN", "OREB", "DREB", "REB",
        "FGA", "PF", "REB_PER_MIN",
        "OPP_PACE"
    ]

else:
    target = "AST"
    supporting_cols = [
        "MIN", "AST", "TOV", "FGA", "PTS",
        "AST_PER_MIN", "USAGE_PROXY",
        "OPP_PACE"
    ]

# Add opponent shot-zone columns if they exist
shot_zone_cols = [
    col for col in filtered.columns
    if any(word in col.lower() for word in [
        "restricted", "paint", "mid", "corner", "break", "backcourt"
    ])
    and any(stat in col.lower() for stat in ["fga", "fgm", "fg_pct"])
]

supporting_cols = supporting_cols + shot_zone_cols
supporting_cols = [col for col in supporting_cols if col in filtered.columns]

top_games = filtered.sort_values(target, ascending=False).head(top_n)

top_avg = top_games[supporting_cols].mean(numeric_only=True)
all_avg = filtered[supporting_cols].mean(numeric_only=True)

comparison = pd.DataFrame({
    "Top Games Avg": top_avg,
    "All Games Avg": all_avg,
    "Difference": top_avg - all_avg,
    "Pct Difference": ((top_avg - all_avg) / all_avg.replace(0, pd.NA)) * 100
}).sort_values("Difference", ascending=False)

st.write(f"### Top {top_n} {target} Games Profile")
st.dataframe(comparison, use_container_width=True)

fig_diff = px.bar(
    comparison.reset_index().rename(columns={"index": "Metric"}),
    x="Metric",
    y="Difference",
    title=f"What changes in KAT's top {top_n} {target} games?"
)

st.plotly_chart(fig_diff, use_container_width=True)

# -----------------------
# Simple scouting takeaway
# -----------------------
st.write("### Data-Driven Scouting Takeaway")

top_drivers = comparison.head(5)

for metric, row in top_drivers.iterrows():
    st.write(
        f"- **{metric}** is higher by **{round(row['Difference'], 2)}** "
        f"in KAT's top {top_n} {target} games."
    )

st.write("### Top Games")
display_cols = [
    "GAME_DATE", "OPP", "SEASON", "SEASON_TYPE",
    "MIN", "PTS", "REB", "AST", "BLK",
    "FGA", "FG3A", "FTA", "USAGE_PROXY", "OPP_PACE"
]
display_cols = [col for col in display_cols if col in top_games.columns]

st.dataframe(
    top_games[display_cols],
    use_container_width=True
)

# -----------------------
# Opponent summary
# -----------------------
st.subheader("Opponent Matchup Summary")

matchup_summary = filtered.groupby("OPP").agg(
    games=("Game_ID", "count"),
    avg_min=("MIN", "mean"),
    avg_pts=("PTS", "mean"),
    avg_reb=("REB", "mean"),
    avg_ast=("AST", "mean"),
    avg_blk=("BLK", "mean"),
    avg_fga=("FGA", "mean"),
    avg_fg3a=("FG3A", "mean"),
    avg_fta=("FTA", "mean"),
    avg_pace=("OPP_PACE", "mean")
).reset_index()

st.dataframe(
    matchup_summary.sort_values("avg_pts", ascending=False),
    use_container_width=True
)