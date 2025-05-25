import Vapor
import Fluent
import FluentSQLiteDriver

@main
struct Run {
    static func main() async throws {
        let app = try await Application.make()

        app.databases.use(.sqlite(.file("db.sqlite")), as: .sqlite)        
        app.http.server.configuration.hostname = "0.0.0.0"
        app.migrations.add(CreateProduct())

        try routes(app)

        try await app.autoMigrate()
        try await app.execute()
    }
}