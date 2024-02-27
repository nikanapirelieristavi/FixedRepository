#მომხმარებლის ნიშნებისგან გამოანგარიშება საშვალო არითმეტიკული და თუ ცხრაზე მეტი იქნება
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you

input_grades = int(input("tell me your first grade:"))
input_grades_1= int(input("tell me your second grade:"))
input_grades_2= int(input("tell me your third grade:"))
input_number = int(input("how many grades you got?"))
sash_arit = input_grades / input_number
if sash_arit > 9:
    print("gilocav moige tosteri samaslariani")
elif 5 > sash_arit < 9:
    print("you are MID")
else:
    0 > sash_arit > 10
    print("there is something wrong with you")


