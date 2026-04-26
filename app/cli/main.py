from app.services.weather_service import get_formatted_weather


def main():
    print("Пошук погоди за країною та датою")
    country = input("Введіть країну: ").strip()
    date_str = input("Введіть дату (YYYY-MM-DD): ").strip()

    result = get_formatted_weather(country, date_str)
    print("\nРезультат:")
    print(result)


if __name__ == "__main__":
    main()
