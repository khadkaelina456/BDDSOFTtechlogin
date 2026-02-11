Feature:Verifying Registration Functionality

    Scenario:Registration successfully
        Given User is on Home Page
        When User click on login button
        And User enters Username
        And User enter Password
        And User click on Login button
        Then User should be registered successfully

    