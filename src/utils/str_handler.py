def split_without_separator(str):
    """
    将字符串分割而不使用分隔符参数，如 has => [h, a, s]

    Args:
        str (str): 源字符串

    Returns:
        list: 分割得到的数组
    """

    res = []
    for i in range(len(str)):
        res.append(str[i])

    return res
