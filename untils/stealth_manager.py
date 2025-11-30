
"""
Stealth and anti-detection manager
"""
import random
import time
from selenium.webdriver.common.action_chains import ActionChains

class StealthManager:
    def __init__(self, driver):
        self.driver = driver
    
    def apply_stealth_techniques(self):
        """Apply all stealth techniques"""
        techniques = [
            self.remove_automation_flags,
            self.random_mouse_movements,
            self.human_typing_pattern,
            self.random_scrolling,
            self.window_size_variation
        ]
        
        for technique in techniques:
            try:
                technique()
                time.sleep(0.5)
            except Exception as e:
                print(f"Stealth technique failed: {e}")
    
    def remove_automation_flags(self):
        """Remove Selenium automation flags"""
        scripts = [
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})",
            "Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})",
            "Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})",
        ]
        
        for script in scripts:
            try:
                self.driver.execute_script(script)
            except:
                pass
    
    def random_mouse_movements(self):
        """Simulate random mouse movements"""
        try:
            actions = ActionChains(self.driver)
            
            # Random movements
            for _ in range(3):
                x_offset = random.randint(-50, 50)
                y_offset = random.randint(-50, 50)
                actions.move_by_offset(x_offset, y_offset)
                actions.perform()
                time.sleep(0.1)
            
            # Reset to original position
            actions.move_by_offset(0, 0)
            actions.perform()
            
        except Exception as e:
            print(f"Mouse movement failed: {e}")
    
    def human_typing_pattern(self):
        """Return human typing delay pattern"""
        return random.uniform(0.08, 0.3)
    
    def random_scrolling(self):
        """Perform random scrolling"""
        try:
            scroll_amount = random.randint(100, 400)
            self.driver.execute_script(f"window.scrollTo(0, {scroll_amount})")
            time.sleep(0.5)
            
            # Sometimes scroll back a bit
            if random.random() > 0.7:
                self.driver.execute_script(f"window.scrollTo(0, {scroll_amount - 50})")
                
        except Exception as e:
            print(f"Scrolling failed: {e}")
    
    def window_size_variation(self):
        """Vary window size randomly"""
        try:
            widths = [1024, 1280, 1366, 1440, 1920]
            heights = [768, 800, 900, 1080]
            
            width = random.choice(widths)
            height = random.choice(heights)
            
            self.driver.set_window_size(width, height)
            
        except Exception as e:
            print(f"Window resize failed: {e}")
