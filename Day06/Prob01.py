
# months = ['dec', 'jul', 'sep', 'nov', 'jun', 'jan', 'oct', 'apr', 'feb', 'may', 'aug', 'mar']

months = ['dec', 'jul', 'sep', 'nov', 'jun', 'jan', 'oct', 'apr', 'feb', 'may', 'aug', 'mar']

print(f"unsorted months : {months}")

print("-" * 60)
from calendar import month_abbr
print(f"month_template :{list(month_abbr)}")

print("-" * 60)
sorted_months = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

# map(lambda, list) =>
# sorted(months, key = list(map(lambda mth : mth.lower(), list(month_abbr))).index)

print(f"Sorted Months :{sorted_months}")

print("-" * 60)

cities = ['thiruvananthapuram', 'hyderabad', 'bangalore', 'mumbai', 'chennai', 'ooty', 'delhi', 'vishakapatnam', 'pune']

print(f"cities :{cities}")

print("-" * 60)

res = sorted(cities, key=len)
print(res)
