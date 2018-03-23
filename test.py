# test1
# (A)

def reverse(string):
    result_list = []
    str_list = list(string)
    for i in range(len(str_list)):
        result_list.append(str_list[-(i+1)])
    return ''.join(result_list)

# (B)

def reverse2(string):
    result_list = []
    str_list = string.split(' ')
    result_list = [reverse(string) for string in str_list]
    return ' '.join(result_list)



# test2
def mod3and5(num):
    multiple3 = num/3
    multiple5 = num/5
    multiple15 = num/15
    result = num - multiple3 - multiple5 + multiple15
    return result

# test3


# test4
# 優惠套餐+偷錢+找錢 = 原價
# 750 + 60 + 90 = 900
# 把找的錢扣掉後----------------
# 優惠套餐+偷錢 = 原價- 找錢
# 750 +60    = 900 -90   = 810
# 這時候如果想把左右式子還原 應該是要兩邊加回總共找的錢90而不是偷的錢，而這兩個金額差了30元所以等是會錯
