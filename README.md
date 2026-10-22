# Module-3 Kokoro Restaurant

This project is my final submission for the Module 3 unit of my Web Development course at South Staffordshire College.

Links to GitHub profile and site and Heroku:

[GitHub Profile](https://github.com/Siaaancode/Module-3)
(INSERT LINKS HERE)
(INSERT LINKS HERE)

![Nav bar / Hero banner](/bookings/static/images/home_page_readme/home_page_readme_image.png)

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

Python will be used as the main programming language to create the functionality and logic required for the program to operate as expected.

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

When users are ready to make a reservation, they can select the Booking option from the navigation or one of the call-to-action buttons. Before a user can make a booking, they will be directed to the login page. If they have not signed up a button will be available for them to do so. Once the user has logged in or signed up, they are redirected back to the homepage and the book now button becomes available, this then directs them to the booking page. The booking process will allow users to select the number of guests, date and time they would like to visit. They can then enter their personal details and provide any special requests or seating preferences before confirming their reservation.

Once the booking has been successfully completed, users will receive a booking confirmation containing their reservation details. This allows them to check that the information is correct and provides a reminder of their upcoming visit. Users will also be able to edit or cancel their reservation if their plans change.

# Website Skeleton
## Wireframes

These wireframes were created during the planning stages of my project to establish a initial layout structure and generate ideas for the functionality to include. They helped to visualise the placement of key information and features, as well as supporting the development of an organised and clean interface. 

### Home Page

The home page will be designed with a clean, minimalist aesthetic, using a limited colour palette and concise content to create a professional and welcoming first impression. The layout will aim to avoid unnecessary clutter, allowing users to identify key information and navigate the website easily.

The navigation bar will feature a minimal selection of links to provide straightforward access to the main sections of the website, including the menu, booking system, restaurant information and contact details. This approach will aim to keep navigation simple and ensure users can find the features they need without unnecessary complexity.

The hero banner is planned to include a carousel of AI-generated images showcasing the restaurant's atmosphere, dining experience and kitchen. The carousel will automatically rotate through the images, adding visual interest while helping users develop an impression of the restaurant before making a booking.

The About Us and Contact sections will be included to provide essential restaurant information and explain what customers can expect from their visit. These sections will aim to make important details easy to find while helping users become familiar with the restaurant.

Overall, the wireframe will focus on establishing a clear visual hierarchy, maintaining consistency and providing an accessible, user-friendly starting point for visitors to the website.

![Nav bar / Hero banner](/bookings/static/images/wireframes/home_page/wireframes_home_page_navbar_and_hero_banner.png)
![About us](/bookings/static/images/wireframes/home_page/wireframes_about_us_section.png)
![Contact us](/bookings/static/images/wireframes/home_page/wireframes_contact_us_section.png)

### Menu Page

The menu page will be designed to present the restaurant's food offerings in a clear and organised layout, allowing customers to browse the available dishes easily. The design will follow the same minimalist aesthetic and colour palette planned for the home page to maintain visual consistency throughout the website.

The menu will be organised into clearly defined sections, with headings to distinguish between different food categories. This structure will aim to make dishes easy to locate while avoiding an overcrowded layout. The wireframe will focus on arranging the content in a logical order, ensuring that users can browse the menu without feeling overwhelmed.

The page will aim to give customers a convenient way to explore the restaurant's offerings before making a reservation. By prioritising readability, simple navigation and a consistent design, the proposed layout will support an accessible and user-friendly experience.

![Menu](/bookings/static/images/wireframes/menu_page/wireframes_menu_page_menu_and_hero_banner.png)

### Booking Page

The booking page will be designed to provide customers with a simple and intuitive way to reserve a table at the restaurant. The layout will aim to maintain consistency with the rest of the website, using clear labels, a straightforward structure and an uncluttered design to make the booking process easy to understand.

An interactive calendar, planned to be powered by FullCalendar, will allow customers to select their preferred booking date visually. The page will also include input fields for the number of guests and an available booking time, helping customers find a suitable reservation based on their party size and the restaurant's availability.

The booking system will be designed to check table availability and prevent overlapping reservations, reducing the risk of overbooking. Clear feedback will be provided if a selected date, time or party size cannot be accommodated. Customers will also be able to access their profile to view, edit or cancel existing reservations.

Overall, the wireframe will prioritise usability, clear communication and efficient booking management. The aim will be to create a straightforward booking experience for customers while supporting restaurant staff in managing table availability.

![Calender](/bookings/static/images/wireframes/booking_page/wireframes_booking_section_calender.png)
![Information section](/bookings/static/images/wireframes/booking_page/wireframes_booking_section_additional_information.png)
![Details](/bookings/static/images/wireframes/booking_page/wireframes_booking_section_detail_section.png)
![Confirmation](/bookings/static/images/wireframes/booking_page/wireframes_booking_confirmation_page.png)

### Error 404 page

The 404 error page wireframe was intentionally kept simple, as its primary purpose is to clearly communicate that the requested page could not be found while providing users with a straightforward way to navigate back to the home page. The minimal layout helps keep the message clear and avoids unnecessary distractions during the error experience.

![Error404](/bookings/static/images/wireframes/error_404/wireframe_404_page.png)


## Page layout and Interface elements

### Homepage

#### Navigation Bar

#### Hero Banner

#### About Us Section

#### Contact Us

#### Footer


### Menu page


### Login page


### Sign up page


### Booking page


### User Profile

#### Edit booking

#### Cancel booking


### Error 404 page


## Responsiveness

Responsive design is an essential industry standard, ensuring that users have a consistent experience across all device sizes. This web application was developed with accessibility as a key priority, following a mobile-first approach. The layout and interface were designed for smaller screens initially, before being progressively enhanced and adapted for larger devices.

All pages of the application achieve a Lighthouse accessibility score of 100, demonstrating a strong commitment to inclusive design and adherence to recognised web accessibility best practices.

# Website Surface
## Design Choice

The design choices made throughout this project were intended to create a clean, modern, and professional aesthetic that aligns with the purpose of the web application. A consistent colour palette, typography, and spacing system were used to establish a strong visual identity while maintaining readability and ease of use. The interface was designed to minimise unnecessary visual clutter, allowing users to focus on the application's core functionality.

## Colour Palette

White - #FFFFFF
Black - #000000
Red - #ff0000

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
- Jest, Javascript testing.
- DevTools, Inspect and Lighthouse.
- WebAIM, Colour contrast checker.
- Favic-o-matic, Favicon generator.
- GoogleFonts, Custom Fonts.
- Python, Backend functionality and application logic.
- Heroku, Deploy and host the website online.
- Django, Python framework.
- FullCalendar, Javascript event calendar library.
- Neon, cloud-hosted PostgreSQL database
- WhiteNoise, Static file serving.
- Gunicorn, WSGI application server for Django

# Database SCHEMA

The Kokoro restaurant booking system uses a relational database to store and manage customer accounts, restaurant tables and bookings. The database is managed through Django's Object-Relational Mapper (ORM), which allows the application to create, retrieve, update and manage records using Python models.

The database consists of three main entities: User, Table and Booking. These entities are connected through relationships that help organise booking information, associate reservations with customers and allocate tables according to their seating capacity.

## Entity Relationship Overview

The database contains the following models:

User Model – Stores customer account information using Django's built-in authentication system.
Table Model – Stores information about the restaurant's tables, including their seating capacity and active status.
Booking Model – Stores reservation details and links each booking to a customer and, where applicable, an allocated table.

The relationships between these entities are:

User to Booking: One user can have multiple bookings, but each booking belongs to one user. This is a one-to-many relationship.
Table to Booking: One table can be associated with multiple bookings over time, but each booking can be allocated to one table. This is also a one-to-many relationship.

These relationships reduce unnecessary duplication of data and allow the application to retrieve related information efficiently.

1. User Model

The User model uses Django's built-in authentication model to manage customer accounts and authentication.

| Field | Description |
| --- | --- |
| id | Automatically generated primary key that uniquely identifies each user |
| username | The username used to identify the account. |
| password | Stores a securely hashed password through Django's authentication system. |
| first_name | Stores the user's first name when provided. |
| last_name | Stores the user's surname when provided. |
| email | Stores the user's email address when provided. |

The Booking model has a foreign key relationship with User. This associates each reservation with the customer who created it and allows customers to view and manage their own bookings.

2. Table Model

The Table model represents the tables available in the restaurant. It allows the application to consider seating capacity and whether a table is active when allocating reservations.

| Field | Description |
| --- | --- |
| id | Automatically generated primary key that uniquely identifies each table record. |
| table_number | A unique number identifying the restaurant table. |
| seats | The maximum number of guests the table can accommodate. |
| is_active | A Boolean field indicating whether the table is available for allocation within the booking system. |

The table_number field must be unique, preventing two table records from having the same table number. The seats field allows the application to select tables with sufficient capacity for the requested party size.

The is_active field allows tables to be excluded from new bookings when they are not in service. The Table model is connected to the Booking model through a foreign key relationship.

3. Booking Model

The Booking model stores the details of restaurant reservations and connects customers with their allocated tables.

| Field | Description |
| --- | --- |
| id | Automatically generated primary key that uniquely identifies each booking. |
| user | A foreign key linking the booking to the customer who created it. |
| table | An optional foreign key linking the booking to an allocated restaurant table. |
| booking_date | The date of the reservation. |
| booking_time | The requested start time of the reservation. |
| guests | The number of guests included in the booking. |
| duration_minutes | The expected duration of the reservation in minutes. |
| status | Records the current status of the booking. |

The user foreign key uses on_delete=models.CASCADE, meaning that deleting a user also deletes their associated booking records. The table foreign key uses on_delete=models.PROTECT, preventing a table from being deleted while booking records still reference it. The table relationship is optional at database level, allowing a booking record to exist without an allocated table where necessary.

The booking date and time fields can also be empty at database level. The application is responsible for validating the booking details before accepting a reservation.

### Booking Status Choices

The Booking model uses predefined status choices to represent the state of a reservation.

| Status | Description |
| --- | --- |
| confirmed | The reservation has been confirmed. |
| cancelled | The reservation has been cancelled and should no longer prevent the table from being booked. |
| completed | The reservation has been completed. |

Using predefined choices helps maintain consistent status values throughout the application. Cancelling a booking changes its status rather than immediately deleting the record, preserving a record of the reservation.

### Data Integrity and Booking Availability

The application uses database relationships and validation logic to help maintain the integrity of booking records and reduce the risk of double bookings.

- Table identification: Each table has a unique table number.
- Seating capacity: The application considers the number of guests when selecting a suitable table.
- Active tables: Only tables marked as active are considered for new reservations.
- Booking conflicts: The application checks whether a table already has a booking that overlaps with the requested reservation period.
- Booking duration: Reservations use a default duration of 120 minutes to calculate when a table becomes available again.
- Opening hours: The application validates booking times against its configured opening hours, from 12:00 to 22:00.
- Date and time validation: The application checks that the requested reservation meets its date and time requirements.
- Cancellation handling: Cancelled bookings are excluded from availability checks so that their tables can become available for future reservations.
- Customer ownership: Customers can manage their own bookings, while the application checks booking ownership when editing or cancelling reservations.

The application uses Django's database transactions when creating bookings to help ensure that the allocation process is handled as a single unit of work. Availability checks and table allocation logic are intended to prevent overlapping reservations for the same table.

Together, these models and validation rules provide the foundation for managing customer reservations, allocating restaurant tables and maintaining consistent booking information.

# Manual/Automated Testing

## Jest (Javascript testing)

### SCREENSHOTS OF TESTS PASSING

## Automated testing using Django's built-in testing framework

### List of tests I've done and screenshots of passing

# Testing
## W3C Validators (HTML and CSS)

W3C HTML validator - Passed

Homepage

![Homepage](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_home_page.png)

Menu page

![Menu page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_menu_page.png)

Login page

![Login page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_log_in_page.png)

Sign up page

![Sign up page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_sign_up_page.png)

Profile page

![Profile page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_profile_page.png)

Booking page

![Booking page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_booking_page.png)

Edit booking page

![Edit booking page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_edit_booking_page.png)

Cancel booking page

![Cancel booking page](/bookings/static/images/html_w3c_validator/heroku_w3c_html_validator_cancel_booking_page.png)

W3C CSS validator - Passed

![styles.css](/bookings/static/images/css_w3c_validator/css_w3c_validator_styles.png)

## DevTools
### Lighthouse

DevTools Lighthouse - Passed

Homepage

![Home page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_home_page.png)

Menu page

![Menu page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_menu_page.png)

Login page

![Login page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_login_page.png)

Sign up page

![Sign up page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_sign_up_page.png)

Profile page

![Profile page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_profile_page.png)

Booking page

![Booking page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_booking_page.png)

Edit booking page

![Edit booking page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_edit_booking_page.png)

Cancel booking page

![Cancel booking page](/bookings/static/images/devtools_lighthouse/devtools_lighthouse_cancel_booking_page.png)

## Testing User Stories
### Tested Scenario - Expected Result
### Actual Result

## Testing evaluation
## Final checks

## Test Checklist:
### User Journey: (BY FUNCTION)

# Deployment

## GitHub Pages Deployment

### How to run this project locally

- First, go to the GitHub Repository for https://github.com/Siaaancode/Module-3
- Click the deployments link, find the most recent deployment and click that, which will open a tab containing the deployed site.
- If a live deployment isn't available, you need to clone the repository to your own machine by typing "git clone" in the terminal, followed by the above link on a local IDE (Integrated Development Environment), such as VSCode.
- Open the project folder within the IDE, open the preview option on one of the HTML files in a browser.


### Steps to deploy this website

- Open GitHub, log in/sign up and create a repository.
- Open the terminal in the IDE and link it to your GitHub account. 
- Then copy the repository information from GitHub to the IDE. This will link them together. 
- Commit your project with commands through the terminal and push them.
- Go back to GitHub and click the settings button, then the pages option.
- Ensure the Source is set to 'Deploy from a branch' and Branch is set to 'main' and '/(root)'
- Once completed, a link at the top of that page will become available. Simply click it, and it will open a new tab of the deployed site. (https://github.com/Siaaancode/Module-3)

## Heroku Deployment

### How to deploy on Heroku

The Kokoro restaurant booking system is deployed using Heroku. The application uses Django for the backend, Neon for the PostgreSQL database, and WhiteNoise to serve static files.

To deploy the application, follow these steps:

1. Prepare the project: Ensure the Django application runs locally and that the required dependencies are listed in requirements.txt.

2. Configure the Python version: Create a .python-version file in the project root and specify the Python version used by the application.

3. Configure the application server: Create a Procfile in the project root to tell Heroku how to start the Django application using Gunicorn.

4. Configure environment variables: Set the required environment variables in Heroku, including the database connection string and Django secret key. Keep sensitive credentials out of the Git repository.

5. Configure static files: Configure Django's static file settings and WhiteNoise so that CSS, JavaScript and other static assets can be served in production.

6. Set up the database: Configure the application to connect to the Neon PostgreSQL database and apply any outstanding database migrations.

7. Deploy the application: Commit the project changes to Git and push the code to the Heroku deployment branch, or trigger a deployment through the connected GitHub repository.

8. Verify the deployment: Open the deployed website and test the main functionality, including account registration, login, booking creation, booking editing, cancellation and static file loading.

## Bugs Discovered

### Fixed

1. Getting Bootstrap CSS to work with Django: I was using the wrong href links to make the CSS compatible with the Django framework. ie, "css/style.css" instead of 
``` {% raw %}{% static 'css/styles.css' %}{% endraw %}. ```

2. Couldn't commit because of the first bug documented: Github uses Jekyll and it interperates the above fix as an issue in the readme file. Commenting the line and adding the 
```{% raw %} and {% endraw %} ``` 
fixed the issue.

3. Error of only 1 available time showing on the booking: The issue was incorrect indentation on these lines of code in the views.py file.
``` current += interval and return JsonResponse({"times": times}) ```

4. Exposure of secret key:

5. Exposure of DATABASE_URL:


### Not Fixed


# Project Evaluation

## Evaluation of project goals

1. Develop a functional and reliable booking system that prioritises a positive user experience, ease of use, and efficiency, while making the booking process simple and straightforward for both businesses and their customers. 

2. Develop an intuitive interface that allows customers to quickly and easily make reservations while selecting their preferred booking requirements, including the date, time, and number of guests.

3. Design an intuitive and accessible user interface that prioritises simplicity, clean design, and ease of use, ensuring the application is easy to navigate for users of all experience levels.

- Did I achieve the goals?
- Did the goals change?

## Final screenshots of finished website

# Credits

## Content
### VSCode

Generated content by VSCode:
1. Content in the about us section
2. Menu items

## Media
### ChatGPT

All images on the homepage carousel were generated by ChatGPT.

## Code
### ChatGPT

I used ChatGPT to understand how I could extend the requirements for the sign up form. Django offered simple requirements, but I wanted additional elements, like firstname, surname and email.

I created a form.py file to add this information:


    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User


    class SignUpForm(UserCreationForm):
        first_name = forms.CharField(max_length=30,     required=True)
        last_name = forms.CharField(max_length=30,  required=True)
        email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
