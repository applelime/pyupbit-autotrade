import pyupbit

# 지원하는 암호화폐 목록
# print(pyupbit.get_tickers())

# fiat(특정 시장)에 가능한 목록만 받아오기
# print(pyupbit.get_tickers(fiat="KRW"))

# 최근 체결 가격 - 리턴 float
# print(pyupbit.get_current_price("KRW-BTC"))
# 여러 종목 검색 - 리턴 dictionary
# print(pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"]))

# 차트 데이터
# df = pyupbit.get_ohlcv("KRW-BTC")
# print(df.tail())
# print(len(df))

# 최근 영업일부터 이전 count일까지 (설정 안하면 디폴트 200)
# df = pyupbit.get_ohlcv("KRW-BTC", count=5)
# print(len(df))

# 조회단위
# print(pyupbit.get_ohlcv("KRW-BTC", interval="day"))             # 일봉 데이터 (5일)
# print(pyupbit.get_ohlcv("KRW-BTC", interval="minute1"))         # 분봉 데이터
# print(pyupbit.get_ohlcv("KRW-BTC", interval="week"))            # 주봉 데이터


# 로그인
access = "1"          # 본인 값으로 변경
secret = "2"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# 잔고조회
print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

# 매도
# print(upbit.sell_limit_order("KRW-XRP", 600, 20))

# 매수
# print(upbit.buy_limit_order("KRW-XRP", 613, 10))

# 시장가 매도/매수 (수수료 포함금액. 10000이면 실제로는 9995)
# print(upbit.buy_market_order("KRW-XRP", 10000)) 
# print(upbit.sell_market_order("KRW-XRP", 10000))
# print(upbit.buy_market_order("KRW-BTC", 10000)) # 실제로 사보니 10000원만 사지고, 수수료 5원으 지갑에서 따로 빠진다.

# 미체결 주문 조회
# upbit.get_order("KRW-LTC")

# 매수/매도 주문 취소 - 위의 리턴값중 uuid로 취소
# print(upbit.cancel_order('50e184b3-9b4f-4bb0-9c03-30318e3ff10a'))