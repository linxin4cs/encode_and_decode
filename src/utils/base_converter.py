import math


def to_decimal(str, origin_base=2):
    """_summary_

    Args:
        str (str): 源字符串
        origin_base (int, optional): 源进制，默认为 2

    Returns:
        int: 十进制结果
    """

    res = 0
    str_len = len(str)

    # 循环判 0
    for i in range(str_len):
        if(str[i] != "0"):
            # 判断当前位是否位最后一位
            if(i == str_len - 1):
                res += int(str[i])
            else:
                res += math.pow(origin_base, str_len - i - 1)

    return int(res)


def to_others(number, target_base=2, bits_len=8):
    """
    将十进制转换为其他进制

    Args:
        number (int): 源十进制数
        target_base (int, optional): 结果进制，默认为 2
        bits_len (int, optional): 结果进制 bit 位数，默认为 8

    Returns:
        str: 结果字符串
    """

    number = int(number)
    # 二进制基础字符串 00000000
    bits_res = "0" * bits_len

    # 判断是否将所有数值转换为二进制
    while(number > 0):
        i = 0

        # 找到一个数，使得它的平方大于或等于源十进制
        while(math.pow(target_base, i) < number):
            i += 1

        # 判断结果二进制长度是否超出基础长度
        val = math.pow(target_base, i)
        if((i == bits_len and val == number) or i > bits_len):
            bits_len += 8
            bits_res = "0" * 8 + bits_res

        # 字符切片，将对应位置更新为 i 的相关数
        if(val == number):
            if(i != 0):
                bits_res = bits_res[:-(i + 1)] + "1" + bits_res[-i:]
            else:
                bits_res = bits_res[:-1] + "1"
            number -= val

        elif(val > number):
            bits_res = bits_res[:-i] + "1" + bits_res[-(i - 1):]
            number -= val / 2

    return bits_res
