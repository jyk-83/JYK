import pyupbit

access = "s74NnWCIjT2V9xKYHwC3rL0AewYvBmewWBYR6Mz5"          # 본인 값으로 변경
secret = "vw39Md09O3qMLMNFYezIuJnceerctTbcItqDXVby"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회