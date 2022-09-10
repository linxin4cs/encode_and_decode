import utils.base_converter as bc
import utils.str_handler as sh

BASE64_TABLE_NUM = {
    "0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", "7": "H", "8": "I", "9": "J", "10": "K", "11": "L", "12": "M", "13": "N", "14": "O", "15": "P", "16": "Q", "17": "R", "18": "S", "19": "T", "20": "U", "21": "V", "22": "W", "23": "X", "24": "Y", "25": "Z",
    "26": "a", "27": "b", "28": "c", "29": "d", "30": "e", "31": "f", "32": "g", "33": "h", "34": "i", "35": "j", "36": "k", "37": "l", "38": "m", "39": "n", "40": "o", "41": "p", "42": "q", "43": "r", "44": "s", "45": "t", "46":
    "u", "47": "v", "48": "w", "49": "x", "50": "y", "51": "z",
    "52": "0", "53": "1", "54": "2", "55": "3", "56": "4", "57": "5", "58": "6", "59": "7", "60": "8", "61": "9",
    "62": "+", "63": "/",
}
BASE64_TABLE_STR = {
    "A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": "6", "H": "7", "I": "8", "J": "9", "K": "10", "L": "11", "M": "12", "N": "13", "O": "14", "P": "15", "Q": "16", "R": "17", "S": "18", "T": "19", "U": "20", "V": "21", "W": "22", "X": "23", "Y": "24", "Z": "25",
    "a": "26", "b": "27", "c": "28", "d": "29", "e": "30", "f": "31", "g": "32", "h": "33", "i": "34", "j": "35", "k": "36", "l": "37", "m": "38", "n": "39", "o": "40", "p": "41", "q": "42", "r": "43", "s": "44", "t": "45", "u": "46", "v": "47", "w": "48", "x": "49", "y": "50", "z": "51",
    "0": "52", "1": "53", "2": "54", "3": "55", "4": "56", "5": "57", "6": "58", "7": "59", "8": "60", "9": "61",
    "+": "62", "/": "63",
}


def encode(str_origin):
    """
    BASE64编码，将字符串进行 BASE64 编码

    Args:
        str_origin (str_origin): 源字符串

    Returns:
        str_origin: 编码后的 BASE64 字符串
    """

    bytes_origin = []
    bytes_res = []
    bits_origin = []
    bits_res = []
    str_origin_res = ""

    # 分组，3 个字节为一组
    for i in range(0, len(str_origin), 3):
        bytes_origin.append(sh.split_without_separator(str_origin[i: i + 3]))

    # 将 3 个字节为一组转换为每组 24 个 bit
    for i in range(len(bytes_origin)):
        item = ""

        for j in range(0, len(bytes_origin[i])):
            item += bc.to_others(ord(bytes_origin[i][j]))

        bits_origin.append(item)

    # 将 24 个 bit 转换为 32 个 bit
    for i in range(len(bits_origin)):
        for j in range(0, len(bits_origin[i]), 6):
            base_str_origin = bits_origin[i][j: j + 6]
            if(len(base_str_origin) < 6):
                bits_res.append(
                    "00" + bits_origin[i][j: j + 6] + "0" * (6 - len(base_str_origin)))
            else:
                bits_res.append("00" + bits_origin[i][j: j + 6])

    # 将 bit 转换为字节
    for i in range(len(bits_res)):
        bytes_res.append(str(bc.to_decimal(bits_res[i])))

    # 将字节转换为 BASE64 码表对应的字符
    for i in range(len(bytes_res)):
        str_origin_res += BASE64_TABLE_NUM.get(bytes_res[i])

    # 判断是否缺填充符
    str_origin_res += "=" * (3 - len(bytes_origin[-1]))
    return str_origin_res


def decode(str_origin):
    """
    BASE64 解码，将 BASE64 码转换为原字符串

    Args:
        str_origin (str): BASE64 码

    Returns:
        str: 解码后的字符串
    """

    str_origin = str_origin.replace("=", "")
    bytes_origin = []
    bytes_res = []
    bits_origin = []
    bits_res = []
    str_res = ""

    # 转换为字节
    for i in range(len(str_origin)):
        bytes_origin.append(BASE64_TABLE_STR.get(str_origin[i]))

    # 转换为 bit
    for i in range(len(bytes_origin)):
        bits_origin.append(bc.to_others(bytes_origin[i]))

    # 转换为结果 bit
    for i in range(0, len(bits_origin), 4):
        item = bits_origin[i: i + 4]
        for j in range(len(item)):
            item[j] = item[j][2:]

        bits_res.append("".join(item))

    # 转换为结果字节
    for i in range(len(bits_res)):
        for j in range(0, len(bits_res[i]), 8):
            bytes_res.append(bits_res[i][j: j + 8])

        if(i == len(bits_res) - 1 and len(bytes_res[-1]) < 8):
            bytes_res.pop(-1)

    for i in range(len(bytes_res)):
        bytes_res[i] = bc.to_decimal(bytes_res[i])

    # 转换为字符串
    for i in range(len(bytes_res)):
        str_res += chr(bytes_res[i])

    return str_res
