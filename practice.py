s = input("Enter a string: ")
dict = {} 
for ch in s:
    if ch in dict: 
        dict[ch] += 1
    else:
        dict[ch] = 1 
for key in dict:
    print(key,':',dict[key])