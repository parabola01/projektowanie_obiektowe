from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class PythonForTheLabTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_01_home_page(self):
        driver = self.driver
        driver.get("https://pythonforthelab.com/")
        self.assertIn("Python for scientific instrument control | Python For The Lab", driver.title)

    def test_02_blog_page(self):
        driver = self.driver
        driver.get("https://pythonforthelab.com/blog/")
        self.assertIn("Python for experimental scientists | Python For The Lab", driver.title)

    def test_03_footer_presence(self):
        driver = self.driver
        driver.get("https://pythonforthelab.com/")
        footer = driver.find_element(By.TAG_NAME, 'footer')
        self.assertTrue(footer.is_displayed())

    def test_04_footer_links(self):
        footer_links = self.driver.find_elements(By.CSS_SELECTOR, 'footer a')
        for link in footer_links:
            url = link.get_attribute('href')
            self.driver.get(url)
            self.assertNotIn("404", self.driver.title)
            self.assertNotIn("Error", self.driver.title)
            self.driver.get("https://pythonforthelab.com/")

    def test_05_hire_me_button(self):
        self.driver.get("https://pythonforthelab.com/")
        hire_me_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Hire Me"))
        )
        hire_me_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/hire-me/")

    def test_06_forum_button(self):
        self.driver.get("https://pythonforthelab.com/")
        forum_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Forum"))
        )
        forum_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://github.com/PFTL/pftl_discussions/discussions")

    def test_07_courses_button(self):
        self.driver.get("https://pythonforthelab.com/")
        courses_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Courses"))
        )
        courses_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/courses/")

    def test_08_books_button(self):
        self.driver.get("https://pythonforthelab.com/")
        books_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Books"))
        )
        books_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/books/")

    def test_09_about_button(self):
        self.driver.get("https://pythonforthelab.com/")
        about_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "About"))
        )
        about_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/about/")

    def test_10_all_the_articles_button(self):
        self.driver.get("https://pythonforthelab.com/")
        all_the_articles_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "All the articles"))
        )
        all_the_articles_button.click()
        new_url = self.driver.current_url
        self.assertEqual(new_url, "https://pythonforthelab.com/blog/")

    def test_11_responsiveness(self):
        self.driver.get("https://pythonforthelab.com/")
        self.driver.set_window_size(350, 450)
        navigation = self.driver.find_element(By.ID, 'menu-button')
        self.assertTrue(navigation.is_displayed())

    def test_12_navigation(self):
        self.driver.get("https://pythonforthelab.com/")
        about_us_link = self.driver.find_element(By.LINK_TEXT, 'About Us')
        about_us_link.click()
        self.assertIn("About Aquiles Carattino from Python for the Lab | Python For The Lab", self.driver.title)

    def test_13_newsletter_presence(self):
        self.driver.get("https://pythonforthelab.com/")
        newsletter_input = self.driver.find_element(By.NAME, "EMAIL")
        self.assertTrue(newsletter_input.is_displayed())

    def test_14_newsletter_button_presence(self):
        self.driver.get("https://pythonforthelab.com/")
        subscribe_button = self.driver.find_element(By.ID, "mc-embedded-subscribe")
        self.assertTrue(subscribe_button.is_displayed())

    def test_15_pagination_links(self):
        self.driver.get("https://pythonforthelab.com/blog/")
        pages = self.driver.find_elements(By.XPATH, "//nav[@aria-label='Pagination']/a[@aria-current='page']")
        self.assertGreaterEqual(len(pages), 5)

    def test_16_invalid_email_submission(self):
        self.driver.get(
            "https://us21.list-manage.com/contact-form?u=f0d9bfa6188cdcc67890a07f6&form_id=23280542e88944b2a32bed276c724d1e")
        self.driver.find_element(By.NAME, "fields.1425").send_keys("johnexample.com")
        self.driver.find_element(By.NAME, "fields.1426").send_keys("Test subject")
        self.driver.find_element(By.NAME, "fields.1427").send_keys("Test message")
        self.driver.find_element(By.NAME, "subscribe").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']/div/strong")))
        self.assertIn("There were some errors with your submission.", error_message.text)

    def test_17_invalid_subscription(self):
        self.driver.get(
            "https://pythonforthelab.us21.list-manage.com/subscribe/post?u=f0d9bfa6188cdcc67890a07f6&id=8a0ca536e8&f_id=00dfebe6f0")
        self.driver.find_element(By.ID, "MERGE0").send_keys("johnexample.com")
        self.driver.find_element(By.NAME, "submit").click()
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".feedback.error")))
        self.assertIn("Please enter a value", error_message.text)

    def test_18_subscription_redirect(self):
        self.driver.get("https://pythonforthelab.com")
        self.driver.find_element(By.ID, "mc-embedded-subscribe").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("list-manage.com"))
        self.assertIn("list-manage.com", self.driver.current_url)

    def test_19_course_cards(self):
        self.driver.get("https://pythonforthelab.com/courses/")
        course_cards = self.driver.find_elements(By.XPATH, "//*[starts-with(@class, 'bg-gradient-to-br')]")
        self.assertGreater(len(course_cards), 0)

    def test_20_contact_button_redirect(self):
        self.driver.get("https://pythonforthelab.com/courses/")
        contact_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'contact-form')]"))
        )
        contact_button.click()
        new_url = self.driver.current_url
        self.assertNotEqual(new_url, "https://pythonforthelab.com/courses/")

    def test_21_logo_redirect(self):
        self.driver.get("https://pythonforthelab.com/")
        logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/')]"))
        )
        logo.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://pythonforthelab.com/"))
        self.assertEqual(self.driver.current_url, "https://pythonforthelab.com/")

    def test_22_meta_description_present(self):
        self.driver.get("https://pythonforthelab.com/")
        meta = self.driver.find_element(By.XPATH, "//meta[@name='description']")
        self.assertTrue(meta.get_attribute("content"))

    def test_23_canonical_link(self):
        self.driver.get("https://pythonforthelab.com/blog/")
        canonical = self.driver.find_element(By.XPATH, "//link[@rel='canonical']")
        href = canonical.get_attribute("href")
        self.assertTrue(href.startswith("https://pythonforthelab.com/"))

    def test_24_page_loads_under_3s(self):
        start = time.time()
        self.driver.get("https://pythonforthelab.com/")
        end = time.time()
        self.assertLess(end - start, 3)

    def test_25_hire_me_button_visible(self):
        self.driver.get("https://pythonforthelab.com/")
        button = self.driver.find_element(By.LINK_TEXT, "Hire Me")
        self.assertTrue(button.is_displayed() and button.is_enabled())

    def test_26_internal_links_have_titles(self):
        self.driver.get("https://pythonforthelab.com/")
        links = self.driver.find_elements(By.TAG_NAME, "a")
        internal_links = [l for l in links if l.get_attribute("href") and ("pythonforthelab.com" in l.get_attribute("href") or l.get_attribute("href").startswith("/"))]
        for link in internal_links:
            title = link.get_attribute("title")
            if title:
                self.assertTrue(len(title) > 0)

    def test_27_blog_has_header(self):
        self.driver.get("https://pythonforthelab.com/blog/")
        header = self.driver.find_elements(By.TAG_NAME, "h1")
        if not header:
            header = self.driver.find_elements(By.TAG_NAME, "h2")
        self.assertGreater(len(header), 0, "Na stronie bloga nie znaleziono nagłówków h1 ani h2")

    def test_28_page_has_h1(self):
        self.driver.get("https://pythonforthelab.com/")
        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertTrue(h1.is_displayed())

    def test_29_all_images_have_alt(self):
        self.driver.get("https://pythonforthelab.com/")
        images = self.driver.find_elements(By.TAG_NAME, "img")
        for img in images:
            alt = img.get_attribute("alt")
            self.assertIsNotNone(alt)

    def test_30_title_tag_present(self):
        self.driver.get("https://pythonforthelab.com/")
        self.assertTrue(self.driver.title)

if __name__ == "__main__":
    unittest.main()
