-- Dimension Table: DimDate
CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    Date DATE,
    DayOfWeek VARCHAR(10),
    Month VARCHAR(10),
    Quarter INT,
    Year INT,
    IsWeekend TINYINT(1),
    DayOfYear INT,  -- New field
    WeekOfYear INT, -- New field
    IsHoliday TINYINT(1) -- New field for holiday analysis
);

-- Dimension Table: DimCustomer
CREATE TABLE DimCustomer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    DateOfBirth DATE,
    Age INT, -- New field
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Country VARCHAR(50),
    LoyaltyProgramID INT
) AUTO_INCREMENT = 1;

-- Dimension Table: DimProduct
CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Brand VARCHAR(50),
    UnitPrice DECIMAL(10, 2),
    ProductDescription TEXT, -- New field
    Size VARCHAR(20) -- New field for size (optional)
) AUTO_INCREMENT = 1;

-- Dimension Table: DimStore
CREATE TABLE DimStore (
    StoreID INT PRIMARY KEY AUTO_INCREMENT,
    StoreName VARCHAR(100),
    StoreType VARCHAR(50),
    StoreOpeningDate DATE,
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Country VARCHAR(50),
    ManagerName VARCHAR(100),
    Region VARCHAR(50), -- New field for geographical analysis
    StoreStatus VARCHAR(50) -- New field (e.g., active, closed)
) AUTO_INCREMENT = 1;

-- Dimension Table: DimLoyaltyProgram
CREATE TABLE DimLoyaltyProgram (
    LoyaltyProgramID INT PRIMARY KEY,
    ProgramName VARCHAR(100),
    ProgramTier VARCHAR(50),
    PointsAccrued INT,
    Benefits TEXT -- New field to store tier benefits
);

-- Fact Table: FactOrders
CREATE TABLE FactOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    DateID INT,
    CustomerID INT,
    ProductID INT,
    StoreID INT,
    QuantityOrdered INT,
    OrderAmount DECIMAL(10, 2),
    DiscountAmount DECIMAL(10, 2),
    ShippingCost DECIMAL(10, 2),
    TotalAmount DECIMAL(10, 2),
    OrderStatus VARCHAR(50), -- New field for order status
    PaymentMethod VARCHAR(50), -- New field for payment method
    FOREIGN KEY (DateID) REFERENCES DimDate(DateID),
    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID),
    FOREIGN KEY (StoreID) REFERENCES DimStore(StoreID)
) AUTO_INCREMENT = 1;
