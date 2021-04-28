import pyupbit
import numpy as np

# ohlcv(open, high, low, close, volume) 으로 당일 시가, 고가, 저가, 종가, 거래량 데이터
df = pyupbit.get_ohlcv("KRW-DOGE", count=30)

# 변동성 돌파 전략. 변동폭에서 k배만큼 상승 일어났을 때 매수
# 변동폭(고가-저가) * k값
k = 0.5
df['range'] = (df['high'] - df['low']) * k

# target (매수가)
# 변동값을 다음날 시가에 더해준다. (shift(1) - 한칸씩 밑으로 내림)
df['target'] = df['open'] + df['range'].shift(1)

# np.where (조건문, 참일때 값, 거짓일 때 값)
fee = 0.0005
# ror (수익률) = 목표치보다 높으면 매수 후 종가에 매도하니 종가/구매가 - 수수료 (대략적)
# 목표치보다 낮으면 매수 안하니 그대로 1
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

# hpr (누적 수익률) = 누적곱 계산
df['hpr'] = df['ror'].cumprod()

# draw down 계산 (누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# mdd = draw down 중 max 값
print("MDD(%): ", df['dd'].max())

df.to_excel("dd-doge.xlsx")