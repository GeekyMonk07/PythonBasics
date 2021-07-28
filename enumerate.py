a = [22, "Anmol", 25.2, False]

# NATIVE WAY
# for i in a:
#     j = a.index(i)
#     print (f"{i} {j}")

for index,item in enumerate(a):
    print(f"{index}. {item}")
