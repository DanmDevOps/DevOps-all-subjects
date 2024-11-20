import speedtest
import csv
import time
from datetime import datetime

# CSV file name
CSV_FILE = "internet_speed.csv"

# Function to initialize the CSV file with headers if it doesn't exist
def initialize_csv(file_name):
    try:
        with open(file_name, mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"])
    except FileExistsError:
        pass  # File already exists, no need to initialize

# Function to measure internet speed
def measure_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return download_speed, upload_speed

# Function to log the data to the CSV file
def log_to_csv(file_name, timestamp, download_speed, upload_speed):
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, f"{download_speed:.2f}", f"{upload_speed:.2f}"])

# Main function to execute the speed test and log data every 5 minutes
def main():
    initialize_csv(CSV_FILE)

    print("Starting internet speed logger. Press Ctrl+C to stop.")
    while True:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            download_speed, upload_speed = measure_speed()

            print(f"{timestamp} - Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps")
            log_to_csv(CSV_FILE, timestamp, download_speed, upload_speed)

            time.sleep(300)  # Wait for 5 minutes
        except KeyboardInterrupt:
            print("\nExiting program. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(300)  # Wait for 5 minutes before retrying

if __name__ == "__main__":
    main()
