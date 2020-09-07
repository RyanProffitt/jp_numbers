# Convert English numebring system to Japanese numbering system
# doesn't accept float / decimal values
# Make each IF statement as is a function as I repeat code a lot
    # idea, check length of the int and then run some recursive function

# prototype function
def convert_to_kanji_number(i):
    kanji = "None"
    if i == 0:
        kanji = "〇"
    if i == 1:
        kanji = "一"
    if i == 2:
        kanji = "二"
    if i == 3:
        kanji = "三"
    if i == 4:
        kanji = "四"
    if i == 5:
        kanji = "五"
    if i == 6:
        kanji = "六"
    if i == 7:
        kanji = "七"
    if i == 8:
        kanji = "八"
    if i == 9:
        kanji = "九"
    # print("The function is returning: " + kanji)
    return(kanji)

# get user input and check that is numeric values
numeric_result = False
while numeric_result == False:
    val = input("Please input a number value: ")
    length = len(val)
    numeric_result = val.isnumeric()
    
int_val = int(val)

# testing for potential automation of the IF statements
print("Length: " + str(length))
text = ""
k = 0
while k < length:
    text = text + "0"
    k += 1
print(text)

# print the 万(10,000) amount
if int_val > 9999:
    rem = int_val // 10000 # get the 万(10,000) amount
    print(rem)
    print("万")
    rem2 = int_val % 10000 # get the remainder
    int_val = rem2

# print the 千(1,000) amount
if int_val > 999:
    rem = int_val // 1000 # get the 千(1,000) amount
    kanji_rem = convert_to_kanji_number(rem)
    print(kanji_rem)
    # print("千")
    rem2 = int_val % 1000
    int_val = rem2

# print the 百(100) amount
if int_val > 99:
    rem = int_val // 100 # get the 百(100) amount
    kanji_rem = convert_to_kanji_number(rem)
    print(kanji_rem)
    # print("百")
    rem2 = int_val % 100
    int_val = rem2

# print the 十(10) value
if int_val > 9:
    rem = int_val // 10
    kanji_rem = convert_to_kanji_number(rem)
    print(kanji_rem)
    rem2 = int_val % 10
    int_val = rem2

# print the 1 - 10 value in Kanji
if int_val >= 0:
    kanji_rem = convert_to_kanji_number(int_val)
    print(kanji_rem)