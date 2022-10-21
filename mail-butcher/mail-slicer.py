import os
def butcher():
 text = str(input("Enter the email address that you want to slice: "))
 (name,domain)=text.split("@")
 (domain,extension)=domain.split(".")
 os.system('cls' if os.name == 'nt' else 'clear')
 print("username: "+name)
 print("domain: "+domain)
 print("extension: "+extension)
choice = -1
while choice!= 0:
 print("""
   __  __       _ _
  |  \/  |     (_) |
  | \  / | __ _ _| |
  | |\/| |/ _` | | |
  | |  | | (_| | | |
  |_|__|_|\__,_|_|_|   _
  |  _ \      | |     | |
  | |_) |_   _| |_ ___| |__   ___ _ __
  |  _ <| | | | __/ __| '_ \ / _ \ '__|
  | |_) | |_| | || (__| | | |  __/ |
  |____/ \__,_|\__\___|_| |_|\___|_|


 """)
 print("1)Slice a mail")
 print("0)Exit")
 choice = int(input("Enter your choice: "))
 if(choice==1):
  butcher()
print("Goodbye!")
