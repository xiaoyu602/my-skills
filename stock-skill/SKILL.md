---
name: stock
description: 查询股票的实时价格和基本信息。当用户问到股票价格、
             某支股票现在多少钱、涨跌幅、市值等相关问题时，必须使用本 Skill。
             支持美股（如 AAPL、TSLA）和港股（如 0700.HK）。
---

# Stock Skill

通过 Yahoo Finance API 查询股票价格（免费，无需注册）。

## 步骤

### 第一步：确认股票代码

- 用户说"苹果"→ AAPL
- 用户说"特斯拉"→ TSLA
- 用户说"腾讯"→ 0700.HK
- 用户说"台积电"→ TSM（美股）或 2330.TW（台股）
- 如果不确定代码，直接问用户

### 第二步：调用 API

```
GET https://query1.finance.yahoo.com/v8/finance/chart/{股票代码}?interval=1d&range=1d
```

例如查苹果：
```
GET https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=1d&range=1d
```

从返回结果中提取：
- `meta.regularMarketPrice`：当前价格
- `meta.chartPreviousClose`：昨日收盘价
- `meta.currency`：货币单位
- `meta.exchangeName`：交易所名称

### 第三步：计算涨跌幅

```
涨跌幅 = (当前价格 - 昨日收盘) / 昨日收盘 × 100%
```

### 第四步：回复用户

用自然语言回答，包含：
- 股票名称和代码
- 当前价格（含货币单位）
- 涨跌幅（用 📈 或 📉 表示）
- 简单说明（如"今天表现不错"）

## 注意事项

- 股市休市时返回的是最后收盘价，需说明"当前为收盘价"
- 不提供买卖建议，只提供数据