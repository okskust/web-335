first_name = 'Oksana'
last_name = 'Kustova'
print(first_name + ' ' + last_name)

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def divide(x,y):
    if y==0:
        print("Divider can't be 0")
    else:
        return x/y

print(add(1,2))
print(subtract(4,1))
print(divide(8,2))