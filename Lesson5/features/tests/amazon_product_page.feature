Feature: Verify color selection on product page

  Scenario: Select and verify each color
    Given I am on the product page
    When I select each available color
    Then the selected color should be highlighted
    Then I close the browser
