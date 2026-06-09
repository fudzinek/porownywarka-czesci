from playwright.sync_api import sync_playwright

LOGIN_URL = "https://pl.e-cat.intercars.eu"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="ic_session.json" if False else None)
    page = context.new_page()

    page.goto(LOGIN_URL)

    print("Zaloguj się ręcznie do Inter Cars.")
    print("Po zalogowaniu naciśnij ENTER w terminalu.")
    input()

    context.storage_state(path="ic_session.json")
    print("Sesja zapisana do pliku ic_session.json")

    browser.close()
