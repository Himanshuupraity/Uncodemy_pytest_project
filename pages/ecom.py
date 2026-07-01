class ecom:
    def __init__(self, page):
        self.page = page
        self.technologies_tab = page.locator('(//a[text()="Technologies"])[1]')
        self.ecommerce_dev_tab = page.locator('(//strong[text()="eCommerce Development"])[1]')
        self.ecommerce_magento = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.ecommerce_codeigniter = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.ecommerce_big_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.ecommerce_cs_cart = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.ecommerce_nop_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.ecommerce_laravel = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.ecommerce_drupal = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.ecommerce_joomla = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.ecommerce_express_js = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ecommerce_opencart = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.ecommerce_wordpress = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.ecommerce_shopify = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.ecommerce_node_js = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.ecommerce_woo_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.ecommerce_prestashop = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.ecommerce_wix = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.ecommerce_react_js = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')  
        self.ecommerce_list = [self.ecommerce_magento,self.ecommerce_codeigniter,self.ecommerce_big_commerce,self.ecommerce_cs_cart,self.ecommerce_nop_commerce,self.ecommerce_laravel,self.ecommerce_drupal,self.ecommerce_joomla,self.ecommerce_express_js,self.ecommerce_opencart,
        self.ecommerce_wordpress,self.ecommerce_shopify,self.ecommerce_node_js,self.ecommerce_woo_commerce,self.ecommerce_prestashop,self.ecommerce_wix,self.ecommerce_react_js]

    def ecom_option_click(self):
        for n in self.ecommerce_list:
            self.technologies_tab.hover()
            self.ecommerce_dev_tab.hover()
            n.click()
            self.page.go_back()
        