*** Settings ***
Resource  ./support/OrderKeywords.robot
Variables  ./data/OrderProductData.py

*** Test Cases ***
NOT LOGGED IN USER ORDERS TWO PRODUCTS
[Tags]    order    card
        Given Navigate to products page without login
            And Add "${SHIRTS}": "${ORDER_TWO_SHIRTS_DATA}[${SHIRTS}]" to cart
            And Proceed to Checkout products "${ORDER_TWO_SHIRTS_DATA}[${SHIRTS}]"
            And Proceed to "Register/Login" from "Checkout" dialog on "Cart" Page
            And Login with valid credendial "${ORDER_TWO_SHIRTS_DATA}['login']"
            And Select "cart" on navbar
        When Proceed to Checkout products "${ORDER_TWO_SHIRTS_DATA}[${SHIRTS}]"
            And Confirm payment with card "${ORDER_TWO_SHIRTS_DATA}['card']"
        Then Order has been confirmed