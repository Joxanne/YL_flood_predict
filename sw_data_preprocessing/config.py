import os

# Base paths
# Assumes structure:
# root/
#   sw_data_preprocessing/ (scripts)
#   inputs/
#   sw_data_all/ (output)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR) # parent of sw_data_preprocessing

INPUTS_DIR = os.path.join(PROJECT_ROOT, 'inputs')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'sw_data_all')

# Raw Flood Data Path - User should configure this if it changes
RAW_FLOOD_DIR = os.path.join(INPUTS_DIR, 'raw_flood_data')

# Rain Data Inputs
RAIN_EXCEL_PATH = os.path.join(INPUTS_DIR, 'typhoon_hourly_rain_up_to_2023_OK.xlsx')
STATIONS_CSV_PATH = os.path.join(INPUTS_DIR, 'CWA_rain_targets_20251126_2323.csv')

# Mapping from Raw Flood Source Folder ID to Target ID (tX)
FLOOD_FOLDER_MAPPING = {
    '20': 't3', '21': 't4', '22': 't5', '23': 't6', '24': 't7',
    '25': 't8', '26': 't9', '27': 't10', '28': 't11', '29': 't12',
    '30': 't13', '31': 't1', '32': 't2'
}

# Mapping from Target ID (tX) to Typhoon Name (must match Excel Sheet Name mostly)
ID_TO_NAME_MAPPING = {
    't1': '2001_桃芝',
    't2': '2004_敏督利',
    't3': '2005_海棠',
    't4': '2008_辛樂克',
    't5': '2009_莫拉克',
    't6': '2012_蘇拉',
    't7': '2013_蘇力',
    't8': '2015_蘇迪勒',
    't9': '2016_梅姬',
    't10': '2017_尼莎',
    't11': '2017_海棠',
    't12': '2021_盧碧',
    't13': '2023_杜蘇芮'
}

# Reverse mapping for Rain processing (Name -> tX)
NAME_TO_ID_MAPPING = {v: k for k, v in ID_TO_NAME_MAPPING.items()}
