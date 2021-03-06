# JobSched
Job Scheduler Project

Project Setup:
- $ mkdir JobSched
- $ cd JobSched
- $ python -mvenv myvenv
- $ source myvenv/bin/activate
- $ git clone git@github.com:DuminakDestroyer/JobSched.git
- $ pip install -r requirements.txt
  
Development:

Make a branch:
- $ git checkout -b *branch name*

Dev Time

Updating your branch:

- $ git status
- $ git add -p
- $ git commit -m "*commit_message*"
- $ git push origin *branch name*

When done, submit Pull Request for review.

Upon approval, update master, rebase

- $ git fetch
- $ git rebase master
- $ git push --force origin *branch name*

Merge:

- $ git checkout master
- $ git merge --no-ff *branch name*

Delete branch:

- $ git branch -d contact-form
- $ git push origin --delete *branch name*
- $ git push origin master

    
Coding Conventions:
- Flake-8
