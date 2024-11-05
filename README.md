# Contents
**Overview**

**UX**

**Tools Used**

**Testing**

**Deployment**

**Credits**

**Acknowledgments**

# Overview
Foresight is a free micro-blogging social networking application designed using Django. At its core Foresight allows individuals to exchange brief text messages, enabling them to share thoughts, ideas and updates in a concise manner. Users can create short posts that capture their insight or experience, making it easy for others to engage with their content.

In addition to sharing their own messages, users can express their appreciation for the contribution of others by liking posts. This feature not only fosters a sense of community but also encourages positive interactions and feedback among users. By liking content, individuals can show support for their peers, highlight valuable insights and promote a culture of recognition and encouragement within the platform, leaving users with a positive user experience
# UX
The five planes of user experience design (UXD) were critical in guiding this project, serving as a foundational framework that informed every decision made throughout its lifecycle. Each plane – strategy, scope, structure, skeleton, and surface – played a significant role in shaping the final product, ensuring that it not only met functional requirements but also resonated with the users.

## Strategy
At the outset, defining the strategic goals of the project was paramount. This involved understanding the target audience, their needs and the problems we aimed to solve. By conducting user research I was able to establish a clear vision that guided the project. This foundation ensured that every feature developed, aligned with the user expectations. Below is a table consisting of user stories and the criteria that ultimately governed the development of the project.

### User Stories
| Title | User Story | Acceptance Criteria |
| ----------- | ----------- | ----------- |
| Create draft post | As a site Admin I can create draft posts so that I can finish writing the content later. |  AC1: Given a logged in user, they can save a draft post.<br><br>AC2: Then they can finish the content at a later time. |
| View List of posts | As a site user, I can view a paginated list of posts so that I can select which post I want to view. | AC1: Given more than one post in the database, these multiple posts are listed.<br><br>AC2: When a user opens the main page a list of posts is seen. |
| Edit & Delete Posts | As a site user I can modify or delete my posts to keep posts relevant. | AC1: Given a logged in user, they can edit their posts.<br><br>AC2: Given a logged in user, they can delete their posts. |
| Account Creation | As a site user I can register an account so that I can start socialising. | AC1: Given an email a user can register an account.<br><br>AC2: Then the user can log in.<br><br>AC3: When the user is logged in they can add posts. |
| Profile Page | As a site user I can view a page dedicated to my content so that I can keep track of my activities. | AC1: Provided a user is logged in, they can view a profile page.<br><br>AC2: They can then see all posts they've made.<br><br>AC3: The user can view all users that they follow & all users following them.
| Like A Post | As a site user I can like other users posts so that I can show appreciation for what has been written. | AC1: Given a logged in user, they can toggle (like & unlike) an illuminated emoji.<br><br>AC2: Posts display a like counter. |
| Follow Other Users | As a site user I can follow other users so that I can stay in the loop. | AC1: Given a logged in user, they can click to follow other users<br><br>AC2: Given a logged in user, they can see a list of all users they've followed. |
| Update Messages | As a site user I would like to be notified each time I make a change to the site, so that I can stay informed. | AC1: When the user submits a form (makes a change to the database) a message to confirm their choice will be displayed.<br><br>AC2:When the user attempts to submit a form but fails, a message highlighting the issue will be displayed. |
| Profile Picture Upload | As a site user I would like to be able to upload a profile picture, so that my post are better distinguished. | AC1: Users can upload an image to be displayed on their profile page.<br><br>AC2: User profile images will be displayed on all of their posts. |
| Reset Password | As a user I can reset my password in case I have forgotten my password. | AC1: Given an email address, a user can reset their account password.<br><br>AC2: Then a user should be able to login with their new password |
| Informative Browser Tab |As a site user I would like browser tabs to indicate the pages content, so that my web experience is unambiguous.| AC1: Browser tabs should display both the name of the site, and a page title that describes the kind of content found on the page. |
| UX Design | As a site user I desire an enjoyable design so that I am motivated to revisit the website. | AC1: Design a visually appealing and user friendly interface that keeps the focus on the main content without causing distractions. |
| Final Deployment | As a site developer, I need to do a final deployment to Heroku to bring the site online. | AC1: Within Foresight setting, DEBUG is set to False in preparation the for final deployment.<br><br>AC2: Foresight has been deployed to Heroku. |
| Create README file | As a developer, I need to create a README file to guide users and fellow developers of the site. | AC1: Detail the planning process of the site.<br><br>AC2: Detail each feature, and describe their purpose.<br><br>AC3: Detail any issues had when developing the site.<br><br>AC4: Document the source of any support received with the project development. |
| Manual Testing | As a site developer, I need to perform test to ensure the sites code is robust. | AC1: Test site functionality under various use cases.<br><br>AC2: Evidence test findings within README. |

