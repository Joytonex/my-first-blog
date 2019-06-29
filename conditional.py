#given the python list a = [1,1,2,3,5,8,13,21,34,55,89],write a python list that print out the programme that is less than 10

a = [1,1,2,3,5,8,13,21,34,55,89]

def lessThanTen():
    for number in a:
        if number < 10:
            print(number)
            
lessThanTen()