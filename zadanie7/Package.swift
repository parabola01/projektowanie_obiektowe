// swift-tools-version: 6.1
import PackageDescription

let package = Package(
    name: "projektowanie_obiektowe",
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", from: "4.80.0"),
        .package(url: "https://github.com/vapor/fluent.git", from: "4.8.0"),
        .package(url: "https://github.com/vapor/fluent-sqlite-driver.git", from: "4.0.0"),
    ],
    targets: [
        .executableTarget(
            name: "projektowanie_obiektowe",
            dependencies: [
                .product(name: "Vapor", package: "vapor"),
                .product(name: "Fluent", package: "fluent"),
                .product(name: "FluentSQLiteDriver", package: "fluent-sqlite-driver"),
            ],
            path: "Sources",
            sources: ["."],
            swiftSettings: [
                .unsafeFlags(["-parse-as-library"], .when(configuration: .debug))
            ]
        )
    ]
)
