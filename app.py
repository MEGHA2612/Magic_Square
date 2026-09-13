import streamlit as st
from styles import apply_styles
from screens import (
    show_start_screen,
    show_game_screen,
    show_attempt_history
)

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------
st.set_page_config(
    page_title="Magic Square",
    page_icon="🔢",
    layout="centered"
)

# --------------------------------
# APP THEME
# --------------------------------
st.html(
    apply_styles()
)

# --------------------------------
# GAME STATE
# --------------------------------
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "home"

# --------------------------------
# SCREEN NAVIGATION
# --------------------------------
if st.session_state.current_screen == "home":
    show_start_screen()
elif st.session_state.current_screen == "game":
    show_game_screen()
elif st.session_state.current_screen == "history":
    show_attempt_history()