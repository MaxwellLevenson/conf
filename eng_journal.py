import datetime
import os
import sys


def create_markdown_file(date_string):
    """Generate the formatted engineering journal markdown file."""
    # Format input date string to desired format.
    date = datetime.datetime.strptime(date_string, "%m.%d.%y")
    weekday = date.weekday()
    beginning_of_week = (
        (date - datetime.timedelta(days=weekday)).strftime("%B %d, %Y")
        if weekday > 0
        else date.strftime("%B %d, %Y")
    )
    end_of_week = (
        (date + datetime.timedelta(days=4 - weekday)).strftime("%B %d, %Y")
        if weekday < 4
        else date.strftime("%B %d, %Y")
    )
    current_month = date.strftime("%B")
    formatted_date = date.strftime("%B %d, %Y")

    current_script_path = os.path.realpath(__file__)
    current_script_dir = os.path.dirname(current_script_path)

    # Create the markdown file.
    md_file_path = os.path.join(current_script_dir, f"{date_string}.md")
    if os.path.exists(md_file_path):
        print("Eng journal already exists!")
        return
    with open(md_file_path, "w") as md_file:
        contents = f"""# Engineering Journal {date_string}

## Morning Reflection
Productivity goal:
Body: /10 -
Work: /10 -

## Goals
### Daily goals ({formatted_date})

### Weekly goals ({beginning_of_week} - {end_of_week})

### Monthly goals (end of {current_month})

### Pomo Planning

## Log

## EOD Reflection
Progress towards feedback from check ins:

### Use TDD, low level coding
### Go slower when debugging, wait for commands to finish
### Be bigger owner, talk to customers, do 3rd party things earlier. Charge into the fire
### Intentionally collaborate more. Share the load, share the knowledge.
### Do some active ideation on new product(s) and direction
"""
        md_file.write(contents)
        print(f"Created new journal at: {md_file_path}")


assert len(sys.argv) == 2
date_string = sys.argv[1]
create_markdown_file(date_string)
