from selenium.webdriver.common.by import By


class CartPageLocator:
    CLICKING_CART = (By.CSS_SELECTOR, "#main > ul > li.product.type-product.post-24.status-publish.first.instock.product_cat-music.has-post-thumbnail.downloadable.virtual.purchasable.product-type-simple > a.added_to_cart.wc-forward")
    COUPON_FIELD = (By.CSS_SELECTOR,"#coupon_code")
    APPLY_COUPON=(By.CSS_SELECTOR,"#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button")
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR,"#post-7 > div > div > div.cart-collaterals > div > div > a")

