import time

_PYAUTOGUI_IMPORT_ERROR = None
try:
    from pyautogui import typewrite
except Exception as exc:  # pragma: no cover - environment specific
    typewrite = None
    _PYAUTOGUI_IMPORT_ERROR = exc


def TypeRacerFill():
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
    except ImportError as exc:  # pragma: no cover - environment specific
        raise ImportError(
            "selenium is required to run this script. Install it with 'pip install selenium'."
        ) from exc

    if typewrite is None:
        raise ImportError(
            "pyautogui is required to run this script. Install it with 'pip install pyautogui'."
        ) from _PYAUTOGUI_IMPORT_ERROR

    baselink = "https://play.typeracer.com/"
    driver = webdriver.Chrome()
    driver.get(baselink)
    driver.implicitly_wait(5)
    driver.find_element(By.LINK_TEXT, "Practice").click()
    print("[2] Retrieving text ...")
    span = driver.find_elements(By.XPATH, "//span[@unselectable='on']")
    if len(span) == 2:
        full_text = span[0].text + " " + span[1].text
    else:
        full_text = span[0].text + span[1].text + " " + span[2].text
    print(full_text)
    for i in range(4, 0, -1):
        print(f"[3] Waiting for countdown ...{i}")
        time.sleep(1)

    typewrite(full_text, interval=0.05)
    driver.quit()


if __name__ == "__main__":
    TypeRacerFill()
