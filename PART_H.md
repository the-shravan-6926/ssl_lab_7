# Part (h): Git Workflow and Merge Conflict Report

## 1. Git Commands Used

The following commands were used to manage the project and its branches:

- `git init` — initialized the Git repository.
- `git add .` — staged project files.
- `git commit -m "message"` — saved changes as commits.
- `git branch feature-grading` — created the grading feature branch.
- `git branch feature-report` — created the report feature branch.
- `git switch master` — switched to the main development branch.
- `git merge feature-grading` — merged the grading branch.
- `git merge feature-report` — merged the report branch.
- `git status` — checked the working tree.
- `git log --oneline --graph --decorate --all` — inspected the commit history.

## 2. Merge Conflict Explanation

A merge conflict occurs when two branches modify the same portion of a file differently. Git cannot automatically decide which changes should be retained.

During this project, conflicting changes were made to `.gitignore` on the `master` and `feature-grading` branches. Git reported an add/add conflict because the file was independently created on both branches.

The conflict was resolved by editing `.gitignore` to retain the required Python ignore rules, staging the resolved file, and completing the merge commit.

## 3. Testing and Validation

The grading system was tested using boundary values: 39, 40, 59, 60, 79, 80, and 100. Invalid marks such as -1 and 101 were also tested. Invalid data types were checked to ensure that appropriate exceptions were raised.

The report functionality was tested using the student CSV file.

## 4. Final Verification

The commands `git status` and `git log --oneline --graph --decorate --all` were used to inspect the final working tree and commit history.

The final repository contains the grading and report feature branches, along with the merge and conflict-resolution history.