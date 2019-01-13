Feature:  
    Scenario: System Privileges for Operation Manager
        Given logged in as an operation manager
        When  a CSA processes an exchange
        Then  I should be able to confirm that the contents of the kit are present
