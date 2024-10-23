
print("find".center(60, "-"))
st = "hello world"
print(f"st :{st}")

pos = st.find("w")
print(f"pos :{pos}")

pos = st.find("l")
print(f"first pos of l :{pos}")

# hard coding
# pos = st.find("l", 6)
# print(f"second pos of l :{pos}")

pos = st.find("l", st.find("l") + 1)
print(f"second pos of l :{pos}")

pos = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"third pos of l :{pos}")

print("replace".center(60,"-"))
st = "hello world"
print(f"st :{st}")

res = st.replace("h", 'H')
print(f"res :{res}")

res1 = res.replace("l", "L")
print(f"res1 :{res1}")

res1 = res.replace("l", "L", 1)
print(f"res1 :{res1}")

res1 = res.replace("l", "L", 2)
print(f"res1 :{res1}")

res = st[:6] + st[6:].replace("l", "L")
print(f"res :{res}")

print("-" * 60)
st = "1234234234234python5678"
print(f"st :{st}")

print(st[0].isalpha())
print(st[0].isnumeric())

for i in range(0, len(st)):
    if st[i].isalpha():
        print(i)
        break

