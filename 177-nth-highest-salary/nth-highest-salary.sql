CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
    
    -- select distinct salary from Employee
    -- group by salary order by salary desc 
    -- limit 1 
    -- offset M

    IFNULL((select distinct salary from Employee
    group by salary order by salary desc 
    limit 1 
    offset M),NULL)

  );
END