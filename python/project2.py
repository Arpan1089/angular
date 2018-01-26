# asking for name
name = input("What is your name ?: ")



#Asking for age
age = input("what is your age ? : ")

#asking for city
city =input("what is your city name ? : ")



#asking what they enjoy
love =input(" what you enjoy most ? : ")


#creating o/p text

string = "Your name is {} you are {} years old as well as you love {}"
output = string.format(name,age,city,love)


#print output to screen
print(output)
