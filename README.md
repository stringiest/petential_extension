# Petential

[About](#About) | [Demo](#Demo) | [Quick Start](#Quick-Start) | [Tech Stack](#Tech-Stack) | [Team Petential](#Team-Petential)

## About
Petential is a web application that allows you and members of your family to keep track of your pet's daily needs.

 * Create a pack for your pet
 * Share you unique 6 letter code with your family, allowing them to join the pack
 * No need to remember your code, your browser will remember you until you log out
 * Track meals and treats
 * Record walks and check your local weather to help plan your walks

## Demo

![Demo](https://user-images.githubusercontent.com/71782749/106255063-68f84800-6211-11eb-9d98-e91c24084ec3.gif)

## Quick Start

1.  Clone this repo
2.  Ensure you have python 3.9 downloaded on your system
3.  Run `source venv/bin/activate` to set up the virtual environment
4.  `cd pet_tential`  to move into the project repo 
5.  [Generate](https://gist.github.com/ndarville/3452907) a Django secret key and save it in petential_extension/pet_tential/pet_tential/secret_key.txt
5.  Run  `pip3 install -r requirements.txt`  to install the dependencies
6.  Run  `python3 manage.py makemigrations`  & `python3 manage.py migrate`to create your database
7.  Run  `python3 manage.py runserver`  to run the server
8.  [Install Node.js](https://nodejs.org/en/)
9. `cd frontend` and run `npm i` to install node modules
10. Run `npm run dev` to start the front end server 
11. Navigate to  [localhost](http://localhost:8000/)  or if your console specifies another port, navigate to that instead of 8000

## Tech Stack

|Use        | Backend|      Frontend|
|--------|--------|------|
|Framework| Django| ReactJS|
|Language   | Python|   Javascript|
|Package Manager| pip| npm|
|Testing|   Unittest| Jest|
|Database| PostgreSQL|      |
|Styling|  |    Material UI|

## Planning

We used the github wiki to plan the project and track our progress:
- We made [User Stories](https://github.com/stringiest/petential_extension/wiki/2.-MVP-&-User-Stories) to drive our features.
- [Entity Relationship Diagrams](https://github.com/stringiest/petential_extension/wiki/3.-Planning) helped plan out database structure.
- [Mockups](https://github.com/stringiest/petential_extension/wiki/4.-Preliminary-Design) were made using Balsamiq.
- We [protected our main branch](https://github.com/stringiest/petential_extension/wiki/5.-Git-Cheatsheet) and required two approvals before merging pull requests. 
- There were lots of great [resources](https://github.com/stringiest/petential_extension/wiki/8.-Resources-we-found-useful) that helped us along the way.

## Team Petential

Petential was made as a 2 week final project for Makers by:

[Mel](https://github.com/TamMelPer) | [Lucy](https://github.com/stringiest) | [Savanna](https://github.com/savannaelbey) | [Georgie](https://github.com/horthbynorthwest)

Extension work was undertaken by Mel, Lucy & Georgie.