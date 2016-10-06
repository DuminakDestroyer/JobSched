# JobSched
Job Scheduler Project

Project Setup:
  $ mkdir JobSched
  $ cd JobSched
  $ python -mvenv myvenv
  $ source myvenv/bin/activate
  $ git clone git@github.com:DuminakDestroyer/JobSched.git
  $ pip install -r requirements.txt
  
Development:
  1. Make a branch:
    $ git checkout -b *branch_name*
  2. Dev Time
  3. Updating your branch:
    $ git status
    $ git add -i
    $ git commit -m "*commit message*"
    $ git push origin *branch name*
  4. When done, submit Pull Request for review.
  5. Upon approval, update master, rebase
    $ git fetch
    $ git rebase master
    $ git push --force origin *branch name*
  6. Merge:
    $ git checkout master
    $ git merge --no-ff *branch name*
  7. Delete branch:
    $ git branch -d contact-form
    $ git push origin master
    $ git push origin --delete <branch_name>
    
 Coding Conventions:
    Flake-8
