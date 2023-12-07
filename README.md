# Batch HTML Validator

This script uses the vnu.jar local validator for HTML5, which adheres to W3C standards. Note that this approach requires Java and the downloading of the vnu.jar file.


## Step 1: Get Java (if you don't already have it)

You need Java. 

You can check the version that you have with the following command:

```BASH
    java -version
```

You can check this version against what's on [Oracle's website](https://www.java.com/en/download/manual.jsp).


## Step 2: Download vnu.jar

A `.jar` file is a java source file archive. This specific one we need has all of the stuff we need to validate our code offline. 

This is [the GitHub page](https://github.com/validator/validator/releases) where you can find the file. It will be in a `.zip` file under the `Assets` heading. 

After you download and unpack the archive, make sure it's somewhere you can access through the CLI.

Note: For convenience, there is a copy of the required files in the `validator-dist` subdirectory.


## Step 3: Use the Script

To run the script:

1. Open the Terminal.

2. Navigate to the directory where your script is saved.

3. Execute the script by running `python3 validate_html_w3c.py`.

4. Enter Directory Path and vnu.jar Path: When prompted, enter the path of the directory containing the HTML files and the full path to vnu.jar.

5. Check the Report: A report file named html_validation_report_w3c.txt will be created on your Desktop, containing the validation results.
