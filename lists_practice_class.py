names = ["Alex", "Mary", "Steve", "John", "Seinfeld", "Alan", "Jane"]

for item in names[:]:
    if item == "Steve" or item == "Alan":
        names.remove(item)

print names[:]
    