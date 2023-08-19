https://lightning.ai/pages/category/education/lightning-bits/ (EP 06-09)

<u>**Version Control Process**</u>
- put folder under source control 
- create .gitignore 
- add everything else 
- make and view changes 
- commit changes

<u>Creating Git Repository</u>
- go to CLI 
- navigate to working directory >> cd <path> 
- initialize git repo >> git init
- add files to track >> git add <file_name_1 file_name_2 ... file_name_n>
- commit changes >> git commit -am "<commit_message>"
- create .gitignore >> touch .gitignore
    - specify files to be ignored >> open .gitignore --> <file_names_to_ignore> --> save
- add .gitignore file (only untracked file in >> git status) >> git add .
- commit changes >> git commit -am "<commit_message>"

<u>Editing Files</u>
- make change to file in repo and save
- see that changes were made >> git status
    - see the differences >> git diff
- commit changes >> git commit -am "<commit_message>"

<u>Branching</u>
- view all branches and current branch >> git branch
- create branch >> git branch <created_branch_name>
- move to new branch >> git checkout <created_branch_name>
    - checkout <=> switch
- make changes in new branch, see changes and diff >> git status >> git diff
- commit changes >> git commit -am "<commit_message>"
- Note: at this point, two versions exist, one in main and one in new branch
- move changes back to main branch and delete created branch
    - move to main branch >> git checkout main
    - merge created branch >> git merge <created_branch_name>
        - could also rebase (approve changes commit by commit)
    - delete created branch >> git branch -D <created_branch_name>

<u>**GitHub**</u>
- create github repo
- link local git controlled repo
    - checks >> git status >> pwd
    - paste github instructions
- add collaborators
    - settings --> collaborators --> add people
- _Collaboration Workflow_
    - git clone <repo_link>
    - everyone create new branch for everything
    - make changes, add, commit
    - push to github >> git push origin <branch_name>
    - make pull request, get feedback
        - recipient of pull request:
            - review, suggest change, leave comment (github ui)
    - implement agreed upon changes from branch --> >> git add . >> git commit -am "" >> git push origin <branch_name>
        - repo owner upon recieval (github ui):
            - squash all commits into one: merge pull requests dropdown --> squash and merge
            - delete branch 