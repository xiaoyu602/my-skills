#!/usr/bin/env python3
"""
生日提醒脚本 — 每周一运行一次
提醒本周（周一到周日）有哪些人过生日
支持阴历和阳历混合
"""

import json
import subprocess
from datetime import datetime, date, timedelta
from pathlib import Path
from lunardate import LunarDate

# 生日数据文件路径
DATA_FILE = Path.home() / "Desktop/my-skills/birthday-skill/birthdays.json"


def load_birthdays():
    if not DATA_FILE.exists():
        print("❌ 找不到生日数据文件，请先用 Claude Code 添加生日")
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def send_notification(title, message):
    script = f'display notification "{message}" with title "{title}" sound name "Glass\"'
    subprocess.run(["osascript", "-e", script])


def lunar_to_solar(lunar_month, lunar_day, year):
    """把阴历日期转换成指定年份的阳历日期"""
    try:
        lunar = LunarDate(year, lunar_month, lunar_day)
        return lunar.toSolarDate()
    except Exception:
        try:
            lunar = LunarDate(year + 1, lunar_month, lunar_day)
            return lunar.toSolarDate()
        except Exception:
            return None


def get_solar_date_this_year(person, year):
    """获取某人今年的阳历生日日期"""
    month, day = map(int, person["date"].split("-"))
    if person.get("type", "solar") == "lunar":
        return lunar_to_solar(month, day, year)
    else:
        try:
            return date(year, month, day)
        except ValueError:
            return None


def main():
    today = date.today()

    # 本周一到周日
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)

    print(f"📅 本周：{monday.strftime('%Y年%m月%d日')} — {sunday.strftime('%m月%d日')}")

    birthdays = load_birthdays()
    print(f"🔍 共有 {len(birthdays)} 条生日记录\n")

    this_week = []

    for person in birthdays:
        name = person["name"]
        birthday_type = "阴历" if person.get("type") == "lunar" else "阳历"

        solar_date = get_solar_date_this_year(person, today.year)
        if solar_date is None:
            continue

        if monday <= solar_date <= sunday:
            days_away = (solar_date - today).days
            this_week.append({
                "name": name,
                "type": birthday_type,
                "date": solar_date,
                "days_away": days_away,
            })

    if this_week:
        # 按日期排序
        this_week.sort(key=lambda x: x["date"])

        for p in this_week:
            if p["days_away"] == 0:
                line = f"🎉 今天！{p['name']}（{p['type']}）"
            elif p["days_away"] == 1:
                line = f"📅 明天 — {p['name']}（{p['type']}）"
            else:
                line = f"📅 {p['date'].strftime('%m月%d日')}（还有{p['days_away']}天）— {p['name']}（{p['type']}）"
            print(line)

        # 合并成一条通知
        summary = "、".join([p["name"] for p in this_week])
        send_notification(
            "🎂 本周生日提醒",
            f"本周过生日：{summary}，记得送上祝福！"
        )
    else:
        print("本周没有人过生日 🙂")


if __name__ == "__main__":
    main()