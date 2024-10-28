
glbX = 500

def fun(x):                 # local var
    global glbX             # do not assign any value
    print(f"x inside :{x}")
    glbX += 100
    print(f"inside :{glbX}")



print(f"glbX before :{glbX}")

fun(100)
print(f"glbX after :{glbX}")