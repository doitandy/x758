import yfinance as yf

# 사용자 입력 받기
ticker_symbol = input("통계 정보를 알고 싶은 종목 티커를 입력하세요: ")

# Yahoo Finance에서 주식 정보 가져오기
stock = yf.Ticker(ticker_symbol)

# 주식 정보 출력
for key, value in stock.info.items():
    print(f"{key}: {value}")

