import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import base64

# ============================================================
# Page setup
# ============================================================

st.set_page_config(
    page_title="Stop Karl-Anthony Towns",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"], .stApp {
    font-family: "Times New Roman", Times, serif !important;
}

.stApp {
    background-color: #f7f8fa;
    color: #0B1F3A;
}

.block-container {
    max-width: 1260px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 3px solid #006BB6;
}

/* Hero landing */
.hero {
    min-height: 58vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.hero-title {
    font-size: 5.4rem;
    font-weight: 800;
    color: #006BB6;
    letter-spacing: -0.04em;
    line-height: 1;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: #334155;
    max-width: 820px;
    margin: 0 auto;
    line-height: 1.45;
}

/* Page title for non-home pages */
.page-title {
    font-size: 3rem;
    font-weight: 800;
    color: #006BB6;
    margin-bottom: 0.25rem;
}

.page-subtitle {
    font-size: 1.05rem;
    color: #334155;
    max-width: 950px;
    line-height: 1.45;
    margin-bottom: 1.25rem;
}

/* Sections */
.section-title {
    font-size: 1.45rem;
    font-weight: 700;
    color: #0B1F3A;
    margin-top: 1.4rem;
    margin-bottom: 0.75rem;
    border-bottom: 2px solid #F58426;
    padding-bottom: 0.35rem;
}

.section-note {
    color: #475569;
    font-size: 0.98rem;
    margin-top: -0.2rem;
    margin-bottom: 1rem;
    line-height: 1.45;
}

/* Cards */
.report-card {
    background-color: #ffffff;
    border-left: 5px solid #F58426;
    border-top: 1px solid #BEC0C2;
    border-right: 1px solid #BEC0C2;
    border-bottom: 1px solid #BEC0C2;
    border-radius: 7px;
    padding: 1rem 1.15rem;
    margin-bottom: 1rem;
}

.report-card h3 {
    color: #006BB6;
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.report-card p,
.report-card li {
    color: #1f2937;
    font-size: 0.98rem;
    line-height: 1.45;
}

/* Metrics */
div[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #BEC0C2;
    border-top: 4px solid #006BB6;
    border-radius: 7px;
    padding: 0.65rem 0.75rem;
}

div[data-testid="stMetricValue"] {
    color: #0B1F3A;
    font-size: 1.45rem;
}

div[data-testid="stMetricLabel"] {
    color: #334155;
    font-size: 0.88rem;
}

/* Buttons */
.stButton button,
.stDownloadButton button {
    background-color: #006BB6 !important;
    color: white !important;
    border: 1px solid #006BB6 !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}

.stButton button *,
.stDownloadButton button * {
    color: white !important;
}

.stButton button:hover,
.stDownloadButton button:hover {
    background-color: #F58426 !important;
    color: white !important;
    border: 1px solid #F58426 !important;
}

.stButton button:hover *,
.stDownloadButton button:hover * {
    color: white !important;
}

/* Kill red focus/active borders */
button:active,
button:focus,
button:focus-visible,
input:focus,
textarea:focus,
div[data-baseweb="select"] > div:focus-within {
    outline: none !important;
    border-color: #F58426 !important;
    box-shadow: 0 0 0 0.15rem rgba(245, 132, 38, 0.25) !important;
    color: inherit !important;
}

/* Nav buttons */
.nav-button button {
    min-height: 54px !important;
    background-color: #ffffff !important;
    color: #006BB6 !important;
    border: 1px solid #BEC0C2 !important;
    border-top: 4px solid #006BB6 !important;
    border-radius: 8px !important;
    font-size: 0.98rem !important;
    font-weight: 800 !important;
}

.nav-button button * {
    color: #006BB6 !important;
}

.nav-button button:hover,
.nav-button button:active,
.nav-button button:focus,
.nav-button button:focus-visible {
    background-color: #F58426 !important;
    color: white !important;
    border-color: #F58426 !important;
}

.nav-button button:hover *,
.nav-button button:active *,
.nav-button button:focus *,
.nav-button button:focus-visible * {
    color: white !important;
}

/* Feature buttons */
.feature-button button {
    min-height: 52px !important;
    text-align: left !important;
    background-color: #006BB6 !important;
    color: white !important;
    border: 1px solid #006BB6 !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    margin-bottom: 0.4rem !important;
}

.feature-button button * {
    color: white !important;
}

.feature-button button:hover,
.feature-button button:active,
.feature-button button:focus,
.feature-button button:focus-visible {
    background-color: #F58426 !important;
    color: white !important;
    border-color: #F58426 !important;
}

.feature-button button:hover *,
.feature-button button:active *,
.feature-button button:focus *,
.feature-button button:focus-visible * {
    color: white !important;
}

/* Sidebar selected pills */
section[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background-color: #006BB6 !important;
    color: white !important;
    border-radius: 6px !important;
    border: 1px solid #005A9C !important;
}

section[data-testid="stSidebar"] span[data-baseweb="tag"] svg {
    fill: white !important;
}

/* Sidebar inputs */
section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    border-color: #BEC0C2 !important;
    background-color: white !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div:focus-within {
    border-color: #F58426 !important;
    box-shadow: 0 0 0 0.15rem rgba(245, 132, 38, 0.25) !important;
}

section[data-testid="stSidebar"] label {
    color: #0B1F3A !important;
    font-weight: 700 !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 1px solid #BEC0C2 !important;
    border-radius: 6px !important;
}

/* Radio cleanup */
div[role="radiogroup"] label {
    color: #0B1F3A !important;
    font-weight: 600 !important;
}

div[role="radiogroup"] label:focus-within {
    color: #006BB6 !important;
    outline: none !important;
    box-shadow: none !important;
}

footer, #MainMenu {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# Helpers
# ============================================================

DISPLAY_NAMES = {
    "PTS": "Points",
    "REB": "Rebounds",
    "AST": "Assists",
    "BLK": "Blocks",
    "STL": "Steals",
    "MIN": "Minutes",
    "FGA": "Field Goal Attempts",
    "FGM": "Field Goals Made",
    "FG_PCT": "Field Goal %",
    "FG3A": "Three-Point Attempts",
    "FG3M": "Three-Pointers Made",
    "FG3_PCT": "Three-Point %",
    "FTA": "Free Throw Attempts",
    "FTM": "Free Throws Made",
    "FT_PCT": "Free Throw %",
    "OREB": "Offensive Rebounds",
    "DREB": "Defensive Rebounds",
    "TOV": "Turnovers",
    "PF": "Personal Fouls",
    "PLUS_MINUS": "Plus-Minus",
    "OPP_PACE": "Opponent Pace",
    "USAGE_PROXY": "Offensive Volume",
    "FG3A_RATE": "Three-Point Attempt Rate",
    "FTA_RATE": "Free Throw Attempt Rate",
    "REB_PER_MIN": "Rebounds per Minute",
    "PTS_PER_MIN": "Points per Minute",
    "AST_PER_MIN": "Assists per Minute",
}


def pretty_name(col):
    return DISPLAY_NAMES.get(str(col), str(col).replace("_", " ").title())


def section(title, note=None):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if note:
        st.markdown(f'<div class="section-note">{note}</div>', unsafe_allow_html=True)


def style_chart(fig):
    fig.update_layout(
        template="plotly_white",
        font=dict(family="Times New Roman", size=14, color="#0B1F3A"),
        title_font=dict(family="Times New Roman", size=21, color="#006BB6"),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        margin=dict(l=45, r=30, t=65, b=45),
        legend=dict(bgcolor="rgba(255,255,255,0)")
    )
    fig.update_xaxes(showgrid=True, gridcolor="#E5E7EB", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#E5E7EB", zeroline=False)
    return fig


def clean_index_table(dataframe):
    out = dataframe.copy()
    out.index = [pretty_name(i) for i in out.index]
    return out.round(2)


def get_shot_zone_cols(dataframe):
    return [
        col for col in dataframe.columns
        if any(word in col.lower() for word in [
            "restricted", "paint", "mid", "corner", "break", "backcourt"
        ])
        and any(stat in col.lower() for stat in ["fga", "fgm", "fg_pct"])
    ]


def direction_phrase(value):
    if value > 0:
        return f"{abs(value):.2f} higher"
    if value < 0:
        return f"{abs(value):.2f} lower"
    return "unchanged"


def set_page(page_name):
    st.session_state.page = page_name


def nav_buttons():
    nav_cols = st.columns(5)

    nav_items = [
        ("Home", "home"),
        ("Scouting", "scouting"),
        ("Matchups", "matchups"),
        ("Trends", "trends"),
        ("Custom Trend", "custom"),
    ]

    for col, (label, page_name) in zip(nav_cols, nav_items):
        with col:
            st.markdown('<div class="nav-button">', unsafe_allow_html=True)
            st.button(
                label,
                key=f"nav_{page_name}",
                use_container_width=True,
                on_click=set_page,
                args=(page_name,)
            )
            st.markdown('</div>', unsafe_allow_html=True)


def page_title(title, subtitle):
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{subtitle}</div>', unsafe_allow_html=True)
    nav_buttons()


# ============================================================
# Load data
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "NBADATA" / "NBADATA" / "kkat_df.csv"

df = pd.read_csv(DATA_PATH)
df["GAME_DATE"] = pd.to_datetime(df["GAME_DATE"])
df = df.sort_values("GAME_DATE").reset_index(drop=True)

# ============================================================
# Sidebar filters
# ============================================================

st.sidebar.header("Set Filters")
st.sidebar.caption("The entire dashboard updates from this filtered game sample.")

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

if filtered.empty:
    st.warning("No games match your filters. Add more seasons, season types, or opponents in the sidebar.")
    st.stop()

st.sidebar.markdown("---")
st.sidebar.header("Export")
st.sidebar.download_button(
    label="Download Full Dataset",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="kkat_df.csv",
    mime="text/csv"
)

# ============================================================
# Page state
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

page = st.session_state.page

# ============================================================
# Home / landing page
# ============================================================

if page == "home":
    st.markdown("""
    <div class="hero">
        <div>
            <div class="hero-title">Stop Karl-Anthony Towns</div>
            <div class="hero-subtitle">
                A scouting dashboard made to <strong>STOP</strong> Karl-Anthony Towns 
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    
    kat_path = BASE_DIR / "ASSETS" / "KATSAD.gif"
    arrow_path = BASE_DIR / "ASSETS" / "DARROW.gif"

    kat_base64 = base64.b64encode(kat_path.read_bytes()).decode()
    arrow_base64 = base64.b64encode(arrow_path.read_bytes()).decode()

    st.markdown(
        f"""
        <div style="
            margin-top: -35px;
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            justify-items: center;
            column-gap: 1.5rem;
        ">
            <img src="data:image/gif;base64,{arrow_base64}" width="150" style="transform: rotate(90deg);">
            <img src="data:image/gif;base64,{kat_base64}" width="400">
            <img src="data:image/gif;base64,{arrow_base64}" width="150" style="transform: rotate(90deg);">
        </div>
        """,
        unsafe_allow_html=True
    )

    section(
        "Overview",
        "Filter out certain games, then scroll to choose an analysis path."
    )

    metric_cols = st.columns(5)
    metric_cols[0].metric("Games", len(filtered))
    metric_cols[1].metric("Avg Points", round(filtered["PTS"].mean(), 1))
    metric_cols[2].metric("Avg Rebounds", round(filtered["REB"].mean(), 1))
    metric_cols[3].metric("Avg Assists", round(filtered["AST"].mean(), 1))
    metric_cols[4].metric("Avg Minutes", round(filtered["MIN"].mean(), 1))

    section(
        "Choose an Analysis Path",
    )

    feature_buttons = [
        ("**Scouting** : Analyze what strategies have slowed KAT down in the past", "scouting"),
        ("**Matchups** : Compare how KAT performs against each team", "matchups"),
        ("**Trends** : Examine KAT's performance over time", "trends"),
        ("**Custom Trend Finder** : Perform your own analysis on KAT's stats", "custom"),
    ]

    for label, page_name in feature_buttons:
        st.markdown('<div class="feature-button">', unsafe_allow_html=True)
        st.button(
            label,
            key=f"home_{page_name}",
            use_container_width=True,
            on_click=set_page,
            args=(page_name,)
        )
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# Scouting page
# ============================================================

if page == "scouting":
    page_title(
        "How do you want to guard KAT?",
        "Choose a defensive goal, compare selected games against his baseline, then inspect the exact games behind the read."
    )

    section(
        "Customize Scouting",
        "These controls only affect the scouting report below."
    )

    setup_col1, setup_col2, setup_col3 = st.columns([1.4, 1, 1])

    with setup_col1:
        goal = st.radio(
            "Target Statistic",
            ["Points", "Rebounds", "Assists"],
            horizontal=False
        )

    with setup_col2:
        game_group = st.radio(
            "Game group",
            ["Top Performances", "Worst Performances"],
            horizontal=False
        )

    with setup_col3:
        top_n = st.slider(
            "Compare N games",
            min_value=5,
            max_value=min(75, len(filtered)),
            value=min(25, len(filtered))
        )

    if goal == "Points":
        target = "PTS"
        supporting_cols = [
            "MIN", "FGA", "FG3A", "FTA",
            "FG_PCT", "FG3_PCT", "FT_PCT",
            "USAGE_PROXY", "FG3A_RATE", "FTA_RATE",
            "OPP_PACE"
        ]

    elif goal == "Rebounds":
        target = "REB"
        supporting_cols = [
            "MIN", "OREB", "DREB",
            "FGA", "PF", "REB_PER_MIN",
            "OPP_PACE"
        ]

    else:
        target = "Assists"
        supporting_cols = [
            "MIN", "TOV", "FGA", "PTS",
            "AST_PER_MIN", "USAGE_PROXY",
            "OPP_PACE"
        ]

    shot_zone_cols = get_shot_zone_cols(filtered)
    supporting_cols = [col for col in supporting_cols + shot_zone_cols if col in filtered.columns]

    ascending_order = True if game_group == "Lowest games" else False
    selected_games = filtered.sort_values(target, ascending=ascending_order).head(top_n)

    selected_avg = selected_games[supporting_cols].mean(numeric_only=True)
    all_avg = filtered[supporting_cols].mean(numeric_only=True)

    comparison = pd.DataFrame({
        "Selected Games Avg": selected_avg,
        "All Games Avg": all_avg,
        "Difference": selected_avg - all_avg,
        "Pct Difference": ((selected_avg - all_avg) / all_avg.replace(0, pd.NA)) * 100
    })

    comparison = comparison.drop(index=target, errors="ignore")

    if game_group == "Highest games":
        comparison = comparison.sort_values("Difference", ascending=False)
    else:
        comparison = comparison.sort_values("Difference", ascending=True)

    group_label = "highest" if game_group == "Highest games" else "lowest"

    if len(comparison) > 0:
        main_driver = comparison.index[0]
        main_diff = comparison.iloc[0]["Difference"]
    else:
        main_driver = None
        main_diff = 0

    section(
        "Main Scouting Read",
    )

    driver_items = ""
    for metric, row in comparison.head(3).iterrows():
        driver_items += (
            f"<li><b>{pretty_name(metric)}</b>: "
            f"{direction_phrase(row['Difference'])} than his filtered average.</li>"
        )

    if main_driver is not None:
        st.markdown(f"""
        <div class="report-card">
            <h3>{goal}</h3>
            <p>
            In Towns' <b>{group_label} {top_n} {pretty_name(target)}</b> games,
            the most important related changes are:
            </p>
            <ul>
                {driver_items}
            </ul>
            <p>
            The strongest related lever is <b>{pretty_name(main_driver)}</b>, which is
            <b>{direction_phrase(main_diff)}</b> than his filtered baseline.
            </p>
        </div>
        """, unsafe_allow_html=True)

    section(
        "Games Profile Data",
        "This table compares the selected games against the full filtered sample."
    )

    st.dataframe(clean_index_table(comparison), use_container_width=True)

    section(
        "Differential Chart",
        "Positive values mean the stat was higher in the selected games. Negative values mean it was lower."
    )

    chart_df = comparison.head(12).reset_index().rename(columns={"index": "Metric"})
    chart_df["Metric"] = chart_df["Metric"].apply(pretty_name)

    fig_diff = px.bar(
        chart_df,
        x="Difference",
        y="Metric",
        orientation="h",
        title=f"Largest Related Changes in {top_n} {game_group} for {pretty_name(target)}"
    )
    fig_diff.update_layout(yaxis=dict(autorange="reversed"))
    fig_diff = style_chart(fig_diff)
    st.plotly_chart(fig_diff, use_container_width=True)

    section(
        "Selected Games Log",
        "These are the exact games used for the scouting comparison."
    )

    display_cols = [
        "GAME_DATE", "OPP", "SEASON", "SEASON_TYPE",
        "MIN", "PTS", "REB", "AST", "BLK",
        "FGA", "FG3A", "FTA", "USAGE_PROXY", "OPP_PACE"
    ]
    display_cols = [col for col in display_cols if col in selected_games.columns]

    selected_games_display = selected_games[display_cols].copy()
    selected_games_display = selected_games_display.rename(
        columns={col: pretty_name(col) for col in selected_games_display.columns}
    )

    st.dataframe(selected_games_display, use_container_width=True)

# ============================================================
# Matchups page
# ============================================================

if page == "matchups":
    page_title(
        "Matchup Data",
        "Compare how Towns performs against different opponents in the current filtered sample."
    )

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
    ).reset_index().round(2)

    metric_choice = st.selectbox(
        "Rank opponents by",
        ["avg_pts", "avg_reb", "avg_ast", "avg_min", "avg_fga", "avg_fta", "avg_pace"],
        format_func=pretty_name
    )

    sorted_matchups = matchup_summary.sort_values(metric_choice, ascending=False)

    fig_matchup = px.bar(
        sorted_matchups,
        x="OPP",
        y=metric_choice,
        title=f"Towns by Opponent: {pretty_name(metric_choice)}"
    )
    fig_matchup = style_chart(fig_matchup)
    st.plotly_chart(fig_matchup, use_container_width=True)

    st.dataframe(sorted_matchups, use_container_width=True)

# ============================================================
# Trends page
# ============================================================

if page == "trends":
    page_title(
        "Trends",
        "Track one core stat over time through a rolling average."
    )

    trend_options = ["PTS", "REB", "AST", "BLK", "MIN", "FGA", "FG3A", "FTA"]

    trend_left, trend_right = st.columns([1, 1])

    with trend_left:
        trend_stat = st.selectbox(
            "Stat to track",
            trend_options,
            format_func=pretty_name,
            index=0
        )

    with trend_right:
        window = st.slider("Rolling average window", 3, 20, 5)

    trend_df = filtered.sort_values("GAME_DATE").copy()
    trend_df[f"{trend_stat}_ROLLING_{window}"] = trend_df[trend_stat].rolling(window).mean()

    fig_trend = px.line(
        trend_df,
        x="GAME_DATE",
        y=[trend_stat, f"{trend_stat}_ROLLING_{window}"],
        hover_data=["OPP", "SEASON", "MIN", "PTS", "REB", "AST", "BLK"],
        title=f"{pretty_name(trend_stat)} with {window}-Game Rolling Average"
    )
    fig_trend = style_chart(fig_trend)
    st.plotly_chart(fig_trend, use_container_width=True)

# ============================================================
# Custom Finder page
# ============================================================

if page == "custom":
    page_title(
        "Custom Trend Finder",
        "Build your own graph to explore any relationship in the filtered sample."
    )

    numeric_cols = filtered.select_dtypes(include=["number"]).columns.tolist()
    bad_cols = ["SEASON_ID", "Player_ID", "Game_ID", "VIDEO_AVAILABLE"]
    numeric_cols = [col for col in numeric_cols if col not in bad_cols]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        x_col = st.selectbox(
            "X-axis",
            ["GAME_DATE"] + numeric_cols,
            index=0,
            format_func=pretty_name
        )

    with c2:
        default_y = numeric_cols.index("PTS") if "PTS" in numeric_cols else 0
        y_col = st.selectbox(
            "Y-axis",
            numeric_cols,
            index=default_y,
            format_func=pretty_name
        )

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
            index=0,
            format_func=pretty_name
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
        fig_custom = px.scatter(
            filtered,
            x=x_col,
            y=y_col,
            color=color_arg,
            size=size_arg,
            hover_data=hover_cols,
            title=f"{pretty_name(y_col)} vs {pretty_name(x_col)}"
        )

    elif chart_type == "Line":
        fig_custom = px.line(
            filtered,
            x=x_col,
            y=y_col,
            color=color_arg,
            hover_data=hover_cols,
            title=f"{pretty_name(y_col)} over {pretty_name(x_col)}"
        )

    else:
        fig_custom = px.bar(
            filtered,
            x=x_col,
            y=y_col,
            color=color_arg,
            hover_data=hover_cols,
            title=f"{pretty_name(y_col)} by {pretty_name(x_col)}"
        )

    fig_custom = style_chart(fig_custom)
    st.plotly_chart(fig_custom, use_container_width=True)