-- myntra database design
CREATE TABLE ProductCategories (
    ProductCategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE Products (
    ProductId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    ProductDescription TEXT NOT NULL,
    ProductPrice INTEGER NOT NULL,
    ProductImage TEXT NOT NULL,
    ProductCategoryId INTEGER NOT NULL,
    FOREIGN KEY (ProductCategoryId) REFERENCES ProductCategories(ProductCategoryId)
);

CREATE TABLE Users (
    UserId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    UserName TEXT NOT NULL,
    UserPassword TEXT NOT NULL,
    UserEmail TEXT NOT NULL,
    UserPhone TEXT NOT NULL,
    UserAddress TEXT NOT NULL,
    UserCity TEXT NOT NULL,
    UserState TEXT NOT NULL,
    UserZip TEXT NOT NULL,
    UserCountry TEXT NOT NULL,
    UserRole TEXT NOT NULL
);



CREATE TABLE Orders (
    OrderId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    OrderDate TEXT NOT NULL,
    OrderStatus TEXT NOT NULL,
    OrderTotal INTEGER NOT NULL,
    UserId INTEGER NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(UserId),

);

CREATE TABLE Payment (
    PaymentId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    PaymentType TEXT NOT NULL,
    Status TEXT NOT NULL,
    OrderId INTEGER NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES Orders(OrderId)
);


CREATE TABLE OrderItems (
    OrderItemId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    OrderId INTEGER NOT NULL,
    ProductId INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES Orders(OrderId),
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);

CREATE TABLE Cart (
    CartId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER NOT NULL,
    ProductId INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(UserId),
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);

CREATE TABLE Wishlist (
    WishlistId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER NOT NULL,
    ProductId INTEGER NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(UserId),
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);

CREATE TABLE FeturedProducts (
    FeaturedProductId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ProductId INTEGER NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);

CREATE TABLE ProductReviews (
    ProductReviewId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ProductId INTEGER NOT NULL,
    UserId INTEGER NOT NULL,
    Review TEXT NOT NULL,
    Rating INTEGER NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);

CREATE TABLE ProductRatings (
    ProductRatingId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ProductId INTEGER NOT NULL,
    UserId INTEGER NOT NULL,
    Rating INTEGER NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId),
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);

CREATE TABLE Address (
    AddressId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    UserId INTEGER NOT NULL,
    Address TEXT NOT NULL,
    City TEXT NOT NULL,
    State TEXT NOT NULL,
    Zip TEXT NOT NULL,
    Country TEXT NOT NULL,
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);



CREATE TABLE SubCategory (
    SubCategoryId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    SubCategoryName TEXT NOT NULL,
    SubCategoryDescription TEXT NOT NULL,
    ProductCategoryId INTEGER NOT NULL,
    FOREIGN KEY (ProductCategoryId) REFERENCES ProductCategories(ProductCategoryId)
);

CREATE TABLE Varients (
    VarientId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Size TEXT NOT NULL,
    Color TEXT, 
    ProductId INTEGER NOT NULL,
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);



