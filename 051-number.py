# coding:utf-8

# 注意：Python中一切都是对象
# 创建数字对象
anInt = 1
aLong = -999999999999999999L
aFloat = 3.142567273837287372632763726723837837
aComplex = 1.23 + 4.56j

# 更新对象
anInt += 1
aFloat = 2.34747387483

# 删除对象
del anInt
del aLong

# print anInt  # 已删除
# print aLong  # 已删除
print aFloat  # 已更新
print aComplex
# -------------------------------------------------

# 整型包括：布尔型，标准整形，长整形
# 整型支持：八进制(以“0”开头)，十进制，十六进制(以“0x”开头)
ai = 0101010
bi = 673
ci = 0x8
di = 74327823L

# 浮点型：Python中的浮点型全部都是双精度浮点型，可以使用十进制或科学计数法来表示。
af = 0.0
bf = -777.
cf = 3.893
ef = 67e3
ff = float(34)

# 复数：复数由实数部和虚数部构成，虚数单位为j
# 表示为：real+imagej
# 实数部和虚数部都是浮点数
ac = 783.3+821.32j
bc = 326.32-73.32j
cc = -56.23-635.3j
dc = -.004+0j
# 复数的内建属性：real,image,conjugate 共轭复数
ec = -8.333-2.99j
print ec.real
print ec.imag
print ec.conjugate()  # 返回共轭复数
# -------------------------------------------------

# 类型转换
# 整型转换为浮点型，非复数型转换为复数型
achange = 3627
bchange = float(achange)
cchange = 28
dchange = complex(28)
print bchange, type(bchange)  # <type 'float'>
print dchange, type(dchange)  # <type 'complex'>



