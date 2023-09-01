from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.dcinside.com/")
    best_postings = page.query_selector_all(".box.besttxt")
    print(best_postings[0].inner_text())
    best_postings[0].click()

    print("clicked !")

    page.wait_for_url("https://gall.dcinside.com/board/view/**")

    img = page.query_selector(".imgwrap.no1")

    img.screenshot(path="example.png")
    browser.close(),
