# Amazon Best Sellers | Cart | Customer Service Page Verification

This repository contains code snippets for automating the verification of Amazon's BestSellers page using the Behave framework, Selenium, and classes. The purpose of this automation is to ensure that specific UI elements are present and correct on the BestSellers page.

## Project Structure

- `configuration/Config.py`: Configuration class containing constants for Chrome driver path and various Amazon page URLs.
- `features/`: Directory containing Behave feature files.
  - `amazon_best_sellers.feature`: Feature file containing the scenario for verifying links on the BestSellers page.
  - `amazon_cart.feature`: Feature file containing the scenario outline for adding products to the cart and verifying.
  - `amazon_customer_service.feature`: Feature file containing the scenario for verifying UI elements on the Customer Service page.
  - `steps/`: Directory containing Behave step definitions.
    - `AmazonBestSellersSteps.py`: Step definition file implementing Behave steps for the BestSellers page scenario.
    - `AmazonCartSteps.py`: Step definition file implementing Behave steps for the cart scenario.
    - `AmazonCustomerServiceSteps.py`: Step definition file implementing Behave steps for the Customer Service page scenario.
- `test/`: Directory containing the test definitions.
  - `AmazonBestSellersTest.py`: Class implementing methods for interacting with the Amazon BestSellers page and performing verifications.
  - `AmazonCartTest.py`: Class implementing methods for interacting with Amazon pages and performing cart verifications.
  - `AmazonCustomerServiceTest`: Class providing methods for interacting with the Amazon Customer Service view to verify the presence of the UI elements using Selenium.
- `chromedriver.exe`: ChromeDriver executable for Selenium (you can replace it with the appropriate version for your OS).

## How to Run

1. Install the required dependencies using:
```bash
pip install behave selenium
```

2. Replace `chromedriver.exe` with the appropriate version for your operating system.

3. Run the tests using:
```bash
behave
```


## Features and Steps

### Feature: Amazon BestSellers Page Verification

Scenario: Verify the presence of links on the BestSellers page
- Step: Given I am on the Amazon BestSellers page
 - Opens the Amazon BestSellers page using a ChromeDriver.
- Step: Then I should see {expected_num_links} links
 - Verifies the presence of the expected number of links on the BestSellers page.

### Feature: Amazon Cart Verification

Scenario Outline: Add product to cart and verify
- Step: Given I am on the Amazon homepage
 - Opens the Amazon homepage using a ChromeDriver.
- Step: When I search for "product"
 - Performs a search for the specified product.
- Step: And I choose the first search result 
 - Selects the first search result to proceed.
- Step: And I add the product to the cart 
 - Adds the product to the cart. 
- Step: And the cart count should be greater than 0
 - Verifies that the cart count is updated after adding the product.
- Step: Then I should see the product "product" in the cart
 - Verifies that the added product is present in the cart.

### Feature: Verify Customer Service Page UI Elements

Scenario: Verify UI elements on Customer Service page
- Step: Given I am on the Customer Service page
 - Opens the Customer Service page using a ChromeDriver.
- Step: Then I verify the "Welcome to Amazon Customer Service" title is present
 - Verifies the presence of the specified title on the Customer Service page.
- Step: And I verify the Issue Card UI elements are present
 - Verifies the presence of Issue Card UI elements on the Customer Service page.
- Step: And I verify the "Search our help library" title is present
 - Verifies the presence of the specified title on the Customer Service page.
- Step: And I verify the Help Search bar is present
 - Verifies the presence of the Help Search bar on the Customer Service page.
- Step: And I verify the "All help topics" title is present
 - Verifies the presence of the specified title on the Customer Service page.
- Step: Then I verify the Help Topics UI elements are present
 - Verifies the presence of Help Topics UI elements on the Customer Service page.

### AmazonBestSellersSteps.py
Contains the step definitions for the BestSellers page scenario.

### AmazonBestSellersTest.py
Contains the AmazonBestSellersTest class with methods for interacting with the page and performing verifications.

### AmazonCartSteps.py
Contains the step definitions for the cart scenario.

### AmazonCartVerificationTest.py
Contains the AmazonCartTest class with methods for interacting with pages and performing verifications.

### AmazonCustomerServiceSteps.py
Contains the step definitions for the Customer Service page scenario.

### AmazonCustomerServiceTest.py
Contains the AmazonCustomerServiceTest class with methods for interacting with the Amazon Customer Service page using Selenium.

## Notes

- The provided code snippets are meant for educational purposes and can serve as a starting point for more extensive test automation.

# Convert Number to Reversed Array of Digits

This repository contains a Python script that converts a non-negative number into a reversed array of its digits. The solution addresses the Codewars kata: [Convert number to reversed array of digits](https://www.codewars.com/kata/5583090cbe83f4fd8c000051).

## Problem Description

Given a random non-negative number, the task is to return the digits of this number within an array in reverse order.

**Example:**
- Input: 35231
  Output: [1, 3, 2, 5, 3]

- Input: 0
  Output: [0]

## Usage

1. Make sure you have Python installed on your system.

2. Download or clone this repository to your local machine.

3. Navigate to the project directory containing the `number_converter.py` script.

4. Run the script using the following command:

```bash
python number_converter.py
```

1. Enter a non-negative number when prompted.

2. The script will output the reversed array of digits for the given number.

## Notes
- The provided code is a solution to the Codewars kata and demonstrates a basic understanding of Python and list comprehensions.
