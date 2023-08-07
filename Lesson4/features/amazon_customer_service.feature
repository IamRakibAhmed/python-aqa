Feature: Verify Customer Service Page UI Elements

  Scenario: Verify UI elements on Customer Service page
    Given I am on the Customer Service page
    Then I verify the "Welcome to Amazon Customer Service" title is present
    And I verify the Issue Card UI elements are present
    And I verify the "Search our help library" title is present
    And I verify the Help Search bar is present
    And I verify the "All help topics" title is present
    Then I verify the Help Topics UI elements are present
