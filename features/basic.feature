# Created by marina_senyutina at 9/27/17
@basic
Feature: #Enter feature name here
  # Enter feature description here

  @basic1
  Scenario: Add item to the cart by using search field
    Given Enter "fox" into the search field
    Then Click the search button
    Then Count all elements in array with more then "4" stars
    And Click on category by img: "Product Details"
    When Change quantity: "3"
    And Change delivery address: "94040"
    And Add items to to cart
    Then Verify "3" amount of items were added to the cart


  @basic2
  Scenario: Add item using Departments menu
    Given Click on any element on home page by text: "Departments"
    And Click on department category: "Books"
    And Click on category by img: "Best Books of September"
    Then Create list of all elements in carousel
    And Select the first available item
    When Change quantity: "3"
    Then Add items to to cart
    Then Verify "3" amount of items were added to the cart


  @basic3
  Scenario: Verify that you can add item into the cart using categories
    Given Click on any element on home page by text: "Departments"
    And  Click on department category: "Textbooks"
    And  Click on category by text: "Science & Mathematics"
    Then Click on category by text: "Mathematics"
    Then Click on category by img: "Product Details"
    Then Choose format
    Then Choose only new one
    Then Choose "3"th item
#    Then Verify 1 amount of items were added to the cart
