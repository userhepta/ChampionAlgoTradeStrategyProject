import pandas as pd
import matplotlib

# Path to the CSV file (1 min bar ohlcv csv)
file_path = 'csv/DAT_ASCII_XAUUSD_M1_all.csv'

# Read the CSV file
df_raw = pd.read_csv(file_path, delimiter=';', header=None)

# Assign column names (adjust based on your data)
df_raw.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume'
