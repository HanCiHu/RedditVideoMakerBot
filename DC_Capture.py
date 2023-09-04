from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    browser.new_context(record_video_dir="./")

    page.goto("https://www.dcinside.com/")

    selector = ".box.besttxt"
    best_postings = page.query_selector_all(selector)
    print(best_postings[0].inner_text())

    page.eval_on_selector(".tab_content", "element => element.scrollIntoView()")
    print("scrolling...")
    page.wait_for_timeout(5000)
    best_postings[0].click()

    print("clicked !")

    page.wait_for_url("https://gall.dcinside.com/board/view/**")

    img = page.query_selector(".imgwrap.no1")

    dimensions = page.evaluate(
        "element => {const { width, height } = element.getBoundingClientRect();return { width, height };}",
        img,
    )
    width = dimensions["width"]
    height = dimensions["height"]

    print(width, height)

    img.screenshot(path="example.png")
    browser.close(),
