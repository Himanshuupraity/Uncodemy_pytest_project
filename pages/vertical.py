class vertical:
    def __init__(self,page):
        self.page = page
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')
        self.vertical_trading = page.locator('//strong[text()="Trading"]')
        self.trading_stock = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.trading_algo= page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.trading_paper = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.trading_custom = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.trading_cfd = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.trading_web = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trading_app = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.trading_list = [self.trading_stock, self.trading_algo, self.trading_paper, self.trading_custom, self.trading_cfd, self.trading_web, self.trading_app]




        
    def trading_option_click(self):
        for i in self.trading_list:
            self.vertical.hover()
            self.vertical_trading.hover()
            i.click()
            self.page.go_back()
        