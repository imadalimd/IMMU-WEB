from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from colorama import Fore, Style

class YouTubeSearcher:
    def __init__(self, driver=None):
        self.driver = driver
    
    def set_driver(self, driver):
        self.driver = driver
    
    def search_and_show(self, query):
        """Search YouTube and show results in Termux"""
        if not self.driver:
            print(f"{Fore.RED}❌ Driver not set!")
            return
        
        try:
            print(f"{Fore.CYAN}🔍 Searching YouTube for: {query}")
            
            # Find search box
            search_box = self.driver.find_element(By.NAME, "search_query")
            search_box.clear()
            
            # Human-like typing
            for char in query:
                search_box.send_keys(char)
                time.sleep(random.uniform(0.05, 0.1))
            
            # Press enter
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            
            # Get search results
            self.show_search_results()
            
        except Exception as e:
            print(f"{Fore.RED}💥 Search Error: {e}")
    
    def show_search_results(self):
        """Extract and display search results in Termux"""
        try:
            print(f"\n{Fore.GREEN}📺 SEARCH RESULTS:")
            print("=" * 60)
            
            # Find video elements
            videos = self.driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")
            
            if not videos:
                print(f"{Fore.YELLOW}⚠️  No videos found!")
                return
            
            for i, video in enumerate(videos[:5]):  # First 5 videos
                try:
                    title_element = video.find_element(By.CSS_SELECTOR, "#video-title")
                    title = title_element.text.strip() or title_element.get_attribute("title")
                    url = title_element.get_attribute("href")
                    
                    # Get channel name
                    channel_element = video.find_element(By.CSS_SELECTOR, "ytd-channel-name a")
                    channel = channel_element.text.strip()
                    
                    # Get views and time
                    metadata = video.find_elements(By.CSS_SELECTOR, "span.style-scope.ytd-video-meta-block")
                    views = metadata[0].text if len(metadata) > 0 else "N/A"
                    time_ago = metadata[1].text if len(metadata) > 1 else "N/A"
                    
                    print(f"\n{Fore.CYAN}🎬 Video {i+1}:")
                    print(f"{Fore.WHITE}   📹 Title: {title}")
                    print(f"   👤 Channel: {channel}")
                    print(f"   👀 Views: {views}")
                    print(f"   ⏰ Uploaded: {time_ago}")
                    print(f"   🔗 URL: {url}")
                    print("-" * 50)
                    
                except Exception as e:
                    print(f"{Fore.YELLOW}⚠️  Error extracting video {i+1}")
                    continue
            
            print(f"{Fore.GREEN}✅ Found {min(len(videos), 5)} videos!")
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error extracting results: {e}")
