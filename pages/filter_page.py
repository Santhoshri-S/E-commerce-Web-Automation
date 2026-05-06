import logging
import allure
from pages.base_page import BasePage
class Filterspage(BasePage):
    @allure.step("Sort products: High to Low")
    def sortbyprice(self):
        # click sort by drop down
        self.page.click("#a-autoid-0")
        self.screenshot("Sort by Dropdown")
        # select "High to Low"     
        self.page.click('#s-result-sort-select_2')
        logging.info("Product sorted sucessfully")

    @allure.step("Get price")
    def get_prices(self):
        prices = self.page.locator("//span[@class='a-price-whole']")
        price_list = []
        for i in range(min(prices.count(), 10)):
            price = prices.nth(i).inner_text().replace(",", "")
            if price.isdigit():
                price_list.append(int(price))
        return price_list
    
    @allure.step("Apply ratings filter")
    def ratings(self):
        rating = self.page.locator("#filter-p_72")
        rating.scroll_into_view_if_needed()
        rating.click()
        logging.info("ratings fetched")

    @allure.step("Out of Stock")
    def outofstock(self):
    # include out of stock
        outStock=self.page.locator("xpath=//span[text()='Include Out of Stock']")
        outStock.scroll_into_view_if_needed()
        outStock.click()
        logging.info("Included out of stock")

    @allure.step("Discounts")
    def alldiscount(self):
        # All Discount
        if self.page.locator("xpath=//span[text()='All Discounts']").count()>0:
            discount=self.page.locator("xpath=//span[text()='All Discounts']")
            discount.scroll_into_view_if_needed()
            discount.click()
            logging.info("Include All Discount")

        if self.page.locator("xpath=//span[contains(text(),'Today')]").count()>0:
            today=self.page.locator("xpath=//span[contains(text(),'Today')]")
            today.scroll_into_view_if_needed()
            today.click()
            logging.info("Include Today's Deals")
        else:
            logging.info("No Today's Deals") 

    @allure.step("pay on delivery")
    def payondelivery(self):
        # Eligible for Pay On Delivery
        pod =self.page.locator("xpath=//span[text()='Eligible for Pay On Delivery']")
        pod .scroll_into_view_if_needed()
        pod .click()
        logging.info("Included Pay on Delivery")
        self.page.wait_for_timeout(10000)
        self.screenshot("Applied more filters",full_page=True)
        
    @allure.step("print sorted elements")
    def print_sorted_elements(self):
        print("Details of Laptop:")
        # print sorted title and price
        self.page.wait_for_selector("xpath=//div[@data-cy='title-recipe']//h2//span")
        title= self.page.locator("xpath=//div[@data-cy='title-recipe']//h2//span")
        prices = self.page.locator("xpath=//span[@class='a-price']//span[@class='a-offscreen']")
        
        count = min(title.count(),prices.count())
        for i in range(count):
            print(title.nth(i).inner_text())
            print(prices.nth(i).inner_text())
            print("\n")

    @allure.step("Pagigation")
    def pagigation(self):
        #next page navigation
        navi=self.page.locator("a.s-pagination-next")
        navi.scroll_into_view_if_needed()
        navi.click()
        
        self.page.wait_for_timeout(10000)
        self.screenshot("Next page Items", full_page=True)
        logging.info("next page navigated sucessfully")

    