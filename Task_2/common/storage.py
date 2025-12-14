import pandas as pd
import os

DATA_PATH = "data/feedback.csv"

COLUMNS = [
    "timestamp",
    "rating",
    "review",
    "user_response",
    "summary",
    "recommended_action"
]

def init_storage():
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    if not os.path.exists(DATA_PATH) or os.path.getsize(DATA_PATH) == 0:
        pd.DataFrame(columns=COLUMNS).to_csv(DATA_PATH, index=False)

def read_data():
    try:
        return pd.read_csv(DATA_PATH)
    except:
        return pd.DataFrame(columns=COLUMNS)

def write_data(df):
    tmp = DATA_PATH + ".tmp"
    df.to_csv(tmp, index=False)
    os.replace(tmp, DATA_PATH)
