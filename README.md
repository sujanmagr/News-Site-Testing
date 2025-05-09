****Final QA Testing Report

Project Title: Automated Testing for Ekantipur News Portal****


1. Project Overview
This project aims to automate the core user functionalities of the Ekantipur News Portal (https://ekantipur.com/) using Selenium WebDriver with Python and PyTest, implemented through the Page Object Model (POM) design pattern. This report outlines the objectives, test implementation, dynamic content handling, and results of functional testing.

2. Objective
Automate the main features of the Ekantipur site (Login, Signup, Writing Article, Search, Live Page).
Implement automation using PyTest with Page Object Model.
Handle dynamic content where applicable.
Provide a detailed testing report with test cases and screenshots.
Ensure a professional QA submission with strong documentation.

3. Tools and Technology Used
Tool/Framework	Version/Details
Programming Language	Python 3.x
Automation Tool	Selenium WebDriver
Test Framework	PyTest
Browser	Google Chrome (Latest)
WebDriver Manager	webdriver-manager
Performance Tool	Apache JMeter (in separate doc)
Design Pattern	Page Object Model (POM)

4. Test Environment
Component	Description
OS	Windows 10
Browser	Google Chrome
Python Version	3.x
IDE	VS Code / PyCharm

5. Test Scenarios and Descriptions
5.1 Login Functionality
Test Objective: To verify that users can successfully log in with valid credentials and fail gracefully with invalid ones.
Test Type: Functional
Status: Pass
Screenshot: 


5.2 Signup Functionality
Test Objective: To validate the user registration process on the site.
Test Type: Functional
Status: Pass


Screenshot:


5.3 Write and Save an Article
Test Objective: To ensure that logged-in users can write and save articles.
Test Type: Functional
Actions Covered:
Write Title
Write Summary
Write Full Article
Insert Link
Insert Image
Save Article
Status: Pass
Screenshot: 


5.4 Live Page (Dynamic Tab Handling)
Test Objective: Validate dynamic page loading and new tab management for the live news section.
Dynamic Content Handling:
Switched to new browser tab
Scroll height and looped scrolling for lazy-loaded content
Status: Pass
Screenshot:


5.5 Search Bar (Dynamic Content)
Test Objective: To test the dynamic search dropdown and result population.
Actions Covered:
Open search menu
Enter search query
Scroll through dynamically loaded results
Dynamic Content Handling:
JavaScript scroll
Slider animation and content loading
Status: Pass


Screenshot: 


6. Test Framework and Script Overview
All test scripts were written using PyTest and follow the Page Object Model (POM) design for better modularity and scalability.
Main Script Includes:
Login test with parameterization for multiple users
Signup test with input fields and confirmation
Article writing with UI interactions
Live page interaction using new tab logic
Search bar testing with scrolling and element wait handling

7.Dynamic Content Handling
Dynamic elements were handled using:
WebDriverWait and expected_conditions for loading waits
driver.execute_script() for scrolling and interaction
driver.switch_to.window() for managing browser tabs


7.1 Ad Popup Handling (Dynamic Control)
During the automation process, a dynamic ad popup occasionally appeared on the home page of the Ekantipur site. This popup obstructed interaction with underlying page elements and needed to be closed before proceeding with actions like maximizing the window or clicking on elements.
To handle this dynamically appearing ad, a utility function was implemented to detect and close the ad if it appears, ensuring that the automation flow remains unaffected.
Why This Matters:
Ensures stability of test runs by handling unexpected UI changes.
Demonstrates ability to work with dynamic and intermittent UI controls.
Makes the automation suite more production-ready and resilient to frontend changes.

8. Test Execution Summary
Test Case	Description	Status
Login (valid/invalid)	Check successful/unsuccessful login	Pass
Signup	User account creation	Pass
Write Article	Writing and saving a full article	Pass
Live Page	New tab handling and scroll	Pass
Search Bar	Dynamic content with scroll	Pass

9. Bug Report
No bugs were found during the automation and validation of each feature.

10. Conclusion
The automation suite effectively covered major functionality of the Ekantipur site using Selenium and Python with PyTest. The framework supports maintainability via the Page Object Model and handles dynamic elements, new tabs, and waits efficiently.
The performance testing is documented separately in the performance report.




Appendix
1.Login Test Case Screenshot

2.Signup Test Case Screenshot

3.Write Article Test Case Screenshot

4.Search Page Test Case Screenshot


End of Report

