import os
import subprocess
import zipfile

def validate_html(file_path, vnu_jar_path):
    result = subprocess.run(['java', '-jar', vnu_jar_path, file_path], capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def get_desktop_path():
    """Returns the desktop path for the current user, regardless of OS."""
    home = os.path.expanduser("~")
    desktop = os.path.join(home, "Desktop")
    return desktop

def scan_directory(directory, vnu_jar_path, report_file):
    # Unzip any zip files first
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                extract_to = os.path.join(root, os.path.splitext(file)[0])
                if not os.path.exists(extract_to):
                    os.makedirs(extract_to)
                print(f"Unzipping {zip_path} to {extract_to}...")
                unzip_file(zip_path, extract_to)

    # Now validate the HTML files
    with open(report_file, 'w') as report:
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Skip files that start with "._"
                if file.endswith('.html') and not file.startswith("._"):
                    file_path = os.path.join(root, file)
                    is_valid, message = validate_html(file_path, vnu_jar_path)
                    result = f"{file_path}: {'Valid' if is_valid else 'Invalid'}\n{message}\n"
                    print(result, end='')
                    report.write(result)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Set the relative path to vnu.jar
    vnu_jar_path = os.path.join(script_dir, 'validator-dist', 'vnu.jar')

    directory = input("Enter the directory path to validate HTML files: ")

    # Automatically save the report to the desktop
    desktop_path = get_desktop_path()
    report_file = os.path.join(desktop_path, 'html_validation_report_w3c.txt')

    scan_directory(directory, vnu_jar_path, report_file)
    print(f"Report generated at: {report_file}")
