# coding:utf-8

from __future__ import division

# 操作符
# 算术操作符：+,-,*,/,%,**
# 注意：除法
print 1 / 2
print float(2 / 3)
print 3 % 2
print 7 ** 4

# 位操作符:只适用于整型
# 取反(~)，按位与(&)，或(|)，异或(^)，左移(<<)，右移(>>)
print ~30
print 78 & -32
print 62 | 82
print 30 ^ 45
print 60 >> 2
print 38 << 3

# 内建函数: cmp(),str(),type()
# 功能内建函数：abs(),coerce(),divmod(),pow(),round()
print cmp(-6, 2)
print cmp(0xff, 255)
print str(632)
print type(0xff)

# 工厂函数：数值工厂函数 int(),float(),long(),complex(),bool()


# 布尔数：在数学运算中，布尔值的True和False分别对应于1和0

# 十进制浮点型：from decimal import Decimal
from decimal import Decimal
dec = Decimal(1.1)
print dec

# 模块:decimal,array,math,operator,random
# 核心模块：random
# |--|--|
# |randint()||
# |randrange()||
# |uniform()||
# |random()||
# |choice()||
