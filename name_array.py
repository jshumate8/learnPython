names = ["Alex", "John", "Mary", "Jerry", "George"]
print(names)
name_to_delete = input("Please give me a name to delete: ")


for i in range(0, len(names)):
    if name_to_delete.lower() == names[i].lower():
        print("OK, I will delete " + name_to_delete + ":")
        del names[i]
        break

print(names)



    

#delete_name(del_input)

