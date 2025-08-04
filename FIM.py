import os
import hashlib
import time

# Function to calculate SHA-512 hash of a file
def calculate_file_hash(filepath):
    sha512_hash = hashlib.sha512()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha512_hash.update(byte_block)
    return sha512_hash.hexdigest()

# Function to create baseline
def create_baseline(directory, baseline_file):
    with open(baseline_file, "w") as bf:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_file_hash(filepath)
                bf.write(f"{filepath}|{file_hash}\n")
    print("[+] Baseline created successfully.")

# Function to load baseline into a dictionary
def load_baseline(baseline_file):
    baseline = {}
    with open(baseline_file, "r") as bf:
        for line in bf:
            path, file_hash = line.strip().split("|")
            baseline[path] = file_hash
    return baseline

# Function to start monitoring
def monitor_files(directory, baseline_file):
    print("[*] Starting file integrity monitoring...")
    baseline = load_baseline(baseline_file)

    while True:
        time.sleep(1)
        current_files = {}
        
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_file_hash(filepath)
                current_files[filepath] = file_hash

                # New file detected
                if filepath not in baseline:
                    print(f"[NEW] {filepath} has been created.")

                # File modified
                elif baseline[filepath] != file_hash:
                    print(f"[MODIFIED] {filepath} has changed.")

        # Check for deleted files
        for filepath in baseline:
            if filepath not in current_files:
                print(f"[DELETED] {filepath} has been deleted.")

# Main menu
def main():
    directory = "./Files"
    baseline_file = "baseline.txt"

    print("\nWhat would you like to do?\n")
    print("A) Collect new Baseline")
    print("B) Begin monitoring files with saved Baseline\n")
    choice = input("Please enter 'A' or 'B': ").upper()

    if choice == "A":
        create_baseline(directory, baseline_file)
    elif choice == "B":
        monitor_files(directory, baseline_file)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
