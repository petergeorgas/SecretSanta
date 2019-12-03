import random
import Person
import os
import sys
import json
from twilio.rest import Client


names = []

## Try to open Names.txt
try:
    with open(os.path.join(sys.path[0], "Names.txt"), "r") as file: ## Open names.txt

        if(os.path.getsize(os.path.join(sys.path[0], "Names.txt")) == 0 ): ## If Names.txt is empty 
            print("Names.txt is empty! Please input your names and phone numbers you would like to use!")
            sys.exit() ## Terminate the program

        for line in file: ## For each line in the file
            temp_list = line.split(" - ") ## Split the line at the -
            ##print(temp_list[0] + ":" + temp_list[1])
            obj = Person.Person(temp_list[0], temp_list[1]) ## Create a new person object
            names.append(obj) ## Append the object to a list 
    person = names.copy() ## Make a duplicate of this list
except IOError:

    with open(os.path.join(sys.path[0], "Names.txt"), "w+") as file: ## If the file doesn't exist ,create it. 
        print("Names.txt did not exist, so it was generated! Please input your names and phone numbers you would like to use!")
        sys.exit() ## Terminate the program 

## Try to open Keys.json
try:

    with open(os.path.join(sys.path[0], "Keys.json"), "r") as keys_file: ## Open keys.json

        keys = json.loads(keys_file.read()) 
except IOError:

    with open(os.path.join(sys.path[0], "Keys.json"), 'w+') as keys_file: ## If the file doesn't exist, create it.
        json.dump({
        "Account_SID" : "",
        "Auth_Token" : "",
        "Account_Number" : ""
        }, keys_file, indent=2)
        print("Keys.json did not exist, so it was generated! Please input your Twilio Account SID and Auth Token!")
        sys.exit() ## Terminate the program 

##Grab the JSON information
account_sid = keys["Account_SID"]
auth_token = keys["Auth_Token"]
account_number = keys["Account_Number"]

client = Client(account_sid, auth_token)

print("[Secret Santa] Beginning pairing...")
i=0
num_pair = 0
while(len(names) > 0 and len(person) > 0):
    rand = random.randint(0, len(names)-1) ## Generate a random int used for an index to pick each person's gift receiver
    if(names[i] != person[rand]): ## If the names don't match
        message = client.messages \
                .create(
                     body = "You have received: " + person[rand].getName() + " for Secret Santa!",
                     from_ = account_number,
                     to = names[i].getNumber()
                 )
        names.remove(names[i])
        person.remove(person[rand])
        num_pair+=1
    else: ## If the names match
        continue ## Try again
    
print("Drawing completed successfully! There were a total of: " + str(num_pair) + " pairings!")