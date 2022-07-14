"""
Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


Your parking garage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1
- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

By the end of this project each student should be able to:
- Explain and/or demonstrate creating classes
- Explain and/or demonstrate creating class methods
- Explain and/or demonstrate class instantiation 


When the project is completed, commit the final changes and submit your GitHub link.
"""

class Parking():

    def __init__(self, parkingDict={}, tickets=[], parkingSpaces=[]): # this is what the code will come with "standard" - in terms of video games this is the basic game
        parkingDict = { 1: '',
                    }
        tickets = 10
        parkingSpaces = 10
        self.parkingDict = parkingDict
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces

    # This will reduce the space available in the parking lot
    def takeTicket(self):
        for i, j in self.parkingDict.items():
            if self.tickets == 0:
                print("We're sorry, there's no more space available until someone makes a payment.")
            while self.tickets != 0:
                userInput = input("Do you want to buy a ticket? Y/N: ").lower()
                if userInput == 'y':
                    self.parkingDict.update({next(iter(self.parkingDict)): 'not paid'})
                    self.tickets -= 1
                    self.parkingSpaces -= 1
                    print(f"WARNING: There are total of {self.parkingSpaces} parking space remaining!")
                    print(f"You're parking space has been reserved and status as {self.parkingDict[1]}")
                elif userInput == 'n':
                    return self.parkingDict
                else:
                    print("Please type the given selection/option, thank you.")

    # This will make more parking space available in the parking lot
    def payForParking(self): 
        askUser = input("Did you pay for your ticket? Y/N: ").lower()
        if askUser == 'y':
            self.parkingDict['not paid'] = 'paid'
            self.tickets += 1
            self.parkingSpaces += 1
            print("Thanks for coming. Your parking pass expires in 15 minutes.")
            print(f"ANNOUNCEMENT: There are now {self.parkingSpaces} spaces available for parking!")
        elif askUser == 'n':
            print("Please pay for parking before leaving.")
        else:
            print("Invalid input.")

    # This will signify end of the simulation (customer leaving our business)
    def leaveGarage(self):
        for spot in self.parkingDict:
            askUser = input("Are you ready to leave the garage? Y/N: ").lower()
            if askUser == 'y' and self.parkingSpaces != 0:
                print("Thank you, have a nice day!")
                break
            elif askUser == 'n':
                print("What would you like to do ?")
            else:
                print("Please type the given selection/option, thank you.")

# This will help to run the simulation
def run():
    Simulation = Parking()
    while True:
        userInput = input("What do you want to do? Park/Pay/Leave: ").lower()

        if userInput == 'park':
            Simulation.takeTicket()

        elif userInput == 'pay':
            Simulation.payForParking()

        elif userInput == 'leave':
            Simulation.leaveGarage()
            break
        
        else:
            print("Please type the given selection/option, thank you.")

run()