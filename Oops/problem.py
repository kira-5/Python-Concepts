# covering inheritance, encapsulation, polymorphism, abstraction, composition, access modifiers, attributes, method chaining, method overloading, and method overriding.


# Design a system for a library management software where users can borrow, return, and reserve books. The system should support multiple users with different roles such as librarians and patrons.

# Create a class hierarchy for the system including classes such as Library, User, Book, Librarian, and Patron.
# Implement inheritance by creating subclasses for different types of users, such as Librarian and Patron, inheriting from the base class User.
# Implement encapsulation by making appropriate member variables and methods private or protected, and providing public methods for accessing and modifying data. Ensure that access to sensitive information is restricted to only authorized classes or methods.
# Utilize polymorphism by implementing methods like borrowBook() and returnBook() in both Librarian and Patron classes, with different implementations depending on the user type.
# Implement abstraction by creating interfaces for common functionalities like Borrowable and Returnable, which can be implemented by classes like Book and LibraryItem.
# Use composition by including objects of one class within another, such as having a Library class contain a collection of Book objects.
# Demonstrate the use of access modifiers (public, private, protected) to control access to member variables and methods within classes, ensuring that only necessary components are exposed to external classes or subclasses.
# Implement attributes within classes to store additional information about users, books, and library items, such as user IDs, book titles, and due dates.
# Enable method chaining by designing methods in a way that allows them to return the current object (this) to support consecutive method calls.
# Implement method overloading by creating multiple versions of methods with the same name but different parameter lists, such as returnBook(Book book) and returnBook(String bookId).
# Demonstrate method overriding by allowing subclasses to provide their own implementation of methods inherited from superclasses, such as toString() method in Book class overriding the toString() method in the Object class.





# Design a banking system that supports various operations for customers including account management, transactions, and online banking functionalities.

# Create a class hierarchy for the banking system including classes such as Bank, Account, Customer, and Transaction.
# Implement inheritance by creating subclasses for different types of accounts, such as SavingsAccount and CheckingAccount, inheriting from the base class Account.
# Implement encapsulation by making appropriate member variables and methods private or protected, and providing public methods for accessing and modifying data. Ensure that sensitive information like account balances and customer details are securely managed.
# Utilize polymorphism by implementing methods like withdraw() and deposit() in both SavingsAccount and CheckingAccount classes, with different implementations based on account type.
# Implement abstraction by creating interfaces for common functionalities like Accountable and Transactable, which can be implemented by classes like Account and Transaction.
# Use composition by including objects of one class within another, such as having a Bank class contain a collection of Account objects.
# Demonstrate the use of access modifiers (public, private, protected) to control access to member variables and methods within classes, ensuring appropriate data protection.
# Implement attributes within classes to store additional information about accounts and transactions, such as account numbers, transaction IDs, and transaction amounts.
# Enable method chaining by designing methods in a way that allows them to return the current object (this) to support consecutive method calls, such as chaining multiple transactions together.
# Implement method overloading by creating multiple versions of methods with the same name but different parameter lists, such as deposit(double amount) and deposit(double amount, String currency).
# Demonstrate method overriding by allowing subclasses to provide their own implementation of methods inherited from superclasses, such as calculateInterest() method in SavingsAccount overriding the same method in the Account class.



# Easy:
# Problem Statement:
# Design a simple calculator application that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The application should allow users to input two numbers and select an operation, then display the result.

# Medium:
# Problem Statement:
# Design a task management application that allows users to create, update, and delete tasks. Each task should have a title, description, due date, and status (e.g., pending, completed). The application should support features such as sorting tasks by due date or status, marking tasks as completed, and filtering tasks based on different criteria.
# Problem Statement:
# Design a weather forecasting application that retrieves weather data from an API and displays it to users. The application should allow users to search for weather forecasts by city name, display current weather conditions, and provide a 5-day forecast. Additionally, users should be able to save their favorite cities for quick access to weather information.



# Hard:
# Problem Statement:
# Design a flight booking system for an airline company that allows users to search for flights based on criteria such as departure city, destination city, date, and number of passengers. The system should display available flights matching the search criteria, allow users to select seats, and proceed with booking. Ensure that the system handles complexities such as seat availability, booking conflicts, and cancellations, and provides a user-friendly interface for managing reservations.