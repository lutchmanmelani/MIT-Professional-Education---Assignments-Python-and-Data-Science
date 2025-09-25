#Changed to input - using python version 3
name = input("what is your name?")
city = input("what city do you live in?")
state = input("What state is that in?")

print("Hello there! It is so great to meet you")
#One way to do this is to print strings on separate lines
print(name)
print("from")
print(city)
print(state)
#Changed from commas to + signs - using python version 3
print(name.title()+ " " + "from " + city.title()+ " " + state.title())

age = input("Pardon my rudeness, but how old are you?")
print("Wow! you look like you could be " + int(age - (0.15 * age)))
