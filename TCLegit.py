#Tassomai Assistant
#Started 28/09/20

#Imports
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Listener, Key
from selenium import webdriver
from ast import literal_eval
from time import sleep, time
from random import randint
import pyautogui as p
p.FAILSAFE = False
import keyboard as k
import collections as c
import pickle
from os import system
from random import randint
#Declarations

#The link to the quiz that we are doing
frontPage = "https://app.tassomai.com/dashboard/learner"

#Coords of the first and second quick button
quizButton = (866, 651)
quizButton2 = (1052, 650)
#Only use this when there is only one quiz button on the screen
quizButton3 = (960, 634)

#These are RGB values for the colours that answers flash when gotten wrong or right.
#We use these values to determine whether an answer was gotten correct or not and update the database accordingly.
Green = (201, 240, 195)
GreenCorrect = (200, 239, 194)
GreenCorrect2 = (199, 238, 193)
Red = (247, 187, 174)
Red2 = (246, 186, 173)

#These are coordinates for the answer buttons. The last coordinate is for the quiz button.
#These are for 1080x1920 resolutions.
#Depending on your screen resolution, you might need to update these.
pos1 = (576, 519)
pos2 = (974, 511)
pos3 = (575, 638)
pos4 = (974, 637)

#Quiz buttons? ~ not sure

#The number of questions answered correctly and incorrectly
#The amount of desired correct and incorrect answers
noCorrect = 0
noIncorrect = 0
noDCorrect   = randint(45, 55)
noDIncorrect = randint(10, 15)
print("Correct: {}, Incorrect: {}".format(noDCorrect, noDIncorrect))

#The directory to the current database we are reading from.
currentDB = "qanda.txt"
with open(currentDB, "rb") as f:
    qanda = pickle.load(f)
    #Used to compare to the final size, after saving
    prevSize = len(qanda)

#Directory to the webdriver.
#options = Options()
#options.add_argument('--disable-gpu')
b = webdriver.Chrome("C:\\Users\\USER\\Desktop\\Scripts\\Sel\\chromedriver.exe")#, options=options)


#This opens the URL in chrome.
b.get("https://www.tassomai.com/login")

#Automatically logging in
#This find the fields on the page that are written to.
email = b.find_element_by_name("email")
password = b.find_element_by_name("password")

#This writes a predefined username and password to the fields.
email.send_keys("USERNAME_HERE")
password.send_keys("PASSWORD_HERE")
password.send_keys(Keys.ENTER)

#Function definitions
#Finds the correct answer and returns the text of it
def findAnswer():
    global noCorrect
    p.moveTo(pos1)
    p.click()
    sleep(0.90)
    for num in range(1,5):
        if num == 1:
            colour = p.pixel(pos1[0], pos1[1])
            if colour == Green:
                noCorrect += 1
                print("\tRecorded", list(infoList[1:])[0], "\n")
                return infoList[1:][0]
                
        elif num == 2:
            colour = p.pixel(pos2[0], pos2[1])
            if colour == Green:
                print("\tRecorded", list(infoList[1:])[1], "\n")
                return infoList[1:][1]
                
        elif num == 3:
            colour = p.pixel(pos3[0], pos3[1])
            if colour == Green:
                print("\tRecorded", list(infoList[1:])[2], "\n")
                return infoList[1:][2]
                
        elif num == 4:
            colour = p.pixel(pos4[0], pos4[1])
            if colour == Green:
                print("\tRecorded", list(infoList[1:])[3], "\n")
                return infoList[1:][3]
            
            else:
                print("Colour unrecognised.")
                return "FAILED"

