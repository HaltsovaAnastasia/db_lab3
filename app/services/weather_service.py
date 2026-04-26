from app.repositories.weather_repository import get_weather_by_country_and_date


def format_weather_results(results):
    if not results:
        return "Нічого не знайдено за вказаними параметрами."

    lines = []

    for weather, air in results:
        lines.append("=" * 50)
        lines.append(f"Країна: {weather.country}")
        lines.append(f"Дата й час оновлення: {weather.last_updated}")
        lines.append(f"Напрям вітру: {weather.wind_direction}")
        lines.append(f"Швидкість вітру (kph): {weather.wind_kph}")
        lines.append(f"Кут вітру: {weather.wind_degree}")
        lines.append(f"Схід сонця: {weather.sunrise}")
        lines.append(f"Стан погоди: {air.condition}")
        lines.append(f"Вологість: {air.humidity}")
        lines.append(f"Видимість (км): {air.visibility_km}")
        lines.append(f"Тиск (mb): {air.pressure_mb}")
        lines.append(f"UV index: {air.uv_index}")
        lines.append(
            f"Чи варто виходити на вулицю: {'Так' if air.should_go_outside else 'Ні'}"
        )

    return "\n".join(lines)


def get_formatted_weather(country: str, date_str: str):
    results = get_weather_by_country_and_date(country, date_str)
    return format_weather_results(results)
