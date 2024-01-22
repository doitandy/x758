import yfinance as yf

# 사용자로부터 특정 종목의 티커 입력받기
ticker_symbol = input("옵션 데이터를 조회하고 싶은 종목의 티커를 입력하세요: ")

# Yahoo Finance에서 주식 정보 가져오기
stock = yf.Ticker(ticker_symbol)

# 주식의 옵션 만료일 가져오기
options_expirations = stock.options

# 첫 번째 만료일에 대한 옵션 데이터 가져오기
if options_expirations:
    options_data = stock.option_chain(options_expirations[0])

    # 콜 옵션 데이터
    calls = options_data.calls
    total_call_volume = calls['volume'].sum()  # 콜 옵션 총 거래량

    # 풋 옵션 데이터
    puts = options_data.puts
    total_put_volume = puts['volume'].sum()  # 풋 옵션 총 거래량

    # 거래량 비교 및 결과 출력
    if total_call_volume > total_put_volume:
        print(f"콜 옵션의 거래량이 더 많습니다: 콜 {total_call_volume} 대 풋 {total_put_volume}")
    elif total_put_volume > total_call_volume:
        print(f"풋 옵션의 거래량이 더 많습니다: 풋 {total_put_volume} 대 콜 {total_call_volume}")
    else:
        print(f"콜과 풋 옵션의 거래량이 동일합니다: {total_call_volume}")
else:
    print("해당 종목에 대한 옵션 데이터가 없습니다.")

