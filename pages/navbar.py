class navbar:
    def __init__(self, page):
        self.page = page
        self.about_us_tab = page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        self.blog_tab = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.contact_us_tab = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.portfolio_tab = page.locator('(//a[@href="https://www.tranktechnologies.com/portfolio"])[1]')

        self.navbar_list=[self.about_us_tab, self.blog_tab, self.contact_us_tab, self.portfolio_tab]

    def navbar_click(self):
        for p in self.navbar_list:
            p.click()
            # self.page.go_back()