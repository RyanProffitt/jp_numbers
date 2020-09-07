# This module contains code to convert a number from japanese representation
# to western representation.

error_check = False

class JpVal():
    MARU = 0
    ICHI = 1
    NI = 2
    SAN = 3
    YON = 4
    SHI = 4
    GO = 5
    ROKU = 6
    NANA = 7
    SHICHI = 7
    HACHI = 8
    KYUU = 9
    JUU = 10
    
    HYAKU = 100
    SEN = 1000
    MAN = 10000
    OKU = 100000000
    CHOU = 1000000000000
    KEI = 100000000000000000
    
class JpRep():
    MARU = "◯"
    ICHI = "一"
    NI = "二"
    SAN = "三"
    YON = "四"
    SHI = "四"
    GO = "五"
    ROKU = "六"
    NANA = "七"
    SHICHI = "七"
    HACHI = "八"
    KYUU = "九"
    JUU = "十"
    
    HYAKU = "百"
    SEN = "千"
    MAN = "万"
    OKU = "億"
    CHOU = "兆"
    KEI = "京"

# convert a kanji character to a single digit
def kanji_to_value(jp_number):

    if jp_number == JpRep.MARU:
        basic_number = JpVal.MARU
        return(basic_number)
    if jp_number == JpRep.ICHI:
        basic_number = JpVal.ICHI
        return(basic_number)
    if jp_number == JpRep.NI:
        basic_number = JpVal.NI
        return(basic_number)
    if jp_number == JpRep.SAN:
        basic_number = JpVal.SAN
        return(basic_number)
    if jp_number == JpRep.SHI:
        basic_number = JpVal.SHI
        return(basic_number)
    if jp_number == JpRep.GO:
        basic_number = JpVal.GO
        return(basic_number)
    if jp_number == JpRep.ROKU:
        basic_number = JpVal.ROKU
        return(basic_number)
    if jp_number == JpRep.SHICHI:
        basic_number = JpVal.SHICHI
        return(basic_number)
    if jp_number == JpRep.HACHI:
        basic_number = JpVal.HACHI
        return(basic_number)
    if jp_number == JpRep.KYUU:
        basic_number = JpVal.KYUU
        return(basic_number)
    if jp_number == JpRep.JUU:
        basic_number = JpVal.JUU
        return(basic_number)
    if jp_number == JpRep.HYAKU:
        basic_number = JpVal.HYAKU
        return(basic_number)
    if jp_number == JpRep.SEN:
        basic_number = JpVal.SEN
        return(basic_number)
    if jp_number == JpRep.MAN:
        basic_number = JpVal.MAN
        return(basic_number)
    if jp_number == JpRep.OKU:
        basic_number = JpVal.OKU
        return(basic_number)
    if jp_number == JpRep.CHOU:
        basic_number = JpVal.CHOU
        return(basic_number)
    if jp_number == JpRep.KEI:
        basic_number = JpVal.KEI
        return(basic_number)

def jap_to_eng(jp_number):

    # My error checking wasn't working... get to later
    # prevent anything except kanji characters as accepted in JpRep

    length = len(jp_number)
    
    # Basic conversions
    if length == 1:
        return(kanji_to_value(jp_number))

    # Complex conversions
    elif length > 1:
        jp_str = ""
        first_value = False
        last_value = False
        
        for i in range(length):

            if i == 0:
                first_value = True
            else:
                first_value = False

            if i == (length - 1):
                last_value = True

            tmp = kanji_to_value(jp_number[i])
            tmp = str(tmp)

            # if first value, we still want the first digit value
            if len(tmp) > 1 and first_value:
                tmp = tmp[i]
                first_value == False
            # if final value, don't want to modify
            elif len(tmp) > 1 and last_value:
                # need to remove the first value of the number
                tmp = tmp[1:]
                last_value == False
            # if neither, we do not need the value
            elif len(tmp) > 1:
                tmp = ""

            jp_str = jp_str + tmp

        int_val = int(jp_str)
        return(int_val)


def main():
    
    # input testing
    # kanji_number = input("Please input a japanese number: ")
    # kanji_number = jap_to_eng(kanji_number)
    # print(kanji_number)

    # basic number tests
    print("◯  == 0: {0}".format(0 == jap_to_eng("◯")))
    print("一 == 1: {0}".format(1 == jap_to_eng("一")))
    print("二 == 2: {0}".format(2 == jap_to_eng("二")))
    print("三 == 3: {0}".format(3 == jap_to_eng("三")))
    print("四 == 4: {0}".format(4 == jap_to_eng("四")))
    print("五 == 5: {0}".format(5 == jap_to_eng("五")))
    print("六 == 6: {0}".format(6 == jap_to_eng("六")))
    print("七 == 7: {0}".format(7 == jap_to_eng("七")))
    print("八 == 8: {0}".format(8 == jap_to_eng("八")))
    print("九 == 9: {0}".format(9 == jap_to_eng("九")))
    print("十 == 10: {0}".format(10 == jap_to_eng("十")))
    print("百 == 100: {0}".format(100 == jap_to_eng("百")))
    print("千 == 1000: {0}".format(1000 == jap_to_eng("千")))
    print("万 == 10000: {0}".format(10000 == jap_to_eng("万")))
    print("億 == 100000000: {0}".format(100000000 == jap_to_eng("億")))
    print("兆 == 1000000000000: {0}".format(1000000000000 == jap_to_eng("兆")))
    print("京 == 100000000000000000: {0}".format(100000000000000000 == jap_to_eng("京")))

    # complex number tests
    print("三十 == 30: {0}".format(30 == jap_to_eng("三十")))
    print("四百二十 == 420: {0}".format(420 == jap_to_eng("四百二十")))
    print("四百二十九 == 429: {0}".format(429 == jap_to_eng("四百二十九")))

if __name__ == "__main__":
    main()