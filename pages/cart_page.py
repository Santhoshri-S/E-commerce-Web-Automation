import logging
import allure
from pages.base_page import BasePage
class CartPage(BasePage):
    @allure.step("Add to Cart")
    def add_to_cart(self):
        if self.page.locator("text=cannot be delivered").count() > 0:
            logging.info(" Product cannot be delivered to this address")
            return False
        
        if self.page.locator("#add-to-cart-button:visible").count() > 0:
            btn=self.page.locator("#add-to-cart-button:visible").first
            btn.scroll_into_view_if_needed()
            btn.click()
            logging.info("Added using direct Add to Cart")
        
        # buying options
        elif self.locator("#buybox-see-all-buying-choices").count() > 0:
            self.page.locator("#buybox-see-all-buying-choices").click()
            self.page.wait_for_selector("input[name='submit.addToCart']")
            self.page.locator("input[name='submit.addToCart']").first.click()
            logging.info("Added using buying options")

        # currently unavailable
        elif self.page.locator("//text()='Currently unavailable'").count() > 0:
            logging.info("Product is out of stock")
            return
    
        else:
            logging.info("No add to cart option found")
    @allure.step("Go to Cart")
    def go_to_cart(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_selector("#nav-cart")
        self.page.locator("#nav-cart").click()
        self.page.wait_for_load_state("domcontentloaded")
        self.screenshot("Cart page")
        logging.info("Cart page opened")

    @allure.step("Increase product quantity")
    def increase(self,times):
        if self.page.locator("text=Only 1 left in stock.").count()>0:
            return False
        
        self.page.locator("xpath=//button//span[@class='a-icon a-icon-small-add']")
        for i in range(times):
            self.page.click("xpath=//button//span[@class='a-icon a-icon-small-add']")
        logging.info(f"quantity increased to {times} more") 
        self.page.wait_for_timeout(10000) 
        self.screenshot("Incremented product quantity", full_page=False)

    @allure.step("Decrease Product Quantity")
    def decrement(self,times):
        if self.page.locator("text=Only 1 left in stock.").count()>0:
            logging.info("Only 1 in stock")
            return False
        
        dec=self.page.locator("xpath=//button//span[@class='a-icon a-icon-small-remove']")
        for i in range(times):
            self.page.click("xpath=//button//span[@class='a-icon a-icon-small-remove']")
        logging.info(f"quantity decreased {times}")  
        self.page.wait_for_timeout(1000) 
        self.screenshot("Decremented product quantity", full_page=False)

    @allure.step("Proceed to Buy")
    def proceed_to_buy(self):

        self.page.wait_for_selector("input[name='proceedToRetailCheckout']")
        btn = self.page.locator("input[name='proceedToRetailCheckout']:visible").first
        btn.scroll_into_view_if_needed()
        btn.click()
        self.page.wait_for_url("**/ap/signin**")
        self.page.wait_for_load_state("domcontentloaded")
        self.screenshot("Proceed to checkout", full_page=False)
        logging.info("Proceeded to checkout")




# pytest -n auto --alluredir=allure-results
# allure generate allure-results --clean
# cd allure-report
# python3 -m http.server 8081