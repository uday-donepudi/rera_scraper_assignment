import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless") 

path = r"C:\path\to\chromedriver.exe" # Update this path to your chromedriver location
service = Service(path)

driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10) 

url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(url)  
all_projects = []
max_projects = 6 # Number of projects to scrape

for i in range(max_projects):  

    # Find project buttons fresh on every iteration
    projects = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".btn.btn-primary")))[:max_projects]
    
    driver.execute_script("arguments[0].scrollIntoView(true);", projects[i])
    driver.execute_script("arguments[0].click();", projects[i])
    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(), 'Project Name')]/following-sibling::strong")))

    try:
        project_name = driver.find_element(By.XPATH, "//label[contains(text(), 'Project Name')]/following-sibling::strong").text
        RERA_Regd_No = driver.find_element(By.XPATH, "//label[contains(text(), 'RERA Regd. No.')]/following-sibling::strong").text

        # Navigate to Promoter Details tab
        driver.find_element(By.XPATH, "//a[contains(text(), 'Promoter Details')]").click()
        time.sleep(0.5)  # Wait for the tab to load

        promoter_name = driver.find_element(By.XPATH, "//label[contains(text(), 'Company Name') or contains(text(), 'Propietory Name')]/following-sibling::strong").text
        address = driver.find_element(By.XPATH, "//label[contains(text(), 'Registered Office Address') or contains(text(), 'Current Residence Address')]/following-sibling::strong").text
        gst_no = driver.find_element(By.XPATH, "//label[contains(text(), 'GST No.')]/following-sibling::strong").text

        project_info = {
            "RERA Regd. No.": RERA_Regd_No,
            "Project Name": project_name,
            "Promoter Name": promoter_name,
            "Address": address,
            "GST No.": gst_no
        }
        all_projects.append(project_info)
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-warning.btn-sm").click()  # Close the modal
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal.fade.show")))

    except Exception as e:
        print(f"Error extracting project {i+1}: {e}")


print("length of all projects:", len(all_projects))
# Print all data in JSON format
print("All Projects:")
print(json.dumps(all_projects, indent=4))

# Quit driver
driver.quit()
