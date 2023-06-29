import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# レイアウトを設定
st.title('Dynamic Graph Example')

# サイドバーに範囲指定スライダーを追加
range_slider = st.sidebar.slider(
    'Select a range', 
    0.0, 
    100.0, 
    (25.0, 75.0)
)

# 上記で選択した範囲でランダムなデータを生成
data = np.random.uniform(range_slider[0], range_slider[1], (100, 2))

# DataFrameに変換
df = pd.DataFrame(data, columns=['x', 'y'])

# グラフをプロット
st.pyplot(df.plot.scatter('x', 'y'))
