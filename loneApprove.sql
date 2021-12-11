
-- branch(branch name, branch city, assets) 
-- customer(customer name, customer street, customer city) 
-- loan(loan number, branch name, amount) 
-- borrower(customer name, loan number)
-- account(account number, branch name, balance ) 
-- depositor(customer name, account number)
-- Consider the above schema. Write a trigger which will check the balance if a customer applies for a loan, and will discard the loan if the loan amount is more than 5 times the balance.
CREATE TRIGGER loan_trigger BEFORE
INSERT ON
loan
FOR
EACH
ROW
BEGIN
    IF NEW.amount > SELECT account.balance*5
    FROM borrower JOIN depositor ON borrower.customer_name = depositor.customer_name JOIN account ON depositor.account_number = account.account_number
    WHERE borrower.loan_number = NEW.loan_number
    THEN
        SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT
    = 'Loan amount is more than 5 times the balance';
END
IF;
END;