#Clicks an answer, dependent on the number passed
def clickAnswer(NOb2p):
    global noCorrect
    global noIncorrect
    
    if NOb2p == 0:
        NOb2p = 4
        
    if NOb2p == 1:
        p.moveTo(pos1)
        p.click()
        sleep(0.90)
        colour = p.pixel(pos1[0], pos1[1])
        if colour == Red or colour == Red2:
            print("\tCorrect answer was Wrong.\n")
            noIncorrect += 1
            
        elif colour == Green or colour == GreenCorrect or colour == GreenCorrect2:
            print("\tAnswer was Right.\n")
            noCorrect += 1
            return "SUCCESS"
            
        else:
            print("Couldn't recognise the colour.")
            print("Debug~ NOb2p:{}, colour:{}".format(NOb2p, colour))
        
    elif NOb2p == 2:
        p.moveTo(pos2)
        p.click()
        sleep(0.90)
        colour = p.pixel(pos2[0], pos2[1])
        if colour == Red or colour == Red2:
            print("\tCorrect answer was Wrong.\n")
            noIncorrect += 1
            
        elif colour == Green or colour == GreenCorrect or colour == GreenCorrect2:
            print("\tAnswer was Right.\n")
            noCorrect += 1
            return "SUCCESS"
            
        else:
            print("Had a problem with the colour.")
            print("Debug~ NOb2p:{}, colour:{}".format(NOb2p, colour))
        
    elif NOb2p == 3:
        p.moveTo(pos3)
        p.click()
        sleep(0.90)
        colour = p.pixel(pos3[0], pos3[1])
        if colour == Red or colour == Red2:
            print("\tCorrect answer was Wrong.\n")
            noIncorrect += 1
            
        elif colour == Green or colour == GreenCorrect or colour == GreenCorrect2:
            print("\tAnswer was Right.\n")
            noCorrect += 1
            return "SUCCESS"
            
        else:
            print("Had a problem with the colour.")
            print("Debug~ NOb2p:{}, colour:{}".format(NOb2p, colour))
        
    elif NOb2p == 4:
        p.moveTo(pos4)
        p.click()
        sleep(0.90)
        colour = p.pixel(pos4[0], pos4[1])
        if colour == Red or colour == Red2:
            print("\tCorrect answer was Wrong.\n")
            noIncorrect += 1
            
        elif colour == Green or colour == GreenCorrect or colour == GreenCorrect2:
            print("\tAnswer was Right.\n")
            noCorrect += 1
            return "SUCCESS"
            
        else:
            print("Had a problem with the colour.")
            print("Debug~ NOb2p:{}, colour:{}".format(NOb2p, colour))

    return "FAILED"

#This is where the limit of correct questions to be answered is defined
try:
    while 1:
        sleep(0.5)
        #This happens if the limit is reached.
        if noDCorrect == noCorrect and noDIncorrect == noIncorrect:
            with open(currentDB, "wb") as f:
                print("\nSize before:", prevSize)
                pickle.dump(qanda, f)
                print("Size after:", len(qanda))
                print("The database has updated automatically.")
                #REMOVE THIS -------------------------------------------------------
                system("shutdown -s -t 0")
            raise Exception("Limit has been reached!")

        #GRABBING INFOLIST
        #Grabs all classes on the page.
        listOfClassesInWebsite = b.find_elements_by_xpath("//*[@class]")
        #This loop iterates through all the classes on the page.
        #It finds the classes that contain the text of the question and answers.
        #It then appends them to "infoList"
        #infoList is a list containing the questions and potential answers
        #in a list in that order
        infoList = []
        for classes2 in listOfClassesInWebsite:
            try:
                if "question-text-and-image" in classes2.get_attribute("class") or "answer__container ng-star-inserted" in classes2.get_attribute("class"):
                    infoList.append(classes2.text)
            except Exception as e:
                print(e)

        #After the update, infoList is filled with empty characters: ["", "", ""]
        #They are removed below.
        infoList = [x for x in infoList if x != ""]
        
        #This happens if there has been an error or if a quiz is finished.
        #The page is redirected to the quiz again.
        if infoList == [] or infoList == [""]:
            #NEW CODE
            b.get("https://app.tassomai.com/dashboard/learner")
            #Going to ONE of the quiz pages (this is the link for the first one)
            #sleep(0.5)
            #p.moveTo(quizButton)
            #p.click()
            sleep(0.5)
            p.moveTo(quizButton)
            p.click()
            continue
            
        #This happens when the question hasn't been seen before
        found = ""
        for key in qanda:
            questionFound = True
            for aQuestion in (literal_eval(key))[1:]:
                if aQuestion not in infoList[1:] or literal_eval(key)[0] not in infoList:
                    questionFound = False
                    break

            if questionFound == True:
                found = key
                break
        if found == "":
            qanda[repr(infoList)] = ""

        #This happens when the question and set of answers has been seen before
        if found != "":
            print("Question recognised.")
            #Text of button to press
            TOb2p = qanda[found]
            #Number of button to press
            NOb2p = list(infoList[1:]).index(TOb2p)+1
            if noCorrect == noDCorrect:
                print("Getting answer wrong.")
                NOb2p -= 1
                
            result = clickAnswer(NOb2p)

        #This happens when there is not an answer stored in qanda for the question
        else:
            print("Question unrecognised.")
            textOfCorrectAnswer = findAnswer()
            if textOfCorrectAnswer != "FAILED":
                qanda[repr(infoList)] = textOfCorrectAnswer
            else:
                print("Question finding failed wtf..........")

except KeyboardInterrupt as e:
    with open("qanda.txt", "wb") as f:
        print("\nSize before:", prevSize)
        pickle.dump(qanda, f)
        print("Size after:", len(qanda))
        print("The database has updated automatically.")
