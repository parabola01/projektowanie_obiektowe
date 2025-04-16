package com.example.zadanie3

import org.springframework.web.bind.annotation.*
import org.springframework.http.ResponseEntity

data class LoginRequest(val username: String, val password: String)
data class LoginResponse(val message: String)

@RestController
@RequestMapping("/api/auth")
class AuthController(private val authService: AuthService) {

    @PostMapping("/login")
    fun login(@RequestBody request: LoginRequest): ResponseEntity<LoginResponse> {
        val authorized = authService.authorize(request.username, request.password)
        return if (authorized) {
            ResponseEntity.ok(LoginResponse("Authorized"))
        } else {
            ResponseEntity.status(401).body(LoginResponse("Unauthorized"))
        }
    }

    @GetMapping("/users")
    fun getUsers(): List<String> {
        return authService.getUsers()
    }
}