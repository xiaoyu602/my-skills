---
name: weather
description: 查询任意城市的实时天气。当用户问到天气、
             气温、下雨、带不带伞等相关问题时，使用本 Skill。
---

# Weather Skill

通过 Open-Meteo API 查询城市天气（免费，无需注册）。

## 步骤

### 第一步：获取城市坐标
调用地理编码 API：
GET https://geocoding-api.open-meteo.com/v1/search?name={城市英文名}&count=1

提取返回结果中的 latitude 和 longitude。

### 第二步：查询天气
GET https://api.open-meteo.com/v1/forecast
  ?latitude={lat}&longitude={lon}
  &current=temperature_2m,weather_code,wind_speed_10m
  &timezone=auto

### 第三步：回复用户
用自然语言描述天气，并给出穿衣/带伞建议。