Feature: 
    Scenario: Funds transfer from one model to another
        Given customer has made payments on his/her account
        When  customer exchanges his/her kit for another model
        Then  already paid amount should be transferred to the new model
