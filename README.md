## Project Description
This project focuses on encryption and decryption of text and was a fun project to help me solidy knowledge in numerous areas including ML, and more. 
Here is an explanation on how the encryption and decrytpion algorithims work:

Encryption: I first take input of the text from the frontend. With the text, I then go through each character and convert it to decimal using the ASCII table, then proceed to convert it to binary. After this conversion into binary, I then shift and rotate all digits by a randolmy generated number, further encrypting the text.
Text Characters->Decimal->Binary

Decryption: To uncover the previous encryption I did on the text, I first go through all possibly shifts/rotations of the digits or every possible combination and convert it from Binary into Decimal and then into ASCII characters. With the text conversion generated from each combination, I then use artificial intelligence to detect which text is most likely English and the decrypted result and not the random gibberish generated from guessing the wrong shift/rotation number. 
Binary-> Decimal-> Text-> Check all Texts with AI and see which one represents English the most

## My personal file contributions(files I created)
I have created the files aienglish.py, aienglishprediction.py, aienglishtrainer.py, datagen.py, encryption.py, and generate.py, which are all files focused on the AI decryption of this project with the exception of encryption.py having both aspects of encryption AND decryption. 

File Descriptions:

aienglish.py: This is the file that I have created, which has all the functions to the AI model including preporcessing, training, and exporting the model(so we dont retrain every time we run the projet and all the model is pre-saved into a file)

aienglishtrainer.py: This file is mainly for calling the functions in aienglish.py and training the Artificial Intelligence Model and was just a simple script for my personal use with all the testing and debugging


datagen.py: Converts the datasets listed in the section below into 1 file and even does data augmentation on the dataset to increase the accuracy of the AI

encryption.py: Has 2 functions encryption and (non-AI) decryption(this decryption is just converting binary to characters so its half-decrypting the text)

generate.py: This file is mainly for getting a random number for encryption as I felt it would make encryption much more secure than using a random number library


## My personal file contributions(files I created) files I modified
I have personally only modified 2 models for the most part, however there are additional files modified with code, which I will also mention here:

model/users.py: In this file I have created the class Binary, which represents the features of each text having the rotation amount, user that requested for encryption, and more details. Apart from this modification, I have also made a updatepfp and self.image variable, which contains the base64 encrypted text of the users profile picture and allows them to upload it to the database. All of this modifications and classes are stored in a database called instance/volumes/sqlite.db.

api/user.py: Over here I had created the class _BinaryCipher, which performs database operations and recieves frontend JSON data. The database operations here include "post", which uploads related information into the database, and "get", which returns all of the text-encryptions made by the user. I have also created the class Images, which has the function "post", that uploads the image, and "get" that takes the image from the database. 

## Datasets used for the ML(I found online)
Here are the filenaes of datasets I have found and the respective links:
https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text filename: tweet_emotions.csv
https://github.com/kartikn27/nlp-question-detection/blob/master/queries-10k-txt filename: englishsentences.txt








## Other contributions
Although I have worked largely on this project, I woudl also like to mention other contributions that came from my teachers who have provided me this backend template. In this they have mainly and most importantly provided, auth_middleware.py, which helps with the login system, other classes in model/users.py and also api/user.py that help with login too. main.py which runs the flask server(although I changed port number), the docker-rlated files, and much more. 




## Everything in Below this was created by my teacher
# Flask Portfolio Starter

Use this project to create a Flask Servr.

Runtime link: <https://flask.nighthawkcodingsociety.com/>
GitHub link: https://github.com/nighthawkcoders/flask_portfolio

## Conventional way to get started

> Quick steps that can be used with MacOS, WSL Ubuntu, or Ubuntu; this uses Python 3.9 or later as a prerequisite.

- Open a Terminal, clone project and cd to project area

```bash
mkdir ~/vscode; cd ~/vscode

git clone https://github.com/nighthawkcoders/flask_portfolio.git

cd flask_portfolio
```

- Install python dependencies for Flask, etc.

```bash
pip install -r requirements.txt
```

- Run from Terminal without VSCode

  - Setup database and init data
  
  ```bash
    ./migrate.sh
    ```

  - Run python server from command line without VSCode

    ```bash
    python main.py
    ```

### Open project in VSCode

- Prepare VSCode and run

  - From Terminal run VSCode

    ```bash
    code .
    ```

  - Open Setting: Ctl-Shift P or Cmd-Shift
    - Search Python: Select Interpreter
    - Match interpreter to `which python` from terminal

  - Select main.py and Play button
  - Try Play button and try to Debug

## Idea

> The purpose of project is to serve APIs.  It is the backend piece of a Full-Stack project.  Review `api` folder in project for endpoints.

### Visual thoughts

> The Starter code should be fun and practical.

- Organize with Bootstrap menu
- Add some color and fun through VANTA Visuals (birds, halo, solar, net)
- Show some practical and fun links (hrefs) like Twitter, Git, Youtube
- Build a Sample Page (Table)
- Show project specific links (hrefs) per page

### Files and Directories in this Project

These are some of the key files and directories in this project

README.md: This file contains instructions for setting up the necessary tools and cloning the project. A README file is a standard component of all properly set up GitHub projects.

requirements.txt: This file lists the dependencies required to turn this Python project into a Flask/Python project. It may also include other backend dependencies, such as dependencies for working with a database.

main.py: This Python source file is used to run the project. Running this file starts a Flask web server locally on localhost. During development, this is the file you use to run, test, and debug the project.

Dockerfile and docker-compose.yml: These files are used to run and test the project in a Docker container. They allow you to simulate the project’s deployment on a server, such as an AWS EC2 instance. Running these files helps ensure that your tools and dependencies work correctly on different machines.

instances: This directory is the standard location for storing data files that you want to remain on the server. For example, SQLite database files can be stored in this directory. Files stored in this location will persist after web application restart, everyting outside of instances will be recreated at restart.

static: This directory is the standard location for files that you want to be cached by the web server. It is typically used for image files (JPEG, PNG, etc.) or JavaScript files that remain constant during the execution of the web server.

api: This directory contains code that receives and responds to requests from external servers. It serves as the interface between the external world and the logic and code in the rest of the project.

model: This directory contains files that implement the backend functionality for many of the files in the api directory. For example, there may be files in the model directory that directly interact with the database.

templates: This directory contains files and subdirectories used to support the home and error pages of the website.

.gitignore: This file specifies elements to be excluded from version control. Files are excluded when they are derived and not considered part of the project’s original source. In the VSCode Explorer, you may notice some files appearing dimmed, indicating that they are intentionally excluded from version control based on the rules defined in .gitignore.

### Implementation Summary

#### July 2023

> Updates for 2023 to 2024 school year.

- Update README with File Descriptions (anatomy)
- Add JWT and add security features to data
- Add migrate.sh to support sqlite schema and data upgrade

#### January 2023

> This project focuses on being a Python backend server.  Intentions are to only have simple UIs an perhaps some Administrative UIs.

#### September 2021

> Basic UI elements were implemented showing server side Flask with Jinja 2 capabilities.

- Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
- The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
- The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
- WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
- Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
- The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
- The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files.
- Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
- The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
- A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.
