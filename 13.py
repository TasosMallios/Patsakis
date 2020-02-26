def luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checkDigits = 0
    checkDigits += sum(odd_digits)
    for d in even_digits:
        checkDigits += sum(digits_of(d*2))
    if checkDigits%10 == 0:
        if int(str(n)[:1]) == 4:
            print ("\nCard Type: Visa")
            print ("valid credit card.")
        elif int(str(n)[:2]) == 51 or int(str(n)[:2]) == 52 or int(str(n)[:2]) == 53 or int(str(n)[:2]) == 54 or int(str(n)[:2]) == 55:
            print ("\nCard Type: MasterCard")
            print ("valid credit card.")
        elif int(str(n)[:4]) == 6011 or int(str(n)[:6]) == 622126 or int(str(n)[:6]) == 622127 or int(str(n)[:6]) == 622128 or int(str(n)[:6]) == 622129 or int(str(n)[:5]) == 62213 or int(str(n)[:5]) == 62214 or int(str(n)[:5]) == 62215 or int(str(n)[:5]) == 62216 or int(str(n)[:5]) == 62217 or  int(str(n)[:5]) == 62218 or int(str(n)[:5]) == 62219 or int(str(n)[:4]) == 6222 or int(str(n)[:4]) == 6223 or int(str(n)[:4]) == 6224 or int(str(n)[:4]) == 6225 or int(str(n)[:4]) == 6226 or int(str(n)[:4]) == 6227 or int(str(n)[:4]) == 6228 or int(str(n)[:5]) == 62290 or int(str(n)[:5]) == 62291 or int(str(n)[:6]) == 622920 or int(str(n)[:6]) == 622921 or int(str(n)[:6]) == 622922 or int(str(n)[:6]) == 622923 or int(str(n)[:6]) == 622924 or int(str(n)[:6]) == 622925 or int(str(n)[:3]) == 644 or int(str(n)[:3]) == 645 or int(str(n)[:3]) == 646 or int(str(n)[:3]) == 647 or int(str(n)[:3]) == 648 or int(str(n)[:3]) == 649 or int(str(n)[:2]) == 65: 
            print ("\nCard Type: Discover")
            print ("valid credit card.")
        else:
            print("\nunrecognized valid credit card.")
    else:
        print("\ninvalid credit card number.")
    checkDigits = checkDigits % 10
    return checkDigits

while True:
    n = input("Incert Credit Card Number:")
    if len(n) != 16:
        print ("Your input is a non 16 digits number.")
    else:
        luhn(n)
    break
