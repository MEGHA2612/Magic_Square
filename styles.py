# --------------------------------
# APPLICATION STYLES
# --------------------------------
def apply_styles():
    return """
    <style>

    /* --------------------------------
       WHOLE STREAMLIT PAGE
    -------------------------------- */
    .stApp {
        background: #171329;
        color: #f5efff;
    }

    /* --------------------------------
       START SCREEN
    -------------------------------- */
    .start-screen {
        text-align: center;
        padding: 20px 10px 10px;
    }
    .start-screen h1 {
        font-size: 42px;
        margin-bottom: 8px;
        color: #d9b8ff !important;
    }
    .start-level {
        font-size: 20px;
        color: #b9a7d9;
    }

    /* --------------------------------
       HOW TO PLAY BOX
    -------------------------------- */
    .how-to-play {
        max-width: 650px;
        margin: 30px auto;
        padding: 25px 30px;
        background: #211a38;
        border: 1px solid #4b3b69;
        border-radius: 18px;
        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.25);
    }
    .how-to-play h2 {
        color: #d9b8ff !important;
        margin-bottom: 20px;
    }
    .how-to-play p {
        color: #e8def5;
        font-size: 16px;
        margin: 12px 0;
        line-height: 1.5;
    }

    /* --------------------------------
       START BUTTON
    -------------------------------- */
    .stButton > button {
        background: #8b4de8;
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        padding: 12px;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background: #a96cff;
        color: white;
        border: none;
        transform: translateY(-2px);
    }

    /* --------------------------------
       METRICS
    -------------------------------- */
    [data-testid="stMetricLabel"] {
        color: #c7b6df !important;
    }
    [data-testid="stMetricValue"] {
        color: #f5efff !important;
    }

    /* --------------------------------
       NORMAL TEXT
    -------------------------------- */
    p, li {
        color: #e8def5;
    }

    /* --------------------------------
       ATTEMPT HISTORY CARD
    -------------------------------- */
    .attempt-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 650px;
        margin: 12px auto;
        padding: 16px 22px;
        background: #211a38;
        border: 1px solid #4b3b69;
        border-radius: 14px;
        box-shadow:
            0 6px 18px rgba(0, 0, 0, 0.25);
    }
    .attempt-number {
        color: #d9b8ff;
        font-size: 17px;
        font-weight: bold;
    }
    .attempt-time {
        color: #e8def5;
        font-size: 16px;
    }
    .attempt-result {
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """