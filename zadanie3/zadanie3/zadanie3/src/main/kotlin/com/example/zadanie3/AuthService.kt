package com.example.zadanie3

import org.springframework.stereotype.Service

@Service
object AuthService {

    private val users = mapOf(
        "admin" to "admin123",
        "user" to "password"
    )

    fun authorize(username: String, password: String): Boolean {
        return users[username] == password
    }

    fun getUsers(): List<String> {
        return users.keys.toList()
    }
}