
for i in range(1, 10):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 31):
    # if i > 25:
    #     break               # stop the iteration
    if i % 2 == 1:
        continue            # skip the iteration
    else:
        print(i, end=" ")
else:
    print("\ncompleted generating numbers...")