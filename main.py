# First question
score = input("Type score between 0.0 and 1.0 : ")

try:
    score = float(score)
    if score < 0 or score > 1:
        print("Tup a value between 0.0 and 1.0 only")
    else:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
except:
    print("Wrong values. Put only numbers")






