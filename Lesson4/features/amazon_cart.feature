Feature: Amazon Cart Verification

  Scenario Outline: Add product to cart and verify
    Given I am on the Amazon homepage
    When I search for "<product>"
    And I choose the first search result
    And I add the product to the cart
    And the cart count should be greater than 0
    Then I should see the product "<product>" in the cart

    Examples:
      | product      |
      | iPhone 13 Pro, 256GB, Graphite - Unlocked (Renewed Premium)    |
      | Nescafe Gold Crema (200g) |
