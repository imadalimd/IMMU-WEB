#!/bin/bash

echo "🤖 KALI LINUX - YouTube Automation Setup"
echo "========================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Update system
echo -e "${YELLOW}📦 Updating system packages...${NC}"
sudo apt update -y && sudo apt upgrade -y

# Install Google Chrome
echo -e "${YELLOW}🌐 Installing Google Chrome...${NC}"
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update -y
sudo apt install google-chrome-stable -y

# Install dependencies
echo -e "${YELLOW}🔧 Installing dependencies...${NC}"
sudo apt install -y python3 python3-pip python3-venv git wget curl xvfb

# Create virtual environment
echo -e "${YELLOW}🐍 Setting up Python environment...${NC}"
python3 -m venv youtube_bot_env
source youtube_bot_env/bin/activate

# Install Python packages
echo -e "${YELLOW}📦 Installing Python packages...${NC}"
pip install selenium undetected-chromedriver webdriver-manager requests beautifulsoup4 colorama

# Create necessary directories
echo -e "${YELLOW}📁 Creating project structure...${NC}"
mkdir -p scripts utils data logs

# Download ChromeDriver
echo -e "${YELLOW}🚀 Setting up ChromeDriver...${NC}"
sudo apt install -y chromium-chromedriver

echo -e "${GREEN}✅ Kali Linux setup completed successfully!${NC}"
echo -e "${GREEN}🚀 Now run: python3 kali_login.py${NC}"
echo -e "${YELLOW}💡 Note: First run may require manual reCAPTCHA solving${NC}"
