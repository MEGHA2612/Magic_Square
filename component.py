import streamlit as st

# --------------------------------
# READ FRONTEND FILES
# --------------------------------
with open("web/grid.html", "r", encoding="utf-8") as file:
    HTML = file.read()

with open("web/grid.css", "r", encoding="utf-8") as file:
    CSS = file.read()

with open("web/grid.js", "r", encoding="utf-8") as file:
    JS = file.read()

# --------------------------------
# CREATE COMPONENT
# --------------------------------
magic_square_component = (
    st.components.v2.component(
        name="magic_square",
        html=HTML,
        css=CSS,
        js=JS,
        isolate_styles=True
    )
)

# --------------------------------
# GAME BOARD
# --------------------------------
def magic_square_board(
    on_check_change=None,
    on_hint_change=None,
    restart=False,
    hints_left=3,
    hint_result=None
):
    return magic_square_component(
        key="magic_square_game",
        data={
            "restart": restart,
            "hints_left": hints_left,
            "hint_result": hint_result
        },
        on_check_change=on_check_change,
        on_hint_change=on_hint_change
    )