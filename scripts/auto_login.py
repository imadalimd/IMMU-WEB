from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import json
import os
from colorama import Fore, Style, init

# Local imports
from .recaptcha_bypass import RecaptchaBypass
from utils.config_loader import ConfigLoader
from utils.stealth_manager import StealthManager
from utils.logger import logger

# Initialize colorama
init(autoreset=True)

class YouTubeAutoLogin:
    def __init__(self):
        self.driver = None
        self.config_loader = ConfigLoader()
        self.credentials = self.config_loader.load_credentials()
        self.recaptcha_bypass = None
        self.stealth_manager = None
        
        # Log initialization
        logger.log_automation_start()
    
    def setup_driver(self):
        """Setup Chrome driver for Termux"""
        try:
            logger.log_info("Browser setup initiated")
            
            options = Options()
            
            # Termux optimized options
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-extensions')
            options.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36')
            
            # Chrome binary path for Termux
            options.binary_location = '/data/data/com.termux/files/usr/bin/chromium'
            
            self.driver = webdriver.Chrome(options=options)
            self.recaptcha_bypass = RecaptchaBypass(self.driver)
            self.stealth_manager = StealthManager(self.driver)
            
            logger.log_success("Browser setup completed")
            return True
            
        except Exception as e:
            logger.log_error(f"Browser setup failed: {e}")
            return False

    # ... (rest of the code remains same)
