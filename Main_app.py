import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_gsheets import GSheetsConnection
import numpy as np
import seaborn as sns

# เชื่อมต่อกับ Google Sheets
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# อ่านข้อมูลจาก Google Sheets
ext_data = conn.read(wroksheet="Sheet1", usecols=list(range(10)), ttl=5)

# ลบข้อมูล NaN ทั้งหมด
ext_data = ext_data.dropna(how="all")
st.dataframe(ext_data)

sns.countplot(x = ext_data["female", data = ext_data]
st.plot()
