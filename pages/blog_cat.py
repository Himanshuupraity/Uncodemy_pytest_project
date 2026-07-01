class blog_cat:
    def __init__(self, page):
        self.page = page
        self.blog_tab = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        self.blog_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.blog_artificial_intelligence = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.blog_content_marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.blog_crm_development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.blog_digital_marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.blog_ecommerce_development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.blog_email_marketing = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"])[1]')
        self.blog_graphic_design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.blog_software_it_company = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"])[1]')
        self.blog_software_development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"])[1]')
        self.blog_ui_ux_design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.blog_web_development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
        self.blog_categories_list = [self.blog_app_development,self.blog_artificial_intelligence,self.blog_content_marketing,self.blog_crm_development,self.blog_digital_marketing,self.blog_ecommerce_development,self.blog_email_marketing,self.blog_graphic_design,self.blog_software_it_company,self.blog_software_development,self.blog_ui_ux_design,self.blog_web_development]

    def blog_cat_option_click(self):
        for r in self.blog_categories_list:
            self.blog_tab.click()
            r.click()
            self.page.go_back()

        