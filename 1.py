palindrom = []
for i in range(2019):
    i_str = str(i)
    if i_str == i_str[::-1]:
        palindrom.append(i_str)
print(palindrom)
