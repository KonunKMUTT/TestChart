import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_gsheets import GSheetsConnection
import numpy as np

# เชื่อมต่อกับ Google Sheets
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# อ่านข้อมูลจาก Google Sheets
ext_data = conn.read(wroksheet="Sheet1", usecols=list(range(10)), ttl=5)

# ลบข้อมูล NaN ทั้งหมด
ext_data = ext_data.dropna(how="all")

# แยกข้อมูล Class, Female และ Male
classes = ext_data["Class"]
females = ext_data["Female"]
males = ext_data["Male"]

# วาด Bar chart
plt.bar(classes, females, label="Female")
plt.bar(classes, males, bottom=females, label="Male")
plt.xlabel("Class")
plt.ylabel("จำนวน")
plt.legend()

# แสดง Bar chart บน Streamlit
st.pyplot(plt)
