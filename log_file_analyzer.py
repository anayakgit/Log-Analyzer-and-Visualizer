import re
import matplotlib.pyplot as plt

# Log file processing handler
class LogProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.error_count = 0
        self.warning_count = 0
        self.info_count = 0

    def process_line(self, line):
        if "ERROR" in line:
            self.error_count += 1
        elif "WARNING" in line:
            self.warning_count += 1
        elif "INFO" in line:
            self.info_count += 1

    def process_log_file(self):
        # Open and read the log file
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.process_line(line.strip())
        self.display_summary()

    def display_summary(self):
        print("\n--- Log Summary ---")
        print(f"INFO: {self.info_count}")
        print(f"WARNING: {self.warning_count}")
        print(f"ERROR: {self.error_count}")
        self.plot_summary()

    def plot_summary(self):
        labels = ['INFO', 'WARNING', 'ERROR']
        counts = [self.info_count, self.warning_count, self.error_count]
        plt.figure(figsize=(6, 4))
        plt.bar(labels, counts, color=['green', 'orange', 'red'])
        plt.title('Log Summary')
        plt.xlabel('Severity')
        plt.ylabel('Count')
        plt.show()

# Main function for processing the log file
def main():
    log_file_path = 'log_file.txt'  # Ensure this is the correct file path
    log_processor = LogProcessor(log_file_path)
    log_processor.process_log_file()  # Process the log file and display summary

if __name__ == "__main__":
    main()
