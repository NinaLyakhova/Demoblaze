from playwright.sync_api import sync_playwright


def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        assert page.inner_text('h1') == 'Playwright enables reliable end-to-end testing for modern web apps.'
        browser.close()