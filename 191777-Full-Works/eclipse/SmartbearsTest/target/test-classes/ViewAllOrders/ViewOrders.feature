Feature: View all Orders
Given the user on the view all orders page.
Scenarios:Check all button
Given user on the view all orders page.
And user clicks Check all button
Then user should see all orders checked
Scenarios: Uncheck all button
Given user on the view all orders Page
And user clicks Unchecked all button
Then user should see all orders unchecked
Scenarios:Check box checking and unchecking
Given user on the view all orders page
And user clicks desrired order's checkbox
Then user should see desired orders checked/unchecked
Scenarios: Delete selected button
Given user on the view all orders page
And user clicks Delete button.
Then user should see all selected orders Page.
Scenario: Edit
Given user on the view all orders Page
And user clicks Edit
Then user should be able to edit selected order.