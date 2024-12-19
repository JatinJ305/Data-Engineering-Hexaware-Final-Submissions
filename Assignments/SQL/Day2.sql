--Task 1 Database Design
USE HMBank;
GO
-- Create Customers Table
CREATE TABLE Customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    DOB DATE NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE,
    phone_number NVARCHAR(15) NOT NULL,
    address NVARCHAR(255)
);

-- Create Accounts Table
CREATE TABLE Accounts (
    account_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    account_type NVARCHAR(20) CHECK (account_type IN ('savings', 'current', 'zero_balance')),
    balance DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Create Transactions Table
CREATE TABLE Transactions (
    transaction_id INT IDENTITY(1,1) PRIMARY KEY,
    account_id INT NOT NULL,
    transaction_type NVARCHAR(20) CHECK (transaction_type IN ('deposit', 'withdrawal', 'transfer')),
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE
);

--Task 2 Select, Where, Between, AND, LIKE:
--Insert at least 10 sample records into each of the following tables.
--Customers
--Accounts
--Transactions
INSERT INTO Customers (first_name, last_name, DOB, email, phone_number, address)
VALUES 
('John', 'Doe', '1985-06-15', 'john.doe@example.com', '1234567890', '123 Elm St, Springfield'),
('Jane', 'Smith', '1990-02-20', 'jane.smith@example.com', '0987654321', '456 Oak St, Springfield'),
('Alice', 'Johnson', '1975-12-01', 'alice.johnson@example.com', '5555555555', '789 Pine St, Springfield'),
('Bob', 'Brown', '1988-07-22', 'bob.brown@example.com', '2222222222', '321 Maple St, Springfield'),
('Charlie', 'Davis', '1995-04-30', 'charlie.davis@example.com', '3333333333', '654 Cedar St, Springfield'),
('Eve', 'Wilson', '1992-10-14', 'eve.wilson@example.com', '4444444444', '987 Birch St, Springfield'),
('Frank', 'Taylor', '1980-09-05', 'frank.taylor@example.com', '7777777777', '159 Spruce St, Springfield'),
('Grace', 'Miller', '1994-03-11', 'grace.miller@example.com', '8888888888', '753 Fir St, Springfield'),
('Hank', 'Anderson', '1982-08-25', 'hank.anderson@example.com', '6666666666', '852 Elm St, Springfield'),
('Ivy', 'Thomas', '1991-05-19', 'ivy.thomas@example.com', '9999999999', '951 Willow St, Springfield');

INSERT INTO Accounts (customer_id, account_type, balance)
VALUES 
(1, 'savings', 1500.00),
(1, 'current', 2500.00),
(2, 'savings', 3000.00),
(2, 'zero_balance', 0.00),
(3, 'current', 5000.00),
(4, 'savings', 800.00),
(4, 'current', 1200.00),
(5, 'savings', 400.00),
(6, 'zero_balance', 0.00),
(7, 'current', 6000.00);

INSERT INTO Transactions (account_id, transaction_type, amount, transaction_date)
VALUES 
(1, 'deposit', 500.00, '2024-01-15 10:00:00'),
(1, 'withdrawal', 200.00, '2024-01-20 15:30:00'),
(2, 'deposit', 1000.00, '2024-01-22 11:15:00'),
(2, 'withdrawal', 500.00, '2024-01-25 09:00:00'),
(3, 'transfer', 1500.00, '2024-01-30 14:45:00'),
(4, 'deposit', 300.00, '2024-02-01 13:20:00'),
(5, 'withdrawal', 100.00, '2024-02-05 12:00:00'),
(6, 'deposit', 200.00, '2024-02-10 16:10:00'),
(7, 'transfer', 1200.00, '2024-02-15 11:30:00'),
(8, 'withdrawal', 50.00, '2024-02-20 10:50:00');

--1. Retrieve the name, account type, and email of all customers
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    a.account_type,
    c.email
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id;

--2. List all transactions corresponding to each customer
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.transaction_date
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id
JOIN 
    Transactions t ON a.account_id = t.account_id;

--3. Increase the balance of a specific account by a certain amount
UPDATE Accounts
SET balance = balance + 100
WHERE account_id = 5; 
select * from Accounts;

--4. Combine first and last names of customers as full_name
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name
FROM 
    Customers;

--5. Remove accounts with a balance of zero where the account type is savings
DELETE FROM Accounts
WHERE balance = 0 AND account_type = 'savings';
select * from Accounts;

--6. Find customers living in a specific city
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name, 
    address
FROM 
    Customers
WHERE 
    address LIKE '%Springfield%';


--7. Get the account balance for a specific account
SELECT 
    balance,account_id
FROM 
    Accounts
WHERE 
    account_id = 3; 

--8. List all current accounts with a balance greater than $1,000
SELECT 
    a.account_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    a.balance
FROM 
    Accounts a
JOIN 
    Customers c ON a.customer_id = c.customer_id
WHERE 
    a.account_type = 'current' AND a.balance > 1000;

--9. Retrieve all transactions for a specific account
SELECT 
    transaction_id,
    transaction_type,
    amount,
    transaction_date
FROM 
    Transactions
WHERE 
    account_id = 1; 

--10. Calculate the interest accrued on savings accounts based on a given interest rate
SELECT 
    a.account_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    (a.balance * 0.05) AS interest_accrued
FROM 
    Accounts a
JOIN 
    Customers c ON a.customer_id = c.customer_id
WHERE 
    a.account_type = 'savings'; 

--11. Identify accounts where the balance is less than a specified overdraft limit
SELECT 
    a.account_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    a.balance
FROM 
    Accounts a
JOIN 
    Customers c ON a.customer_id = c.customer_id
WHERE 
    a.balance < 100; 

--12. Find customers not living in a specific city
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name, 
    address
FROM 
    Customers
WHERE 
    address NOT LIKE '%Springfield%'; 


--Aggregate functions
--1. Find the average account balance for all customers
SELECT 
    AVG(balance) AS average_balance
FROM 
    Accounts;

--2. Retrieve the top 10 highest account balances
SELECT 
    account_id,
    customer_id,
    balance
FROM 
    Accounts
ORDER BY 
    balance DESC
OFFSET 0 ROWS 
FETCH NEXT 10 ROWS ONLY;

--3. Calculate Total Deposits for All Customers on a specific date
SELECT 
    SUM(amount) AS total_deposits
FROM 
    Transactions
WHERE 
    transaction_type = 'deposit' AND 
    CAST(transaction_date AS DATE) = '2024-01-15';  

--4. Find the Oldest and Newest Customers
SELECT 
    MIN(DOB) AS oldest_customer,
    MAX(DOB) AS newest_customer
FROM 
    Customers;

--5. Retrieve transaction details along with the account type
SELECT 
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.transaction_date,
    a.account_type
FROM 
    Transactions t
JOIN 
    Accounts a ON t.account_id = a.account_id;

--6. Get a list of customers along with their account details
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    a.account_id,
    a.account_type,
    a.balance
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id;

--7. Retrieve transaction details along with customer information for a specific account
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.transaction_date
FROM 
    Transactions t
JOIN 
    Accounts a ON t.account_id = a.account_id
JOIN 
    Customers c ON a.customer_id = c.customer_id
WHERE 
    a.account_id = 1;  

--8. Identify customers who have more than one account
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    COUNT(a.account_id) AS number_of_accounts
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
HAVING 
    COUNT(a.account_id) > 1;

--9. Calculate the difference in transaction amounts between deposits and withdrawals
SELECT 
    account_id,
    SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) AS total_deposits,
    SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS total_withdrawals,
    (SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) - 
     SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END)) AS balance_difference
