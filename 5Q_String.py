def str_i(str): 
    if len(str) == 0: 
        return str 
    else: 
        return str_i(str[1:]) + str[0] 
  
str = input (" String a ser invertida: ")
print ("a string invertida é : ",str_i(str))  