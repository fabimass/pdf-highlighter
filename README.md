# pdf-highlighter
Script that highlights keywords inside a pdf file.

### How to use it:

* Put the keywords you want to find inside the *keywords.csv* separating different keywords with a comma. You can also put them in different lines, it doesn't matter.

> Example: developer,data,software

* You can also search for patterns using regular expressions. For this, put the pattern you want to match inside *regex()*.

> Example: regex(\d{3}-\d{3}-\d{4})

* After the script runs, you will see a new pdf file highlighted accordingly inside the *output* folder.
