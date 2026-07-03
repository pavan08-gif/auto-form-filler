    element_name.click()
    element_name.send_keys(row[0])
    element_age.click()
    element_age.send_keys(str(row[1]))
    element_email.click()
    element_email.send_keys(row[2])
    element_submit = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[aria-label = "Submit"]')))
    element_submit.click()
    
driver.quit()

