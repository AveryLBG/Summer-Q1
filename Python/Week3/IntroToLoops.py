
#Make a list of ppl at your table.
Geniuses = [ "Avery", "Marshawn", "Max", "Semaj", "Kauri" ]

#Use a list to print their names.
for genius in Geniuses:
    print(genius)
# Prompt the user to print the list again
answer = input("Do you want me to print the list again? Y/N")
while answer == "Y":
    for genius in Geniuses:
        print(genius)
    answer = input("Do you want me to print the list again? Y/N")
