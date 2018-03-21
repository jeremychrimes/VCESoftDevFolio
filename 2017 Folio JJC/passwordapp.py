## Jezz Chrimes <jjchr2@schools.vic.edu.au>
from hashlib import md5 ## Importing the library to hash the users password input as md5.
from time import sleep 
password = "dc647eb65e6711e155375218212b3964" ##Setting the password the computer wants.
Times = [1,5,10,20,60,1440] # setting the time out times 
lockedout = 0 ##Setting a variable to record the number of times the user has been locked out
login = False ## A variable to break the loop if the user gets the password 
attempt = 0
while (login == False) : # Setting the attempts 
    userPassword = input("Password: ").encode("UTF-8")
    userPassword = md5(userPassword).hexdigest()
    if (userPassword == password):
        print ("Congratulations you found the password however the police are on their way becuause we have reason to belive that you have breached our security policies")
        login = True 
    else:
        attempt += 1
        print("Password Incorrect")
        if (attempt > 4):
            print ("Access Denied! you have been locked out for {0} minutes".format(Times[lockedout]))
            sleep(Times[lockedout]* 60)
            lockedout += 1 
    
