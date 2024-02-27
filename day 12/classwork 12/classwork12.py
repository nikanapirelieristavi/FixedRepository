#შექმენით ფუნქცია რომელსაც ექნება ორი პარამეტრი 
#1) სახელი 
#2) ასაკი
#ფუნქცია უნდა პრინტავდეს წინადადებას სახელისა და ასაკის გამოყენებით,
#გამოიძახეთ ეს ფუნქცია ოჯახის ყველა წევრისთვის.
people = "nika, levani, nino"
def age_name(name,age,):
   name1 = print(input("input your name: "))
   name2 = print(input("input your name: "))
   name3 = print(input("input your name: "))
   
   age1 = print(int(input()))
   age2 = print(int(input()))
   age3 = print(int(input()))
   names = [name1, name2, name3]
   names.insert(1, age1, 2, age2, 3, age3)
   
    
    
        
age_name(15,"nika")
age_name(45, "levani")
age_name(40, "nino")