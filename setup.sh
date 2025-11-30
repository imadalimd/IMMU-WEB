#!/bin/bash

echo "🤖 IMMU-WEB YouTube Automation Setup"
echo "===================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Update packages
echo -e "${YELLOW}📦 Updating packages...${NC}"
pkg update -y && pkg upgrade -y

# Install dependencies
echo -e "${YELLOW}🔧 Installing dependencies...${NC}"
pkg install -y python git wget curl

# Install Chromium
echo -e "${YELLOW}🌐 Installing Chromium...${NC}"
pkg install -y chromium

# Install Python packages (without undetected-chromedriver)
echo -e "${YELLOW}🐍 Installing Python packages...${NC}"
pip install selenium requests beautifulsoup4 colorama

# Create necessary directories
echo -e "${YELLOW}📁 Creating directories...${NC}"
mkdir -p scripts utils data logs

echo -e "${GREEN}✅ Setup completed successfully!${NC}"
echo -e "${GREEN}🚀 Now run: python run.py${NC}"
