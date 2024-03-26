from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service("./chromedriver.exe"))
driver.maximize_window()
wait = WebDriverWait(driver, 60)

driver.get("http://192.168.2.92/")
wait.until(EC.url_to_be('http://192.168.2.92/'))

driver.find_element(By.ID, "username").send_keys("fsfsdf")
driver.find_element(By.ID, "pass").send_keys("12345678")
driver.find_element(By.CLASS_NAME, "button").click()
message = driver.find_element(By.ID, "warning").text

if "Kullanıcı adı veya şifre yanlış" in message:
    print("Kullanıcı adı veya şifre hatalı")

driver.get("http://192.168.2.92/")

driver.find_element(By.ID, "username").send_keys("aleynakepez")
driver.find_element(By.ID, "pass").send_keys("***")
driver.find_element(By.CLASS_NAME, "button").click()

print("kullanıcı adı ve şifre doğru")
# time.sleep(2)

# makine oee raporu
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
driver.find_element(By.CSS_SELECTOR, "#report > p > i").click()
driver.find_element(By.XPATH, '//a[@href="./oee-report.html"]').click()
time.sleep(1)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "multiselect-selected-text"))
)
button.click()
time.sleep(1)

def click_checkbox():
    checkbox_1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='form-check-input' and @value='1']"))
    )

    checkbox_1.click()

click_checkbox()
time.sleep(1)
print("makine-100 seçildi.")

button = driver.find_element(By.ID, "SearchButton").click()

driver.execute_script("window.scrollTo(0, 1000)")

# üretim raporu
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#report > p > i").click()
time.sleep(1)

driver.find_element(By.XPATH, '//a[@href="./production-report.html"]').click()
time.sleep(1)

select = driver.find_element(By.CLASS_NAME, "multiselect-selected-text").click()


def select_all_checkboxes():
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        if not checkbox.is_selected():  # Zaten işaretli değilse işaretle
            checkbox.click()

select_all_checkboxes()

icon_button = driver.find_element(By.CLASS_NAME, "fa-caret-down").click()

driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[5]").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[5]").click()

driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/button[2]").click()
driver.find_element(By.ID, "SearchButton").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(1)

# kesici uç raporu
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#report > p > i").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="./cuttingtool-report.html"]').click()
time.sleep(1)

# kestirimci bakım raporu

driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#report > p > i").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="./predictive-maintenance-report.html"]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//button[text()="Detay"]').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 650)")
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class="btn btn-secondary buttons-copy buttons-html5"]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//button[@class="btn btn-secondary buttons-csv buttons-html5"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class="btn btn-secondary buttons-excel buttons-html5"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[@class="btn btn-secondary buttons-pdf buttons-html5"]').click()
time.sleep(1)

# driver.find_element(By.XPATH, '//button[@class="btn btn-secondary buttons-print"]').click()
# time.sleep(2)

driver.find_element(By.XPATH,
                    '//button[@class="btn btn-secondary buttons-collection dropdown-toggle buttons-colvis"]').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,
                    'a.dt-button.dropdown-item.buttons-columnVisibility.active[data-cv-idx="0"]').click()
driver.find_element(By.CSS_SELECTOR,
                    'a.dt-button.dropdown-item.buttons-columnVisibility.active[data-cv-idx="1"]').click()
driver.find_element(By.CSS_SELECTOR,
                    'a.dt-button.dropdown-item.buttons-columnVisibility.active[data-cv-idx="2"]').click()

# makine duruş raporu
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#report > p > i").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="./breakdown-report.html"]').click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, 'multiselect-selected-text').click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@class='form-check-input' and @value='1']").click()
time.sleep(1)
driver.find_element(By.ID, "searchIcon").click()
time.sleep(1)

svg_selector = ".apexcharts-zoomin-icon"
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, svg_selector))
)
action = ActionChains(driver)
action.click(element).perform()
time.sleep(1)

sg_selector = ".apexcharts-zoomout-icon"
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, sg_selector))
)
action = ActionChains(driver)
action.click(element).perform()

driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)
# driver.find_element(By.ID, "example1_next").click()
# time.sleep(1)

# operatör raporu
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#report > p > i").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="./operator-report.html"]').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'multiselect-selected-text').click()
time.sleep(1)

checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[@class='form-check-input' and @value='ea9e713b-a8d8-4aa9-b61f-2c3c7691356a']"))
)
checkbox.click()
time.sleep(2)
driver.find_element(By.ID, "SearchButton").click()
time.sleep(1)

# veri sorgulama> veri görselleştirme
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)
driver.find_element(By.ID, "search").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="./historical-monitoring.html"]').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "multiselect-selected-text").click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "multiselect-search").send_keys("MKN-12")
driver.find_element(By.XPATH, "//input[@class='form-check-input' and @value='123']").click()
driver.find_element(By.ID, "SearchButton").click()
time.sleep(1)

