class c_form:

    def __init__(self, page):
        self.page = page
        self.contact_us_tab = page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.name_input = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email_input = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_otp_btn = page.locator('(//button[@type="button"])[2]')
        self.otp_input = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company_input = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.choose_service = page.locator('(//select[@name="service"])[2]')
        self.phone_input = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message_textarea = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit_btn = page.locator('(//input[@type="submit"])[2]')

    def form_option_fill(self):
        self.contact_us_tab.click()
        self.name_input.fill("Himanshu")
        self.email_input.fill("abcd@gmail.com")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.send_otp_btn.click()
        self.otp_input.fill("0000")
        self.company_input.fill("Uncodemy")
        self.choose_service.select_option("Graphic Design")
        self.phone_input.fill("8923332289")
        self.message_textarea.fill("I am just testing the page")
        # self.submit_btn.click()