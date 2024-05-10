import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_number =int(input("enter how many numbers you want to include"))
nr_letters= int(input("enter how many  letters you want to include"))
nr_symbols = int(input("enter how many symbols you want to include"))

password =[]
for char in range(1,nr_number+1):
  password.append(random.choice(letters))
for char in range(1,nr_number+1):
  password.append(random.choice(symbols))
for char in range(1,nr_symbols+1) :
  password.append(random.choice(numbers))  
print(password)   
