#!/usr/bin/env python3
import argparse
import datetime
import os
import sys

def create_post(title, date_str):
    try:
        # Parse the input date
        post_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        
        # Convert title to lowercase and replace spaces with hyphens
        filename_title = title.lower().replace(' ', '-')
        
        # Create the full filename
        filename = f"_posts/{date_str}-{filename_title}.markdown"
        
        # YAML front matter
        front_matter = f"""---
layout: post
title: "{title}"
date: {post_date.strftime('%Y-%m-%d %H:%M:%S')} -0600
categories: blog
---



---


Other Posts You May Want To Cover in Syrup:
"""
        # Create the file
        with open(filename, 'w') as f:
            f.write(front_matter)
        print(f"Created new post: {filename}")
        
    except ValueError:
        print("Error: Date must be in YYYY-MM-DD format")
        sys.exit(1)

def valid_date(s):
    try:
        return datetime.datetime.strptime(s, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new blog post')
    parser.add_argument('-d', '--date', 
                        type=valid_date,
                        help='Post date in YYYY-MM-DD format',
                        required=True)
    parser.add_argument('-t', '--title',
                        type=str,
                        help='Title of the blog post',
                        required=True)
    
    args = parser.parse_args()
    create_post(args.title, args.date)