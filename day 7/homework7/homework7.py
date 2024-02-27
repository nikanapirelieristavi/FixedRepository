
# ბილეთი ღირს 25 ლარი,
# მაგრამ ბავშვებისთვის უფასოა,
# გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, 
# გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ
ticket = 25
adult=1
child=0
number1 = int(input("input the number of adults:"))
number2 = int(input("input the number of children:"))

print(ticket*adult*number1 + ticket*child*number2)
