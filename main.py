#!/usr/bin/env python3
"""
IMMU-WEB YouTube Automation - Main Controller
"""

import os
import sys
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('clear')

def print_banner():
    banner = f"""
    {Fore.CYAN}╔═══════════════════════════════════════╗
    ║              {Fore.YELLOW}IMMU-WEB{Fore.CYAN}                  ║
    ║         {Fore.GREEN}YouTube Termux Automation{Fore.CYAN}       ║
    ║          {Fore.MAGENTA}5 reCAPTCHA Bypass Methods{Fore.CYAN}     ║
    ╚═══════════════════════════════════════╝
    """
    print(banner)

def main_menu():
    clear_screen()
    print_banner()
    
    print(f"{Fore.WHITE}🔧 {Fore.CYAN}AVAILABLE OPTIONS:")
    print(f"{Fore.GREEN}1. 🔐 Auto Login to YouTube (5 Bypass Methods)")
    print(f"{Fore.GREEN}2. 🔍 Search Videos & Show Results") 
    print(f"{Fore.GREEN}3. 📺 Analyze Channel Videos")
    print(f"{Fore.GREEN}4. 🚀 Full Automation Test")
    print(f"{Fore.RED}5. ❌ Exit")
    
    choice = input(f"\n{Fore.YELLOW}👉 Select option: {Fore.WHITE}")
    return choice

def run_full_automation():
    """Full dream test automation"""
    print(f"\n{Fore.CYAN}🎯 STARTING FULL AUTOMATION TEST...")
    
    # Step 1: Auto Login
    from scripts.auto_login import YouTubeAutoLogin
    bot = YouTubeAutoLogin()
    
    if bot.auto_login():
        print(f"{Fore.GREEN}✅ Login Successful!")
        
        # Step 2: Search Test
        from scripts.youtube_searcher import YouTubeSearcher
        searcher = YouTubeSearcher(bot.driver)
        searcher.search_and_show("termux tutorials")
        
        # Step 3: Channel Analysis
        from scripts.channel_analyzer import ChannelAnalyzer
        analyzer = ChannelAnalyzer(bot.driver)
        analyzer.get_channel_videos("https://www.youtube.com/@Termux")
        
        print(f"{Fore.GREEN}🎉 FULL AUTOMATION TEST COMPLETED!")
        
        # Keep browser open
        input(f"{Fore.YELLOW}Press Enter to close browser...")
        bot.close_browser()
    else:
        print(f"{Fore.RED}❌ Login Failed!")

def main():
    try:
        while True:
            choice = main_menu()
            
            if choice == '1':
                from scripts.auto_login import YouTubeAutoLogin
                bot = YouTubeAutoLogin()
                if bot.auto_login():
                    input(f"{Fore.YELLOW}Press Enter to continue...")
                    bot.close_browser()
                
            elif choice == '2':
                from scripts.auto_login import YouTubeAutoLogin
                from scripts.youtube_searcher import YouTubeSearcher
                
                bot = YouTubeAutoLogin()
                if bot.auto_login():
                    searcher = YouTubeSearcher(bot.driver)
                    query = input(f"{Fore.YELLOW}Enter search query: {Fore.WHITE}")
                    searcher.search_and_show(query)
                    input(f"{Fore.YELLOW}Press Enter to continue...")
                    bot.close_browser()
                
            elif choice == '3':
                from scripts.auto_login import YouTubeAutoLogin
                from scripts.channel_analyzer import ChannelAnalyzer
                
                bot = YouTubeAutoLogin()
                if bot.auto_login():
                    analyzer = ChannelAnalyzer(bot.driver)
                    channel_url = input(f"{Fore.YELLOW}Enter channel URL: {Fore.WHITE}")
                    analyzer.get_channel_videos(channel_url)
                    input(f"{Fore.YELLOW}Press Enter to continue...")
                    bot.close_browser()
                
            elif choice == '4':
                run_full_automation()
                
            elif choice == '5':
                print(f"{Fore.CYAN}👋 Thanks for using IMMU-WEB!")
                break
            else:
                print(f"{Fore.RED}❌ Invalid option!")
                input(f"{Fore.YELLOW}Press Enter to continue...")
                
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}👋 Program interrupted!")

if __name__ == "__main__":
    main()
