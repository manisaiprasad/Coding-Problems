def isUnique(list):
    uniqe = []
    for letter in list:
        if letter in uniqe:
            return False
        else:
            uniqe.append(letter) 

    return True

print(isUnique("abc"))
    
