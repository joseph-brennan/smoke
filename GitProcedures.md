# Git Flow for Smoker (Team # 1)
***

## Procedures for GIT normally

### Clone Remote Repo
```shell
  $ cd #/.../smoke
  $ git clone <url-remote> <local-destination>   # Team's remote repository
```

### Config (If you would like to)
  **Method One**
  ```shell
    $ cd #/.../smoke
    $ git config --global user.email "your-git-email"
  ```

  **Method Two**
  ```shell
    $ vi .gitconfig    # easier way to edit variables
  ```

***

## Basics

  **Pull**
  ```shell
    $ cd #/.../smoke
    $ git pull
  ```

  **Commit File** (example file: README.md
  ```shell
    $ cd #/.../smoke
    $ git add README.md
    $ git commit -m "commiting README.md"
    $ git push
  ```

  **Commit Multiple Files**
  ```shell
    $ cd #/.../smoke
    $ git add <file-name> <file-name> <file-name>
    $ git commit -am "commiting all files watched by git that have been changed"
    $ git push
   ```
   - source: https://stackoverflow.com/a/23621748

***

 ## Git-Flow

    - From the man himself https://nvie.com/posts/a-successful-git-branching-model/
    - By utilizing git-flow in your projects you are not losing any function of the regular git commands
    - **Download Instructions** --  https://github.com/nvie/gitflow/wiki/Installation

  **Set Up**
  ```shell
    $ cd #/.../smoke
    $ git-flow init
  ```
   - this will step you through the process of initializing prefrences text in brackets [] are defaults, leave the defaults   alone

 ### Main Branches

   + master
   + develop

 ### Support Branches

   + Feature Branches
        + Typically branch from develop
        + Always merge back into develop
        + name it feature-(your-unique-feature-name)

        - These branches exist as long as the feature is in development, but will eventually make it to the dev branch

        - **Creating Feature Branch**
          Creates a new feature branch from develop and switches to it.
           ```shell
            $ cd #/.../smoke
            $ git branch    # check you are in develop branch, if not checkout develop branch
            $ git-flow feature start feature-<feature's-name>  
           ```
        - **Finishing a Feature**  (when you want to merge it back into develop)
          ```shell
            $ cd #/.../smoke
            $ git-flow feature finish <finished-feature>
          ```

          - Merges feature into develop
          - Removes feature branch
          - switches to develop branch

        - **Publish a Feature**

        - **Pulling Features**

   + Release Branches      

   + HotFix Branches

***
***

 ### Sources

  1. https://danielkummer.github.io/git-flow-cheatsheet/
        - gives a quick burndown of the main git-flow commads (great resource).
  2. https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet
        - git cheat sheet if you haven't found one already.
  3. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
        - help on how to create .md files (cool stuff extra).
  4. https://nvie.com/posts/a-successful-git-branching-model/
