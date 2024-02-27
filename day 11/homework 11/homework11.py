
# შექმენით ფუნქცია რომელსაც გადაეცემა 3 პარამეტრი(სამკუთხედის გვერდები) 
# და დაპრინტავს "ასეთი სამკუთხედი იარსებებს", 
# ან დაპრინტავს "ასეთი სამკუთხედი ვერ იარსებებს" )

def triangle (first,second,third):
    if first or second or third > 0:
        print("this triangle is valid!")
    else:
        print("this triangle does not exist!")

triangle(4, 5, 6)
    
