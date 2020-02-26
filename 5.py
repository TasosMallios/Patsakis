filename = input("Incert Text Filename:")
with open(filename,'r') as f:
        
    for line in f:
        line = line.replace('.', '')
        line = line.replace(',', '')
        line = line.replace('-', '')
        line = line.replace('"', '')
        line = line.replace('_', '')
        line = line.replace('!', '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace('{', '')
        line = line.replace('}', '')
        line = line.replace('/', '')
        line = line.replace('?', '')
        line = line.replace(';', '')
        line = line.replace(':', '')
        line = line.replace('`', '')


        for word in line.split():
            if word.isalpha():
                if len(word) > 3:
                    print(word[1:]+word[0]+"ay")    
                else:
                    print(word)
            else:
                print(word)
