import yfinance as yf
from datetime import datetime, timedelta

def get_last_weekday(date):
    # 주말일 경우 금요일로 조정
    while date.weekday() > 4:  # 주말 (5: 토요일, 6: 일요일)
        date -= timedelta(1)
    return date

# 주식 티커 입력 받기
ticker_symbol = input("가격을 조회하고 싶은 주식의 티커를 입력하세요: ")

# 해당 티커의 주식 정보 가져오기
stock = yf.Ticker(ticker_symbol)

# 현재 주식 가격 가져오기
current_price = stock.info.get('regularMarketPrice', None)

# 오늘 날짜와 어제 날짜 계산
today = datetime.now()
yesterday = get_last_weekday(today - timedelta(1))

# 어제(또는 최근 거래일)의 종가 데이터 가져오기
history = stock.history(start=yesterday.strftime('%Y-%m-%d'), end=yesterday.strftime('%Y-%m-%d'))
yesterday_close = history['Close'].iloc[0] if not history.empty else "정보 없음"

# 결과 출력
if today.weekday() > 4:  # 주말일 경우
    print(f"주말입니다. {ticker_symbol}의 가장 최근 종가는 {yesterday_close}입니다.")
else:  # 평일일 경우
    print(f"현재 {ticker_symbol}의 가격은 {current_price}입니다.")
    print(f"전날 {ticker_symbol}의 종가는 {yesterday_close}입니다.")

