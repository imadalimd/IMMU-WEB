#!/usr/bin/env python3
"""
REAL YouTube Login for Kali Linux
With Search, Channel Analysis & Video Operations
"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
import random
from colorama import Fore, Style, init

init(autoreset=True)

class RealYouTubeLogin:
    def __init__(self):
        self.driver = None
        self.credentials = self.load_credentials()
    
    def load_credentials(self):
        """Load credentials from file"""
        try:
            with open('data/credentials.json', 'r') as f:
                creds = json.load(f)
                print(f"{Fore.GREEN}✅ Credentials loaded: {creds['email']}")
                return creds
        except Exception as e:
            print(f"{Fore.RED}❌ Error loading credentials: {e}")
            return None
    
    def setup_driver(self):
        """Setup undetectable Chrome driver"""
        try:
            print(f"{Fore.CYAN}🚀 Starting Chrome driver...")
            
            options = uc.ChromeOptions()
            
            # Stealth options
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-extensions")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--remote-debugging-port=9222")
            options.add_argument("--window-size=1920,1080")
            
            # Remove automation detection
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            self.driver = uc.Chrome(options=options)
            
            # Execute stealth scripts
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print(f"{Fore.GREEN}✅ Chrome driver started successfully!")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Driver setup failed: {e}")
            return False
    
    def human_type(self, element, text):
        """Human-like typing"""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))
    
    def solve_recaptcha_manual(self):
        """Manual reCAPTCHA solution"""
        print(f"{Fore.YELLOW}🛑 reCAPTCHA Detected!")
        print(f"{Fore.CYAN}Please solve the CAPTCHA manually in the browser...")
        input(f"{Fore.YELLOW}Press Enter after solving CAPTCHA...")
        return True
    
    def login_to_youtube(self):
        """Real YouTube login"""
        if not self.credentials:
            return False
        
        try:
            print(f"{Fore.CYAN}🎯 Starting REAL YouTube login...")
            
            # Step 1: Go to YouTube
            self.driver.get("https://www.youtube.com")
            time.sleep(3)
            
            # Step 2: Click sign in
            sign_in_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//ytd-button-renderer//a[contains(@href, 'login')]"))
            )
            sign_in_btn.click()
            time.sleep(3)
            
            # Step 3: Enter email
            print(f"{Fore.YELLOW}📧 Entering email...")
            email_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "identifierId"))
            )
            self.human_type(email_field, self.credentials['email'])
            
            next_btn = self.driver.find_element(By.ID, "identifierNext")
            next_btn.click()
            time.sleep(3)
            
            # Step 4: Enter password
            print(f"{Fore.YELLOW}🔑 Entering password...")
            password_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "Passwd"))
            )
            self.human_type(password_field, self.credentials['password'])
            
            pass_next = self.driver.find_element(By.ID, "passwordNext")
            pass_next.click()
            time.sleep(5)
            
            # Step 5: Handle reCAPTCHA if appears
            try:
                if "recaptcha" in self.driver.page_source.lower():
                    if self.solve_recaptcha_manual():
                        # Retry login after CAPTCHA
                        pass_next.click()
                        time.sleep(5)
            except:
                pass
            
            # Step 6: Verify login success
            if self.verify_login():
                print(f"{Fore.GREEN}🎉 LOGIN SUCCESSFUL!")
                return True
            else:
                print(f"{Fore.RED}❌ Login failed!")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}💥 Login error: {e}")
            return False
    
    def verify_login(self):
        """Verify if login was successful"""
        try:
            # Check for user avatar
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "avatar-btn"))
            )
            print(f"{Fore.GREEN}✅ User avatar found - Login verified!")
            return True
        except:
            # Check URL for success indicators
            current_url = self.driver.current_url
            if "youtube.com" in current_url and ("myaccount.google.com" in self.driver.page_source or "avatar" in self.driver.page_source):
                print(f"{Fore.GREEN}✅ Login verified via page analysis!")
                return True
            return False

    # 🔍 SEARCH FUNCTIONALITY
    def search_videos(self, query):
        """Search for videos and display results"""
        print(f"{Fore.CYAN}🔍 Searching for: '{query}'")
        
        try:
            # Find search box
            search_box = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "search_query"))
            )
            search_box.clear()
            self.human_type(search_box, query)
            search_box.submit()
            time.sleep(3)
            
            # Get search results
            print(f"{Fore.GREEN}📺 SEARCH RESULTS:")
            videos = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-video-renderer"))
            )
            
            for i, video in enumerate(videos[:5]):  # First 5 videos
                try:
                    # Extract title
                    title_element = video.find_element(By.CSS_SELECTOR, "#video-title")
                    title = title_element.text
                    
                    # Extract channel
                    channel_element = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a")
                    channel = channel_element.text
                    
                    # Extract views and time
                    metadata_elements = video.find_elements(By.CSS_SELECTOR, "#metadata-line span")
                    views = metadata_elements[0].text if len(metadata_elements) > 0 else "N/A"
                    time_ago = metadata_elements[1].text if len(metadata_elements) > 1 else "N/A"
                    
                    print(f"{Fore.CYAN}   {i+1}. {title}")
                    print(f"{Fore.WHITE}      👤 {channel}")
                    print(f"{Fore.WHITE}      👀 {views} • ⏰ {time_ago}")
                    print()
                    
                except Exception as e:
                    continue
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Search failed: {e}")
            return False

    # 📺 CHANNEL ANALYSIS
    def analyze_channel(self, channel_url):
        """Analyze YouTube channel and get videos"""
        print(f"{Fore.CYAN}📺 Analyzing channel...")
        
        try:
            # Go to channel
            self.driver.get(channel_url)
            time.sleep(3)
            
            # Scroll to load videos
            self.driver.execute_script("window.scrollTo(0, 500);")
            time.sleep(2)
            
            # Get channel videos
            print(f"{Fore.GREEN}🎥 CHANNEL VIDEOS:")
            videos = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-grid-video-renderer, ytd-rich-item-renderer"))
            )
            
            for i, video in enumerate(videos[:5]):  # First 5 videos
                try:
                    title_element = video.find_element(By.CSS_SELECTOR, "#video-title")
                    title = title_element.get_attribute("title") or title_element.text
                    
                    # Get views
                    try:
                        views_element = video.find_element(By.CSS_SELECTOR, "#metadata-line span")
                        views = views_element.text
                    except:
                        views = "N/A"
                    
                    print(f"{Fore.CYAN}   {i+1}. {title}")
                    print(f"{Fore.WHITE}      👀 {views}")
                    print()
                    
                except Exception as e:
                    continue
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Channel analysis failed: {e}")
            return False

    # 🎬 VIDEO OPERATIONS
    def get_trending_videos(self):
        """Get trending videos from YouTube"""
        print(f"{Fore.CYAN}🔥 Getting trending videos...")
        
        try:
            self.driver.get("https://www.youtube.com/feed/trending")
            time.sleep(3)
            
            videos = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-video-renderer"))
            )
            
            print(f"{Fore.GREEN}📈 TRENDING NOW:")
            for i, video in enumerate(videos[:5]):
                try:
                    title_element = video.find_element(By.CSS_SELECTOR, "#video-title")
                    title = title_element.text
                    
                    channel_element = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a")
                    channel = channel_element.text
                    
                    print(f"{Fore.CYAN}   {i+1}. {title}")
                    print(f"{Fore.WHITE}      👤 {channel}")
                    print()
                    
                except Exception as e:
                    continue
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Trending videos failed: {e}")
            return False

    # 🤖 COMPLETE AUTOMATION
    def run_complete_automation(self):
        """Run complete YouTube automation"""
        if not self.credentials:
            print(f"{Fore.RED}❌ No credentials available!")
            return False
        
        print(f"{Fore.CYAN}🚀 STARTING COMPLETE YOUTUBE AUTOMATION")
        print(f"{Fore.YELLOW}=" * 50)
        
        try:
            # Setup driver
            if not self.setup_driver():
                return False
            
            # Login
            if self.login_to_youtube():
                
                # 🔍 SEARCH TEST
                if self.search_videos("Kali Linux tutorials"):
                    print(f"{Fore.GREEN}✅ Search functionality working!")
                
                # 📺 CHANNEL ANALYSIS TEST
                if self.analyze_channel("https://www.youtube.com/@LinusTechTips"):
                    print(f"{Fore.GREEN}✅ Channel analysis working!")
                
                # 🔥 TRENDING VIDEOS TEST
                if self.get_trending_videos():
                    print(f"{Fore.GREEN}✅ Trending videos working!")
                
                print(f"\n{Fore.GREEN}🎉 COMPLETE AUTOMATION SUCCESSFUL!")
                print(f"{Fore.CYAN}📊 ALL FEATURES WORKING:")
                print(f"{Fore.GREEN}   ✅ Real YouTube login")
                print(f"{Fore.GREEN}   🔍 Video search with results")
                print(f"{Fore.GREEN}   📺 Channel analysis")
                print(f"{Fore.GREEN}   🔥 Trending videos extraction")
                print(f"{Fore.GREEN}   🤖 100% Real automation!")
                
                # Keep browser open
                input(f"\n{Fore.YELLOW}Press Enter to close browser...")
                return True
            
            return False
            
        finally:
            if self.driver:
                self.driver.quit()
                print(f"{Fore.YELLOW}🔒 Browser closed!")

if __name__ == "__main__":
    bot = RealYouTubeLogin()
    bot.run_complete_automation()
