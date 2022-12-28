<h1  align="center"> OctaneWear Racing webiste </h1>



This is a discussion forum, where simracing fans, simracers, real life racing drivers and fans of any motorsport can come in, discuss various topics and relax with other like-minded individuals.

The idea behind creating a forum is to bring back the old and forgotten art of place where people can share their knowledge and this knowledge will not be removed. Forums like these used to be a lot more common in first decade of this milenia and this project is to highlight its great features.

![amiresponsive snapshot](/readme_assets/amiresponsive.PNG)


## Table of Contents
* [User Experience](#user-experience-uxser-experience)
* [Wireframes](#wireframes)
    * [Desktop](#desktop-view)
    * [Mobile](#mobile-view)
* [Technologies used](#technologies-used)
* [Features](#features)
* [References and sources](#references-and-sources)
* [Testing](#testing)
    * [Testing user experience](#testing-user-experience)
    * [Further testing](#further-testing)
    * [Known bugs](#known-bugs)
    * [Resolved bugs](#resolved-bugs)
* [Future Learnings and features](#future-learnings-and-features)
* [Deployment](#deployment)
* [Credits](#credits)
---
## User Experience (UX)

- ## User stories
    - First Time Visitor Goals
        1. As a first time visitor, I want to be welcomed to the website and straight up understand what to expect
        2. As a first time visitor, I want to be able to navigate the website easily
        3. As a first time visitor, I want to have the option to create a new account and share my thoughts or questions
    - Returning Visitor Goals
        1. As a returning visitor, I want to be able to see what new threads have appeared on the forum
        2. As a returning visitor, I want to keep the discussions flowing and be part of the community
        3. As a returning visitor, I want to be able to clearly see my frieds and who is posting
    - Frequent user goals
        1. As a frequent user, I want to communicate right away
        2. As a frequent user, I want to see changes made in the forum
        3. As a frequent user, I want to be continuously updated about new threads and posts

- ## Design:

- ### Color Scheme:

	-   Using a high contrast black and white with OctaneWear Blue Accents (#197BBD)

- ### Typography:
	-   IBM Plex Sans across the whole forum

    -   No other fonts were used to keep uniformity of the Forum and ease to read

- ### Imagery:
	-   As a functional tool, other than the brand, no other pictures were used

---
* [Go back to top](#table-of-contents)
---
## Wireframes

### Desktop View

-   [Index](https://zheikon.github.io/octanewear_race_team/assets/img/readme/main.png)

-   [Schedule](https://zheikon.github.io/octanewear_race_team/assets/img/readme/schedule.png)

-   [Sponsors](https://zheikon.github.io/octanewear_race_team/assets/img/readme/sponsors.png)

-   [Team](https://zheikon.github.io/octanewear_race_team/assets/img/readme/team.png)

### Mobile View

-   [Index](https://zheikon.github.io/octanewear_race_team/assets/img/readme/mainmobile.png)

-   [Schedule](https://zheikon.github.io/octanewear_race_team/assets/img/readme/schedulemobile.png)

-   [Sponsors](https://zheikon.github.io/octanewear_race_team/assets/img/readme/sponsorsmobile.png)

-   [Team](https://zheikon.github.io/octanewear_race_team/assets/img/readme/teammobile.png)

---
* [Go back to top](#table-of-contents)
---

## Technologies used
 - HTML5
 - CSS3
 - Python3
 - JavaScript
 - Bootstrap
 - Django
 
 ### Frameworks, Libraries & Programs used
  1. Google Fonts were used to import the 'IBM Plex Sans' font into the style.css file which is used on all pages throughout the project.
  2. Photoshop was used to create the logo, resizing images and editing photos for the website.
  3. Balsamiq was used to create the wireframes during the design process.
  4. github is used to store the projects code after being pushed from GitPod.
  5. gitpod is used for writing all of the code and to push project into github.
  6. fontawesome is used for social networks icons and calendar entries.
  7. Heroku is used to run and publish the actual website.
  8. ElephantSQL is used to run and maintain databases required for the project.
  9. Cloudinary is implemented, but not used at present.

---
* [Go back to top](#table-of-contents)
---
## Features

-   Responsive on all device sizes
    
-   Interactive elements

-   Registration, login and logout

-   Admin interface for Superuser

-   Users can add a new threads, post pictures, and add new posts under each thread

-   Every user also can edit and delete their own threads and posts

-   No other user can delete any other posts or threads - Bypassing through using a direct link was disabled

---
* [Go back to top](#table-of-contents)
---
## References and sources

-   Inspiration and some code used from "I think therefore I blog" and "Hello Django" part of training course at Code Institute: https://codeinstitute.net/ie/

-   W3 schools for a lot of CSS assists: https://www.w3schools.com/

-   Used tutorial to understand how to implement Update and Edit Threads from: https://www.youtube.com/watch?v=J7xaESAddDQ&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=6&ab_channel=Codemy.com

-   used JavaScript to slugify title on 'Edit Thread' from StackOverflow: https://stackoverflow.com/questions/1053902/how-to-convert-a-title-to-a-url-slug-in-jquery

-   Used Codemy youtube tutorial to assist me with BootStrap styling of the project and understanding how bootstrap works: https://www.youtube.com/@Codemycom

---
* [Go back to top](#table-of-contents)
---

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- [CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) 

    - [CSS](/readme_assets/css_validated.PNG)

- [HTML Validator](https://validator.w3.org/) 

    - [index](/readme_assets/index_validated.PNG) 
    - [thread](/readme_assets/thread_validated.PNG) 
    - [post-delete](/readme_assets/delete_post_validated.PNG) 
    - [thread-update](/readme_assets/update_thread_validated.PNG)

- LightHouse - Part of Google Chrome

    -   [Index](/readme_assets/lighthouse_index.PNG)
    -   [Thread](/readme_assets/Lighthouse_thread.PNG)
    -   [Add New Thread](/readme_assets/lighthouse_addnewthread.PNG)

---
* [Go back to top](#table-of-contents)
---

#### Testing user experience

- First Time Visitor Goals
 
    - The initial website contains list of newest threads and discussions
    - Header contains links to log in and log out, as well as create a new thread. All threads are visible in easy to navigate form
    - Option to register is visible from anywhere on the website in the header

- Returning Visitor Goals

    - Last updated/created threads are always on the top
    - After single click to the thread, the user is always taken to the latest and newest posts
    - Names of users are highlighted and clearly visible

- Frequent user goals
    
    - Option to stay logged in is present
    - New and updated threads always pop in first

---
* [Go back to top](#table-of-contents)
---

### Further Testing

-   The Website was tested on Google Chrome, Firefox and Brave Browsers
-   The website was viewed on a variety of devices such as Desktop, Laptop, Huawei P30 pro, Huawei P20, iPhone 11.
-   A large amount of testing was done to ensure that all pages were linking correctly and features worked without any issues.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
-   An external group of testers was used to ensure any bugs to be found. Some feedback taken and added into [Future Features](#future-learnings-and-features)

---
* [Go back to top](#table-of-contents)
---

### Known Bugs

- Upvote and Downvote can be casted by single user
- CKeditor used for more advanced formatting does not appear to be mobile friendly


---
* [Go back to top](#table-of-contents)
---

### Resolved Bugs

- **W3 validator was showing that paragraph tags were not ended correctly**
  - this was resolved by having Django insert posts and threads into divs instead of paragraphs
- **Single long word could break the design of website (deliberate damage testing)**
  - fixed by adjusting word wrapping in style.css

---
* [Go back to top](#table-of-contents)
---

## Future Learnings and features

-   Post counter visible from Index page

-   Rich editor for Posts as well as Threads

-   ability to 'reply' to specific posts and including quoted text

-   Profile pages with statistics for users

-   Profile pictures

-   Bio for Profiles

-   Categories, so the Forum can differenciate between vastly different topics

---
* [Go back to top](#table-of-contents)
---

# Deployment

## - GitHub Pages

## - Heroku/ElephantSQL Pages

---
* [Go back to top](#table-of-contents)
---

## Credits

-   The slack team who provided me feedback before submission and helped with testing

-   CodeInstitute Tutors for helping with figuring out the Pagination for Posts

-   Codemy channel on [Youtube](https://www.youtube.com/@Codemycom) for nice and straight forward tutorials

-   StackOverflow for a lot of tips and tricks

-   Google, my best friend!

---
* [Go back to top](#table-of-contents)
---