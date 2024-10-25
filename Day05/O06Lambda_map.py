
l1 = list(range(1, 11))
print(f"l1 :{l1}")

square = list(map(lambda x : x ** 2, l1))
print(f"squares :{square}")

# conversions = currency, weight, litres
expenses = [8500, 12000, 10000, 25800, 19000, 16350, 5000]
# convert this into dollars using map and lambda function

print(expenses)
dollars=list(map(lambda x:x/84,expenses))
print(dollars)

print("-" * 60)

months = ['dec', 'jul', 'sep', 'nov', 'jun', 'jan', 'oct', 'apr', 'feb', 'may', 'aug', 'mar']

# sort these months according to the calendar