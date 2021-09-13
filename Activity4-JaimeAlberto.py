firstName = "Jaime"
lastName = "Alberto"
favoriteColor = "Red"
favoriteMeal = "Pizza" 

#F-String
print(f"My first name is {firstName}, My last Name is {lastName}, My favorite color is {favoriteColor}, Myfavorite meal is {favoriteMeal}")


#Argument by name:
solution = "My first name is {a}, My last Name is {b}, My favorite color is {c}, Myfavorite meal is {d}".format(a="Jaime", b="Alberto", c="Red", d="Pizza")
print(solution)

#Argument by Position:
##### Start on 0 when counting positions
solution2 = "My first name is {0}, My last Name is {1}, My favorite color is {2}, Myfavorite meal is {3}".format("Jaime", "Alberto", "Red", "Pizza")
print(solution2) 

#Concatenation:
solution3 = "My first name is " + firstName + " My last Name is " + lastName + " My favorite color is " + favoriteColor + " My favorite meal is " + favoriteMeal
print(solution3)