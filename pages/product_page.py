import logging
import random
import allure
from pages.base_page import BasePage
class ProductPage(BasePage):
    @allure.step("Add product to cart")
    def open_product(self):
        self.page.wait_for_selector("//div[@data-cy='title-recipe']//h2//span")
        with self.page.expect_popup() as popup:
            self.page.locator("//div[@data-cy='title-recipe']//h2//span").first.click()
        product_page = popup.value
        product_page.wait_for_load_state("domcontentloaded")
        self.screenshot("Product page", full_page=True)
        logging.info("Product opend sucessfully")
        return product_page
    
    @allure.step("Random product selector")
    def random_product_selector(self):
        self.page.wait_for_selector("//a//h2//span", timeout=60000)
        products = self.page.locator("//a//h2//span")
        count = products.count()
        if count == 0:
            print("Product not found")
            return None   
        index = random.randint(0, min(count - 1, 10))
        product = products.nth(index)   
        product.scroll_into_view_if_needed()
        with self.page.expect_popup() as popup:
            product.click()
        product_page = popup.value
        product_page.wait_for_load_state("domcontentloaded")
        self.screenshot(" Random Product page", full_page=True)
        print(f"Opened random product index: {index}")
        return product_page
    