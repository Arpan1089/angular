#known users list

known_users =['arpan', 'sumeet' ,'priyanka']
print(len(known_users))

name = input('what is your name ').strip()
if name in known_users:
     print('hello ! {}'.format(name))
     remove = input('would you like to be removed from the system (y/n) ') .lower()
     if remove == 'y':
          
          known_users.remove(name)
          
else:
     print('you are not registered yet !')
     check = input('Do you want to be registered : y/n').lower().strip()
     if check == 'y':
          known_users.append(name)
          print(known_users)
         
         
