def Payment(n):
    d = {}
    x = {}
    result = 0
    key = "Tax"

    value = int(input("\nWhats the tax of the products?(without the percent symbol):\n"))

    x[key] = value 

    for i in range(n):
        print("\nWhats the name of the product", i+1, "?") 
        keys = input()
        values = int(input("\nWhat did it cost?(without the Euro symbol):\n"))
        d[keys] = values
        d.update(x)
        result = sum(d.values()) - d["Tax"]
        tax = (result*d["Tax"])/100
        result = result+tax
    print("\nYour Payment Amount is", result, "€\n")
    print(d)

n = int(input("Enter Number of Products:"))
Payment(n)