## Scope
Once the strategy was in place, I moved on to defining the scope of the project. This included outlining the specific features and functionalities that would be included in the initial release. By prioritizing features based on user needs and strategic goals, I was able to create a roadmap that balanced ambition with feasibility. In order to deliver a high quality minimal viable product, I focused on the following key features.
- Provide users with page allowing them to read and write posts.
- Provide users with a method to follow other site users activity.
- Provide users with a way to show appreciation for posts.

## Structure
With clear scope established I turned my attention to the structure design of the project. This involved creating information architecture that organized content and features in a logical manner, making it easy for users to navigate the project. flowcharts were developed to visualize how users would interact with the system, ensuring that the structure supported intuitive navigation and efficient task completion. This dimension was critical in laying the groundwork for a seamless user experience. The flowchart below depicts the journey taken through the program when using the website.
- When a user initially logs into the site they will be directed to the home page.
- Providing a user is logged in, they will have full access to the site, and will be presented with all navigational links.
- From here users can navigate to one of the other pages; Profile, Socialize ect. Each time a user changes page, the site with check for authentication.
- If an unauthenticated user accesses the website via a link directed towards a page requiring authentication, the user will simply be directed towards the home page.

## Skeleton

The skeleton plane focused on the layout and interface design, where I transferred the structural blueprint into tangible design elements. This included designing the visual hierarchy, interactive elements and overall aesthetics of the product. By considering usability principle and accessibility standards, I aimed to create an interface that was not only visually appealing but also functional and inclusive. This attention to detail in the skeleton phase was essential for fostering user engagement and satisfaction. 
Balsamiq served as the tool for crafting all the wireframes for this project. Below, you can explore screenshots of the initial project design, which has largely retained its form in the final project, with some minor changes to streamline the appearance.

## Surface
### Features
- Navigation Bar: The navigation bar provides authenticated user with direct links to all site pages, streamlining the user journey, leading to effortless site engagement.

- Paginated post list: The centrepiece of the website is the posts list, prominently displayed on the home page. Here users can explore an array of posts contributed by fellow site members, by using the ‘Next’ and ‘Previous’ buttons conveniently positions at the bottom of the page.

- Post creation form: At the top of the home page, just above the posts, there's a dedicated space where user can express their thoughts and ideas with other members of the site. Simply type in your message and hit the submit button to share your insight.

- Like button: Each post includes a ‘Like’ button that users can click to express their appreciation for the content, signalling to the author that they found the post meaningful and valuably.

- Post Edit/ Delete button: Users have the option to modify or delete their posts with ease by simply clicking on the designated button that corresponds with their desired action, allowing users to make adjustments to their content.

- Profile page: The profile page acts as a focal point for all thinks pertaining to the user. It displays a collection of the users posts, highlights a roster of followers, and profile the user is following. Moreover, users have the option to upload a profile picture, giving their page a personal flair that makes it distinctly their own.

- Follow button: Each profile page features a Follow/ Unfollow button, giving you, the current logged-in user a way of staying connected with the author of your favourite posts. When the button is toggled the profile owner’s username will be added to list of other users that you have previously followed, over on your own profile page.

- Profile list: The Socialize link in the navigation bar takes users to a comprehensive list of all Foresight profiles. Each profile card features a profile pictures, a clickable Username link to the respective profile, and a timestamp showing when the user was last active.

- Login/ Register: The login portal offers secure and user friendly entry for registered users, enabling easy access to the site. Users can quickly log in with their credentials to explore various features. New users can register with Foresight by completing a brief form that includes, choosing a Username, providing a valid Email address for verification, and creating a secure Password.

- Update messages: A message will pop up on screen after the user takes an action, confirming their selections. Notifications will be shown for activities like logging in, deleting a post, and following another user.

### Potential Future Features
- Automated Post Censorship – Have post automatically checked for inappropriate language and replace offensive words with asterisk prior to being submitted to the database. Post will be automatically authorized, making for a more efficient and positive user experience.

# Tools Used
- Balsamiq Wireframes - for creating wireframes & flowcharts

- Git -  for version control and tracking changes

- GitHub - for storing the code

- Gitpod - for developing the project

- Heroku - for deployment of the project

