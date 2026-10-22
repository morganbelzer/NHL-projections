
import streamlit as st

import pandas as pd



st.title("NHL Win Projections")

ratings = pd.read_csv("ratings.csv").set_index("team")["rating"]

proj = pd.read_csv("projections.csv").set_index("team")

EDGE = 20



tab1, tab2 = st.tabs(["Matchup", "Season projections"])

with tab1:

    teams = sorted(ratings.index)

    home = st.selectbox("Home", teams, index=teams.index("TOR"))

    away = st.selectbox("Away", teams, index=teams.index("BUF"))

    if home == away:

        st.warning("Pick two different teams.")

    else:

        p = 1 / (1 + 10 ** (-((ratings[home] + EDGE) - ratings[away]) / 400))

        st.metric(f"{home} (home) win probability", f"{p:.1%}")

        st.metric(f"{away} win probability", f"{1 - p:.1%}")

with tab2:

    st.dataframe(proj.sort_values("projected_wins", ascending=False))
