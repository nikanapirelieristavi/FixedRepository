#family = ["tamuna", "saba", "mate"]
#full_sentence = "My moms name is: {}, My brothers name is: {}, My name is: {}".format(family[0],family[1],family[2])
#print(full_sentence)  დაემატოს ასაკები და დაიპრინტოს თითოეული რამდენი წლის 
#არის ერთ გრძელ წინადადებად ხოლო მეორე დაპრინტვაზე დაიპრინტოს რამდენი წლის გახდნენ 10 წელში

family = ["nika", "levani", "nino"]
age = [15, 45, 40]
full_sentence = "my mom's name is {}, she is {}, my dad's name is {}, he is {}, my name is {}, I am {} years old".format(family[2],age[2],family[1],age[1],family[0],age[0])
print(full_sentence)
age2 =[25, 55, 50]
full_sentence2 = "my mom's name is {}, she is {}, my dad's name is {}, he is {}, my name is {}, I am {} years old".format(family[2],age2[2],family[1],age2[1],family[0],age2[0])
print(full_sentence2)


x=[2, 4, 6, 2, 4, 7, 2, 9]
for i in range (2):
    x.remove(4)
print(x)