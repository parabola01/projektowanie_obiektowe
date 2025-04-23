package main

import (
	"github.com/labstack/echo/v4"
	"example.com/zadanie4/controllers"
)

func main() {
	e := echo.New()
	e.GET("/weather", controllers.GetWeather)
	e.Logger.Fatal(e.Start(":8080"))
}
