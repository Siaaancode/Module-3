# Module-3 (INSERT PROJECT NAME HERE)

This project is my final submission for the Module 3 unit of my Web Development course at South Staffordshire College.

Links to GitHub profile and site:

(INSERT LINKS HERE)
(INSERT LINKS HERE)

(IMAGE OF MAIN PAGE HERE)

## Table of Contents

1. [Project information](#project-description)
2. [Strategy](#website-strategy)
3. [User Stories](#user-stories-user-research)
4. [Scope](#website-scope)
5. [Structure](#website-structure)
6. [Skeleton](#website-skeleton)
7. [Surface](#website-surface)
8. [Technologies used](#technologies-used) 
9. [Testing](#testing)
10. [Deployment](#deployment)

# Project Description

This project is being developed to help businesses manage customer bookings in a reliable and organised manner. By creating an easy-to-use and well-structured program, businesses will be able to manage their bookings more efficiently, reducing the risk of overbooking, missed appointments, and unexpected changes. The program will provide a simple and intuitive interface that is easy for users to navigate and understand, helping businesses keep track of their customer bookings with less stress.

# Website Strategy

The strategy of this project is to develop a user-friendly and intuitive table booking system that provides users with an easy and efficient way to create and manage bookings. The primary users of the program will be businesses and the staff responsible for managing their reservations, as well as customers who are looking to visit the business. The project will be specifically targeted towards restaurants, but the program could also be adapted for other businesses that require a booking system, such as hairdressers, barbers, heritage sites, and other visitor attractions.

The booking system will be presented in a simple and easy-to-understand format, allowing customers to quickly and efficiently make reservations. The main information users will be required to enter will be the number of people in their booking, along with their preferred date and time.

Once this information has been submitted, the user will have a limited amount of time to enter their personal details and confirm the booking. The selected time slot will be temporarily held during this process, preventing another customer from booking the same slot before the first user has completed their reservation. This will provide a better user experience by reducing the risk of double bookings and preventing customers from losing their selected time slot while entering their details.

Python will be used as the main programming language to create the functionality and instructions required for the program to operate as expected.

Django will be used as the web framework for developing the application and managing the database. It will allow the system to securely store and manage important booking information, including customer reservations and available time slots for the business.

## Project Goals

1. Develop a functional and reliable booking system that prioritises a positive user experience, ease of use, and efficiency, while making the booking process simple and straightforward for both businesses and their customers. 
2. Develop an intuitive interface that allows customers to quickly and easily make reservations while selecting their preferred booking requirements, including the date, time, and number of guests.
3. Design an intuitive and accessible user interface that prioritises simplicity, clean design, and ease of use, ensuring the application is easy to navigate for users of all experience levels.

## Target Audience

1. Restaurant owners and staff – Users responsible for managing customer reservations and keeping track of bookings.

2. Customers – Users looking to quickly and easily make, view, or manage a restaurant reservation.

## User Stories (User Research)

### Must-have

"As an employee, I need to be able to view all the bookings. This would help me organise and prepared for the day and future days."

Feature: Staff can view current and upcoming reservations in an organised format.

"As a employee, I need to be able to see the details of the bookings. This would help me organise the tables and ensure we have enough seats and staff available for how busy it might be."

Feature: Staff can access important information such as the customer name, number of guests, date and booking time.

"As a restaurant owner, I want to be sure that the restaurant is never overbooked. This would help me maintain a good reputation with customers and avoid disappointment."

Feature: The system uses the restaurant's available capacity to prevent too many customers from being booked for the same time.

"As a customer, I want to be able to easily create, edit and delete my reservation. This would make my life easier and save me time."

Feature: Customers can select the number of guests, date and time they want to book, as well as edit and delete anything they may have got wrong.

"As a customer, I want to receive a booking confirmation. This would help me make sure I haven't got any important information wrong and serve as a reminder for the date and time of my reservation."

Feature: Customers receive a clear confirmation once their reservation has been successfully created.

### Should-have

"As a customer, it would be really useful if there was a period of time where my booking is temporarily reserved while I'm filling out my details, so the slot doesn't get booked by someone else before me"

Feature: Available booking slots are temporarily held while the customer completes their details, helping to prevent the same slot being booked by multiple customers.

"As a customer, it would be really helpful if any fully booked slots and dates were automatically crossed off. This would avoid the disappointment of trying to book a reservation that I can't have."

Feature: The system should clearly show which dates and times are available or unavailable.

### Could-have

"As an employee, it would be really helpful if I could adjust the booking status. With the ability to manage the booking status, we could avoid confusion to if a table has arrived, placed their order, etc."

Feature: Allow staff to mark bookings as confirmed, cancelled, completed, or no-show, placed order, etc.

"As a customer, it would be useful to be able to make special requests. This would be helpful so I could prepare the restaurant for any requests me and my party may have, leaving no room for issues on the day."

Feature: Allow customers to add requests such as accessibility requirements, dietary information, or special occasions.

"As a customer, I might want to sit in a specific area of the restuarant. I would be nice to have the option."

Feature: Allow customers to request a preferred seating area, such as indoor, outdoor, or window seating.

## Research

## Websites Research

### Website 1 - Wangsnoods
https://wangsnoods.com/

1. What's good?

Main page

- Good quality photography of restaurant.
- Key information positioned near the top of the page, allowing users to find important details with minimal scrolling.

Booking System page

- Simple and easy to navigate booking form:
    1. Previous days crossed off.
    2. Any unavailble dates based on party size crossed off.
    3. Gives users the options to choose area they'd like to sit (where available).
    4. Gives additional information below booking section, that is useful for customers to know or be aware of.
    5. When user has chosen date, time, seating area a message appears informing the user of what time the table needs to be available after, ie, booking for 7:30pm, table needs to be returned by 9:15pm. 
    This message pops up again, once the user clicks next to move forward with the booking.
    6. When booking, once users have got to the section of inputting their details, the system starts a countdown timer of 5 minutes where the table is held so it cannot be booked by another user.
    There is a section of the details section where the users can add comments.

Christmas page

- Christmas information available, so users can plan any size of parties or classes.

Standard Menu page

- The menu of this restaurant does change frequenctly but they have offered a sample menu just to give users an idea of what they can expect.

2. What's bad?

- There isn't always a call to action button available on homepage (responsiveness).
- Christmas menu is so small, so it's really hard to read.

3. What features could I use?

- A lot of the booking features I think would be really useful to incorporate to improve user experience and ease of use.
    1. Automatic unavailablilty
    2. Preserved time slots
    3. Choice of seating area

4. What could I improve?

- Some of the pages have a responsiveness issues, as well as image sizing issues.

### Website 2 Pasture
https://pasturerestaurant.com/

1. What's good?

- A clean and well-designed homepage that provides users with a range of useful features and relevant information.
- A clear and easy-to-navigate reservation page with a clean and consistent aesthetic.
- Provides information about walk-in availability and allows users to receive notifications through an “Alert Me” button if a table becomes available due to a cancellation.
- Provides a clear point of contact for enquiries regarding private dining experiences and events.
- Temporarily holds the selected reservation for five minutes while the customer enters their booking details, helping to prevent the table from being booked by another customer.

2. What's bad?

- Dates with no availability are not clearly disabled in the booking system. Instead, users can select an unavailable date before being prompted to choose an alternative location.


3. What features could I use?

- An automatic image slideshow on the homepage that showcases the restaurant and creates a visually engaging experience for users.
- A clean and consistent aesthetic throughout the booking system, with a smooth and intuitive interface that makes it easy for users to navigate and complete their reservation.


4. What could I improve?

- Automatically disables dates that are fully booked, preventing users from selecting unavailable dates and making the booking process more efficient.

### Website 3

1. What's good?

-
-
-

2. What's bad?

-
-
-

3. What features could I use?

-
-
-

4. What could I improve?

-
-
-

## Research Outcomes

Through this research, I developed a clearer understanding of the elements and features required to meet the needs of all users, as well as the standards and best practices that should be followed to ensure the project is effective and user-friendly.

### Top priorities for customers

1. Easy and intuitive booking process: Be able to book a reservation quickly with minimal steps.
2. Booking confirmation: Have confidence that the booking has been successful.
3. Accurate information: Have all required information available and accessible when needed.
4. Easy cancellation and modification: Be able to review, edit and cancel any reservations made.
5. Special requests: Users have the option to add special requests, such as allergies/ dietary requirements, accessibility requests, etc.

### Top priorities for staff

1. Efficient booking management: Be able to view and manage bookings easily.
2. Ability to organise dining experience: Know who has arrived, whos placed a 
drink/food order, etc.
3. Manage special requests: View important booking information, such as, allergies/ dietary requirements, accessibility needs or special occassions.
4. Simple staff interface: Ensuring the system is straightforward and quick to use.

# Website Scope

For this project, I used an Agile development approach, using GitHub Projects to organise, prioritise, and track the development of the web application’s features.

## MVP (minimum viable product)

Each user story has been labelled as either a must-have, should-have, or could-have. The must-have requirements are considered essential and non-negotiable, as they are fundamental to the core purpose of the application. The should-have requirements are important features that add significant value and enhance the overall functionality of the system. The could-have requirements are optional features that would improve the application further but are not essential for meeting the main objectives of the project.

## Features
### Must-Have

- Staff can view current and upcoming reservations in an organised format.
- Staff can access important information such as the customer name, number of guests, date and booking time.
- The system uses the restaurant's available capacity to prevent too many customers from being booked for the same time.
- Customers can select the number of guests, date and time they want to book, as well as edit and delete anything they may have got wrong.
- Customers receive a clear confirmation once their reservation has been successfully created.

### Should-Have

- Available booking slots are temporarily held while the customer completes their details, helping to prevent the same slot being booked by multiple customers.
- The system should clearly show which dates and times are available or unavailable.

### Could-Have

- Allow staff to mark bookings as confirmed, cancelled, completed, or no-show, placed order, etc.
- Allow customers to add requests such as accessibility requirements, dietary information, or special occasions.
- Allow customers to request a preferred seating area, such as indoor, outdoor, or window seating.

## How user features support user stories:

Although responsiveness was not explicitly included as a user story, it is considered a fundamental requirement for any modern web application or program. The application has been designed to provide an accessible and user-friendly experience across a range of devices and screen sizes, ensuring all users can interact with the application effectively.

1. Staff can view current and upcoming reservations in an organised format.
2. Staff can access important information such as the customer name, number of guests, date and booking time.
3. Allow staff to mark bookings as confirmed, cancelled, completed, or no-show, placed order, etc.

Giving staff greater control over bookings can help them manage their shifts more efficiently. Having access to important booking details and an organised overview of reservations can help staff prepare for busy periods and manage customer demand more effectively.

By giving staff the ability to mark reservations, allows them to confidently keep track of the customers visit and ensure a good experience. This could also help staff to manage and spread out the workload, for example, avoid too many orders being needed from the kitchen or bar at one time.

4. The system uses the restaurant's availability capacity to prevent too many customers from being booked for the same time.

Implementing an availability cap for the restaurant can help prevent overbooking, reducing disappointment for customers while also minimising pressure on staff when the restaurant reaches full capacity.

5. Customers can select the number of guests, date and time they want to book, as well as edit and delete anything they may have got wrong.

Giving customers control over these key booking details helps create a positive and user-friendly experience, while reducing the likelihood of errors and frustration during the reservation process.

6. Customers receive a clear confirmation once their reservation has been successfully created.

The system will automatically send a confirmation email and/or message to the customer, providing reassurance that their reservation has been successfully secured. This can improve the overall user experience by giving customers a clear record of their booking and reducing uncertainty.

7.  Available booking slots are temporarily held while the customer completes their details, helping to prevent the same slot being booked by multiple customers.

This feature provides customers with reassurance that their selected booking slot will remain available while they enter their details. It also helps reduce frustration caused by losing a reservation during the booking process, while minimising the risk of double bookings and overbooking for staff.

8. The system should clearly show which dates and times are available or unavailable.

This feature instantly tells the user which dates aren't available for them to book, so they aren't diappointed after entering all their key information. These dates would also automatically change with other pieces of key information added. For example, page loads and the weekend is already all booked up, user enters the party size is 6, it updates to say that there are no slots available for Friday for that party size (but if it was a party of 2, it would be available), user looks at available times on Thursday for the party size, available shots show as bookable.

9. Allow customers to add requests such as accessibility requirements, dietary information, or special occasions.

This feature allows users to share additional information with the restaurant that is specific to their party or booking. Examples included above, but additional examples could be the party needs additional time at the table, party needs highchairs, etc. This helps users express specific needs and staff to be prepared for these needs.

10. Allow customers to request a preferred seating area, such as indoor, outdoor, or window seating.

This specific feature would hold a very minor impact on the user experience but is more of a nice addition. 

# Website Structure

The website will be structured to provide an easy, intuitive, and consistent experience for both customer and staff users.

The homepage will give visitors an immediate insight into the restaurant's atmosphere and identity through a clear navigation bar, engaging hero banner, and informative About Us section.

The navigation bar will provide quick access to key areas of the website, including the About Us section, menu, contact information, and booking call-to-action. It will also include Log In and Sign Up options, allowing users to easily access their accounts and manage their bookings.

The hero banner will feature a selection of high-quality photographs showcasing the restaurant, food, and surroundings. This will give visitors a clear impression of the cuisine, atmosphere, and overall dining experience before making a reservation.

The About section provides users with an engaging introduction to the restaurant, giving them an insight into its atmosphere, values, and overall dining experience. It will also include a description of the cuisine and highlight what makes the restaurant a welcoming and enjoyable place to visit.

The contact section will be incorporated into the website footer, ensuring that it is easily accessible from every page and providing a consistent user experience. It will include the restaurant's address, contact details, and opening hours, allowing customers to quickly find essential information whenever they need it.

## User Journey

When users first visit the website, they will be greeted by the homepage, which provides an introduction to the restaurant and encourages them to explore the website or make a booking. From the homepage, users can navigate to the Booking, About Us, Menu and Contact Us sections.

Users can learn more about the restaurant through the About Us section, which provides information about the restaurant's atmosphere, cuisine and overall dining experience. A call-to-action button will then encourage users to continue to the booking page if they are interested in making a reservation.

Users can also visit the Menu page to explore some of the dishes available at the restaurant. This gives users an idea of what they can expect before visiting. A disclaimer will explain that the menu may change daily and that some dishes are subject to availability.

If users need to find information about the restaurant, they can access the Contact Us section. This will provide the restaurant's address, telephone number, email address and opening hours. The contact information will also be available in the footer across all pages, allowing users to access it easily throughout their journey.

When users are ready to make a reservation, they can select the Booking option from the navigation or one of the call-to-action buttons. The booking process will allow users to select the number of guests, date and time they would like to visit. They can then enter their personal details and provide any special requests or seating preferences before confirming their reservation.

Once the booking has been successfully completed, users will receive a booking confirmation containing their reservation details. This allows them to check that the information is correct and provides a reminder of their upcoming visit. Users will also be able to edit or cancel their reservation if their plans change.

# Website Skeleton
## Wireframes

These wireframes were created during the planning stages of my project to establish a initial layout structure and generate ideas for the functionality to include. They helped to visualise the placement of key information and features, as well as supporting the development of an organised and clean interface. 

### Home Page

![Nav bar / Hero banner](/assets/images/wireframes/home_page/wireframes_home_page_navbar_and_hero_banner.png)
![About us](/assets/images/wireframes/home_page/wireframes_about_us_section.png)
![Contact us](/assets/images/wireframes/home_page/wireframes_contact_us_section.png)

### Menu Page
![Menu](/assets/images/wireframes/menu_page/wireframes_menu_page_menu_and_hero_banner.png)

### Booking Page
![Calender](/assets/images/wireframes/booking_page/wireframes_booking_section_calender.png)
![Information section](/assets/images/wireframes/booking_page/wireframes_booking_section_additional_information.png)
![Details](/assets/images/wireframes/booking_page/wireframes_booking_section_detail_section.png)
![Confirmation](/assets/images/wireframes/booking_page/wireframes_booking_confirmation_page.png)


## Page layout and Interface elements
### (INSERT DIFFERENT PAGE ELEMENTS HERE) 
### (INSERT DIFFERENT PAGE ELEMENTS HERE)
### (INSERT DIFFERENT PAGE ELEMENTS HERE)
### (INSERT DIFFERENT PAGE ELEMENTS HERE)
### (INSERT DIFFERENT PAGE ELEMENTS HERE)

## Responsiveness

Responsive design is an essential industry standard, ensuring that users have a consistent experience across all device sizes. This web application was developed with accessibility as a key priority, following a mobile-first approach. The layout and interface were designed for smaller screens initially, before being progressively enhanced and adapted for larger devices.

All pages of the application achieve a Lighthouse accessibility score of 100, demonstrating a strong commitment to inclusive design and adherence to recognised web accessibility best practices.

# Website Surface
## Design Choice

The design choices made throughout this project were intended to create a clean, modern, and professional aesthetic that aligns with the purpose of the web application. A consistent colour palette, typography, and spacing system were used to establish a strong visual identity while maintaining readability and ease of use. The interface was designed to minimise unnecessary visual clutter, allowing users to focus on the application's core functionality.

## Colour Palette

White - #FFFFFF
Black - #000000
Flag Red - #CC2020

## Typography

For the typography I have chosen GoogleFont' Work Sans (https://fonts.google.com/specimen/Work+Sans?previewlayout=grid&lang=en_Latn&preview.script=Latn&preview.lang=en_Latn). For a secondary font, I will be using monospace as a backup in case the google font fails to load.

# Technologies used (EDIT THESE SO APPROPRIATE)

- HTML, Structure of the website.
- CSS, Styling and layout.
- Javascript, interactivity.
- Git, version control.
- GitHub, Code hosting and project management.
- W3C, Markup and CSS validator.
- JSLint, Javascript validator.
- DevTools, Inspect and Lighthouse.
- WebAIM, Colour contrast checker.
- Favic-o-matic, Favicon generator.
- GoogleFonts, Custom Fonts.
- localStorage API
- Python, Backend functionality and application logic.
- Heroku, Deploy and host the website online.
- Django, Python framework.

# Manual/Automated Testing

# Testing
## W3C Validators (HTML and CSS)

(INSERT IMAGE EXAMPLES OF PASSES)
(INSERT IMAGE EXAMPLES OF PASSES)
(INSERT IMAGE EXAMPLES OF PASSES)

## DevTools
### Lighthouse

(INSERT IMAGE EXAMPLES OF PASSES)
(INSERT IMAGE EXAMPLES OF PASSES)
(INSERT IMAGE EXAMPLES OF PASSES)

## Testing User Stories
### Tested Scenario - Expected Result
### Actual Result

## Testing evaluation
## Final checks

W3C HTML validator - Passed
W3C CSS validator - Passed
DevTools Lighthouse - Passed
Github Pages - Passed

## Test Checklist:
### User Journey: (BY FUNCTION)

# Deployment - GitHub Pages

## How to run this project locally

- First, go to the GitHub Repository for https://github.com/Siaaancode/Module-3
- Click the deployments link, find the most recent deployment and click that, which will open a tab containing the deployed site.
- If a live deployment isn't available, you need to clone the repository to your own machine by typing "git clone" in the terminal, followed by the above link on a local IDE (Integrated Development Environment), such as VSCode.
- Open the project folder within the IDE, open the preview option on one of the HTML files in a browser.


## Steps to deploy this website

- Open GitHub, log in/sign up and create a repository.
- Open the terminal in the IDE and link it to your GitHub account. 
- Then copy the repository information from GitHub to the IDE. This will link them together. 
- Commit your project with commands through the terminal and push them.
- Go back to GitHub and click the settings button, then the pages option.
- Ensure the Source is set to 'Deploy from a branch' and Branch is set to 'main' and '/(root)'
- Once completed, a link at the top of that page will become available. Simply click it, and it will open a new tab of the deployed site. (https://github.com/Siaaancode/Module-3)

## Bugs Discovered

### Fixed

### Not Fixed

# Project Evaluation
## Final screenshots of finished website

# Credits
## Content
## Media

## Code
### ChatGPT



# TO BE DELETED ONCE COMPLETED
## REVIEW USER STORIES AND RE-PRIORITISE THEM