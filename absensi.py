import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException        


nim = '1631710037' 
password = '19980628MU'
#INITIAL USER
msg = "Anda Sudah Absen Hari Ini"

driver = webdriver.Chrome('./chromedriver')
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    
    
driver.get('http://siakad.polinema.ac.id/');
time.sleep(3)

Eusername = driver.find_element_by_name('username')
Eusername.send_keys(nim)
Epassword = driver.find_element_by_name('password')
Epassword.send_keys(password)
Epassword.submit()
time.sleep(2)

#isi Absen
def isi_absen():
    driver.get('http://siakad.polinema.ac.id/mahasiswa/tr_absensi/add')
    time.sleep(3)
    
    for checkbox in driver.find_elements_by_xpath("//input[@value='NK20032700002']"):
        checkbox.click()
        time.sleep(1)
    driver.find_element_by_name('btn_submit').click()

# CHECK ABSEN 
def check_absen():
    driver.get('http://siakad.polinema.ac.id/mahasiswa/tr_absensi/index')
    check = check_exists_by_xpath("//a[@href='http://siakad.polinema.ac.id/mahasiswa/tr_absensi/add']")
    if check :
        isi_absen()
        return False
    else :
        driver.quit()
        print msg
        return True
        
#Running Until Finished
Finished = False    
while not Finished :
    Finished = check_absen()
