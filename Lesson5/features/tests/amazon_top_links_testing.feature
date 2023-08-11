Feature: Tests  for amazon BestSellers functionality

  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify the opened page