FROM 
    Transactions
GROUP BY 
    account_id;

--10. Calculate the average daily balance for each account over a specified period
SELECT 
    a.account_id,
    AVG(a.balance) AS average_daily_balance
FROM 
    Accounts a
JOIN 
    Transactions t ON a.account_id = t.account_id
WHERE 
    t.transaction_date BETWEEN '2024-01-01' AND '2024-01-31'  -- Specify your date range.
GROUP BY 
    a.account_id;

--11. Calculate the total balance for each account type
SELECT 
    account_type,
    SUM(balance) AS total_balance
FROM 
    Accounts
GROUP BY 
    account_type;

--12. Identify accounts with the highest number of transactions ordered by descending order
SELECT 
    a.account_id,
    COUNT(t.transaction_id) AS number_of_transactions
FROM 
    Accounts a
JOIN 
    Transactions t ON a.account_id = t.account_id
GROUP BY 
    a.account_id
ORDER BY 
    number_of_transactions DESC;

--13. List customers with high aggregate account balances, along with their account types
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    a.account_type,
    SUM(a.balance) AS total_balance
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name, a.account_type
HAVING 
    SUM(a.balance) > 1000;  -- Specify the desired threshold.

--14. Identify and list duplicate transactions based on transaction amount, date, and account
SELECT 
    amount,
    CAST(transaction_date AS DATE) AS transaction_date,
    account_id,
    COUNT(*) AS duplicate_count
