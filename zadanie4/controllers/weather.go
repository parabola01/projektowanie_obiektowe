package controllers

import (
	"encoding/json"
	"fmt"
	"net/http"
	"github.com/labstack/echo/v4"
)

type GeocodingResponse struct {
	Results []struct {
		Latitude  float64 `json:"latitude"`
		Longitude float64 `json:"longitude"`
		Name      string  `json:"name"`
	} `json:"results"`
}

type WeatherResponse struct {
	CurrentWeather struct {
		Temperature float64 `json:"temperature"`
		Windspeed   float64 `json:"windspeed"`
	} `json:"current_weather"`
}

type OutputWeather struct {
	City        string  `json:"city"`
	Temperature float64 `json:"temperature"`
	Windspeed   float64 `json:"windspeed"`
}

func GetWeather(c echo.Context) error {
	city := c.QueryParam("city")
	if city == "" {
		return c.String(http.StatusBadRequest, "Brak parametru 'city'")
	}

	geoURL := fmt.Sprintf("https://geocoding-api.open-meteo.com/v1/search?name=%s&count=1", city)
	geoResp, err := http.Get(geoURL)
	if err != nil {
		return c.String(http.StatusInternalServerError, "Błąd pobierania współrzędnych")
	}
	defer geoResp.Body.Close()

	var geoData GeocodingResponse
	err = json.NewDecoder(geoResp.Body).Decode(&geoData)
	if err != nil || len(geoData.Results) == 0 {
		return c.String(http.StatusBadRequest, "Nie udało się znaleźć lokalizacji")
	}

	lat := geoData.Results[0].Latitude
	lon := geoData.Results[0].Longitude
	resolvedName := geoData.Results[0].Name

	weatherURL := fmt.Sprintf("https://api.open-meteo.com/v1/forecast?latitude=%f&longitude=%f&current_weather=true", lat, lon)
	weatherResp, err := http.Get(weatherURL)
	if err != nil {
		return c.String(http.StatusInternalServerError, "Błąd pobierania danych pogodowych")
	}
	defer weatherResp.Body.Close()

	var weather WeatherResponse
	err = json.NewDecoder(weatherResp.Body).Decode(&weather)
	if err != nil {
		return c.String(http.StatusInternalServerError, "Błąd parsowania danych pogodowych")
	}

	output := OutputWeather{
		City:        resolvedName,
		Temperature: weather.CurrentWeather.Temperature,
		Windspeed:   weather.CurrentWeather.Windspeed,
	}

	return c.JSON(http.StatusOK, output)
}
