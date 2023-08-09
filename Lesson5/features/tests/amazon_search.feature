Feature: Verify product information on Amazon search results page

  Scenario: Check presence of product name and image for each product
    Given I am on the Amazon homepage
    When I search for "laptop" using the search bar
    Then I should see a list of search results
    And each search result should have a product name
    And each search result should have a product image
    Then I close the browser
