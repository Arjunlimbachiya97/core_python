import re
a = "arhfj +91 1234567890  91 9874563210"

b = (re.compile(r"\d[+91]|\d{10}$"))

ma = b.finditer(a)
print(ma)
for i in ma:
    print(i)