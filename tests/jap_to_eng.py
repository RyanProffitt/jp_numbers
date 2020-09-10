# This module contains code to convert a number from japanese representation
# to western representation.

error_check = False

class JpVal():
    # single digit numbers
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
    
    #multiple digit numbers
    JUU = 10
    HYAKU = 100
    SEN = 1000
    MAN = 10000
    OKU = 100000000
    CHOU = 1000000000000
    KEI = 100000000000000000
    
class JpRep():
    # single digit numbers
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

    # multiple digit numbers
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

    # Check to confirm string has been input
    if type(jp_number) is not str:
        return(print("Please input a Kanji numerical values."))

    length = len(jp_number)

    # Basic conversions
    if length == 1:
        return(kanji_to_value(jp_number))

    # Complex conversions

    if length != 1:

        jp_str = ""

        multiple_counter = "1"

        # For loop is reversed for simplicity
        for i in reversed(range(length)):

            tmp_str = kanji_to_value(jp_number[i])
            tmp_str = str(tmp_str)

            # Check to confirm that str can be converted to int - else exit program
            try:
                int_tmp_str = int(tmp_str)
            except:
                return(print("You have input non-numeric Kanji."))

            # Check position of the digit

            first_digit = False
            last_digit = False

            if (i + 1) == len(jp_number):
                last_digit = True
            
            if i == 0:
                first_digit = True

            # Test digit and next digit if 0 - 9 Kanji or 10+ Kanji
            
            current_multi_digit = False
            current_single_digit = False
            next_multi_digit = False
            next_single_digit = False
            prev_multi_digit = False
            prev_single_digit = False

            
            # Current [i] digit check
            if len(tmp_str) > 1:
                current_multi_digit = True
            else:
                current_single_digit = True

            # Next value [i - 1] digit check
            if i != 0:
                next_tmp_str = kanji_to_value(jp_number[(i - 1)])
                next_tmp_str = str(next_tmp_str)
                if len(next_tmp_str) > 1:
                    next_multi_digit = True
                else:
                    next_single_digit = True
            
            # Previous value [i + 1] digit check
            if last_digit == False:
                prev_tmp_str = kanji_to_value(jp_number[(i + 1)])
                prev_tmp_str = str(prev_tmp_str)
                if len(prev_tmp_str) > 1:
                    prev_multi_digit = True
                else:
                    prev_single_digit = True

            # Check the current multiple counter - to track 0's required
            tmp_length = len(tmp_str)
            zero_counter = ""

            if tmp_length > len(multiple_counter):
                int_ = int(tmp_str) // (int(multiple_counter) * 10)
                zero_counter = str(int_)
                zero_counter = zero_counter[1:]
                multiple_counter = tmp_str

            # Start transforming the Japanese to English
            
            if current_multi_digit and next_multi_digit:
                tmp = "1"

            if current_multi_digit and next_single_digit:
                tmp = ""

            if current_multi_digit and next_single_digit and prev_multi_digit:
                a = kanji_to_value(jp_number[i])
                b = kanji_to_value(jp_number[(i + 1)])
                c = int(a / b)
                c = str(c)
                if len(c) > 1:
                    tmp = c[2:]

            if current_multi_digit and next_single_digit and prev_single_digit:
                tmp = zero_counter

            if current_single_digit:
                tmp = str(tmp_str)

            if first_digit and current_multi_digit:
                tmp = "1"

            if last_digit and current_multi_digit:
                if next_single_digit:
                    tmp = str(tmp_str)
                    tmp = tmp[1:]
                elif next_multi_digit:
                    tmp = str(tmp_str)

            # Add to the string
            jp_str = tmp + jp_str

    # Return the string as an integer value
    jp_str = int(jp_str)
    return(jp_str)

def main():
    
    # Input testing
    # kanji_number = input("Please input a japanese number: ")
    # kanji_number = jap_to_eng(kanji_number)
    # print(kanji_number)

    # Basic number tests
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

    # Complex number tests
    print("三十 == 30: {0}".format(30 == jap_to_eng("三十")))
    print("三百三 == 303: {0}".format(303 == jap_to_eng("三百三")))
    print("四百二十 == 420: {0}".format(420 == jap_to_eng("四百二十")))
    print("四百二十九 == 429: {0}".format(429 == jap_to_eng("四百二十九")))
    print("四千百二十九 == 4129 {0}".format(4129 == jap_to_eng("四千百二十九")))
    print("四万百二十九 == 40129 {0}".format(40129 == jap_to_eng("四万百二十九")))
    print("四億百二十九 == 400000129 {0}".format(400000129 == jap_to_eng("四億百二十九")))
    print("四億四百三 == 400000403 {0}".format(400000403 == jap_to_eng("四億四百三")))
    print("四億二万九千三百三十一 == 400029331 {0}".format(400029331 == jap_to_eng("四億二万九千三百三十一")))

    # Intentional errors
    print("Hello == Error")
    jap_to_eng("hello")
    print("四億e四3百三 == Error")
    jap_to_eng("四億e四3百三")
    print("2345 == Error")
    jap_to_eng("2345")

if __name__ == "__main__":
    main()