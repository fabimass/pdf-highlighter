import fitz
import csv
import re

# Load the keywords from the csv file
with open('keywords.csv') as f:
    reader = csv.reader(f)
    keywords = list(reader)

print(keywords)

# This regex is for detecting regex-type keywords
regexKw = re.compile('regex\([^\\)]*\\)')


# Read pdf document
doc = fitz.open("input.pdf")

# Go through each of the document pages
for page in doc:
    
    # Get the bare text (this will be use for regex matching)
    text = page.get_text()

    # Go through each one of the keywords
    for row in keywords:
        for kw in row:

            # Check if the keyword is normal or regex
            regexType = regexKw.search(kw)
            
            # Regex-type keyword
            if regexType is not None:
                # Extracts the regex part from the keyword and create a regex object
                regexPattern = re.compile(regexType.group().replace('regex(', '').replace(')', ''))
                # Scans the text looking for patterns
                matches = regexPattern.findall(text)
                
                # Go through each one of the regex matches
                if matches is not None:
                    for match in matches:
                        # Find the match in the text
                        findings = page.searchFor(match)

                        # Highlight each one of the findings
                        if findings is not None:
                            for finding in findings:
                                highlight = page.addHighlightAnnot(finding)
                                highlight.update()

            # Normal keyword
            else:
                # Find the keyword in the text
                findings = page.searchFor(kw)
                
                # Highlight each one of the findings
                if findings is not None:
                    for finding in findings:
                        highlight = page.addHighlightAnnot(finding)
                        highlight.update()


# Create a new pdf file with the keywords highlighted
doc.save("output.pdf")