class Packing:
    def __init__(self):
    # 1. Create a list of items in your room you can potentially pack.
        self.roomItems = ["Clothes", "Toothbrush", "Toothpaste", "Comb", "Phone", "Notebook", "Laptop"]
    #2. Create an empty list to represent your travel bag 
        self.bagList = []
    #3. Repeatedly prompt the user for items to put in their travel bag by removing them from the the list of items in your room to your travel bag list.
    def Pack(self):
        print("You are packing items from your room into a bag. You will be asked whether you want certain items to go into the bag or not.")
        Invalid = False
        for x in self.roomItems:
            self.packDecision = input("Do you want " + x + " to be packed? Type Y if yes. ").upper()
            if self.packDecision == "Y":
                self.bagList.append(x)
            else:
                continue

        self.pHolderList = [x for x in self.roomItems if x not in self.bagList] 
        self.roomItems = self.pHolderList
                


                
        #4. Once the list is complete, finalize it by creating a tuple representing your luggage. It should have every item in your travel bag. Empty the travel bag list as you do this.

        #5. Print the contents of your luggage for the trip,
        print("")
        print("Your Bag: " + str(self.bagList))
        print("")
        print("Your Room: " + str(self.roomItems))

