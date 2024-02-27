# def abbrev_name(name):
#     words = name.split()
#     first_letter = words[0][0]
#     second_letter = words[1][0]
#     last = first_letter + '.' + second_letter
#     print(last)
# print(abbrev_name("Sandro Zabakhidze"))

# def find_needle(haystack):
#     for number in range(len(haystack)):
#         if haystack[number] == "needle":
#             return(number)
#         else:
#             return "there isn't a single needle in the haystack"
        
# print(find_needle("one, needle four, five, something"))

# def make_upper_case(s):
#     return s.upper()

# def sum_array(a):
#     x = a[0]
#     for num in a:
#         x+=1
#         if float in a:
#             float(num + x)
#         else:
#             num+x
#     print(num)

# es araswori iyo

# sum_array([1, 2, 3])

# def sum_array(a):
#     integer = 0
#     sum = 0
#     while integer <= len(a):
#         sum+=a[integer]
#         integer+=1

#esec araswori iyo;-;
def sum_array(a):
    return sum(a)
#30 wuti amaze vfiqrobdi

# def are_you_playing_banjo(name):
#     if "r" or "R" in range(len(name)):
#         print("yes")
#     else:
#         print("no")

def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        print("yes")
    else:
        print("no")

def invert(lst):
    for x in lst:
        return x * -1

