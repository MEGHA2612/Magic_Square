# --------------------------------
# APPLICATION SCREENS
# --------------------------------
import streamlit as st


# --------------------------------
# START SCREEN
# --------------------------------
def show_start_screen():
    st.html(
        """
        <div class="start-screen">
            <h1>Magic Square</h1>
            <h2>A logic test for your brain.</h2>
            <div class="start-level">
                Simple 3 × 3 magic square gird.
            </div>
        </div>
        """
    )

    # --------------------------------
    # HOW TO PLAY
    # --------------------------------
    st.html(
        """
        <div class="how-to-play">
            <h2>📖 How to Play</h2>

            <p>1. Fill the 3 × 3 grid with numbers <b>1–9</b>.</p>
            <p>2. Use each number <b>only once</b>.</p>
            <p>3. Every row, column & diagonal must add up to <b>15</b>.</p>
            <p>4. Click a cell and <b>type the number directly</b>.</p>
            <p>5. You have <b>3 hints</b> to help you.</p>
            <p>6. No time limit — <b>take your time!</b></p>
            <p>7. Your stopwatch starts when you press <b>START</b>.</p>
        </div>
        """
    )

    # --------------------------------
    # START BUTTON
    # --------------------------------
    if st.button("▶ START", use_container_width=True):
        st.session_state.current_screen = "game"
        st.rerun()

# --------------------------------
# GAME SCREEN
# --------------------------------
def show_game_screen():
    from config import (
        GRID_SIZE,
        TARGET_SUM,
        TOTAL_HINTS
    )
    from component import magic_square_board
    from validation import validate_magic_square
    from hint import get_hint

    # --------------------------------
    # INITIALIZE GAME STATE
    # --------------------------------
    if "attempts" not in st.session_state:
        st.session_state.attempts = []

    if "hints_left" not in st.session_state:
        st.session_state.hints_left = TOTAL_HINTS

    if "restart_game" not in st.session_state:
        st.session_state.restart_game = False

    if "hint_requested" not in st.session_state:
        st.session_state.hint_requested = False

    if "hint_result" not in st.session_state:
        st.session_state.hint_result = None

    if "hint_number" not in st.session_state:
        st.session_state.hint_number = 0

    # --------------------------------
    # GAME INFORMATION
    # --------------------------------
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 Target Sum", TARGET_SUM)

    with col2:
        st.metric("💡 Hints", st.session_state.hints_left)

    # --------------------------------
    # HINT CALLBACK
    # --------------------------------
    def handle_hint():
        st.session_state.hint_requested = True

    # --------------------------------
    # GAME BOARD
    # --------------------------------
    result = magic_square_board(
        on_check_change=lambda: None,
        on_hint_change=handle_hint,
        restart=st.session_state.restart_game,
        hints_left=st.session_state.hints_left,
        hint_result=st.session_state.hint_result
    )

    # --------------------------------
    # PROCESS HINT REQUEST
    # --------------------------------
    if (result.hint is not None and st.session_state.hints_left > 0):
        current_grid = result.hint["grid"]
        hint = get_hint(current_grid)

        if hint is not None:
            # Use one hint
            st.session_state.hints_left -= 1
            # Give every hint a unique number
            st.session_state.hint_number += 1
            # Store the hint for the frontend
            st.session_state.hint_result = {
                "row": hint["row"],
                "col": hint["col"],
                "value": hint["value"],
                "id": st.session_state.hint_number
            }
        st.session_state.hint_requested = False

        # Rerun once so the updated hint
        # is sent to the JavaScript component
        st.rerun()

    # --------------------------------
    # GET CHECK RESULT
    # --------------------------------
    check_result = result.check
    grid = None
    elapsed_time = 0
    if check_result is not None:
        grid = check_result["grid"]
        elapsed_time = check_result["elapsed"]

    # --------------------------------
    # VALIDATE ANSWER
    # --------------------------------
    if grid is not None:
        valid, message = validate_magic_square(grid, TARGET_SUM)

        # --------------------------------
        # SAVE ATTEMPT
        # --------------------------------
        attempt_number = (len(st.session_state.attempts) + 1)

        st.session_state.attempts.append(
            {
                "attempt": attempt_number,
                "time": elapsed_time,
                "completed": valid
            }
        )

        # --------------------------------
        # SHOW RESULT
        # --------------------------------
        if valid:
            st.success(message)
        else:
            st.error(message)

            # ----------------------------
            # RESET HINTS
            # ----------------------------
            st.session_state.hints_left = (TOTAL_HINTS)
            st.session_state.hint_result = (None)
            st.session_state.hint_number = (0)

            # ----------------------------
            # RESTART GAME
            # ----------------------------
            st.session_state.restart_game = True
            st.rerun()

    # --------------------------------
    # RESET RESTART FLAG
    # --------------------------------
    if st.session_state.restart_game:
        st.session_state.restart_game = False

    # --------------------------------
    # ATTEMPT HISTORY BUTTON
    # --------------------------------
    if st.button("📊 ATTEMPT HISTORY", use_container_width=True):
        st.session_state.current_screen = ("history")
        st.rerun()

    # --------------------------------
    # HOME BUTTON
    # --------------------------------
    if st.button("🏠 HOME", use_container_width=True):
        st.session_state.current_screen = ("home")
        st.rerun()

# --------------------------------
# ATTEMPT HISTORY SCREEN
# --------------------------------
def show_attempt_history():
    st.title("📊 Attempt History")
    st.write("Here you can view all your attempts.")

    # --------------------------------
    # NO ATTEMPTS
    # --------------------------------
    if not st.session_state.attempts:
        st.info("No attempts yet. Start playing!")
    else:
        for attempt in st.session_state.attempts:
            attempt_number = (attempt["attempt"])
            elapsed_time = (attempt["time"])
            completed = (attempt["completed"])
            minutes = (elapsed_time // 60)
            seconds = (elapsed_time % 60)
            time_text = (f"{minutes:02d}:{seconds:02d}")

            if completed:
                result_text = ("✅ Completed")
            else:
                result_text = ("❌ Not Completed")
            st.html(
                f"""
                <div class="attempt-card">
                    <div class="attempt-number">
                        Attempt {attempt_number}
                    </div>
                    <div class="attempt-time">
                        ⏱️ {time_text}
                    </div>
                    <div class="attempt-result">
                        {result_text}
                    </div>
                </div>
                """
            )

    # --------------------------------
    # BACK TO GAME
    # --------------------------------
    if st.button("← BACK TO GAME", use_container_width=True):
        st.session_state.current_screen = ("game")
        st.rerun()