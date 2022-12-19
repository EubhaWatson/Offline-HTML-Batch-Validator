#!/bin/zsh

# Store the parent directory in a variable
parent_dir=$1

# Use find to search for all HTML files in the parent directory
html_files=($(find "$parent_dir" -name "*.html"))

# Iterate over each HTML file
for file in "${html_files[@]}"; do
  # Use curl to send the file to the W3C validator
  response=$(curl -s -F "uploaded_file=@$file" "https://validator.w3.org/check")
  
  # Extract the validation result from the response
  result=$(echo "$response" | grep -oP '(?<=This document was successfully checked as )(.*)(?=\.|line)')
  
  # Print the result
  if [[ "$result" == "HTML5" ]]; then
    echo "$file is valid HTML5"
  else
    echo "$file is not valid HTML5"
  fi
done