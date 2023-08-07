Feature: Amazon BestSellers Page Verification

  Scenario: Verify the presence of links on the BestSellers page
    Given I am on the Amazon BestSellers page
    Then I should see 5 links