import os
import subprocess

# Remove the "docsoutput" folder if it already exists
if os.path.exists("docsoutput"):
    subprocess.run(["rm", "-rf", "docsoutput"]).wait()

# Create a new "docsoutput" folder
os.makedirs("docsoutput")

# Get all the reStructuredText files in the current directory
rst_files = [f for f in os.listdir('.') if f.endswith('.rst')]

# Convert each reStructuredText file to HTML using pandoc and save it in "docsoutput" folder
for rst_file in rst_files:
    output_file = "docsoutput/" + os.path.splitext(rst_file)[0] + ".html"
    proc = subprocess.run(["pandoc", "-f", "rst", "-t", "html", "-o", output_file, rst_file])
    proc.wait()
    del proc
