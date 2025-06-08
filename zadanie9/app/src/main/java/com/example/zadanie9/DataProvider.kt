package com.example.zadanie9

object DataProvider {
    val categories = listOf(
        Category(1, "Elektronika"),
        Category(2, "Książki"),
        Category(3, "Odzież")
    )

    val products = listOf(
        Product(1, 1, "Laptop", 3500.0),
        Product(2, 1, "Smartfon", 2500.0),
        Product(3, 2, "Książka", 79.99),
        Product(4, 3, "Koszulka", 49.99),
        Product(5, 3, "Spodnie", 150.00)
    )

    fun getProductsForCategory(categoryId: Int): List<Product> {
        return products.filter { it.categoryId == categoryId }
    }
}
