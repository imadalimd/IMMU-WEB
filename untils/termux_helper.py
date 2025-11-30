"""
Termux-specific helper functions
"""
import os
import sys
from colorama import Fore, Style

class TermuxHelper:
    def __init__(self):
        self.is_termux = self.check_termux_environment()
    
    def check_termux_environment(self):
        """Check if running in Termux"""
        return 'com.termux' in os.environ.get('PREFIX', '')
    
    def setup_termux_environment(self):
        """Setup Termux-specific environment"""
        if not self.is_termux:
            print(f"{Fore.YELLOW}⚠️  Not running in Termux environment")
            return False
        
        print(f"{Fore.GREEN}✅ Running in Termux environment")
        
        # Termux-specific setup
        try:
            # Add Termux binary path if needed
            termux_bin = '/data/data/com.termux/files/usr/bin'
            if termux_bin not in os.environ['PATH']:
                os.environ['PATH'] = termux_bin + ':' + os.environ['PATH']
            
            return True
        except Exception as e:
            print(f"{Fore.RED}❌ Termux setup failed: {e}")
            return False
    
    def check_dependencies(self):
        """Check if all dependencies are installed"""
        dependencies = [
            'chromium',
            'python',
            'git'
        ]
        
        missing_deps = []
        for dep in dependencies:
            if not self.check_package_installed(dep):
                missing_deps.append(dep)
        
        if missing_deps:
            print(f"{Fore.RED}❌ Missing dependencies: {', '.join(missing_deps)}")
            return False
        
        print(f"{Fore.GREEN}✅ All dependencies installed")
        return True
    
    def check_package_installed(self, package):
        """Check if a package is installed"""
        try:
            if package == 'chromium':
                # Check chromium
                result = os.system('which chromium > /dev/null 2>&1')
                return result == 0
            else:
                # Check other packages
                result = os.system(f'which {package} > /dev/null 2>&1')
                return result == 0
        except:
            return False
    
    def get_system_info(self):
        """Get Termux system information"""
        info = {
            'is_termux': self.is_termux,
            'python_version': sys.version,
            'current_directory': os.getcwd()
        }
        
        print(f"{Fore.CYAN}📊 System Information:")
        for key, value in info.items():
            print(f"   {key}: {value}")
        
        return info
