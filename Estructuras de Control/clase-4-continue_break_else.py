"""
continue => permite saltar a la siguiente posición
break => rompe (cancela) el ciclo
else => ejecuta una porción de código cuando termina el ciclo
"""

frameworks = ["Flask", "Django", "FastApi", "Pyramid"]

# Continue:
# for f in frameworks:
#     if f == "Flask":
#         print("Es Flask")
#         continue
#     print(f)

# Break
# for f in frameworks:
#     if f == "Flask":
#         print("Es Flask")
#         break
#     print(f)

# Else
# for f in frameworks:
#     if f == "Flask":
#         print("Es Flask")
#     print(f)
# else:
#     print("El ciclo terminó")

# Else
number = 1
while number < 10:
    if number == 5:
        print("Es 5")
        # continue
    print(number)
    number += 1
else:
    print("El ciclo terminó")