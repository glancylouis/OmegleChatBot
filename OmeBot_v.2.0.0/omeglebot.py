# IMPORTS
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    try:
        print("THIS PROGRAM IS MADE BY ELRISH JOHN RULL, ENJOY!")

        time.sleep(0.7)
        print("\nChecking Chromedriver...")
        time.sleep(0.5)
        exe = 'chromedriver.exe'

        # CHECKING IF CHROMEDRIVER EXISTS

        if not os.path.exists(os.path.abspath(exe)):
            print('You don\'t have a Chromedriver, please download it.')

        if os.path.exists(os.path.abspath(exe)):
            print("\nChromedriver FOUND!")

            print("\n==================================================")
            print("\nPlease put your [3] interests here : ")
            ints1 = str(input(">> 1 : "))
            ints2 = str(input(">> 2 : "))
            ints3 = str(input(">> 3 : "))
            print("\n==================================================")

            # GETTING USER'S MESSAGE
            print("\nPlease put your message here : ")
            mymsg = input(">> Your Message : ")

            # MESSAGE COUNT
            repeats = int(input("\n>> How many messages you want to send : "))
            print("\n==================================================")
            print("\nNOTE : \nLARGE INTERVALS IS MORE PRONE TO ERRORS"
                  "\nSMALL INTERVALS IS MORE PRONE TO CAPTCHA"
                  "\nSUGGESTED INTERVAL IS BETWEEN 1s - 1.5s")
            interval = float(input("\n>> Intervals between messages in seconds : "))
            print("\n==================================================")

            print("\nRunning in 3...")
            time.sleep(1)
            print("Running in 2...")
            time.sleep(1)
            print("Running in 1...")
            time.sleep(1)

            # CHROMEDRIVER PATH
            service = Service(os.path.abspath(exe))
            driver = webdriver.Chrome(service=service)

            # INPUT URL
            print("\n==================================================")
            print("\nOpening Chrome...")
            driver.maximize_window()
            driver.get("https://www.omegle.com/")

            time.sleep(0.5)

            # SCROLLING
            driver.execute_script("window.scrollBy(0,500)", "")

            time.sleep(0.5)

            # INPUT INTERESTS
            print("\nPutting your interests...")
            interest = driver.find_element(By.CSS_SELECTOR,
                                           "#topicsettingscontainer > div > div.topictageditor.needsclick > input")
            time.sleep(0.3)
            interest.send_keys(ints1)
            interest.send_keys(",")
            interest.send_keys(ints2)
            interest.send_keys(",")
            interest.send_keys(ints3)
            interest.send_keys(",")

            # START
            print("\nStarting...")
            start = driver.find_element(By.CSS_SELECTOR, "#textbtn")
            start.click()

            # CONFIRMING PERMISSIONS
            print("\nChecking permissions...")

            wait = WebDriverWait(driver, 30)

            chckbox1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                              "body > div:nth-child(11) > div > p:nth-child(2) > label > input[type=checkbox]")))
            chckbox1.click()

            chckbox2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                              "body > div:nth-child(11) > div > p:nth-child(3) > label > input[type=checkbox]")))
            chckbox2.click()

            time.sleep(0.5)

            print("\nFinding a match...")

            # START CHATTING
            confirm = driver.find_element(By.CSS_SELECTOR,
                                          "body > div:nth-child(11) > div > p:nth-child(4) > input[type=button]")
            confirm.click()

            time.sleep(1.5)
            print("\n==================================================")

            increment = 0

            # MESSAGE HERE
            for a in range(repeats):
                waitTime = WebDriverWait(driver, 30)
                findElement = waitTime.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         'body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea')))

                msg = driver.find_element(By.CSS_SELECTOR,
                                          'body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea')
                msg.send_keys(mymsg)

                # SEND MESSAGE

                send = driver.find_element(By.CSS_SELECTOR,
                                           "body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > "
                                           "td.sendbthcell > div > button")
                send.click()

                increment += 1

                print("\nSuccessfully sent a message : " + str(increment))

                # NEW MESSAGE
                waitTime = WebDriverWait(driver, 20)
                findElementFix = waitTime.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                            'body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.chatmsgcell > div > textarea')))

                newChat = waitTime.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                     "body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button")))
                newChat.click()
                time.sleep(interval)
                newChat.click()

                newChatFix = waitTime.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                        "body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button")))
                time.sleep(0.1)
                newChatFix.click()
                time.sleep(0.2)
                time.sleep(0.5)

                if waitTime == 5:
                    newChatFix1 = driver.find_element(By.CSS_SELECTOR,
                                                      "body > div.chatbox3 > div > div > div.controlwrapper > table > tbody > tr > td.disconnectbtncell > div > button")
                    time.sleep(0.1)
                    newChatFix.click()

                if repeats == increment:
                    print("\n==================================================")

                    print("\nTHE LIMIT IS REACHED YOU SENT " + str(increment) + " MESSAGES SUCCESSFULLY")

                    print("\n==================================================")

                    toQuit = input("\nInput something to exit : ")
                    print("\nQuitting...")
                    time.sleep(0.8)
                    exit()

    except (Exception,):
        print("\n==================================================")

        print("\nENCOUNTERED AN ERROR")

        print("\n==================================================")

        print("\nRICKROLL WILL PLAY...")

        driver.switchTo().alert().accept()

        driver.get("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        toQuit = input("\nInput something to exit : ")
        print("\nQuitting...")
        time.sleep(0.8)
        exit()

except (Exception,):
    print('\nAUTOMATION HAS STOPPED DUE TO CAPTCHA' + ', PLEASE RESTART THE PROGRAM TO CONTINUE')
    print("\n==================================================")
    print("\nRICKROLL WILL PLAY...")
    driver.get("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    driver.switch_to.alert.accept()
    toQuit = input("\nInput something to exit : ")
    print("\nQuitting...")
    time.sleep(0.8)
    exit()



# CREATED BY ELRISH JOHN
