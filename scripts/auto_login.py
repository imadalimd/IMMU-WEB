import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import json
import os
from colorama import Fore, Style, init
from .recaptcha_bypass import RecaptchaBypass

# Initialize colorama
init(autoreset=True)

class YouTubeAutoLogin:
    def __init__(self):
        self.driver = None
        self.credentials = self.load_credentials()
        self.recaptcha_bypass = None
    
    def load_credentials(self):
        """Load credentials from JSON file"""
        try:
            with open('data/credentials.json', 'r') as f:
                creds = json.load(f)
                print(f"{Fore.GREEN}✅ Loaded credentials for: {creds['email']}")
                return creds
        except FileNotFoundError:
            print(f"{Fore.RED}❌ data/credentials.json not found!")
            return None
        except Exception as e:
            print(f"{Fore.RED}❌ Error loading credentials: {e}")
            return None
    
    def setup_driver(self):
        """Setup Chrome driver for Termux"""
        try:
            options = uc.ChromeOptions()
            
            # Termux optimized options
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-extensions')
            options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')
            
            self.driver = uc.Chrome(options=options)
            self.recaptcha_bypass = RecaptchaBypass(self.driver)
            
            print(f"{Fore.GREEN}✅ Browser setup completed!")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Browser setup failed: {e}")
            return False
    
    def human_type(self, element, text):
        """Human-like typing simulation"""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.08, 0.2))
            
            # Random pause to simulate thinking
            if random.random() < 0.1:
                time.sleep(random.uniform(0.3, 0.7))
    
    def auto_login(self):
        """Automatic YouTube login with reCAPTCHA bypass"""
        if not self.credentials:
            return False
            
        try:
            print(f"{Fore.CYAN}🚀 Starting YouTube Auto-Login...")
            
            if not self.setup_driver():
                return False
            
            # Apply initial stealth
            self.recaptcha_bypass.method1_stealth_mode()
            
            # Step 1: Go to YouTube
            print(f"{Fore.YELLOW}📺 Navigating to YouTube...")
            self.driver.get("https://www.youtube.com")
            time.sleep(3)
            
            # Step 2: Click sign in
            try:
                sign_in_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Sign in')]"))
                )
                sign_in_btn.click()
                time.sleep(2)
                print(f"{Fore.GREEN}✅ Sign in button clicked!")
            except:
                print(f"{Fore.YELLOW}⚠️  Sign in button not found, trying direct login...")
                self.driver.get("https://accounts.google.com/")
                time.sleep(3)
            
            # Step 3: Enter email
            print(f"{Fore.YELLOW}📧 Entering email...")
            email_field = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "identifierId"))
            )
            self.human_type(email_field, self.credentials['email'])
            
            next_btn = self.driver.find_element(By.ID, "identifierNext")
            next_btn.click()
            time.sleep(3)
            
            # Step 4: Enter password
            print(f"{Fore.YELLOW}🔑 Entering password...")
            password_field = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.NAME, "Passwd"))
            )
            self.human_type(password_field, self.credentials['password'])
            
            pass_next = self.driver.find_element(By.ID, "passwordNext")
            pass_next.click()
            time.sleep(5)
            
            # Step 5: Check for reCAPTCHA and handle
            if self.recaptcha_bypass.is_recaptcha_present():
                print(f"{Fore.RED}🛑 reCAPTCHA Detected! Activating bypass system...")
                if self.recaptcha_bypass.execute_all_methods():
                    print(f"{Fore.GREEN}✅ reCAPTCHA Bypassed!")
                else:
                    print(f"{Fore.RED}❌ reCAPTCHA bypass failed!")
                    return False
            
            # Final login check
            if self.check_login_success():
                print(f"{Fore.GREEN}🎉 YouTube Login Successful!")
                return True
            else:
                print(f"{Fore.RED}❌ Login Failed!")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}💥 Login Error: {e}")
            return False
    
    def check_login_success(self):
        """Check if login was successful"""
        try:
            # Multiple success indicators
            success_urls = [
                "myaccount.google.com",
                "mail.google.com", 
                "youtube.com",
                "accounts.google.com"
            ]
            
            current_url = self.driver.current_url
            for url in success_urls:
                if url in current_url:
                    print(f"{Fore.GREEN}✅ Redirected to: {url}")
                    return True
            
            # Check for user avatar
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "avatar-btn"))
            )
            return True
            
        except:
            return False
    
    def get_driver(self):
        return self.driver
    
    def close_browser(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()
            print(f"{Fore.YELLOW}🔒 Browser closed!")
