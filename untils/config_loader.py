
"""
Configuration loader utility
"""
import json
import os
from colorama import Fore, Style

class ConfigLoader:
    def __init__(self):
        self.config_path = "data/credentials.json"
    
    def load_credentials(self):
        """Load credentials from JSON file"""
        try:
            if not os.path.exists(self.config_path):
                print(f"{Fore.RED}❌ Configuration file not found: {self.config_path}")
                return None
            
            with open(self.config_path, 'r') as f:
                credentials = json.load(f)
                print(f"{Fore.GREEN}✅ Loaded credentials for: {credentials['email']}")
                return credentials
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error loading configuration: {e}")
            return None
    
    def validate_credentials(self, credentials):
        """Validate if credentials are present"""
        if not credentials:
            return False
        
        required_fields = ['email', 'password']
        for field in required_fields:
            if field not in credentials or not credentials[field]:
                print(f"{Fore.RED}❌ Missing required field: {field}")
                return False
        
        return True
