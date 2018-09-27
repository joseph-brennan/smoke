# Building a Jenkins Docker image
This file will help users unfamiliar with Docker and Jenkins build and run an image, and test with Jenkins.

## Building the Image
`CD` to the main directory that holds the Dockerfile.
To build the Dockerfile run the command `docker build -t "some_name" . --no-cache"
This will build an image with whatever name was used for `"some_name"`

## Running the Image
To run the image use the command `docker run -p 8080:8080 "some_name"`
Using `-p 8080:8080` isn't necessarily required, but it is good practice.
This will run the `"some_name"` image and fire it up on `localhost:8080`
**Pay attention to the block that says your admin user password**
It is not required for this situation, but make sure you know its location

## Creating and running a job in Jenkins
Upon firing up Jenkins and navigating to `localhost:8080` install suggested plugins
Either create a new user (pointless for this situation) or continue as admin
Hit "Save and Finish" and then hit "Start using Jenkins"
Upon seeing the Jenkins main dashboard, hit create new jobs
Enter an item name, select Freestyle project, and hit okay
Under the section marked "Source Code Management", select Git
Enter the repository url and add your credentials for the repo*
*optional: select a specific branch
Scroll down to the Build section, and add a "Build using .travis.yml" build step
Hit apply and save, on the next screen hit "Build now"
It should start building the project, click on the grey circle to see the console output

