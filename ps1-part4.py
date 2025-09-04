score = 0

prior_arrests = int(input("Prior arrests: " ))
local_ordinance = input("Prior arrests for local ordinance (Y/N): " )
age = int(input("Age at release: " ))

if prior_arrests >= 2:
    score = score + 1
if prior_arrests >= 5:
    score = score + 1
if local_ordinance == "Y":
    score = score + 1
if 18 <= age <= 24:
    score = score + 1
if age >= 40:
    score = score - 1
print("The recidivism risk score is",score)
