import random

list = [0] * 5200000
x = [1] * 4800000
test = list + x

majority = 0

for i in range(100):
    count = 0

    s20 = random.sample(test, 20)
    for ele in s20:
        if ele == 0:
            count += 1
    if count > 20 / 2:
        majority += 1

print("sample size 20:", majority)

majority = 0

for i in range(100):
    count = 0

    s20 = random.sample(test, 100)
    for ele in s20:
        if ele == 0:
            count += 1
    if count > 100 / 2:
        majority += 1

print("sample size 100:", majority)

majority = 0

for i in range(100):
    count = 0

    s20 = random.sample(test, 400)
    for ele in s20:
        if ele == 0:
            count += 1
    if count > 400 / 2:
        majority += 1

print("sample size 400:", majority)
