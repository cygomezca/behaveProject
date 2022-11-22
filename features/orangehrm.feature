Feature: OrangeHRM Logo
  Scenario: Presencia del logo de OrangeHRM en el home page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser
