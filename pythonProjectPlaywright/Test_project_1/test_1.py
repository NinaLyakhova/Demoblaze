from playwright.sync_api import sync_playwright


def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()


def test_bank_XYZ():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        assert page.inner_text('title') == 'XYZ Bank'
        page.click('div.center:nth-child(1) > button:nth-child(1)')
        page.screenshot(path='screen\example.png')
        browser.close()
