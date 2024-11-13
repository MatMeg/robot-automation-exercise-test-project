*** Settings ***
Resource  ./../../CommonsKeywords.resource
Variables  ./data/OrderProductData.py

*** Keywords ***
Navigate to products page without login
    Open "Automation Exercise" Page on Browser
    Select "products" on navbar

Add "${category}": "${products_list}" to cart
    Search for "${category}" on products
    Add products "${products_list}" to cart (continue shopping)
    Select "cart" on navbar



    


    