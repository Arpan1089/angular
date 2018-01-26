films = {
    "Tiger":[18 ,22],
    "Sex in balcony ":[58 ,122],
    "Tom and jerry ":[8 ,42]
    }

film_name =   input('which film do you want to watch : ?').strip().title()
if film_name in films :
   age = int(input('how would are you ?').strip())
   if age >= films[film_name][0] and films[film_name][1] > 0:
       print('your ticket is booked go and fuck ')
   else:
      print('sorry your age or seat is finished')

