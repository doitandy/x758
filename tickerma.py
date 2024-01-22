import yfinance as yf
import pandas as pd

# 종목 티커 입력 받기
ticker_symbol = input("이동평균선을 확인하고 싶은 종목의 티커를 입력하세요: ")

# 데이터 다운로드 (최근 1년)
data = yf.download(ticker_symbol, period="1y")

# 이동평균선 계산
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_100'] = data['Close'].rolling(window=100).mean()

# 최근 이동평균선 값 출력
print(f"최근 20일 이동평균 가격: {data['SMA_20'].iloc[-1]}")
print(f"최근 50일 이동평균 가격: {data['SMA_50'].iloc[-1]}")
print(f"최근 100일 이동평균 가격: {data['SMA_100'].iloc[-1]}")

