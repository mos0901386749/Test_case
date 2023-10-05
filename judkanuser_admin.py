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

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("8888888888888")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()
time.sleep(5)

# ค้นหา <div> โดยใช้ XPath
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "จัดการ")]')

# คลิกที่ <div>
div_element.click()
time.sleep(5)

# ค้นหา <div> โดยใช้ข้อความ "รายชื่อผู้ใช้" ในหน้าเว็บ
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "รายชื่อผู้ใช้")]')
div_element.click()
time.sleep(5)

# # ค้นหาปุ่มโดยใช้ XPath
# pen_button = driver.find_element_by_xpath('//button[@class="btn btn-warning text-white mx-1 mt-1"]')

# # คลิกปุ่ม
# pen_button.click()
# time.sleep(3)

# # ค้นหา input โดยใช้ attribute 'name'
# input_element = driver.find_element_by_name('first_name')

# # ลบข้อมูลที่อยู่ใน input ก่อนหน้า (ถ้ามี)
# input_element.clear()

# # ใส่ข้อมูลที่คุณต้องการ
# input_element.send_keys('ขวัญธิชา')
# time.sleep(3)

# # ค้นหาปุ่ม "บันทึก" โดยใช้ attribute 'class'
# save_button = driver.find_element_by_class_name('btn-success')

# # คลิกปุ่ม "บันทึก"
# save_button.click()
# time.sleep(3)

# # ค้นหาปุ่ม "ตกลง" โดยใช้ attribute 'class'
# confirm_button = driver.find_element_by_class_name('swal2-confirm')

# # คลิกปุ่ม "ตกลง"
# confirm_button.click()
# time.sleep(3)