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


# คลิกปุ่ม "สมัครสมาชิก" โดยใช้ XPath
register_button = driver.find_element(By.XPATH, "//span[text()='สมัครสมาชิก']")
register_button.click()


# ระบุ element ของ input field ด้วย XPath
id_card_input = driver.find_element(By.XPATH, "//input[@name='id_card']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
id_card_input.clear()

# กรอกเลขบัตรประชาชน
id_card_input.send_keys("1111111111111")
time.sleep(2)

# ระบุ element ของ <select> โดยใช้ XPath
prefix_select = driver.find_element(By.XPATH, "//select[@name='prefix_name']")

# ใช้ Select class จาก Selenium WebDriver เพื่อจัดการกับ <select>
prefix_dropdown = Select(prefix_select)

# เลือกคำนำหน้าที่คุณต้องการ (เช่น "นาย")
prefix_dropdown.select_by_value("นาย")
time.sleep(2)

# ระบุ element ของ input field ชื่อด้วย XPath
first_name_input = driver.find_element(By.XPATH, "//input[@name='first_name']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
first_name_input.clear()

# กรอกชื่อที่คุณต้องการ
first_name_input.send_keys("สมจิตร")
time.sleep(2)

# ระบุ element ของ input field นามสกุลด้วย XPath
last_name_input = driver.find_element(By.XPATH, "//input[@name='last_name']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
last_name_input.clear()

# กรอกนามสกุลที่คุณต้องการ
last_name_input.send_keys("จองจอหอ")
time.sleep(2)

# ระบุ element ของ dropdown เพศด้วย XPath
gender_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='gender']"))

# เลือกเพศที่คุณต้องการ โดยใช้ value หรือ text ของตัวเลือก
# เช่น เลือก "ชาย"
gender_dropdown.select_by_value("ชาย")
time.sleep(2)

# ระบุ element ของ input field วันที่ด้วย XPath
birthday_input = driver.find_element(By.XPATH, "//input[@name='birthday']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
birthday_input.clear()

# กรอกวันที่ที่คุณต้องการ (ในรูปแบบ 'yyyy-mm-dd')
birthday_input.send_keys("10-09-1969")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field น้ำหนักด้วย XPath
weight_input = driver.find_element(By.XPATH, "//input[@name='weight']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
weight_input.clear()

# กรอกน้ำหนักที่คุณต้องการ
weight_input.send_keys("69")  # เปลี่ยนเป็นน้ำหนักที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field ส่วนสูงด้วย XPath
height_input = driver.find_element(By.XPATH, "//input[@name='height']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
height_input.clear()

# กรอกส่วนสูงที่คุณต้องการ
height_input.send_keys("169")  # เปลี่ยนเป็นส่วนสูงที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field เบอร์โทรด้วย XPath
phone_input = driver.find_element(By.XPATH, "//input[@name='phoneNumber']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
phone_input.clear()

# กรอกเบอร์โทรที่คุณต้องการ
phone_input.send_keys("0812345678")  # เปลี่ยนเป็นเบอร์โทรที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field โรคประจำตัวด้วย XPath
congenital_disease_input = driver.find_element(By.XPATH, "//input[@name='congenital_disease']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
congenital_disease_input.clear()

# กรอกข้อมูลโรคประจำตัวที่คุณต้องการ
congenital_disease_input.send_keys("โรคหัวใจ")  # เปลี่ยนเป็นข้อมูลโรคประจำตัวที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field ประวัติแพ้ยาด้วย XPath
drugallergy_input = driver.find_element(By.XPATH, "//input[@name='drugallergy']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
drugallergy_input.clear()

# กรอกประวัติแพ้ยาที่คุณต้องการ
drugallergy_input.send_keys("พารา")  # เปลี่ยนเป็นประวัติแพ้ยาที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field รหัสผ่านด้วย XPath
password_input = driver.find_element(By.XPATH, "//input[@name='password']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
password_input.clear()

# กรอกรหัสผ่านที่คุณต้องการ
password_input.send_keys("111111")  # เปลี่ยนเป็นรหัสผ่านที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field ชื่อด้วย XPath
contact_first_name_input = driver.find_element(By.XPATH, "//input[@name='contact_first_name']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
contact_first_name_input.clear()

# กรอกชื่อที่คุณต้องการ
contact_first_name_input.send_keys("สมใจ")  # เปลี่ยนเป็นชื่อที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field นามสกุลด้วย XPath
contact_last_name_input = driver.find_element(By.XPATH, "//input[@name='contact_last_name']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
contact_last_name_input.clear()

# กรอกนามสกุลที่คุณต้องการ
contact_last_name_input.send_keys("จองจอหอ")  # เปลี่ยนเป็นนามสกุลที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ dropdown ความสัมพันธ์ด้วย XPath
relation_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='contact_relation_id']"))

# เลือกความสัมพันธ์ที่คุณต้องการ โดยใช้ value หรือ text ของตัวเลือก
# เช่น เลือก "บิดา"
relation_dropdown.select_by_value("ภรรยา")
# หรือ relation_dropdown.select_by_visible_text("บิดา")
time.sleep(2)

# ระบุ element ของ input field เบอร์โทรด้วย XPath
contact_phone_input = driver.find_element(By.XPATH, "//input[@name='contact_phoneNumber']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
contact_phone_input.clear()

# กรอกเบอร์โทรที่คุณต้องการ
contact_phone_input.send_keys("0812512323")  # เปลี่ยนเป็นเบอร์โทรที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field บ้านเลขที่ด้วย XPath
address_input = driver.find_element(By.XPATH, "//input[@name='address']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
address_input.clear()

# กรอกบ้านเลขที่ที่คุณต้องการ
address_input.send_keys("88")  # เปลี่ยนเป็นบ้านเลขที่ที่คุณต้องการ
time.sleep(2)

from selenium.webdriver.support.ui import Select

# ระบุ element ของ dropdown จังหวัดด้วย XPath
province_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='province']"))

# เลือกจังหวัดที่คุณต้องการ โดยใช้ value หรือ text ของตัวเลือก
# เช่น เลือก "กรุงเทพมหานคร"
province_dropdown.select_by_value("สุพรรณบุรี")
# หรือ province_dropdown.select_by_visible_text("สุพรรณบุรี")
time.sleep(2)

# ระบุ element ของ input field อำเภอด้วย XPath
district_input = driver.find_element(By.XPATH, "//input[@name='district']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
district_input.clear()

# กรอกข้อมูลอำเภอที่คุณต้องการ
district_input.send_keys("สองพี่น้อง")  # เปลี่ยนเป็นข้อมูลอำเภอที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field ตำบลด้วย XPath
subdistrict_input = driver.find_element(By.XPATH, "//input[@name='subdistrict']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
subdistrict_input.clear()

# กรอกข้อมูลตำบลที่คุณต้องการ
subdistrict_input.send_keys("เนินพระปรางค์")  # เปลี่ยนเป็นข้อมูลตำบลที่คุณต้องการ
time.sleep(2)

# ระบุ element ของ input field รหัสไปรษณีย์ด้วย XPath
postcode_input = driver.find_element(By.XPATH, "//input[@name='postcode']")

# ล้างข้อมูลที่อาจจะมีอยู่ใน input field ก่อนจะกรอก
postcode_input.clear()

# กรอกรหัสไปรษณีย์ที่คุณต้องการ
postcode_input.send_keys("72110")  # เปลี่ยนเป็นรหัสไปรษณีย์ที่คุณต้องการ
time.sleep(2)

# ระบุ element ของปุ่ม "บันทึก" ด้วย XPath
save_button = driver.find_element(By.XPATH, "//button[@class='btn btn-success mx-1' and contains(text(), 'บันทึก')]")

# คลิกปุ่ม "บันทึก"
save_button.click()
time.sleep(3)

from selenium.webdriver.common.by import By

# ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
confirm_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")

# คลิกปุ่ม "ตกลง"
confirm_button.click()
time.sleep(5)