FROM 
    Transactions
GROUP BY 
    amount, CAST(transaction_date AS DATE), account_id
HAVING 
    COUNT(*) > 1;


--Task 4 : Subquery and its type:

--1. Retrieve the customer(s) with the highest account balance
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    a.balance
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id
WHERE 
    a.balance = (SELECT MAX(balance) FROM Accounts);

--2. Calculate the average account balance for customers who have more than one account
SELECT 
    AVG(balance) AS average_balance
FROM 
    Accounts
WHERE 
    customer_id IN (
        SELECT 
            customer_id
        FROM 
            Accounts
        GROUP BY 
            customer_id
        HAVING 
            COUNT(account_id) > 1
    );

--3. Retrieve accounts with transactions whose amounts exceed the average transaction amount
SELECT 
    a.account_id,
    a.account_type,
    a.balance
FROM 
    Accounts a
WHERE 
    a.account_id IN (
        SELECT 
            t.account_id
        FROM 
            Transactions t
        WHERE 
            t.amount > (SELECT AVG(amount) FROM Transactions)
    );


--4. Identify customers who have no recorded transactions
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name
FROM 
    Customers c
LEFT JOIN 
    Accounts a ON c.customer_id = a.customer_id
LEFT JOIN 
    Transactions t ON a.account_id = t.account_id
WHERE 
    t.transaction_id IS NULL;


--5. Calculate the total balance of accounts with no recorded transactions
SELECT 
    SUM(a.balance) AS total_balance_no_transactions
FROM 
    Accounts a
WHERE 
    a.account_id NOT IN (
        SELECT 
            DISTINCT t.account_id
        FROM 
            Transactions t
    );

--6. Retrieve transactions for accounts with the lowest balance
SELECT 
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.transaction_date,
    a.account_id,
    a.balance
FROM 
    Transactions t
JOIN 
    Accounts a ON t.account_id = a.account_id
WHERE 
    a.balance = (SELECT MIN(balance) FROM Accounts);

--7. Identify customers who have accounts of multiple types
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name
FROM 
    Customers c
JOIN 
    Accounts a ON c.customer_id = a.customer_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
HAVING 
    COUNT(DISTINCT a.account_type) > 1;

--8. Calculate the percentage of each account type out of the total number of accounts
SELECT 
    a.account_type,
    COUNT(a.account_id) * 100.0 / (SELECT COUNT(*) FROM Accounts) AS percentage
FROM 
    Accounts a
GROUP BY 
    a.account_type;

--9. Retrieve all transactions for a customer with a given customer_id
SELECT 
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.transaction_date,
    a.account_id
FROM 
    Transactions t
JOIN 
    Accounts a ON t.account_id = a.account_id
WHERE 
    a.customer_id = 1;  


--10. Calculate the total balance for each account type, including a subquery within the SELECT clause
SELECT 
    account_type,
    SUM(balance) AS total_balance,
    (SELECT COUNT(*) FROM Accounts) AS total_accounts
FROM 
    Accounts
GROUP BY 
    account_type;
