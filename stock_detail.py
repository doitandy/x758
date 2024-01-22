import yfinance as yf

# 사용자로부터 기업 티커 입력 받기
ticker_symbol = input("기업의 재무재표와 배당정보를 알기 원하는 기업의 티커를 입력하세요: ")

# 해당 티커로 Yahoo Finance 객체 생성
stock = yf.Ticker(ticker_symbol)

# 재무제표 출력
print("\nFinancials:")
print(stock.financials.to_string())

# 대차대조표 출력
print("\nBalance Sheet:")
print(stock.balance_sheet.to_string())

# 배당 정보 출력
print("\nDividends:")
print(stock.dividends.to_string())

