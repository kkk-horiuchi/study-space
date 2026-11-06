import streamlit as st
import requests

st.title("AWSサービス解説アプリ")
st.write("サービス名を入力すると、解説が表示されるよ")

# APIのURLを格納
API_URL = "URLを入れる"

# 入力フォーム
service_name = st.text_input("サービス名を入力してね",placeholder="ここに入力")

# APIにリクエストを送る
params_data = {"message":service_name}
response = requests.get(API_URL,params=params_data)

# レスポンスの確認
if response.status_code == 200:
    # 成功時の処理（200は成功）
    explanation = response.text
    st.success("解説を取得したよ！")
    st.write(explanation)
else:
    # エラー時の処理
    st.error("エラー発生！")