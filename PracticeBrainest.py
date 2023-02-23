from statistics import mean
list_numbers=[]
while True:
    number = input("Enter a number: ")
    if number == "done":
        avarage = mean(list_numbers)
        total = sum(list_numbers)
        size=len(list_numbers)
        break
    else:        
        try:
            number= int(number)
            list_numbers += number
        except:
            print("Bad data, put un number please: ")

print(total, size, avarage)


def pay(time, rate):
    if time<=40:
        pay = 40*rate
    else:
        pay = 40*rate + (time-40)*rate*1.5

    print(pay)




def computergrade(score):
    if score<0 or score>1:
        return "Your score is out of range"
    elif score >=0.9:
        return "A"
    elif score >=0.8:
        return "B"
    elif score >=0.7:
        return "C"
    elif score >=0.6:
        return "D"
    else:
        return "F"

score = input("Enter score: ")
try:
    score = float(score)
    print(computergrade(score))
except:
    print("Enter un number:")