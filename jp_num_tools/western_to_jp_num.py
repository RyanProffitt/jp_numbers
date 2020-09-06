#This module contains code to convert a number from western representation
# to japanese representation.

from enum import Enum

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

#This function accepts a number in western representation
# and converts it to Kanji Japanese representation.
#Parameters
#    number - the number as an integer or string
#Returns
#    
def to_jp_num(number):
    #gets the number type
    num_type = type(number)
    
    if num_type is str:
        number = number.remove(",")
        if not number.isalnum():
            raise ValueError("The string passed to this function is not a number.")
        number = number.lstrip("0")
        number_len = len(number)
        
        int_number = int(number)
    elif num_type is int:
        int_number = number
    else:
        raise ValueError("Input must be string or integer!")
    
    #Basic Number Conversions
    if int_number == 0:
        return "" #need a better way to handle maru
    if int_number == 1:
        return JpRep.ICHI
    if int_number == 2:
        return JpRep.NI
    if int_number == 3:
        return JpRep.SAN
    if int_number == 4:
        return JpRep.SHI
    if int_number == 5:
        return JpRep.GO
    if int_number == 6:
        return JpRep.ROKU
    if int_number == 7:
        return JpRep.SHICHI
    if int_number == 8:
        return JpRep.HACHI
    if int_number == 9:
        return JpRep.KYUU
    if int_number == 10:
        return JpRep.JUU
    
    #Complex conversions
    jp_str = ""
    
    #Handle KEIs
    tmp = int_number // JpVal.KEI
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.KEI
    elif tmp == 1:
        jp_str = jp_str + JpRep.KEI
    int_number = int_number - (tmp * JpVal.KEI)
    
    #Handle CHOUs
    tmp = int_number // JpVal.CHOU
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.CHOU
    elif tmp == 1:
        jp_str = jp_str + JpRep.CHOU
    int_number = int_number - (tmp * JpVal.CHOU)
    
    #Handle OKUs
    tmp = int_number // JpVal.OKU
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.OKU
    elif tmp == 1:
        jp_str = jp_str + JpRep.OKU
    int_number = int_number - (tmp * JpVal.OKU)
    
    #Handle 10000s
    tmp = int_number // JpVal.MAN
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.MAN
    elif tmp == 1:
        jp_str = jp_str + JpRep.MAN
    int_number = int_number - (tmp * JpVal.MAN)
    
    #Handle 1000s
    tmp = int_number // JpVal.SEN
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.SEN
    elif tmp == 1:
        jp_str = jp_str + JpRep.SEN
    int_number = int_number - (tmp * JpVal.SEN)
    
    #Handle 100s
    tmp = int_number // JpVal.HYAKU
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.HYAKU
    elif tmp == 1:
        jp_str = jp_str + JpRep.HYAKU
    int_number = int_number - (tmp * JpVal.HYAKU)
    
    #Handle 10s
    tmp = int_number // JpVal.JUU
    if tmp > 1:
        jp_str = jp_str + to_jp_num(tmp) + JpRep.JUU
    elif tmp == 1:
        jp_str = jp_str + JpRep.JUU
    
    tmp = int_number % 10
    jp_str = jp_str + to_jp_num(tmp)
    
    print(jp_str)
    
    return jp_str

def main():
    #Basic Number Tests
    print("1 == 一: {0}".format("一" == to_jp_num(1)))
    print("2 == 二: {0}".format("二" == to_jp_num(2)))
    print("3 == 三: {0}".format("三" == to_jp_num(3)))
    print("4 == 四: {0}".format("四" == to_jp_num(4)))
    print("5 == 五: {0}".format("五" == to_jp_num(5)))
    print("6 == 六: {0}".format("六" == to_jp_num(6)))
    print("7 == 七: {0}".format("七" == to_jp_num(7)))
    print("8 == 八: {0}".format("八" == to_jp_num(8)))
    print("9 == 九: {0}".format("九" == to_jp_num(9)))
    print("10 == 十: {0}".format("十" == to_jp_num(10)))
    
    #Complex Number Tests
    print("14 == 十四: {0}".format("十四" == to_jp_num(14)))
    print("19 == 十九: {0}".format("十九" == to_jp_num(19)))
    print("21 == 二十一: {0}".format("二十一" == to_jp_num(21)))
    print("27 == 二十七: {0}".format("二十七" == to_jp_num(27)))
    print("55 == 五十五: {0}".format("五十五" == to_jp_num(55)))
    print("80 == 八十: {0}".format("八十" == to_jp_num(80)))
    print("99 == 九十九: {0}".format("九十九" == to_jp_num(99)))
    
    print("100 == 百: {0}".format("百" == to_jp_num(100)))
    print("900 == 九百: {0}".format("九百" == to_jp_num(900)))
    print("1000 == 千: {0}".format("千" == to_jp_num(1000)))
    print("2222 == 二千二百二十二: {0}".format("二千二百二十二" == to_jp_num(2222)))
    print("22222 == 二万二千二百二十二: {0}".format("二万二千二百二十二" == to_jp_num(22222)))
    print("222222222 == 二億二千二百二十二万二千二百二十二: {0}"
          .format("二億二千二百二十二万二千二百二十二" == to_jp_num(222222222)))
    print("2222222222222 == 二兆二千二百二十二億二千二百二十二万二千二百二十二: {0}"
          .format("二兆二千二百二十二億二千二百二十二万二千二百二十二" == to_jp_num(2222222222222)))
    print("22222222222222222 == 二京二千二百二十二兆二千二百二十二億二千二百二十二万二千二百二十二: {0}"
          .format("二京二千二百二十二兆二千二百二十二億二千二百二十二万二千二百二十二" == to_jp_num(22222222222222222)))
    
    #Tests designed to break the function
    try:
        to_jp_num(1.23)
        print("Passing a float fails: False")
    except:
        print("Passing a float fails: True")
    
    #outlier tests
    #print("0 == ◯: {0}".format("◯" == to_jp_num(0)))
    
    print("Done Testing!")
    
if __name__ == "__main__":
    main()
