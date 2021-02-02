from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
import cv2
import matplotlib.pyplot as pl
from deepface import DeepFace

import time
print('\t*************** Created by Ashutosh Kumar ****************************')
print('\t***************\tashutosh_ibg\t***************************')
print("Please change your Directory.If you already chaneged the directory .please ignore  ")
phone=int(input('Enter Your Mobile Number: '))

folder="E:\\project\\tinder\\images\\"

s=['Man','Women']
gender=int(input('Select Your Gender\n 1. Male \n 2. Women\n'))
if gender == 1:
    ugender = 'Man'
else:
    ugender = 'Women'

website='https://www.okcupid.com/login'
site= webdriver.Firefox(executable_path='geckodriver.exe')
site.get(website)
time.sleep(2)
wait=WebDriverWait(site,10)
hwait=WebDriverWait(site,5000)
print("Entered")
try:
    element=wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button[3]')))
    print(element)
    element.click()

    site.find_element_by_name('phone-number').click()
    time.sleep(4)
    site.find_element_by_name('phone-number').send_keys(phone)
    try:
        print("Try->try")
        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button'))).click ()
        try:
            print ("Try->try->try")
            a1=hwait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/span/img')))
            print(a1.get_attribute('src'))

        except:
            print ("Try->try->except")
            wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/input[1]'))).click()
            # site.find_element_by_xpath ('/html/body/div[6]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/input[1]').send_keys(OTP)
    except:
        print('try->except')
        wait.until (ec.element_to_be_clickable ((By.XPATH,'/html/body/div[6]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button'))).click ()
        print ("Enter Your OTP Manually")
        ad = 100
        for q in ad:
            try:
                a1 = hwait.until (ec.element_to_be_clickable ((By.XPATH,
                                                               '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/span/img')))
                a2 = hwait.until (ec.element_to_be_clickable ((By.XPATH,
                                                               '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/span/img')))
                a3 = hwait.until (ec.element_to_be_clickable ((By.XPATH,
                                                               '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[3]/span/img')))
                pic1 = a1.get_attribute ('src')
                pic2 = a2.get_attribute ('src')
                pic3 = a3.get_attribute ('src')
                array = [pic1, pic2, pic3]
                print (array)
                print (pic2)
                print (pic3)
                cpic = []
                for i in range (len (array)):

                    print (pic1)
                    site.execute_script ("window.open('" + str (array[i]) + "');")
                    time.sleep (5)
                    site.switch_to.window (site.window_handles[1])
                    time.sleep (3)
                    site.get_screenshot_as_file (folder+ str (i) + ".png")
                    time.sleep (5)
                    site.execute_script ("window.close();")
                    site.switch_to.window (site.window_handles[0])

                    try:
                        img = cv2.imread (folder+ str (i) + ".png")
                        pl.imshow (img[:, :, ::-1])
                        result = DeepFace.analyze (img, actions=['gender'])
                        print (result)
                        cpic.append (result['gender'])
                        os.remove (folder + str (i) + ".png")

                    except:
                        cpic.append ('Not')
                        pass

                if cpic[0] == cpic[1] == cpic[2]:
                    if cpic[0] and cpic[1] and cpic[2] != 'Not':
                        site.switch_to.window (site.window_handles[0])
                        wait.until (ec.element_to_be_clickable (
                            (By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click ()
                        time.sleep (2)
                        # for send message hwait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/span[5]/a'))).click()
                        #
                    else:
                        wait.until (ec.element_to_be_clickable ((By.XPATH,
                                                                 '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click ()


                elif cpic[0] == cpic[1]:
                    if cpic[0] and cpic[1] != 'Not':
                        site.switch_to.window (site.window_handles[0])
                        wait.until (ec.element_to_be_clickable (
                            (By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click ()
                        time.sleep (2)
                    else:
                        wait.until (ec.element_to_be_clickable ((By.XPATH,
                                                                 '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click ()

                elif cpic[1] == cpic[2]:
                    if cpic[1] and cpic[2] != 'Not':
                        site.switch_to.window (site.window_handles[0])
                        wait.until (ec.element_to_be_clickable (
                            (By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click ()
                        time.sleep (2)
                    else:
                        wait.until (ec.element_to_be_clickable ((By.XPATH,
                                                                 '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click ()

                elif cpic[0] == cpic[2]:
                    if cpic[1] and cpic[2] != 'Not':
                        wait.until (ec.element_to_be_clickable (
                            (By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click ()
                    else:
                        wait.until (ec.element_to_be_clickable ((By.XPATH,
                                                                 '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click ()
                else:

                    wait.until (ec.element_to_be_clickable ((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]'))).click ()
                    time.sleep(2)
            except Exception as a:
                print(a)
                print('Run again')


except :
    element=wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button[3]')))
    print(element)
    element.click()
    site.find_element_by_name('phone-number').click()
    time.sleep(4)
    site.find_element_by_name('phone-number').send_keys(phone)
    try:
        print("Try->try")
        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button'))).click()
        try:
            print ("Try->try->try")

            a1=hwait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/span/img')))
            print(a1.get_attribute('src'))

        except:
            print ("Try->try->except")
            wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/input[1]'))).click()
                # site.find_element_by_xpath ('/html/body/div[6]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/input[1]').send_keys(OTP)
    except:
        print('try->except')
        wait.until (ec.element_to_be_clickable ((By.XPATH,'/html/body/div[6]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/button'))).click ()
        print("Enter Your OTP Manually")
        ad=100
        for q in ad:
            try:
                a1 = hwait.until (ec.element_to_be_clickable ((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/span/img')))
                a2 = hwait.until (ec.element_to_be_clickable ((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/span/img')))
                a3 = hwait.until (ec.element_to_be_clickable ((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[2]/div/div/div[3]/span/img')))
                pic1=a1.get_attribute ('src')
                pic2=a2.get_attribute ('src')
                pic3=a3.get_attribute ('src')
                array=[pic1,pic2,pic3]
                print(array)
                print(pic2)
                print(pic3)
                cpic=[]
                for i in range (len (array)):

                    print (pic1)
                    site.execute_script ("window.open('" + str(array[i]) + "');")
                    time.sleep (5)
                    site.switch_to.window(site.window_handles[1])
                    time.sleep(3)
                    site.get_screenshot_as_file(folder+str(i)+".png")
                    time.sleep(5)
                    site.execute_script ("window.close();")
                    site.switch_to.window (site.window_handles[0])

                    try:
                        img = cv2.imread (folder+str(i)+".png")
                        pl.imshow (img[:, :, ::-1])
                        result = DeepFace.analyze (img, actions=['gender'])
                        print (result)
                        cpic.append(result['gender'])
                        os.remove(folder+str(i)+".png")

                    except:
                        cpic.append ('Not')
                        pass

                if cpic[0] == cpic[1]==cpic[2]:
                    if cpic[0] and cpic[1] and cpic[2] != 'Not':
                        site.switch_to.window (site.window_handles[0])
                        wait.until(ec.element_to_be_clickable((By.XPATH,'site.switch_to.window(site.window_handles[1])'))).click()
                        time.sleep(2)
                        #for send message hwait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/span[5]/a'))).click()
                        #
                    else:
                        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click()


                elif cpic[0] == cpic[1]:
                    if cpic[0] and cpic[1] != 'Not':
                        site.switch_to.window (site.window_handles[0])
                        wait.until(ec.element_to_be_clickable ((By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click()
                        time.sleep(2)
                    else:
                        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click()

                elif cpic[1]==cpic[2]:
                    if cpic[1] and cpic[2] != 'Not':
                        site.switch_to.window (site.window_handles[0])
                        wait.until(ec.element_to_be_clickable ((By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click()
                        time.sleep(2)
                    else:
                        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click()

                elif cpic[0] == cpic[2]:
                    if cpic[1] and cpic[2] != 'Not':
                        wait.until(ec.element_to_be_clickable ((By.XPATH, 'site.switch_to.window(site.window_handles[1])'))).click()
                    else:
                        wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]/div'))).click()
                else:
                    wait.until (ec.element_to_be_clickable ((By.XPATH, '/html/body/div[1]/main/div[1]/div[3]/div/div[1]/div/div/div/div/div[1]/div[2]/button[1]'))).click()
                    time.sleep(2)



            except Exception as a:
                print(a)
                print('Run again')
