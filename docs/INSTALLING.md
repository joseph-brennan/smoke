# Windows Install Instructions
**Requires Windows 10 with HyperV**

1. Download [Git Bash](https://git-scm.com/downloads)

2. Download [Docker](https://store.docker.com/editions/community/docker-ce-desktop-windows)
    * Allow access to `C:` during installation

3. Navigate to `Control Panel\All Control Panel Items\Programs and Features`
    * Click on "Turn Windows features on or off"
    * Check the box "Hyper-V"
    * Restart Computer

4. Open Git Bash and navigate to a comfortable directory to place your repository
    * `cd <folder_name>` (to change directory; can tab-complete names)
    * `ls` (shows contents of a directory)

5. Clone the repository (from Git Bash)
    * `git clone <repo_url>`

6. Either from Git Bash or PowerShell, navigate into the `smokr` directory
    * If using PowerShell, use `dir` instead of `ls`

7. Launch Docker and log in
    * **If running on a machine with low memory, close all non-terminal applications before launching or the Docker install may break**

8. In your terminal of choice, run `docker-compose up` 
    * The launch process may take a while

9. Wait for message: `Listening at http://localhost:8080`

10. Navigate to: [http://localhost:8080](http://localhost:8080)

---

# Linux Install Instructions
**All instructions through terminal**

1. Install git 
    * If Fedora or similar, use `sudo dnf install git-all`
    * If Debian or similar, use `sudo apt install git-all`

2. Install Docker 
    * If Fedora or similar, use `sudo yum install docker`
    * If Debian or similar, use `sudo apt-get install docker` (may be able to just use "apt")

3. Install docker-compose 
    * If Fedora or similar, use `sudo yum install docker-compose`
    * If Debian or similar, use `sudo apt-get install docker-compose`

4. Ensure the install occurred correctly
    * Run `groups`
    * If there is no docker group, go to step 5, else, go to step 6

5. Run `sudo usermod -aG docker <your_user_name_here>`

6. Allow docker to run at start-up
    * `sudo systemctl enable docker` 

7. Restart computer and navigate to a comfortable directory to place your repository
    * `cd <folder_name>` (to change directory; can tab-complete names)
    * `ls -al` (shows contents of directory)

8. Clone the repository
    * Run 'git clone <repo_url>`

9. Navigate into the newly created smoke directory

10. Launch Docker and log in
    * `sudo systemctl start docker`

11. Run the project
    * `docker-compose up` 

12. Wait for message: `Listening at http://localhost:8080`

13. Navigate to: [http://localhost:8080](http://localhost:8080)

---

# Mac Install Instructions

## Homebrew Method
**Recommended**

1. Install Homebrew 
    * `/usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/Install)"`

2. Install Caskroom
    * `brew tap caskroom/cask`

3. Install Docker
    * `brew cask install docker`

4. Navigate to a comfortable directory to clone the repository
    * `cd <folder_name>` (to change directory; can tab-complete names)
    * `ls -al` (shows contents of directory)

5. Clone the repository
    * Run `git clone <repo_url>`

6. Navigate into the newly created `smoke` directory

7. Launch the Docker app and log in

8. Run the project
    * `docker-compose up`

9. Wait for message: `Listening at http://localhost:8080`

10. Navigate to: [http://localhost:8080](http://localhost:8080)




## Docker Website Install

1. Install [Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac)

2. Navigate to a comfortable directory to clone the repository
    * `cd <folder_name>` (to change directory; can tab-complete names)
    * `ls -al` (shows contents of directory)

3. Clone the repository
    * `git clone <repo_url>`

4. Navigate into the newly created `smoke` directory

5. Launch the Docker app and log in

6. Run the project
    * `docker-compose up`

7. Wait for message: `Listening at http://localhost:8080`

8. Navigate to: [http://localhost:8080](http://localhost:8080)
