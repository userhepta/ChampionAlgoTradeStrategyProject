import pandas as pd
import matplotlib

# Path to the CSV file (1 min bar ohlcv csv)
file_path = 'csv/DAT_ASCII_XAUUSD_M1_all.csv'

# Read the CSV file
df_raw = pd.read_csv(file_path, delimiter=';', header=None)

# Assign column names (adjust based on your data)
df_raw.columns = ['datetime', 'open', 'high', 'low', 'close', 'volume']  # Add more columns if needed
df_raw = df_raw.drop(columns='volume')

# Attempt to convert DateTime column, coercing errors to NaT (Not a Time)
df_raw['datetime'] = pd.to_datetime(df_raw['datetime'], format='%Y%m%d %H%M%S')

# # Localize to US Eastern Time (EDT, UTC-4) [if needed]
# df_raw['datetime'] = df_raw['datetime'].dt.tz_localize('America/New_York')

# # Convert to Hong Kong Time (HKT, UTC+8) [if needed]
# df_raw['datetime'] = df_raw['datetime'].dt.tz_convert('Asia/Hong_Kong')

df_raw = df_raw.set_index('datetime')

# Make a copy of the original dataset
df_intraday = df_raw.copy()
df_intraday = df_intraday.reset_index()

# Generate the datetime of the last row data
df_intraday["last_datetime"] = df_intraday["datetime"].shift(1)
# Generate the time difference between the current row and the last row
df_intraday["datetime_diff_from_last"] = df_intraday["datetime"] - df_intraday["last_datetime"]

# Generate the datetime of the next row data
df_intraday["next_datetime"] = df_intraday["datetime"].shift(-1)
# Generate the time difference between the next row and the current row
df_intraday["datetime_diff_to_next"] = df_intraday["next_datetime"] - df_intraday["datetime"]

df_test = df_intraday["datetime_diff_from_last"].value_counts(normalize=True)
df_test = df_test.mul(100).round(3).astype(str) + "%"
print(df_test)

df_datetime_diff_count = df_intraday["datetime_diff_from_last"].value_counts()
df_test1 = df_datetime_diff_count.sort_index().reset_index()
df_test2
