""" 
[Start Date: 2025|02|5] [Total Time (hr): 9 hr 20 mins] [Finish Date: 2025|02|27] 
[Author: FirstOfLast]
"""
import os
import json
from datetime import datetime

def createEntry():

    entries = readFile()
    print("")
    while True:
        entryName = input("\t\tEnter the title for your new entry in the journal: ")
        if entryName in entries:
           print("\t\t\tThe entered title already exists in the journal!")
        else:
            break

    entryMessage = input(f'\t\tEnter the content for your entry titled "{entryName}": ')

    entryDate = input(f'\t\tEnter the date (YYYY-MM-DD) for your entry titled "{entryName}": ')
    try:
        datetime.strptime(entryDate, "%Y-%m-%d")
    except ValueError:
        print("\t\t\tInvalid date format! Using today's date instead.")
        entryDate = datetime.today().strftime("%Y-%m-%d")

    entry = {entryName : {"Message" : entryMessage, "Date" : entryDate}}
    entries.update(entry)
    writeFile(entries)

    print(f'\t\tSaved the new entry titled "{entryName}" to the journal!\n')

def viewEntries():

    entries = readFile()
    titles = findKeys(entries)
    viewChoice = int(input("\n\t\tWhich entry do you want to view: "))
    print(f'\n\t\t\t\t\tTitle\t: {titles[viewChoice]} \n\t\t\t\t\tMessage\t: {entries[titles[viewChoice]]["Message"]} \n\t\t\t\t\tDate\t: {entries[titles[viewChoice]]["Date"]}\n')

def deleteEntry():

    entries = readFile()

    titles = findKeys(entries)
    deleteChoice = int(input("\n\t\tWhich entry would you like to delete from the journal: "))

    if titles[deleteChoice] in entries:
        del entries[titles[deleteChoice]]
        writeFile(entries)
        print(f'\t\tSuccessfully removed the entry in the journal with the title "{titles[deleteChoice]}"\n')
    else:
        print("\t\tThere is no entry with the title you mentioned in the journal\n")

def searchEntry():
    entries = readFile()
    searchChoice = input("\n\t\tEnter the title you want to search for in the journal: ")
    if searchChoice in entries:
        print(f'\n\t\t\t\t\tTitle: {searchChoice} \n\t\t\t\t\tMessage: {entries[searchChoice]["Message"]} \n\t\t\t\t\tDate: {entries[searchChoice]["Date"]}\n')

# Code for one of the optional requirement (i.e. edit an entry) for the program
# Not completed !!!, teh below code is for edit a differtly foramted json, which i used before changes # it backj to the style I am using right now

# def editEntry():
#     entries = readFile()
#     searchEntry = input("\t\tEnter the title of the entry you want to search for to edit: ")
#     editSuccessful = False
#     for entry in entries:
#         if entry['Title'] == searchEntry:
#             ch2 = "y"
#             while ch2 == "y":
#                 userEditChoice = int(input(f"\t\t\tWhat do you want to edit in entry titled {entry['Title']} \n\t\t\t\t1. Title\n\t\t\t\t2. Message\n\t\t\t\t3. Date\n\t\t\tEnter your choice: "))
#                 if userEditChoice == 1:
#                     entry["Title"] = input("\t\t\t\tEnter a new title: ")
#                     for entryAgain in entries:
#                         if entryAgain['Title'] == entry["Title"]:
#                             entryAgain["Title"] = input("\t\t\t\tThe entered title already exists in the journal! Please use a different title: ")
#                         else:
#                             continue
#                 elif userEditChoice == 2:
#                     entry["Message"] = input("\t\t\t\tEnter a new message: ")
#                     editSuccessful = True
#                     ch2 = input("\t\t\tDo you want to make any other change(y/n): ")
#                 elif userEditChoice == 3:
#                     entry["Date"] = input("\t\t\t\tEnter a new message: ")
#                     editSuccessful = True
#                     ch2 = input("\t\t\tDo you want to make any other change(y/n): ")
#                 else:
#                     userEditChoice = int(input("\t\t\t\tInvalid choice!!!\n\t\t\tEnter a valid choice: "))
#     if editSuccessful == True:
#         print(f"\t\tSuccessfully edited the entry titled '{entry['Title']}'")
#     else:
#         print("\t\tThere is no entry with the title you mentioned in the journal")
#     writeFile(entries)
#     entries.append(entry)
#     writeFile(entries)   

def readFile():
    if os.path.exists("02-journal/python/data.json"):
        with open("02-journal/python/data.json", "r") as jsonFile:
            entries = json.load(jsonFile)
    else:
        entries = {}
    return entries

def findKeys(entries):
    enum = 1
    titles = {}
    print("\n\t\tAll the entry titles in the journal")
    for key in entries:
        title = {enum : key}
        print(f'\t\t\t{enum}. {key}')
        titles.update(title)
        enum += 1
    return titles

def writeFile(entries):
    with open("02-journal/python/data.json", "w") as jsonFile:
        json.dump(entries, jsonFile, indent=4)

def main():
    
    ch = "y"
    
    while ch == "y":

        userChoice = int(input("Welcome to your journal\n\t0. Exit the program\n\t1. Create a new entry\n\t2. View one of your entries\n\t3. Delete a previous entry\n\t4. Search for a previous entry\n\tEnter your choice: "))

        if userChoice == 0:
            exit()

        elif userChoice == 1:
            createEntry()
            ch = input("\tDo you want to countinue(y/n): ")
            print("")

        elif userChoice == 2:
            viewEntries()
            ch = input("\tDo you want to countinue(y/n): ")
            print("")

        elif userChoice == 3:
            deleteEntry()
            ch = input("\tDo you want to countinue(y/n): ")
            print("")

        elif userChoice == 4:
            searchEntry()
            ch = input("\tDo you want to countinue(y/n): ")
            print("")

        else:
            print("\t\tInvalid choice!!!\n")
        
main()