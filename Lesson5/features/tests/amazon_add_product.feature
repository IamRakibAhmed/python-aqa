Feature: Amazon Product to cart Cart

  Scenario Outline: Add product to cart and verify
    Given Open Amazon page
    When Search for "<product>"
    And Choose the first search result
    And Add the product to the cart
    And The cart count should be greater than 0
    Then "<product>" should be present in the cart

    Examples:
      | product      |
      | iPhone 13 Pro, 256GB, Graphite - Unlocked (Renewed Premium)    |
      | Nescafe Gold Crema (200g) |
