'''
两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
如果同一位的数字相同则为 0，不同则为 1

任何数和本身异或则为 0

任何数和 0 异或是 本身

异或满足交换律。 即 a ^ b ^ c ，等价于 a ^ c ^ b

'''

# 除了一个数字出现一次，其他都出现了两次
def singleNumber(self, nums):
    single_number = 0
    for num in nums:
        single_number ^= num
    return single_number

# 除了一个数字出现一次，其他都出现了三次
def singleNumber2(self, nums):
    res = 0
    for i in range(32):
        cnt = 0  # 记录当前 bit 有多少个1
        bit = 1 << i  # 记录当前要操作的 bit
        for num in nums:
            if num & bit != 0:
                cnt += 1
        if cnt % 3 != 0:
            # 不等于0说明唯一出现的数字在这个 bit 上是1
            res |= bit

    return res - 2 ** 32 if res > 2 ** 31 - 1 else res

# 除了两个数字出现一次，其他都出现了两次
'''
将这两个不同的数字分成两组 A 和 B; 每一组的数据进行异或
1.两个独特的的数字分成不同组
2.相同的数字分成相同组
'''
def singleNumbers(self, nums):
    ret = 0  # 所有数字异或的结果
    a = 0
    b = 0
    for n in nums:
        ret ^= n
    # 找到第一位不是0的
    h = 1
    while(ret & h == 0):
        h <<= 1
    for n in nums:
        # 根据该位是否为0将其分为两组
        if (h & n == 0):
            a ^= n
        else:
            b ^= n

    return [a, b]

