# cricket
player_count = 11
rating = 8.78
has_won_world_cup = True
team_name = "India"

print(player_count)
print(rating)
print(has_won_world_cup)
print(team_name)
# name of the current module
print(__name__)  # double underscore  => dunder_name

a, b, c = 10, 20, 'hello'
print(a, b, c, sep=", ")
print(a, b, c, sep=": ")

# apply formatting for the entire file - ctrl + alt + L
a = b = c = 256
print(a, b, c, sep=", ")

print("-" * 60)
first_name = "Sachin"
last_name = "Tendulkar"

# interpolation
print(f"My name is {first_name} and I am also known as {last_name}")

frt1 = 'Apple'
frt2 = 'Orange'

print(f"{frt1} is costlier than {frt2}")
prc = 385
wgt = 5
print(f"{frt1} is {prc} per kg and we get a discount of 20% if we buy more than 3 kgs {prc * wgt * 0.8}")

print("-" * 60)
# strings can be enclosed in " " or ' '
team_name = "Royal Challengers"
print("The team name is ", team_name)

print("-" * 60)
team_name = "'Royal Challengers'"
print("The team name is ", team_name)

print("-" * 60)
team_name = '"Royal Challengers"'
print("The team name is ", team_name)

print("-" * 60)
team_name = '\'Royal Challengers\''
print("The team name is ", team_name)

print("-" * 60)
team_name = "\"Royal Challengers\""
print("The team name is ", team_name)


print("=" * 60)
if __name__ == '__main__':
    print("hello world")
