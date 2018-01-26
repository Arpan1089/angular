from random import choice
questions =['why we kiss ?' ,'why sex?' ,'why icnt ?']
question =choice(questions)
ans =input(question).strip().lower()
while ans != "just because":
    ans=input("why?")

print('ooooo')
