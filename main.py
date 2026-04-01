import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import ALL_TOOLS
from skills.trip_briefing import trip_briefing

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("錯誤：請在 .env 中設定 GEMINI_API_KEY")
    sys.exit(1)

client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """你是「旅遊前哨站」，一個專業的旅遊助手 AI。
你可以幫使用者：
- 查詢天氣（使用 weather_tool）
- 搜尋景點（使用 search_tool）
- 產生完整行前簡報（使用 trip_briefing）

請用繁體中文回答。當使用者提到想去某個地方旅遊時，主動提供相關資訊。
當使用者說「出發」或要求行前簡報時，請使用 trip_briefing 工具產生完整簡報。
"""

all_tools = ALL_TOOLS + [trip_briefing]

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        tools=all_tools,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=False,
        ),
    ),
)

print("=== 旅遊前哨站 ===")
print("我是你的旅遊助手！你可以問我天氣、景點、旅遊建議，或說「出發」取得行前簡報。")
print("輸入 quit 結束對話。\n")

while True:
    user_input = input("你：").strip()
    if user_input.lower() in ("quit", "exit", "bye", "再見"):
        print("祝你旅途愉快！再見！")
        break
    if not user_input:
        continue
    try:
        response = chat.send_message(user_input)
        print(f"\n助手：{response.text}\n")
    except Exception as e:
        print(f"\n[錯誤] {e}\n")
