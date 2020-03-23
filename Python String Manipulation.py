dataString = input("Please enter your last name, first name, your favorite color, your favorite animal, and your favorite team: ")

firstCommalocation = dataString.find(",")
secondCommalocation = dataString.find(",",firstCommalocation+1)
thirdCommalocation = dataString.find(",",secondCommalocation+1)
fourthCommalocation = dataString.find(",",thirdCommalocation+1)

lastName=dataString[0:firstCommalocation]
firstName=dataString[firstCommalocation+1:secondCommalocation]
favoriteColor=dataString[secondCommalocation+1:thirdCommalocation]
favoriteAnimal=dataString[thirdCommalocation+1:fourthCommalocation]
favoriteTeam=dataString[fourthCommalocation+1:]

print("My name is "+firstName+" "+lastName+", my favorite color is "+favoriteColor+", my favorite animal is a "+favoriteAnimal+", and my favorite team is the "+favoriteTeam+".")
