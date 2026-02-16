#!/bin/bash

# 1. Check if this is already a Git repo
if [ ! -d ".git" ]; then
    echo "This folder is not linked to GitHub yet."
    echo "Enter the SSH URL of your new GitHub repo (e.g., git@github.com:user/repo.git):"
    read repo_url
    
    git init
    git remote add origin "$repo_url"
    git branch -M main
    echo "Remote linked to: $repo_url"
fi

# 2. Ask for the commit message
echo "Enter your commit message (Revision 2, Update, etc.):"
read message

# 3. Default message if empty
if [ -z "$message" ]; then
  message="Update $(date)"
fi

# 4. Run the Git commands
git add .
git commit -m "$message"

# 5. Push (and set upstream if it's the first time)
git push -u origin main

echo "------------------------------"
echo "Successfully uploaded to GitHub!"
