
/* String functions*/
select ascii('CB'); /*return leftmost ascii value*/
select char(66); /*return ascii value to character*/
select len('Microsift sql');/*return length*/
select lower('JHON');/*convert to lowercase*/
select replace('Microsoft sql','sql','server');/*replace*/
select reverse('python');/*reverse the string */
select upper('aparna');/*converts to upper*/
select str(136.564,8,4);/*STR(number, length, decimals)*/

/* Date Functions*/
select  getdate ();/*get current date and time*/
select dateadd (mm, 2, '2023-12-07');/*add months to existed date */
select datediff ( year, convert (datetime, '2006-05-06'), convert ( datetime, '2009-01-01'));/*it will return the difference of date,months,years also*/
select datepart (mm, '2008-5-22');/*return months value*/
select day ( '2023-05-30');/*return value of date of that particular day*/
select month ('2023-05-31');/*return month value*/
select year ( '2023-05-3');/*return year value*/

/*Mathematical Functions*/
select abs(-101);/*returns absolute value*/
select sin(1.5);/*returns angle in radians*/
select ceiling(14.01);/*returns the smallest or greater to the specified value*/
select exp(4.5);/*returns the exponencial value*/
select floor(14.75);
select log(5.4);/*return logarithmic value*/

/*Rankig Functions*/
/* row()_number-giving consecutive numbers to rank*/
select * from employee;
select id,name,salary,ROW_NUMBER() over(order by salary desc) as rownumber
from employee;
select * from employee;
/*rank()-used to give rank if duplicates allowed ranking will be changed based on duplicates  */
select id,name,salary,rank() over(order by salary) as rank
from employee;

/*dense_rank()-used to give ranks consecutively even if duplicates are allowed*/
select id,name,salary,dense_rank() over(order by salary desc) as rank
from employee;

/*ntile() function- it will divide give the rank in groups*/
select id,name,salary,ntile(2) over(order by salary) as rank
from employee;/*without condition*/

select name,salary,ntile(4) over(order by salary) as rank
from employee where salary>10000;/*with condition*/
