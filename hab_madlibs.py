name = input("Enter your name: ")
age = input("Enter your age: ") 
gender = input("Enter your gender: ")
food = input("Enter your favorite food: ")
color = input("Enter your favorite color: ")
adjective = input("Enter an adjective: ")   
verb = input("Enter a verb +ing: ")  
time = input("Enter a time of day (e.g., morning, afternoon, evening): ")
place = input("Enter a place: ")

title = 'Give me a STAR if you like this project!'
ending = 'Thank you! DONT FORGET TO STAR!'
madib = f"""I am {name}, a {age} year old {gender}.
 I like {food} and my favorite color is {color}. 
 I live in a {adjective} tree house like Tarzan.
 I love {verb} with the MONKEYS in the {time}
 at {place}."""

print(title)
print(madib)
print(ending)