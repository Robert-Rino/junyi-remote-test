# test1
# (A)

def reverse(string):
    result_list = []
    str_list = list(string)
    for i in range(len(str_list)):
        result_list.append(str_list[-(i+1)])
    return ''.join(result_list)





# test2
def mod3and5(num):
    multiple3 = num/3
    multiple5 = num/5
    multiple15 = num/15
    result = num - multiple3 - multiple5 + multiple15
    return result

# test 3

