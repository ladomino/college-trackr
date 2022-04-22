College Trackr

# Description
College Trackr is an app designed to allow parents and students to track their college admissions process.
Parents and Students can save the colleges they've selected, track the college admissions applications that have been submitted or being worked on, select from tasks they must complete, and setup sticky notes to themselves to track things that must get completed for each college.  Ideally it can be used hand in hand with a Students School Naviance account and for a parent to make sure they track all the items that need to get done and create their own notes in their home.


# MVP Goals
- Create a profile - signup/login
- Select Colleges you are interesting in applying to and tracking.
- Add a College/School/Bootcamp you are interested in applying to if it does not exist.
- View your Colleges you are tracking.
- Show a specific College you are interested in applying to.
- Add an Application to a College you are applying to.
- View an Application to a College you are applying to.
- Edit an Application to a College you are applying to.
- Delete an Application to a College you are no longer interested in applying to.
- View all Applications to all Colleges you are applying or have applied to.
- View all Tasks you can add for an Application.
- Add Task(s) you need for an Application.
- Create a Task you need for an Application.
- Track Tasks via the application/college you are still working on. Color code them like Sticky Notes.
- Delete a Task you no longer need for an Application.
- Present a Status of the Application, making sure it is incomplete if mandatory Tasks are not complete.

# Stretch Goals
- Add in Tracking Sending Scores from standardized tests, transcripts, AP, IB and community
 college credits.
- Send an email notification to the profile user when Tasks get Added.
- Highlight in Red when Due Dates are approaching.
- Allow for file uploads like resumes, essays, letters of recommendation tracking.
- Add in Financial Aid tracking table.
- Add in Scholarship Table tracking with dates and applications.

# User Stories
- As a user, I want to be able to:

- Create a personalized account

- Colletes:  List all colleges that a user is able to Track.
- Colleges:  Save and View specific colleges that are Tracked.
- Colleges:  Add a colleges if it is not available in the list of colleges for Tracking.

- Applications: Add/Delete/Edit and View an application to a colleges
- Applications: List all applications that are submitted to colleges

- Tasks:  List all Tasks for an application that were added.
- Tasks:  Add/Delete/Edit and View specifc tasks for a college.

# Admin Stories
- As an Admin,  I want to be able to:

- Create and manage users
- Add/Edit/Delete Colleges
- Add/Edit/Delete Applications
- Add/Edit/Delete Tasks

# Front End - Client
- React
- Javascript
- Node
- Axios

# Back End - API
- Django
- Python
- SQL (PostgreSQL)

# Full CRUD

- As a User, Full CRUD for Applications and Tasks
- As an Administrator,  FULL CRUD for Colleges, Applications, Tasks

# Wire Frames

## Home
![Home](assets/home.png)

## Signup/Login
![Login](assets/signupandlogin.png)

## Track Your Colleges
![TrackColleges](assets/trackcolleges.png)

## College Tracking List
![Index](assets/index.png)

## New Application
![NewApp](assets/newapplication.png)

## College Tracking Full Details
![TrackCollegeDetails](assets/collegetrackingdetails.png)

## View Applications 
![ViewApp](assets/viewapplications.png)

# Tasks
![ViewTasks](assets/tasks.png)

# ERD
![ERD](assets/collegetrackr_erd.png)

# Restful Routing API

| METHOD | URL                                      | FUNCTIONALITY           | VIEW               |
|--------|------------------------------------------|-------------------------|--------------------|
| GET    | /collegetkr                              | Home page               |                    |
| GET    | /collegetkr/about                        | About page              |                    |
| GET    | /collegetkr/colleges                     | Index Colleges          |                    |
| POST   | /collegetkr/colleges/create              | Create College          |                    |
| POST   | /collegetkr/colleges/:id/track           | Create CollegeToUser    |                    |
| DELETE | /collegetkr/colleges/:id/untrack         | Delete CollegeToUser    |                    |
| GET    | /collegetkr/colleges/:id                 | Display College         |                    |
| GET    | /collegetkr/apps                         | Index Applications      |                    |
| POST   | /collegetkr/apps/:collegeid/create       | Create Application      |                    |
| PATCH  | /collegetkr/apps/:collegeid/edit/:appid  | Edit Application        |                    |
| DELETE | /collegetkr/apps/:collegeid/delete/:appid| Delete Application      |                    |
| GET    | /collegetkr/tasks/:appid                 | Display Tasks           |                    |        
| POST   | /collegetkr/tasks/:appid/create          | Create Task             |                    |
| PATCH  | /collegetkr/tasks/:appid/edit/:taskid    | Edit Task               |                    |
| DELETE | /collegetkr/tasks/:appid/delete/:taskid  | Delete Task             |                    |
| GET    | /signup                                  | Sign up                 | sign_up            |
| POST   | /signup                                  | Create user             | sign_up            |
| GET    | /login                                   | Sign in                 | login_view         |
| POST   | /login                                   | Log in verification     | login_view         |
| GET    | /logout                                  | Log out                 | logout_view        |

# Home Page

# SETTING UP INSTRUCTIONS