# makine yeterlilik analizi
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
time.sleep(1)
driver.find_element(By.XPATH, '//a[@href="./machine-capability.html"]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@value='Current']").click()
driver.find_element(By.ID, "allMachinesSelect").click()
driver.find_element(By.ID, "6").click()
driver.find_element(By.ID, "allOperators").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[text()='Ali Can Güneş']").click()

driver.find_element(By.ID, "SearchButton").click()
time.sleep(1)
driver.find_element(By.ID, "upperToleranceInput").send_keys("60,30")
time.sleep(1)
driver.find_element(By.ID, "lowerToleranceInput").send_keys("59.70")
time.sleep(1)

lnn = driver.find_element(By.ID, "input3")
driver.execute_script("arguments[0].value = '';", lnn)
new_value = "60"
lnn.send_keys(new_value)
time.sleep(1)

xxn = driver.find_element(By.ID, "input6")
driver.execute_script("arguments[0].value = '';", xxn)
new_value = "60,07"
xxn.send_keys(new_value)
time.sleep(1)

driver.find_element(By.ID, "olcumDegerleriKaydetBtn").click()
driver.execute_script("window.scrollTo(0, 100)")
time.sleep(1)

input_element = driver.find_element(By.ID, "acceptableMinNumber")
driver.execute_script("arguments[0].value = '';", input_element)
driver.find_element(By.ID, "acceptableMinNumber").send_keys("16")
time.sleep(1)
driver.find_element(By.ID, "saveMachineCapabilityBtn").click()
time.sleep(1)
driver.find_element(By.ID, "saveData").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
time.sleep(1)

driver.find_element(By. XPATH, "/html/body/div[2]/div/div[6]/button[1]").click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, -100)")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@value='Current']").click()
driver.find_element(By.ID, "SearchButton").click()
time.sleep(1)
driver.find_element(By.ID, "olcumDegerleriKaydetBtn").click()
time.sleep(1)

input_element = driver.find_element(By.ID, "acceptableMinNumber")
driver.execute_script("arguments[0].value = '';", input_element)
driver.find_element(By.ID, "acceptableMinNumber").send_keys("11")
driver.find_element(By.ID, "saveMachineCapabilityBtn").click()
driver.find_element(By.ID, "saveData").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
time.sleep(1)
driver.find_element(By. XPATH, "/html/body/div[2]/div/div[6]/button[1]").click()
time.sleep(1)

#stok yönetim işlemleri
#stoktakiler
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
driver.find_element(By.ID, "takimOffsetIslemleri").click()
driver.find_element(By.XPATH, '//a[@href="./stocks.html"]').click()

driver.find_element(By.ID, "ucAdiSelect").click()
time.sleep(5)
driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[1]/div/div/div[2]/table/tbody/tr[2]/td/div[1]/select/option[2]").click()
driver.find_element(By.ID, "cekmeceAdiSelect").click()
driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[1]/div/div/div[2]/table/tbody/tr[2]/td/div[2]/select/option[7]").click()
driver.find_element(By.ID, "stocksSearchBtn").click()
time.sleep(5)

driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[2]/div/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[9]/button[1]").click()
driver.find_element(By.ID, "stocksMachines").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[2]/div[1]/select/option[2]").click()
time.sleep(5)
driver.find_element(By.ID, "toolsWithMachines").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[2]/div[2]/select/option[2]").click()
time.sleep(5)
driver.find_element(By.ID, "makineyeAtaBtn").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
time.sleep(3)


driver.find_element(By.ID, "ucAdiSelect").click()
driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[1]/div/div/div[2]/table/tbody/tr[2]/td/div[1]/select/option[3]").click()
driver.find_element(By.ID, "cekmeceAdiSelect").click()
driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[1]/div/div/div[2]/table/tbody/tr[2]/td/div[2]/select/option[8]").click()
driver.find_element(By.ID, "stocksSearchBtn").click()
time.sleep(1)

driver.find_element(By.XPATH, "/html/body/div/div[3]/section[1]/div/div/div[2]/table/tbody/tr[3]/td/div[2]/button").click()
driver.find_element(By.ID, "barkodaGoreAratBtn").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[1]/button/span").click()
time.sleep(1)

driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[2]/div/div/div/div/div[2]/div/div[2]/div/table/tbody/tr/td[9]/button[1]").click()
time.sleep(3)
driver.find_element(By.ID, "stocksMachines").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[2]/div[1]/select/option[2]").click()
driver.find_element(By.ID, "toolsWithMachines").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div[2]/div[2]/select/option[2]").click()
driver.find_element(By.ID, "makineyeAtaBtn").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[6]/button[1]").click()
time.sleep(3)

# pot bilgisi
driver.find_element(By.CSS_SELECTOR, "i.fas.fa-bars").click()
driver.find_element(By.ID, "takimOffsetIslemleri").click()
driver.find_element(By.XPATH, '//a[@href="./pots-information.html"]').click()
driver.find_element(By.ID, "potMachinesSelect").click()
driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[1]/div/div/div[2]/table/tbody/tr[2]/td/div[1]/div/select/option[2]").click()
driver.find_element(By.ID, "searchBtn").click()
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element(By.XPATH,
                    "/html/body/div/div[3]/section[2]/div/div/div/div/div[2]/div/div[3]/div[2]/div/ul/li[8]/a").click()

