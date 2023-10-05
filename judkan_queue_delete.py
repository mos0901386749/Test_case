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
id_input.send_keys("7777777777777")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()
time.sleep(5)

# ค้นหา <div> โดยใช้ XPath
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "จัดการจองคิว")]')

# คลิกที่ <div>
div_element.click()
time.sleep(5)

# ค้นหา <input> ด้วย name attribute และคลิกที่มัน
birthday_input = driver.find_element(By.XPATH, "//input[@name='queue_date']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
birthday_input.clear()

# กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
birthday_input.send_keys("09-21-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
time.sleep(5)

# ค้นหาปุ่มด้วย ID
cancel_button = driver.find_element(By.ID, 'buttoCancels')

# คลิกที่ปุ่ม
cancel_button.click()
time.sleep(3)

# ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
# รอให้ปุ่มปรากฏ
wait = WebDriverWait(driver, 5)
confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ใช่, ลบคิว']")))

# คลิกที่ปุ่ม
confirm_button.click()
time.sleep(5)
