# AI agent 開發分組實作

> 課程：AI agent 開發 — Tool 與 Skill
> 主題：旅遊前哨站

---

## Agent 功能總覽

這個 Agent 是一個旅遊助手，使用 Google Gemini API 搭配 Function Calling，能根據使用者的自然語言輸入自動呼叫對應工具。

| 使用者輸入           | Agent 行為                             | 負責組員 |
| -------------------- | -------------------------------------- | -------- |
| 「台北天氣如何？」   | 呼叫 weather_tool，查詢即時天氣        | 呂紹銘   |
| 「東京有什麼景點？」 | 呼叫 search_tool，搜尋熱門景點         | 曹世杰   |
| 「我要去台北，出發」 | 執行 trip_briefing Skill，產出行前簡報 | 林楷祐   |

---

## 組員與分工

| 姓名   | 負責功能     | 檔案                      | 使用的 API     |
| ------ | ------------ | ------------------------- | -------------- |
| 呂紹銘 | 天氣查詢     | `tools/weather_tool.py`   | wttr.in        |
| 曹世杰 | 景點搜尋     | `tools/search_tool.py`    | 內建景點資料庫 |
| 林楷祐 | Skill 整合   | `skills/trip_briefing.py` | —              |
| 曹世杰 | Agent 主程式 | `main.py`                 | Gemini API     |

---

## 專案架構

```
├── tools/
│   ├── __init__.py          # 匯出所有工具
│   ├── weather_tool.py      # 天氣查詢工具
│   └── search_tool.py       # 景點搜尋工具
├── skills/
│   ├── __init__.py
│   └── trip_briefing.py     # 行前簡報 Skill
├── main.py                  # Agent 主程式（CLI 入口）
├── requirements.txt         # Python 依賴套件
├── .env                     # 環境變數（GEMINI_API_KEY）
└── README.md
```

---

## 使用方式

```bash
# 1. 建立虛擬環境
python3 -m venv .venv
source .venv/bin/activate

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 設定 API Key（在 .env 中填入）
# GEMINI_API_KEY=你的key

# 4. 啟動 Agent
python main.py
```

---

## 執行結果

```
=== 旅遊前哨站 ===
我是你的旅遊助手！你可以問我天氣、景點、旅遊建議，或說「出發」取得行前簡報。
輸入 quit 結束對話。

你：板橋天氣如何

助手：板橋目前的天氣是：
  氣溫：20°C
  體感溫度：20°C
  濕度：88%
  風速：10 km/h
  天氣描述：小陣雨

你：東京有什麼好玩的

助手：以下是東京的熱門景點推薦：
  1. 淺草寺
  2. 明治神宮
  3. 秋葉原

你：我要去東京，幫我做行前簡報

助手：🗼 東京行前簡報

【天氣概況】
  氣溫：22°C，晴天，體感溫度 21°C

【推薦景點】
  1. 東京鐵塔
  2. 澀谷十字路口
  3. 新宿御苑

祝你旅途愉快！
```

---

## 各功能說明

### 天氣查詢（weather_tool）

- **Tool 名稱**：weather_tool
- **使用 API**：[wttr.in](https://wttr.in)（免費天氣 API）
- **輸入**：城市名稱（支援中英文，如「台北」或「Taipei」）
- **輸出**：溫度、體感溫度、濕度、風速、天氣描述
- **實作細節**：內建中英文城市對照表，自動將中文城市名轉換為英文再查詢

```python
def weather_tool(city: str) -> dict:
    """查詢指定城市的目前天氣狀況。"""
```

### 景點搜尋（search_tool）

- **Tool 名稱**：search_tool
- **使用 API**：內建景點資料庫（涵蓋 14 個城市）
- **輸入**：城市名稱、可選的搜尋關鍵字
- **輸出**：隨機推薦 3 個熱門景點
- **支援城市**：台北、高雄、台中、台南、東京、大阪、京都、首爾、曼谷、新加坡、香港、巴黎、倫敦、紐約

```python
def search_tool(city: str, keyword: str = "") -> dict:
    """搜尋指定城市的熱門景點。"""
```

### Skill：行前簡報（trip_briefing）

- **組合了哪些 Tool**：weather_tool、search_tool
- **執行順序**：

```
Step 1: 呼叫 weather_tool → 取得目的地天氣資訊
Step 2: 呼叫 search_tool → 取得推薦景點列表
Step 3: 組合輸出 → 產生包含天氣與景點的完整行前簡報
```

---

## 技術細節

- **LLM**：Google Gemini 2.5 Flash
- **SDK**：google-genai（Google 官方 Python SDK）
- **核心機制**：Automatic Function Calling — SDK 自動從 Python 函式的 type hints 和 docstring 產生工具定義，Gemini 判斷何時呼叫哪個工具，SDK 自動執行並回傳結果
- **對話模式**：多輪對話（使用 `client.chats.create()` 維持對話歷史）

---

## 心得

### 遇到最難的問題

> 在串接 GEMINI API 時，一直在用Gemini 2.0 Flash Lite 做測試，結果根本沒額度用。後來才發現要切換到 Gemini 2.5 Flash 才有額度，浪費了不少時間在 debug。

### Tool 和 Skill 的差別

> Tool 是單一功能的原子操作（如查天氣、搜景點），Skill 則是組合多個 Tool 來完成更高層次的任務（如行前簡報同時取得天氣和景點資訊）。

### 如果再加一個功能

> （待填寫）
