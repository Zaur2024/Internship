Feature: Filter Secondary Deals

  Scenario: User can filter the Secondary deals by “want to buy” option

    Given the user opens the main page
    And the user is logged in
    When the user clicks on the Secondary option
    And the user clicks on Filters
    And the user filters by "want to buy"
    And the user clicks Apply Filter
    Then all cards have a "Want to buy" tag


