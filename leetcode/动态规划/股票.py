'''
一天结束时，可能有持股、可能未持股、可能卖出过1次、可能卖出过2次、也可能未卖出过

所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]

具体一天结束时的6种状态：

未持股，未卖出过股票：说明从未进行过买卖，利润为0
dp[i][0][0]=0
未持股，卖出过1次股票：可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
未持股，卖出过2次股票:可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
持股，未卖出过股票：可能是今天买的，也可能是之前买的（昨天也持股）
dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
持股，卖出过1次股票：可能是今天买的，也可能是之前买的（昨天也持股）
dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
持股，卖出过2次股票：最多交易2次，这种情况不存在
dp[i][1][2]=float('-inf')
'''

'''
最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
'''
def maxProfit1(self, prices) -> int:
    if not prices:
        return 0
    res = 0
    low = prices[0]
    for i in range(1,len(prices)):
        low = min(low,prices[i])
        res = max(prices[i] - low,res)
    return res


'''
可以尽可能地完成更多的交易（多次买卖一支股票）。
'''
def maxProfit2(self, prices) -> int:
    re = 0 
    for i in range(1,len(prices)):
        dif = prices[i] - prices[i-1]
        if dif > 0:
            re += dif
    return re

'''
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易

设定四个变量hold1,hold2,release1,release2
hold1代表当前持有第一支股票的最优解,hold2代表当前持有第二支股票的最优解,
release1代表当前刚卖完第一支股票的最优解,release2代表当前卖完第二支股票的最优解
'''
def maxProfit(self, prices) -> int:
    hold1,hold2 = (-2)**31,(-2)**31
    release1,release2 = 0,0
    for  i  in  range(len(prices)):
        release2 = max(release2,hold2+prices[i])
        #release2的最大值为当前状态与先前持有股票并卖掉的最大值
        hold2 = max(hold2,release1-prices[i])
        #hold2的最大值为当前状态与先前交易过依次并买入股票的最大值
        release1 = max(release1,hold1+prices[i])
        #release1的最大值为当前状态与先前持有股票并卖掉的最大值
        hold1 = max(hold1,(-1)*prices[i])
        #hold1的最大值为当前状态与先前未持有股票直接买入的最大值
    return  max(release1,release2)

