# 📝 Final QA Testing Report  

## 📌 Project Title  
**Automated Testing for Ekantipur News Portal**  

---

## 1️⃣ Project Overview  
This project automates the **core user functionalities** of the [Ekantipur News Portal](https://ekantipur.com/) using **Selenium WebDriver with Python** and **PyTest**, following the **Page Object Model (POM)** design pattern.  
The report outlines the objectives, test implementation, dynamic content handling, and results of functional testing.  

---

## 2️⃣ Objectives  
- ✅ Automate the main features of the Ekantipur site (Login, Signup, Writing Article, Search, Live Page).  
- ✅ Implement automation using **PyTest** with **POM**.  
- ✅ Handle **dynamic content** where applicable.  
- ✅ Provide a **detailed testing report** with test cases and screenshots.  
- ✅ Ensure a **professional QA submission** with strong documentation.  

---

## 3️⃣ Tools & Technology Used  

| Tool / Framework   | Version / Details |
|--------------------|------------------|
| Programming Language | Python 3.x |
| Automation Tool     | Selenium WebDriver |
| Test Framework      | PyTest |
| Browser             | Google Chrome (Latest) |
| WebDriver Manager   | webdriver-manager |
| Performance Tool    | Apache JMeter *(in separate doc)* |
| Design Pattern      | Page Object Model (POM) |

---

## 4️⃣ Test Environment  

| Component | Description |
|-----------|-------------|
| OS        | Windows 10 |
| Browser   | Google Chrome |
| Python    | 3.x |
| IDE       | VS Code / PyCharm |

---

## 5️⃣ Test Scenarios & Descriptions  

### 🔹 5.1 Login Functionality  
- **Objective:** Verify successful login with valid credentials and failure with invalid ones.  
- **Type:** Functional  
- **Status:** ✅ Pass  
- *Screenshot:* *(to be added)*  

---

### 🔹 5.2 Signup Functionality  
- **Objective:** Validate the user registration process.  
- **Type:** Functional  
- **Status:** ✅ Pass  
- *Screenshot:* *(to be added)*  

---

### 🔹 5.3 Write & Save an Article  
- **Objective:** Ensure logged-in users can write and save articles.  
- **Type:** Functional  
- **Actions Covered:**  
  - Write Title  
  - Write Summary  
  - Write Full Article  
  - Insert Link  
  - Insert Image  
  - Save Article  
- **Status:** ✅ Pass  
- *Screenshot:* *(to be added)*  

---

### 🔹 5.4 Live Page (Dynamic Tab Handling)  
- **Objective:** Validate dynamic page loading and new tab management for live news.  
- **Dynamic Handling:**  
  - Switched to new browser tab  
  - Scroll height & loop scrolling for lazy-loaded content  
- **Status:** ✅ Pass  
- *Screenshot:* *(to be added)*  

---

### 🔹 5.5 Search Bar (Dynamic Content)  
- **Objective:** Test dynamic search dropdown and results.  
- **Actions Covered:**  
  - Open search menu  
  - Enter search query  
  - Scroll through dynamically loaded results  
- **Dynamic Handling:**  
  - JavaScript scroll  
  - Slider animation & content loading  
- **Status:** ✅ Pass  
- *Screenshot:* *(to be added)*  

---

## 6️⃣ Test Framework & Script Overview  
- Written in **PyTest** with **Page Object Model (POM)** for scalability.  
- Includes:  
  - Login test with parameterization  
  - Signup with input validation  
  - Article writing with UI interactions  
  - Live page handling via new tab logic  
  - Search bar testing with waits & scrolling  

---

## 7️⃣ Dynamic Content Handling  

- Used `WebDriverWait` and `expected_conditions` for element loading  
- `driver.execute_script()` for scrolling & interaction  
- `driver.switch_to.window()` for tab handling  

### 🛑 7.1 Ad Popup Handling  
- **Problem:** Ad popup occasionally blocked elements.  
- **Solution:** Utility function detects & closes popup dynamically.  
- **Why It Matters:**  
  - Stabilizes test runs  
  - Handles unexpected UI changes  
  - Makes automation more **production-ready**  

---

## 8️⃣ Test Execution Summary  

| Test Case           | Description                          | Status |
|---------------------|--------------------------------------|--------|
| Login (valid/invalid) | Verify login functionality           | ✅ Pass |
| Signup              | User account creation                | ✅ Pass |
| Write Article       | Writing and saving article           | ✅ Pass |
| Live Page           | Tab handling & scrolling             | ✅ Pass |
| Search Bar          | Dynamic content handling             | ✅ Pass |

---

## 9️⃣ Bug Report  
No bugs were found during automation & validation of features.  

---

## 🔟 Conclusion  
- The automation suite effectively covers major functionality of the **Ekantipur site**.  
- Supports **maintainability** with POM.  
- Efficient handling of **dynamic elements, new tabs, and waits**.  
- **Performance Testing** documented separately.  

---

## 📎 Appendix (Screenshots)  
1. Login Test Case Screenshot  
2. Signup Test Case Screenshot  
3. Write Article Test Case Screenshot  
4. Search Page Test Case Screenshot  

---

✅ *End of Report*  
