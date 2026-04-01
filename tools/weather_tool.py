import requests

CITY_MAP = {
    "台北": "Taipei",
    "高雄": "Kaohsiung",
    "台中": "Taichung",
    "台南": "Tainan",
    "東京": "Tokyo",
    "大阪": "Osaka",
    "京都": "Kyoto",
    "首爾": "Seoul",
    "曼谷": "Bangkok",
    "新加坡": "Singapore",
    "香港": "Hong Kong",
    "巴黎": "Paris",
    "倫敦": "London",
    "紐約": "New York",
}


def weather_tool(city: str) -> dict:
    """查詢指定城市的目前天氣狀況。

    Args:
        city: 城市名稱，例如 Taipei, Tokyo, Paris，也支援中文如台北、東京

    Returns:
        包含溫度、濕度、天氣描述的字典
    """
    city_en = CITY_MAP.get(city, city)
    try:
        url = f"https://wttr.in/{city_en}?format=j1"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        current = data["current_condition"][0]
        return {
            "city": city,
            "temperature_c": current["temp_C"],
            "humidity": current["humidity"],
            "description": current["weatherDesc"][0]["value"],
            "feels_like_c": current["FeelsLikeC"],
            "wind_speed_kmph": current["windspeedKmph"],
        }
    except Exception as e:
        return {"city": city, "error": f"天氣查詢失敗：{e}"}
