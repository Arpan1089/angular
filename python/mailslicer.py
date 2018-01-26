#getting user mail
user_mail= input("please enter your mail address : ").strip()
#arpan18.kmr@gmail.com
user_name = user_mail[0:user_mail.index('@')]

#domain name

domain =user_mail[user_mail.index('@') +1 :user_mail.index('com')]

string = 'user name is {} and domain name is {}'
output = string.format(user_name,domain)

print(output)
