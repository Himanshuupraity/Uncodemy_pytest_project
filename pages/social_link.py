

class social:
    def __init__(self, page):
        self.page = page
        self.facebook = page.locator('//img[@alt="Facebook"]')
        self.linkedin = page.locator('//img[@alt="LinkedIn"]')
        self.instagram = page.locator('(//img[@alt="Instagram"])[1]')
        self.pinterest = page.locator('(//img[@alt="Instagram"])[2]')
        self.twitter = page.locator('//img[@alt="Twitter"]')
        self.youtube = page.locator('//img[@alt="Youtube"]')
        self.quora = page.locator('//img[@alt="Quora"]')

        self.social_list = [self.facebook, self.linkedin,self.instagram,self.pinterest,self.twitter,self.youtube,self.quora]

    def social_click(self):
        for social_icon in self.social_list:
            with self.page.expect_popup() as popup_info:
                social_icon.click()
            new_page = popup_info.value
            new_page.wait_for_load_state()
            print("Opened URL:", new_page.url)
            new_page.close()

