import schedule
import time
from BackupRecoveryScript.src.src.backup import encrypt_file, backup_file

def automated_backup():
    encrypt_file("example.txt")
    backup_file("example.txt", "backup/")

schedule.every().day.at("10:00").do(automated_backup)

while True:
    schedule.run_pending()
    time.sleep(1)