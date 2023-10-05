from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ระบุพาธของ ChromeDriver 
chrome_driver_path = "C:/Mos/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")
time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("0608254406082")
password_input.send_keys("06082544")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

Home_button = driver.find_element(By.ID, 'Home-medical')

# คลิกที่ปุ่ม
Home_button.click()
time.sleep(5)

img_element = driver.find_element(By.ID, 'HospitalLogo.17')  # หรือใช้ By.CLASS_NAME หรือวิธีการค้นหาอื่น ๆ

img_element.click()
time.sleep(3)

calendar_button = driver.find_element(By.ID, 'Home-calendarDays')

# คลิกที่ปุ่ม
calendar_button.click()
time.sleep(3)

img_element = driver.find_element(By.ID, 'HospitalLogo.17')  # หรือใช้ By.CLASS_NAME หรือวิธีการค้นหาอื่น ๆ

img_element.click()
time.sleep(3)

queue_button = driver.find_element(By.ID, 'Home-Queue')

queue_button = driver.find_element(By.CLASS_NAME, 'btn-close')

# คลิกที่ปุ่ม
queue_button.click()
time.sleep(3)


img_element = driver.find_element(By.ID, 'HospitalLogo.17')  # หรือใช้ By.CLASS_NAME หรือวิธีการค้นหาอื่น ๆ

img_element.click()
time.sleep(3)

iqueue_button = driver.find_element(By.ID, 'Home-iconQ')

# คลิกที่ปุ่ม
iqueue_button.click()
time.sleep(3)

img_element = driver.find_element(By.ID, 'HospitalLogo.17')  # หรือใช้ By.CLASS_NAME หรือวิธีการค้นหาอื่น ๆ

img_element.click()
time.sleep(3)









