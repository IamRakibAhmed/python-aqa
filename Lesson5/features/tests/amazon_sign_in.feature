Feature: Amazon Sign in tests

 Scenario: Sign in page can be opened from Sign In popup
   Given I am on the Amazon homepage
   When Click Sign In from popup
   Then Verify Sign In page opens
   Then I close the browser