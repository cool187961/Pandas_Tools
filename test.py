import streamlit as st
import pandas as pd
import datetime

# 1. 網頁標題
st.set_page_config(page_title="自動化日期轉換工具", layout="centered")
st.title("🚀 我的自動化工具 (Beta)")

# 2. 檔案上傳功能
uploaded_file = st.file_uploader("請上傳 Excel 檔案", type=["xlsx", "xls"])

if uploaded_file:
    # 讀取資料
    df = pd.read_excel(uploaded_file)
    st.write("### 原始資料預覽", df.head())
    
    # 3. 操作按鈕
    if st.button("開始執行日期轉換"):
        with st.spinner('處理中...'):
            # 這裡放入你之前的邏輯 (範例)
            df['處理日期'] = pd.to_datetime(datetime.datetime.now()).strftime('%m%d')
            
            st.success("✅ 處理完成！")
            st.write("### 處理後結果", df.head())
            
            # 4. 提供下載按鈕
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="點我下載處理好的檔案",
                data=csv,
                file_name="processed_data.csv",
                mime="text/csv",
            )