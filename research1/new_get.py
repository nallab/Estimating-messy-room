import time
import urllib.request
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import ssl
options = webdriver.ChromeOptions()

options.add_argument('--headless')
driver = webdriver.Chrome(options = options)
#driver.get('https://www.google.com/')
driver.get("https://www.google.co.jp/imghp?hl=ja&tab=ri&authuser=0&ogbl")
#print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('部屋')
#search_box.send_keys("房间")
#search_box.send_keys("messy room")
#search_box.send_keys("غرفة فوضوية")
#search_box.send_keys("अस्त - व्यस्त कमरा")
#search_box.send_keys("chambre mal rangée")
#search_box.send_keys("cuarto desordenado")
#search_box.send_keys('散らかった部屋')
#search_box.send_keys('杂乱的房间')
search_box.submit()

img = driver.find_element_by_id("islrg")
img2 = img.find_elements_by_tag_name("a")
#print(len(img2))
img3 = [im.get_attribute("href") for im in img2]
#print(img3)
img_num = 1
for i, im in enumerate(img3):
    time.sleep(5)
    print('{0}'.format(i))
    print(im)
    #temp = im.get_attribute("href")
    if im == None:
        print('sorry this is not url... next')
    else:
        print("url get!!")
        try:
            driver.get(str(im))
            time.sleep(5)
            #画像を取得する関数を実装する
            img_array = driver.find_elements_by_tag_name("img")
            #img_array = driver.find_element_by_class_name("imgArea")
            #print(len(img_array))
            for l, im_tag in enumerate(img_array):
                time.sleep(3)
                src = im_tag.get_attribute("src")
                print(src)
                #if src.startswith('https://www.') == True or 'png' in src: 
                if ('jpg' in src) == False:
                    print('this img is not room')
                    pass
                else:
                    time.sleep(5)
                    #os.makedirs('download/'.format(i), exist_ok = True)
                    #urllib.request.urlretrieve(src, 'download/images{0}/{1}.png'.format(i,l+1))
                    #urllib.request.urlretrieve(src, 'download/all/{0}.png'.format(img_num))
                    #urllib.request.urlretrieve(src, 'download/all_new2/{0}.png'.format(img_num))
                    urllib.request.urlretrieve(src, 'download/all_messy/{0}.png'.format(img_num))
                    #urllib.request.urlretrieve(src, 'download/all_messy_new/{0}.png'.format(img_num))
                    time.sleep(5)
                    img_num += 1
                if l == 5:
                    break
                
            driver.back()
        except AttributeError:
            print("fuck")
            time.sleep(5)
            driver.quit()
        except urllib.error.HTTPError:
            print("this page is very dangerous ...skip!!")
            time.sleep(5)
            driver.back()
            #driver.quit()
        except ssl.CertificateError:
            print("this page occured ssl problem very ...skip!!")
            time.sleep(5)
            driver.back()
        except TypeError:
            print("this page is Nonetype ...skip!!")
    #print(im.get_attribute("src"))
    
    if i == 50:
        break

driver.quit()