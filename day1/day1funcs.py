nums_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def numstr_to_num(numstr:str):
    for index in range(len(nums_str)):
        if nums_str[index] == numstr:
            return nums_num[index]

def find_number(text:str):
    firstnum = None
    lastnum = None
    for index in range(len(text)):
        if text[index] in nums_num:
            if firstnum == None:
                firstnum = text[index]
            lastnum = text[index]
        for num in nums_str:
            if text[index:index+len(num)] == num:
                if firstnum == None:
                    firstnum = numstr_to_num(num)
                lastnum = numstr_to_num(num)
    
    return int(firstnum + lastnum)
