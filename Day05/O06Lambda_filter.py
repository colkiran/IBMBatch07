
l1 = list(range(1, 31))
print(f"l1 :{l1}")

# filter condition  - multiples of 3
res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

res1 = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res1 :{res1}")

res2 = list(filter(lambda x : len(x) <= 4, sentence.split()))
print(f"res2 :{res2}")