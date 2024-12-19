--Task 1 Database Design

USE CodingChallenge;
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

--Task 2:
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
Select * from Customers;
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
Select * from Accounts;
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
Select * from Transactions;
--Querying Data by Using Joins and Subqueries and Subtotal(Rollup in MSSQL)
--Query 1: List all customers along with their account details using an INNER JOIN.
SELECT C.customer_id, C.first_name, C.last_name, A.account_type, A.balance
FROM Customers C
INNER JOIN Accounts A ON C.customer_id = A.customer_id;

--Query 2: Retrieve the transaction history of a specific customer (e.g., John Doe) using a subquery.
SELECT T.transaction_id, T.transaction_type, T.amount, T.transaction_date
FROM Transactions T
WHERE T.account_id IN (
    SELECT A.account_id
    FROM Accounts A
    JOIN Customers C ON A.customer_id = C.customer_id
    WHERE C.first_name = 'John' AND C.last_name = 'Doe'
);

-- Query 3: Find customers who have made withdrawals and display the amount withdrawn using a JOIN.
SELECT C.first_name, C.last_name, T.amount, T.transaction_date
FROM Customers C
JOIN Accounts A ON C.customer_id = A.customer_id
JOIN Transactions T ON A.account_id = T.account_id
WHERE T.transaction_type = 'withdrawal';


--Query 4: List customers who have zero balance accounts using a JOIN.
SELECT C.first_name, C.last_name, A.account_type, A.balance
FROM Customers C
JOIN Accounts A ON C.customer_id = A.customer_id
WHERE A.balance = 0;

--Query 5: Calculate the total balance for each account type using Subtotal. 
SELECT 
    account_type, 
    SUM(balance) AS total_balance
FROM 
    Accounts
GROUP BY 
    ROLLUP(account_type);

--Queries Using GROUP BY and HAVING Clauses
--Query 6: Count the number of accounts for each account type using GROUP BY.
SELECT account_type, COUNT(account_id) AS account_count
FROM Accounts
GROUP BY account_type;

--Query 7: Get the total amount of withdrawals made by each customer where the 
--total amount exceeds 500 using GROUP BY and HAVING.
SELECT C.first_name, C.last_name, SUM(T.amount) AS total_withdrawals
FROM Customers C
JOIN Accounts A ON C.customer_id = A.customer_id
JOIN Transactions T ON A.account_id = T.account_id
WHERE T.transaction_type = 'withdrawal'
GROUP BY C.first_name, C.last_name
HAVING SUM(T.amount) > 500;

--Query 8: Count the Number of Accounts by Account Type and Filter by Having More Than One Account
SELECT account_type, COUNT(account_id) AS total_accounts
FROM Accounts
GROUP BY account_type
HAVING COUNT(account_id) > 1;
