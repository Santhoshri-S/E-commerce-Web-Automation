# Amazon E-Commerce Web Automation Framework

## 📌 Project Overview

This project is an end-to-end web automation framework developed for automating major workflows of an e-commerce platform similar to Amazon using Playwright with Python and Pytest.

The framework follows industry-standard automation practices such as:

* Page Object Model (POM)
* Data-Driven Testing
* Parallel Execution
* Retry Mechanism
* Allure Reporting
* Screenshot & Video Capture
* Logging Integration
* Scalable Framework Design

---

# 🚀 Features

## ✅ Automated Functionalities

* Product Search
* Product Filtering
* Sort By Price
* Ratings Filter
* Discount Filter
* Pay On Delivery Filter
* Include Out of Stock
* Random Product Selection
* Add To Cart
* Cart Quantity Increment/Decrement
* Proceed To Checkout Validation

---

# 🛠️ Tech Stack

| Technology           | Purpose              |
| -------------------- | -------------------- |
| Python               | Programming Language |
| Playwright           | Browser Automation   |
| Pytest               | Test Framework       |
| Allure Report        | Advanced Reporting   |
| pytest-xdist         | Parallel Execution   |
| pytest-rerunfailures | Retry Failed Tests   |
| Git & GitHub         | Version Control      |

---

# 📂 Project Structure

```text
E-commerce-Web-Automation/
│
├── pages/
│   ├── base_page.py
│   ├── search_bar.py
│   ├── filter_page.py
│   ├── product_page.py
│   ├── cart_page.py
│
├── tests/
│   ├── automation_flow1.py
│   ├── automation_flow2.py
│
├── screenshots/
├── videos/
├── allure-results/
├── allure-report/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🧠 Framework Design

The framework is developed using the Page Object Model (POM) design pattern.

## Advantages of POM

* Reusable code
* Better maintainability
* Easy debugging
* Reduced duplication
* Scalable automation architecture

---

# ⚡ Key Automation Features

## ✅ Dynamic Locator Handling

* XPath using contains()
* Dynamic Playwright locators
* Parent-child hierarchy handling

---

## ✅ Synchronization Handling

* wait_for_selector()
* wait_for_load_state()
* Explicit waits
* scroll_into_view_if_needed()

---

## ✅ Screenshot Integration

Sample Screenshots are automatically captured and attached to Allure reports.

---

## ✅ Video Recording

Playwright video recording is enabled for debugging failed executions.

---

## ✅ Logging Support

Python logging is integrated for execution tracking and debugging.

---

# 📊 Allure Reporting

Allure Report integration provides:

* Step-wise execution details
* Screenshots
* Videos
* Logs
* Failure analysis
* Execution summary

---

# ▶️ Test Execution Commands

## Run All Tests

```bash
pytest
```

---

## Parallel Execution

```bash
pytest -n auto
```

---

## Retry Failed Tests

```bash
pytest --reruns 2
```

---

## Generate Allure Results

```bash
pytest -n auto --alluredir=allure-results
```
---

## Generate Allure Report

```bash
allure generate allure-results --clean
```

---

## Open Allure Report

```bash
cd allure-report
python3 -m http.server 8081
```

Open browser:

```text
http://localhost:8081
```

---
## Direct Trigerring:

```bash
pytest -n auto --alluredir=allure-results

allure generate allure-results --clean

cd allure-report

python3 -m http.server 8081
```

# 📸 Screenshots & Reports

* Screenshots are stored in `screenshots/`

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/efbcc499-e51d-4ca0-b023-32f8d3220816" />
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/8ea10d56-857f-47f4-ae9a-0aec4677d1ca" />

* Videos are stored in `videos/`

  
[fa2d90fba626e27940954f1a29f3db61.webm](https://github.com/user-attachments/assets/5bc06f7f-a422-4877-b7fa-da0c162ce797)

[fc9f7f31346bac3ab13b58a11c4cdc31.webm](https://github.com/user-attachments/assets/3f130842-9426-4a8d-841c-7792f10edb0d)
  
* Allure reports are stored in `allure-report/`
<img width="1530" height="829" alt="image" src="https://github.com/user-attachments/assets/59f84e54-6a1d-4d49-a990-06d953fb8cd8" />

---

# 🧪 Test Scenarios Covered

## Scenario 1

* Search product
* Apply filters
* Open product
* Add to cart
* Increase quantity
* Proceed to checkout

---

## Scenario 2

* Search product
* Apply sorting
* Select random product
* Add to cart
* Validate cart page
* Proceed to login page

---

# 🔥 Advanced Features

* Data-driven testing using parametrization
* Parallel execution support
* Retry mechanism for flaky tests
* Screenshot capture on failure
* Video attachment support
* End-to-end workflow automation

---

# 🚀 Future Enhancements

* API + UI Integration
* Database Validation
* Docker Integration
* Jenkins CI/CD
* GitHub Actions
* Cross-Browser Execution
* Cloud Execution

---

# ⭐ Interview Summary

This project demonstrates a scalable Playwright-Pytest automation framework using industry-standard automation practices including:

* POM Architecture
* Allure Reporting
* Parallel Execution
* Retry Mechanism
* Dynamic Locator Handling
* Logging Integration
* Screenshot & Video Capture

---

# 👨‍💻 Author

Santhoshri S

GitHub:
https://github.com/Santhoshri-S

---
