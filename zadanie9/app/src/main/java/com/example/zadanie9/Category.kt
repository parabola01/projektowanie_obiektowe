package com.example.zadanie9

data class Category(
    val id: Int,
    val name: String
)

data class Product(
    val id: Int,
    val categoryId: Int,
    val name: String,
    val price: Double
)