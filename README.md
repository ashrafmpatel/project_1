# project_2 Documentation
Bootcamp Project 2
Objective

To create a fully automated CI pipeline, based around the program created during project 1. 
The two aspects of this project are to:
	1. Set up an initial automated pipeline and;
	2. To push changes through the pipeline
	
	
Project Initiation

I propose to create a private repository in docker and configure Nexus. 
Set up Jenkins Pipeline and host a Nexus repository in my provisioned Virtual Machine.
Configure Docker and Nexus to ensure my application from Project 1 runs in a container on the Virtual Machine.
Generate an image and  ensure it is stored in the Nexus repo.
Automate the above process by creating a Jenkinsfile that ,connects to the Nexus repository and docker.


Planning, Design and Project Tracking

Trello


ERD

![image](https://github.com/ashrafmpatel/project_1/assets/139867139/3d1ef18f-e6a5-41b0-94e0-3b5a071008ee)

Steps

	1. Cleaning out any images that is stored under Nexus3 folder
	2. Then map the docker container ports to the matching host ports eg. 8081:8081 and start up the containers.
	3. Then run the command to retrieve the admin password from the running containers and use to sign-in to Nexus
	
	



















Create Docker Image


















Testing


















![image](https://github.com/ashrafmpatel/project_1/assets/139867139/3547ede1-df06-4842-b2ad-1fcf4770c44c)

