import logging
import allure
from pages.base_page import BasePage
class SearchBar(BasePage):
    @allure.step("Search product: {product}")
    def search_bar(self,product):
        self.page.fill("#twotabsearchtextbox", product)
        self.screenshot("Search bar")
        self.page.click("#nav-search-submit-button")
        logging.info(f"Searching element is sucessfull:{product}")
        allure.attach(
            f"Searched for {product}",
            name="Search Log",
            attachment_type=allure.attachment_type.TEXT
        )
        
        self.wait_for_page_load()


