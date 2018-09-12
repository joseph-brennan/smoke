# Git Contributions for Smoke

This is a rundown of how contributors working on the Smoke project should handle their git repositories.

### Quick Concepts

  - Branches - checkout a branch = switching to that branch as your "Working Directory"
    - This simply means when I add, commit, push any files; I am doing it inside that branch.

  - These instructions infer that you have already cloned a fork of the original Smoke repository.

  - If you are familiar with git commands and you would like to see a comparison of git commands and their git-flow counterparts: https://gist.github.com/JamesMGreene/cdd0ac49f90c987e45ac

***
## Procedures without Git-flow

  While we may not be utilizing the git-flow extension we should still follow the concepts of Git-Flow, this means that we need to have **master** and **develop** branches inside of our forked-repository.

  - The master branch holds finished (Stable) code.
  - The develop branch is a complete history of the project.

  If you are new to Git-Flow there is another type of branch that we are going to need to know about and that is the **Feature** branch.

  - Feature branches hold code that we are currently working on.
  - A new feature branch should be made for each new feature being worked on.
  - A feature branch's name should be: feature/<feature-name>

### Create a Feature Branch

  ```shell
    $ git checkout -b feature/<feature-name> develop
  ```
  This checks out a new branch based off of **develop**, creating one if the branch does not already exist.

  - From this point the user can edit, stage, and commit changes

### Push a Feature Branch

  ``` shell
    $ git push --set-upstream origin feature/<feature-name>
  ```
  This pushes any commits to the repository under the branch feature/<feature-name>.

  This is called "publishing" a feature, meaning you are allowing others to see and make changes.

### Finishing a Feature

  ``` shell
    $ git checkout develop
    $ git merge --no-ff feature/<feature-name>
    $ git branch -d feature/<feature-name>
    $ git push origin develop
  ```
  - When a feature is finished and you are ready to include it into the develop branch, you checkout the develop branch
  - Merge the feature branch into the develop branch.  The --no-ff flag tells git to remember the existence of this branch.
  - Delete the branch
  - Push the changes to develop

***

## Procedures with Git-Flow

Git Flow is more than just a couple extra commands to ease collaboration between development teams. It is a conceptual framework for collaboration.  This framework has a few core ideas, Git Flow repositories have **master** and **develop** branches:

- The master branch holds finished (Stable) code.
- The develop branch contains a complete history of the project.

There is another type of branch that we are going to need to know about and that is the **Feature** branch.

- Feature branches hold code that we are currently working on.
- A new feature branch should be made for each new feature being worked on.
- A feature branch's name should be: feature/<feature-name>

### Initializing a Git-Flow Repository

  ``` shell
    $ git checkout develop
    $ git flow init -d
    Initialized empty Git repository in ~/project/.git
    Branch name for production releases: [master]
    Branch name for "next release" development: [develop]

    How to name your supporting branch prefixes?
    Feature branches? [feature/]
    Release branches? [release/]
    Hotfix branches? [hotfix/]
    Support branches? [support/]
    Version tag prefix? []
  ````
  - Checkout the develop branch and run the init command. The -d flag tell git flow that we would like to use the default branch naming.
  - This allows us to perform git flow commands on the repository.

### Creating a Feature Branch

  ``` shell
    $ git flow feature start <feature-name>
  ```
  Creates a new feature branch based on develop and switches to it.

### Publishing a Feature Branch

  ``` shell
    $ git flow feature publish <feature-name>
  ```
  Publishes a feature branch to the repository so that it can be used by other users.

### Finishing a Feature Branch

  ``` shell
    $ git flow feature finish <feature-name>
  ```
  Merges the feature branch into develop, removes the feature branch, switches to the develop branch.

### Getting a Published Feature

  ``` shell
    $ git flow feature pull origin <feature-name>
  ```

***  
#### Resources used:

  1. https://github.com/nvie/gitflow/wiki/Command-Line-Arguments
        -  list of git flow commands including flags and how they affect the operations
  2. https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
        -  Great tutorial for Git-Flow from Atlassian
  3. https://danielkummer.github.io/git-flow-cheatsheet/
