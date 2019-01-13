###### Case
The Fenix International Software Team is working on an Exchange Tool, allowing a CSA  (customer service associate) to exchange the ReadyPay kit on a customer’s account to  another model at the wish of the customer.     
Previously if a customer wanted to exchange their kit for a different model, a CSA (customer  service associate) would have to cancel their account, create a new account, and transfer  the balance manually. This was a complex process and had the undesired effect of  cancelling the customer’s original account.     
The new tool will allow the CSA to change the kit on the existing account, and transfer the  balance in one simple form. Aside from being a far simpler process to follow, this also has  the benefit of not cancelling active accounts and affecting historical sales figures.

###### Questions
Write feature tests (and make them pass)for the scenarios for any of the below 2 userstories using a testing tool of your  choice.(behave, cucumber, lettuce) 
```
(1) Given I have made payments on my account,  
As a Customer,   
When I exchange my kit for another model,   
I want to transfer my 'Amount Paid',   
So that I don't lose the money I've already paid to ReadyPay 
 
(2) Given I have days of power remaining on my account,  
As a Customer,   
When I exchange my kit,   
I want the days of power to be transferred to my new kit,   
So that I don't have to make another payment for power immediately.    

(3) As Operations Manager,   
When a CSA processes an exchange,   
I want them to confirm that the contents of the kit are present,   
So that we don't accept incomplete kits from customers and shrink our inventory
```
**N.B.** *[behave](https://behave.readthedocs.io/en/latest/) was used for user-stories (1) and (3).*
  
