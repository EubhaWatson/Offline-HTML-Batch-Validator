import os
import subprocess

def validate_html(file_path, vnu_jar_path):
    result = subprocess.run(['java', '-jar', vnu_jar_path, file_path], capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def scan_directory(directory, vnu_jar_path, report_file):
    with open(report_file, 'w') as report:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    is_valid, message = validate_html(file_path, vnu_jar_path)
                    result = f"{file_path}: {'Valid' if is_valid else 'Invalid'}\n{message}\n"
                    print(result, end='')
                    report.write(result)

if __name__ == "__main__":
    directory = input("Enter the directory path to validate HTML files: ")
    vnu_jar_path = input("Enter the full path to vnu.jar: ")
    report_file = '/Users/watson/Desktop/html_validation_report_w3c.txt'
    scan_directory(directory, vnu_jar_path, report_file)
    print(f"Report generated at: {report_file}")