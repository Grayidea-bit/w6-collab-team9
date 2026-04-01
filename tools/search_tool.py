import random

ATTRACTIONS = {
    "taipei": ["台北101", "故宮博物院", "士林夜市", "象山步道", "龍山寺", "西門町", "大稻埕", "北投溫泉", "貓空纜車", "華山文創園區"],
    "kaohsiung": ["駁二藝術特區", "旗津海岸", "蓮池潭", "美麗島站", "六合夜市", "壽山動物園"],
    "taichung": ["彩虹眷村", "高美濕地", "逢甲夜市", "宮原眼科", "審計新村", "國立自然科學博物館"],
    "tainan": ["赤崁樓", "安平古堡", "花園夜市", "神農街", "奇美博物館", "林百貨"],
    "tokyo": ["淺草寺", "東京鐵塔", "澀谷十字路口", "明治神宮", "築地市場", "秋葉原", "新宿御苑", "上野公園"],
    "osaka": ["大阪城", "道頓堀", "通天閣", "環球影城", "心齋橋", "黑門市場"],
    "kyoto": ["金閣寺", "伏見稻荷大社", "嵐山竹林", "清水寺", "祇園", "二條城"],
    "seoul": ["景福宮", "明洞", "北村韓屋村", "南山塔", "弘大商圈", "廣藏市場"],
    "bangkok": ["大皇宮", "臥佛寺", "恰圖恰市集", "考山路", "水上市場", "暹羅廣場"],
    "singapore": ["魚尾獅公園", "濱海灣金沙", "聖淘沙", "牛車水", "小印度", "植物園"],
    "hong kong": ["維多利亞港", "太平山頂", "迪士尼樂園", "廟街夜市", "星光大道", "大澳漁村"],
    "paris": ["艾菲爾鐵塔", "羅浮宮", "凱旋門", "聖母院", "蒙馬特", "香榭麗舍大道"],
    "london": ["大笨鐘", "倫敦塔橋", "大英博物館", "白金漢宮", "倫敦眼", "海德公園"],
    "new york": ["自由女神像", "時代廣場", "中央公園", "帝國大廈", "布魯克林大橋", "大都會博物館"],
}

CITY_NAME_MAP = {
    "台北": "taipei", "高雄": "kaohsiung", "台中": "taichung", "台南": "tainan",
    "東京": "tokyo", "大阪": "osaka", "京都": "kyoto", "首爾": "seoul",
    "曼谷": "bangkok", "新加坡": "singapore", "香港": "hong kong",
    "巴黎": "paris", "倫敦": "london", "紐約": "new york",
}


def search_tool(city: str, keyword: str = "") -> dict:
    """搜尋指定城市的熱門景點。

    Args:
        city: 城市名稱，例如 Taipei, Tokyo，也支援中文如台北、東京
        keyword: 可選的搜尋關鍵字，用來篩選景點

    Returns:
        包含景點列表的字典
    """
    city_lower = CITY_NAME_MAP.get(city, city.lower())
    spots = ATTRACTIONS.get(city_lower, [])
    if not spots:
        return {"city": city, "attractions": [], "message": f"抱歉，目前沒有 {city} 的景點資料"}
    if keyword:
        spots = [s for s in spots if keyword.lower() in s.lower()]
    selected = random.sample(spots, min(3, len(spots)))
    return {"city": city, "attractions": selected}
