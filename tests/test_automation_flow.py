import pytest
import allure
from pages.search_bar import SearchBar
from pages.filter_page import Filterspage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
@allure.feature("Amazon Automation 1")
@allure.story("End-to-End Flow")
@pytest.mark.parametrize("product",["laptop","Mobile","HeadPhones"])
def test_automation(page,product):
    with allure.step("Search Product"):
        searchs=SearchBar(page)
        searchs.search_bar(product)

    with allure.step("Apply filter"):
        filters = Filterspage(page)
        filters.sortbyprice()
        filters.ratings()
        filters.outofstock()
        filters.alldiscount()
        filters.payondelivery()
        filters.print_sorted_elements()
        filters.pagigation()

    with allure.step("Product"):
        product = ProductPage(page)
        product_page = product.open_product()
    
    with allure.step("cart Action"):
        cart = CartPage(product_page)
        cart.add_to_cart()
        cart.go_to_cart()
        cart.increase(2)
        cart.decrement(1)
        cart.proceed_to_buy()
        assert "cart" in product_page.url.lower()
        assert "amazon" in product_page.url.lower()
    print("End to End encryption is done")
    