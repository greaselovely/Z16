#!/usr/bin/env python3
import os
import sys
import argparse
import datetime
import subprocess



def valid_date(s):
    """Validate and return a YYYY-MM-DD date string."""
    try:
        return datetime.datetime.strptime(s, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid date: '{s}'. Must be YYYY-MM-DD.")

def create_post(directory, title, date_str):
    """Create a new post file in the specified directory with proper YAML front matter."""
    post_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    filename_title = title.lower().replace(' ', '-')
    filename = os.path.join(directory, f"{date_str}-{filename_title}.markdown")

    # Determine layout and category based on directory
    if directory == "_certs":
        layout = "cert"
        category = "certs"
    elif directory == "_posts":
        layout = "post"
        category = "blog"
    else:
        layout = "post"
        category = "blog"  # Default for any other directories

    front_matter = (
        "---\n"
        f"layout: {layout}\n"
        f'title: "{title}"\n'
        f"date: {post_date.strftime('%Y-%m-%d %H:%M:%S')} -0600\n"
        f"categories: {category}\n"
        "---\n\n\n\n"
        "![ImageTitleExample]({{ site.baseurl }}/images/image_name_here.png \"Image Title Example\")\n\n"
    )

    # If this is the _posts directory, add extra content
    if directory == "_posts":
        front_matter += (
            "---\n\n"
            "Other Posts You May Want To Cover in Syrup:\n"
        )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(front_matter)
    
    print(f"Created new post: {filename}")
    return filename

def get_validated_input(prompt, validator, default=None, required=True):
    """Prompt the user until they provide a valid input based on the validator function."""
    while True:
        user_input = input(f"{prompt} [{default}]: ").strip() if default else input(f"{prompt}: ").strip()
        if not user_input and default is not None:
            return default  # Use the default if the user just presses Enter
        if not user_input and not required:
            return None
        try:
            return validator(user_input)
        except (ValueError, argparse.ArgumentTypeError) as e:
            print(e)

def main():
    parser = argparse.ArgumentParser(description='Create a new blog post.')
    parser.add_argument('-d', '--date', type=valid_date, help='Post date in YYYY-MM-DD format')
    parser.add_argument('-t', '--title', type=str, help='Title of the blog post')

    args = parser.parse_args()

    # Look for all directories starting with '_' except '_layouts'
    all_dirs = [
        d for d in os.listdir('.') if os.path.isdir(d) and d.startswith('_') and d != '_layouts'
    ]
    if not all_dirs:
        print("No valid Jekyll directories (starting with '_') found besides '_layouts'.")
        sys.exit(1)

    # Default to today's date but allow the user to enter a different one
    today_str = datetime.datetime.today().strftime('%Y-%m-%d')
    date_str = args.date or get_validated_input("Enter post date (YYYY-MM-DD)", valid_date, default=today_str)

    # Prompt for post title if not provided
    title = args.title or get_validated_input("Enter post title", lambda s: s if s else None)

    # Prompt the user to select the directory for the new post if not passed as an argument
    print("Select which directory you want to create the post in:")
    for i, d in enumerate(all_dirs, 1):
        print(f"{i}. {d}")

    while True:
        try:
            choice = int(input("Enter the number of the directory: "))
            chosen_dir = all_dirs[choice - 1]
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")

    filename = create_post(chosen_dir, title, date_str)

    # Open the new post in the default editor
    editor = os.getenv('EDITOR', 'code')
    subprocess.run([editor, filename])

if __name__ == "__main__":
    main()
