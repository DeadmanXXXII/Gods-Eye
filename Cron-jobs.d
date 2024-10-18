# Run Shodan scan every hour
0 * * * * /path/to/shodan_scan.py

# Run Nmap scan every 30 minutes
*/30 * * * * /path/to/nmap_scan.sh

# Run social media harvesting daily
0 1 * * * /path/to/social_media_harvest.sh

# Monitor Telegram messages every 30 minutes
*/30 * * * * /path/to/telegram_monitor.py