- Bootstrap5 - for developing responsive and mobile first websites

- Google Fonts - for providing the fonts
    
- Favicon.io - for generating the favicon

- Font Awesome - for adding icons in the navbar
    
- Cloudinary - for storing static images

- Chrome Developer Tools - for testing and debugging the website

- Lighthouse - for accessibility and performance reporting

- The W3C Markup Validation Service - for validating HTML

- Jigsaw - for validating CSS

- JSHint - for validating JavaScript

- PEP8 Validator - for validating the python code

# Testing
## Manual Testing
| Feature Referenced | Expected outcome | Testing procedure | Result |
| ----------- | ----------- | ----------- |---------- |
| User Login | Providing a user inputs valid credentials, upon clicking the login button, they will be granted access to all of the sites features. | Attempted logging in to the site, with both superuser credentials, and regular user credentials to confirm full access to the site. | This feature functioned as expected |
| User Logout | Upon clicking the Logout button, users will lose access to the majority of site features and will only be able to view post on the home page. | Clicked on the logout button within the logout page to confirm loss of access. | This feature functioned as expected |
| User Account Signup | Upon submitting a unique username, Email address, and a password of their choosing (providing they meet the sign-up criteria), a user will be allocated a profile page and afforded access to the site. | Create an account by inputting a username, Email address, and a password, then clicking on the sign-up button.<br><br>The form was tested without filling in the Email or username input field, both triggered an error message that guides the user on how to proceed.<br><br>The password field was tested with all numbers, as well as an insufficient number of characters, both triggering an error message that guides the user on how to proceed. | This feature functioned as expected |
| Page Pagination | Providing the list displayed has a number of items(such as posts) greater than the pre-determined paginated limit, then a next button will be displayed at the bottom of the page to take the user to the next page within the list. Consequently a previous button will be displayed that will return the user to previous page within the list. | Due to having a sufficient number of list items, I was able to reduce the paginated limit to a value of 2, 5, and 6, then checked the next and previous buttons were present. | This feature functioned as expected |
| Password Reset | After submitting an Email address that is recognised by the database. The user that is linked to said Email address will be sent an Email containing a link that directed them to a page whereby they can reset their account password. | Clicked on the forgot password link within the login page, and was taken to the reset password form. After submitting the form with the email address linked to my user profile, I was sent a reset password link(Due to reset password portion of Django allauth package not being wired up to an SMTP, the reset link was sent to a file within the projects directory, instead of being sent to my personal email address). After locating and clicking on the link, I was taken to a change password form, that requested two insistences of the new password to be submitted.<br><br>The form was tested without filling in the Email or username input field, both triggered an error message that guides the user on how to proceed.<br><br>The password field was tested with all numbers, as well as an insufficient number of characters, both triggering an error message that guides the user on how to proceed. | This feature functioned as expected |
| Create Post | Providing the form input field is populated with a value, clicking on the ‘Post’ button below will save the given value to the database and display the it on the home page. | Added some text to the post form input field and clicked the submit button. I checked the database, and the home page to confirm the new added value. | This feature functioned as expected |
| Update Post | Once the form submit button on the ‘edit_post’ page has been clicked, the value within the input field should overwrite the previous instance of the post in the database and on the home page. | Clicked the edit post icon to navigate to the edit post page. From there I changed the post’s instance text within the input field, and clicked submit. I then checked to see the changes to the post had taken effect. | This feature functioned as expected |
| Delete Post | When the delete confirmation button is clicked, the post referenced within the URL should be removed from the database. | Clicked on the delete post icon to display the delete post modal. I then clicked the confirm deletion button, before checking both the database, and all site pages containing the mentioned post to confirm all traces of the post were removed. | This feature functioned as expected |
| Like/ Unlike Post | When a user clicks the ‘Like’/ ‘Unlike’ button at the bottom of a post, a count of likes will be incremented/ decremented within the database. This value corresponds with the number displayed within the post(Next to the heart ). | Clicked on the like button within a users post, and checked to see if the posts likes incremented by 1. I then proceeded to the profile of the mentioned post’s author, to confirm the same actions took place there too. | This feature functioned as expected |
| Upload/ Update Profile Image | When an authorized user clicks on the gear icon located near the main image at the top of their profile page, they should be presented with a modal that hosts an upload button. By clicking on the upload button the user should be guided through the process to upload a profile image. | Clicked the gear icon followed by the upload button. From here I selected an image within my PC’s directory, and clicked the button within the panel to select my choice. I was then redirected back to the profile page(with my new image choice showing). | This feature functioned as expected |
| Follow/ Unfollow Profile | Upon clicking a follow button on a profile page, a link to that profile will be added to the authorized user’s profile page. Concurrently a link to the authorized user’s profile will be added to the profile page that corresponds with where the follow button was originally clicked. The unfollow button reverses these actions. | Clicked the follow button on a users profile page, as well as within the Socialize page. Then proceeded to check whether the corresponding profile pages show the correct links on their pages. Ensuring these links disappear after clicking the unfollow button. | This feature functioned as expected |
| View Other User Profile | Upon clicking a user profile page link, the authorized user should be redirected to said page. | Clicked the link(Username) to a profile page from origins across the site. | This feature functioned as expected |
| Update Messages | Authenticated users will be presented with notification messages at the top of the page, upon performing action across the site. The messages should correspond with action taken. | The following tasks were completed to test this functionality, ensuring the correct message was displayed;<br><br>- Logged in/ Logged out<br>- Submitted a post<br>- Edited a post.<br>- Deleted a post<br>- Followed/ Unfollowed a profile page.<br>- Uploaded a profile image<br>- Submit a post whilst unauthenticated. | This feature functioned as expected |

