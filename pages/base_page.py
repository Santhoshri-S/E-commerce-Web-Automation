import allure
class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, selector):
        element = self.page.locator(selector)
        element.wait_for(state="visible")
        element.click()

    def fill(self, selector, value):
        element = self.page.locator(selector)
        element.wait_for(state="visible")
        element.fill(value)

    def screenshot(self, name, full_page=False):
        path=f"screenshots/{name}.png"
        self.page.screenshot(path=path,full_page=full_page,animations="disabled")
        allure.attach.file(
            path,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def wait_for_page_load(self):
        self.page.wait_for_load_state("domcontentloaded")
