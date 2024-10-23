
print("makestrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")

a = "helowrd"
b = "HELOWRD"

# lenght of a and b should be the same

resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("Translate".center(60, "-"))

res = st.translate(resTbl)
print(f"res :{res}")

print("-" * 60)

st = "****hello****"
print(f"st :{st}")

# lstrip
print(st.lstrip("*"))

# rstrip
print(st.strip("*"))
