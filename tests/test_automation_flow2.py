import pytest
import allure
from pages.search_bar import SearchBar
from pages.filter_page import Filterspage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@allure.feature("Amazon Automation 1")
@allure.story("End-to-End Flow")
@pytest.mark.parametrize("product_name", ["laptop", "Mobile", "HeadPhones"])
def test_automation(page, product_name):

    with allure.step("Search Product"):
        searchs = SearchBar(page)
        searchs.search_bar(product_name)

    with allure.step("Apply filter"):
        filters = Filterspage(page)
        filters.sortbyprice()
        filters.ratings()
        filters.outofstock()
        filters.alldiscount()
        filters.payondelivery()
        filters.print_sorted_elements()

    with allure.step("Product"):
        product_obj = ProductPage(page)
        product_page = product_obj.random_product_selector()

    
        if product_page is None:
            pytest.skip("No product found")

    with allure.step("cart Action"):
        cart = CartPage(product_page)

        cart.add_to_cart()
        cart.go_to_cart()
        assert "cart" in product_page.url.lower()
        cart.proceed_to_buy()
        assert "signin" in product_page.url.lower()

    print("End-to-End flow completed")