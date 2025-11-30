from selenium.webdriver.common.by import By
import time
from colorama import Fore, Style

class ChannelAnalyzer:
    def __init__(self, driver=None):
        self.driver = driver
    
    def set_driver(self, driver):
        self.driver = driver
    
    def get_channel_videos(self, channel_url):
        """Get channel videos and show in Termux"""
        if not self.driver:
            print(f"{Fore.RED}❌ Driver not set!")
            return
        
        try:
            print(f"{Fore.CYAN}📺 Analyzing Channel: {channel_url}")
            
            # Ensure URL is proper
            if not channel_url.startswith('http'):
                channel_url = 'https://' + channel_url
            
            self.driver.get(channel_url)
            time.sleep(4)
            
            # Scroll to load videos
            self.driver.execute_script("window.scrollTo(0, 800);")
            time.sleep(2)
            
            # Extract videos
            self.extract_channel_videos()
            
        except Exception as e:
            print(f"{Fore.RED}💥 Channel Analysis Error: {e}")
    
    def extract_channel_videos(self):
        """Extract and display channel videos"""
        try:
            print(f"\n{Fore.GREEN}🎥 CHANNEL VIDEOS:")
            print("=" * 60)
            
            # Try different selectors for videos
            selectors = [
                "ytd-rich-item-renderer",
                "ytd-grid-video-renderer",
                "ytd-video-renderer"
            ]
            
            videos = []
            for selector in selectors:
                videos = self.driver.find_elements(By.CSS_SELECTOR, selector)
                if videos:
                    break
            
            if not videos:
                print(f"{Fore.YELLOW}⚠️  No videos found on this channel!")
                return
            
            for i, video in enumerate(videos[:5]):  # First 5 videos
                try:
                    # Try different title selectors
                    title_selectors = [
                        "#video-title",
                        ".ytd-rich-grid-media #video-title",
                        "a#video-title-link"
                    ]
                    
                    title = "N/A"
                    for title_selector in title_selectors:
                        try:
                            title_element = video.find_element(By.CSS_SELECTOR, title_selector)
                            title = title_element.text.strip() or title_element.get_attribute("title")
                            if title and title != "N/A":
                                break
                        except:
                            continue
                    
                    # Try to get views
                    try:
                        views_element = video.find_element(By.CSS_SELECTOR, "#metadata-line span")
                        views = views_element.text
                    except:
                        views = "N/A"
                    
                    print(f"\n{Fore.CYAN}📹 Video {i+1}:")
                    print(f"{Fore.WHITE}   🎬 Title: {title}")
                    print(f"   👀 Views: {views}")
                    print("-" * 50)
                    
                except Exception as e:
                    print(f"{Fore.YELLOW}⚠️  Error extracting video {i+1}")
                    continue
            
            print(f"{Fore.GREEN}✅ Found {min(len(videos), 5)} videos from channel!")
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error extracting videos: {e}")
