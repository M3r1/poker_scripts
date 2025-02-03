from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

### Actions
CALL = "CALL"
RAISE = "RAISE"

### Positions
NAN = "NaN"
BTN = "BTN"
LJ = "LJ"
HJ = "HJ"
BB = "BB"
SB = "SB"

### SCENARIOS
VS_RAISE = "vs raise"
VS_3BET = "vs 3bet"
VS_4BET = "vs 4bet"
OPEN = "Open"

#######################
#######################
#######################
SCENARIO = VS_RAISE
HERO = BB
VILLAIN = HJ
ACTION = CALL
#######################
#######################
#######################

def get_call_or_raise_percentage_text(call_or_raise):
    if call_or_raise == CALL:
        return "--call-percentage"
    else:
        return "--raise-percentage"

def get_all_elements(selenium_driver, find_elements_method, elements_identifier):
    return selenium_driver.find_elements(find_elements_method, elements_identifier)

def get_elements_by_text(all_elements, element_text):
    return [btn for btn in all_elements if btn.text==element_text]

def get_combo_percentage(call_or_raise, combo_style, is_fraction):
    call_or_raise = get_call_or_raise_percentage_text(call_or_raise)

    all_attributes = combo_style.split(";")
    call_or_raise_percentage = next(attribute for attribute in all_attributes if call_or_raise in attribute)
    percentage = call_or_raise_percentage.split(":")[1].strip()

    if is_fraction:
        fraction = next(attribute for attribute in all_attributes if "--action-height" in attribute)
        fraction = fraction.split(":")[1].strip()[0:-1]

        if fraction == "NaN":
            fraction = "0"
        
        percentage = float(percentage) * (float(fraction) / 100.0)
    
    return round((float(percentage) * 100))

def get_flopzilla_range_string(all_combo_elements, is_fraction):
    all_combos_filtered = [combo for combo in all_combo_elements if combo.text != "BUILT-IN" and combo.text != "YOUR RANGES" and combo.text != ""] 

    flopzilla_range_string = ""
    for combo in all_combos_filtered:
        percentage = get_combo_percentage(ACTION, combo.get_attribute("style"), is_fraction)
        if percentage != 0:
            flopzilla_range_string = flopzilla_range_string + f"[{percentage}]{combo.text}[/{percentage}]" + ","

    return flopzilla_range_string[:-1]

def get_open_or_vs_raise_flopzilla_range_string(all_landing_page_game_elements, driver, scenario):
    get_elements_by_text(all_landing_page_game_elements, scenario)[0].click()

    all_scenarios_page_elements = get_all_elements(driver, "class name", "ion-color")
    get_elements_by_text(all_scenarios_page_elements, HERO)[0].click()

    if SCENARIO != OPEN:
        all_scenarios_hero_page_elements = get_all_elements(driver, "class name", "ion-color")

        get_elements_by_text(all_scenarios_hero_page_elements, VILLAIN)[-1].click()

    all_combos = get_all_elements(driver, "class name", "ion-activatable")
    
    return get_flopzilla_range_string(all_combos, scenario == VS_3BET or scenario == VS_4BET)


driver = webdriver.Chrome(executable_path='C:/Users/gilim/.wdm/drivers/chromedriver/win64/131.0.6778.264/chromedriver-win32/chromedriver.exe')


driver.get("https://app.pokertrainer.se/rangeeditor")
driver.maximize_window()

all_landing_page_elements = get_all_elements(driver, "class name", "ion-color")
get_elements_by_text(all_landing_page_elements, "Cash")[0].click()
get_elements_by_text(all_landing_page_elements, "GTO")[0].click()

all_landing_page_game_elements = get_all_elements(driver, "class name", "ion-color")
get_elements_by_text(all_landing_page_game_elements, "6")[0].click()
get_elements_by_text(all_landing_page_game_elements, "100")[0].click()

print(get_open_or_vs_raise_flopzilla_range_string(all_landing_page_game_elements, driver, SCENARIO))



driver.quit()
