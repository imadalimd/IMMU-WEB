import time
import random
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecaptchaBypass:
    def __init__(self, driver):
        self.driver = driver
    
    def method1_stealth_mode(self):
        """Method 1: Stealth Mode & Human Behavior"""
        print("🛡️  Method 1: Activating Stealth Mode...")
        
        # Remove automation traces
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
        
        # Human-like delays
        time.sleep(random.uniform(2, 5))
        
        # Random mouse movements simulation
        self.driver.execute_script("window.scrollTo(0, %d)" % random.randint(100, 500))
        
        return True
    
    def method2_mobile_emulation(self):
        """Method 2: Mobile User Agent"""
        print("📱 Method 2: Switching to Mobile Mode...")
        
        mobile_user_agents = [
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"
        ]
        
        user_agent = random.choice(mobile_user_agents)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
        
        self.driver.refresh()
        time.sleep(3)
        return True
    
    def method3_cookie_session_reuse(self):
        """Method 3: Cookie & Session Manipulation"""
        print("🍪 Method 3: Cookie Session Manipulation...")
        
        try:
            # Clear existing cookies
            self.driver.delete_all_cookies()
            
            # Add some generic cookies
            cookies = [
                {'name': 'CONSENT', 'value': 'YES+cb.20210601-17-p0.en+FX+917', 'domain': '.youtube.com'},
                {'name': 'PREF', 'value': 'f1=50000000&al=en', 'domain': '.youtube.com'},
            ]
            
            for cookie in cookies:
                try:
                    self.driver.add_cookie(cookie)
                except:
                    pass
            
            self.driver.refresh()
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"❌ Cookie method failed: {e}")
            return False
    
    def method4_ip_rotation_simulation(self):
        """Method 4: IP Rotation Simulation"""
        print("🌐 Method 4: IP Rotation Simulation...")
        
        try:
            # Different endpoints try karo
            endpoints = [
                "https://music.youtube.com",
                "https://gmail.com",
                "https://drive.google.com",
                "https://photos.google.com"
            ]
            
            for endpoint in endpoints:
                try:
                    self.driver.get(endpoint)
                    time.sleep(2)
                    
                    # Check if we're redirected to login
                    if "accounts.google.com" not in self.driver.current_url:
                        print(f"✅ Direct access to {endpoint}")
                        return True
                        
                except Exception as e:
                    continue
            
            return False
            
        except Exception as e:
            print(f"❌ IP rotation failed: {e}")
            return False
    
    def method5_wait_bypass(self):
        """Method 5: Time-based Bypass"""
        print("⏰ Method 5: Time-based Bypass...")
        
        try:
            # Long wait (reCAPTCHA sometimes auto-solves)
            wait_time = random.randint(20, 30)
            print(f"⏳ Waiting {wait_time} seconds for potential auto-bypass...")
            
            for i in range(wait_time):
                time.sleep(1)
                # Check if page changed (login successful)
                if "myaccount.google.com" in self.driver.current_url or "youtube.com" in self.driver.current_url:
                    print("✅ Auto-bypass detected!")
                    return True
            
            # Try refreshing after wait
            self.driver.refresh()
            time.sleep(3)
            return True
            
        except Exception as e:
            print(f"❌ Time-based bypass failed: {e}")
            return False
    
    def execute_all_methods(self):
        """Execute all 5 bypass methods"""
        print("🎯 Executing 5 reCAPTCHA Bypass Methods...")
        
        methods = [
            self.method1_stealth_mode,
            self.method2_mobile_emulation,
            self.method3_cookie_session_reuse,
            self.method4_ip_rotation_simulation,
            self.method5_wait_bypass
        ]
        
        for i, method in enumerate(methods, 1):
            print(f"\n🔄 Trying Method {i}/5...")
            try:
                if method():
                    # Check if bypassed
                    if not self.is_recaptcha_present():
                        print(f"✅ Method {i} Successfully Bypassed reCAPTCHA!")
                        return True
                    else:
                        print(f"⚠️  Method {i} executed but reCAPTCHA still present")
                else:
                    print(f"❌ Method {i} failed")
            except Exception as e:
                print(f"💥 Method {i} error: {e}")
            
            time.sleep(2)
        
        print("❌ All bypass methods failed!")
        return False
    
    def is_recaptcha_present(self):
        """Check if reCAPTCHA is still present"""
        try:
            page_source = self.driver.page_source.lower()
            return "recaptcha" in page_source or "captcha" in page_source
        except:
            return False
