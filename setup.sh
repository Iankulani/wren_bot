#!/bin/bash
# ============================================
# AWESOME WREN BOT - Installation Script
# Author: Ian Carter Kulani, MSc
# ============================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     🐦 AWESOME WREN BOT - Cybersecurity Command Center      ║"
echo "║                     Installation Script                       ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check Python version
echo -e "${BLUE}[1/6] Checking Python version...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"
else
    echo -e "${RED}✗ Python 3.7+ is required. Please install Python first.${NC}"
    exit 1
fi

# Create virtual environment
echo -e "${BLUE}[2/6] Creating virtual environment...${NC}"
python3 -m venv wren_env
source wren_env/bin/activate
echo -e "${GREEN}✓ Virtual environment created${NC}"

# Upgrade pip
echo -e "${BLUE}[3/6] Upgrading pip...${NC}"
pip install --upgrade pip setuptools wheel
echo -e "${GREEN}✓ Pip upgraded${NC}"

# Install Python dependencies
echo -e "${BLUE}[4/6] Installing Python dependencies...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Install system dependencies
echo -e "${BLUE}[5/6] Installing system dependencies...${NC}"

# Detect OS
OS=$(uname -s)
case "$OS" in
    Linux*)
        echo -e "${YELLOW}Detected Linux - Installing system packages...${NC}"
        if command -v apt-get &> /dev/null; then
            sudo apt-get update
            sudo apt-get install -y nmap nikto hydra dsniff macchanger hping3 traceroute whois curl wget netcat-openbsd
        elif command -v yum &> /dev/null; then
            sudo yum install -y nmap nikto hydra dsniff macchanger hping3 traceroute whois curl wget nc
        elif command -v pacman &> /dev/null; then
            sudo pacman -S --noconfirm nmap nikto hydra dsniff macchanger hping3 traceroute whois curl wget netcat
        else
            echo -e "${YELLOW}⚠ Could not detect package manager. Please install manually:${NC}"
            echo "  nmap, nikto, hydra, dsniff, macchanger, hping3, traceroute, whois, curl, wget, netcat"
        fi
        ;;
    Darwin*)
        echo -e "${YELLOW}Detected macOS - Installing via Homebrew...${NC}"
        if command -v brew &> /dev/null; then
            brew install nmap hydra dsniff macchanger hping3 traceroute whois curl wget netcat
            echo -e "${YELLOW}Note: Nikto requires manual installation on macOS${NC}"
        else
            echo -e "${RED}Homebrew not found. Install manually: brew install nmap hydra dsniff macchanger hping3 traceroute whois curl wget netcat${NC}"
        fi
        ;;
    *)
        echo -e "${YELLOW}⚠ Unknown OS. Skipping system dependencies.${NC}"
        ;;
esac

# Create configuration directory
echo -e "${BLUE}[6/6] Creating configuration directories...${NC}"
mkdir -p .wren_bot/{payloads,workspaces,scans,nikto_results,whatsapp_session,phishing_pages,reports,traffic_logs,phishing_templates,captured_credentials,ssh_keys,ssh_logs,time_history,wordlists,web_static,api_keys,sessions}
mkdir -p reports
echo -e "${GREEN}✓ Configuration directories created${NC}"

# Create run script
echo -e "${BLUE}Creating run script...${NC}"
cat > run_wren.sh << 'EOF'
#!/bin/bash
source wren_env/bin/activate
python3 wren_bot.py "$@"
EOF
chmod +x run_wren.sh

echo -e "${GREEN}"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    ✅ INSTALLATION COMPLETE!                  ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  To start the bot:                                            ║"
echo "║    ./run_wren.sh                                              ║"
echo "║                                                               ║"
echo "║  Or activate the environment manually:                        ║"
echo "║    source wren_env/bin/activate                               ║"
echo "║    python3 wren_bot.py                                        ║"
echo "║                                                               ║"
echo "║  Web Interface: http://localhost:8080                        ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"