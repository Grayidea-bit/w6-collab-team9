from tools.weather_tool import weather_tool
from tools.search_tool import search_tool


def trip_briefing(city: str) -> dict:
    """產生指定城市的完整行前簡報，包含天氣、景點推薦和旅遊建議。

    Args:
        city: 目的地城市名稱，例如 Taipei, Tokyo，也支援中文如台北、東京

    Returns:
        包含天氣、景點和建議的完整簡報字典
    """
    weather = weather_tool(city)
    attractions = search_tool(city)
    return {
        "city": city,
        "weather": weather,
        "attractions": attractions,
    }