## Solved Bugs
| Feature Referenced | Issue | Solution |
| ----------- | ----------- | ----------- |
| Post Delete Confirmation Button | When clicking on the confirm deletion button within the post delete modal, the primary key of the post wasn't being passed into the URL correctly due to there being too many spaces within the passed value. This resulted in the URL being unrecognised, and an error being raised.<br><br>Another issue with the delete button, is that the post ID would only be passed if the outer area of the bin icon button was clicked and not the icon itself. | Within the button element where the primary key is passed (As an attribute), I removed the excess spaces, and provided a line-break between other attributed within the buttons code to prevent a forced line-break between sensitive values, when saving the file.<br><br>To fix the second bug I simply passed the post ID though the icon as well as the outer area of the button. |
| Cloudinary Images | Within Google Developer tools, the console displayed a warning message, explaining that the Cloudinary images being used were being displayed via an HTTP url, instead of HTTPS. | Within setting.py I configured the URLs being used, and forced Cloudinary to display images with the more secure HTTPS URL. The code for this fix is mentioned in the credits section. |
| Favicon | The Google Developer tools were displaying warning message within the console, stating that the favicon manifest file could be found. | To solve this I removed a line of code within the head element of the base.html file requesting the favicon manifest data. |

## Mobile Devices Used For Testing Responsivity
- iPhone 16 Pro Max

- iPhone 16

- Samsung Galaxy S24 Ultra

- Samsung Galaxy s24 FE
 
- Pixel 9 Pro

- Pixel 9
 
- Pixel 8a
 
- OnePlus 12

- OnePlus 12R
 
- Asus ROG Phone 8 Pro

## Deployment
### Deploy on Heroku
The site was deployed to Heroku using the following steps:
1. Navigate to heroku.com and create an account
2. Click the "New" button in the top right corner
3. Select "Create new app"
4. Enter the app name
5. Select Region and click "Create app"
6. Go to the Settings tab and click "Reveal config vars"
7. Add any necessary config vars
8. Click the Deploy tab
9. Scroll down to Connect to GitHub and sign in / authorize when prompted
10. Find the repository you want to deploy and click "Connect"
11. Scroll down to Manual deploy and choose the main branch
12. Click "Deploy Branch"
13. The app should now be deployed and you can click on the "View" button to view the live site

### Fork the repository
Forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.
1. Navigate to the GitHub Repository you want to fork
2. On the top right of the page under the header, click the "Fork" button
3. This will create a duplicate of the full project in your GitHub Repository.

### Clone the repository
Navigate to the GitHub Repository you want to clone:
1. Click on the "Code" drop down button
2. Click on HTTPS
3. Copy the repository link to the clipboard
4. Open your IDE of choice (git must be installed for the next steps)
5. Type git clone copied-git-url into the terminal
6. The project will now have been cloned on your local machine for use.

# Credit
## Code
- Thanks to tim-mentor for providing the following code within the #bug-reports channel on Slack:

`import cloudinary`

`cloudinary.config(secure=True,)`

- Thanks to the CI walkthrough project for providing me with the some solid starting block for this projects success. Some element reference in my own code include; The Navigation Bar and the Page Nav Buttons.
# Acknowledgments
The completion of this project would not have been possible without the support of my partner; the patience, motivation, and enthusiasm she offers is second to none!