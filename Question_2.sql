-- Q2 a
SELECT COUNT(OrderID) as speedy_express_orders
FROM (SELECT ShipperID from Shippers WHERE ShipperName = 'Speedy Express') speedyexpress
LEFT JOIN Orders ON speedyexpress.ShipperID = Orders.ShipperID;
-- Answer: 54

-- Q2 b
SELECT MAX(OrderCount), LastName
FROM (
	SELECT COUNT(OrderID) as OrderCount, EmployeeID
    FROM ORDERS GROUP BY(EmployeeID)
) EmployeeOrderCount
LEFT JOIN Employees ON Employees.EmployeeID = EmployeeOrderCount.EmployeeID;
-- Answer: Peacock

-- Q2 c
SELECT MAX(prod_sum), ProductName FROM (
	SELECT SUM(Quantity) as prod_sum, ProductID FROM OrderDetails
	INNER JOIN (
		SELECT OrderID FROM Orders
		INNER JOIN (SELECT CustomerID FROM Customers where Country = 'Germany') Germans 
		ON Orders.CustomerID = Germans.CustomerID
	) German_Orders
	ON OrderDetails.OrderID = German_Orders.OrderID
	GROUP BY ProductID
) Max_German_Product
LEFT JOIN Products
ON Max_German_Product.ProductID = Products.ProductID
-- Answer: Boston Crab Meat
