# 🧠 My Claude Skills

一个专为 [Claude Code](https://claude.ai/code) 打造的 Skill 合集，持续更新中。

## 📦 包含的 Skills

### 🌤️ weather-skill — 查天气
查询任意城市的实时天气和未来 3 天预报。

**触发方式：**
> "帮我查一下台北今天的天气"
> "明天上海会下雨吗？"
> "北京现在多少度？"

**使用的 API：** [Open-Meteo](https://open-meteo.com/)（免费，无需注册）

---

### 📈 stock-skill — 查股票
查询美股、港股、台股的实时价格和涨跌幅。

**触发方式：**
> "苹果股票现在多少钱？"
> "帮我查一下特斯拉今天涨了多少"
> "腾讯港股现在怎么样？"

**使用的 API：** [Yahoo Finance](https://finance.yahoo.com/)（免费，无需注册）

---

## 🚀 安装方法

### 第一步：克隆仓库

```bash
git clone https://github.com/xiaoyu602/my-skills.git
```

### 第二步：链接到 Claude Code

```bash
ln -s ~/你存放的路径/my-skills ~/.claude/skills
```

### 第三步：启动 Claude Code 测试

```bash
claude
```

然后直接问天气或股票，Claude 会自动使用对应的 Skill。

---

## 🛠️ 如何贡献

欢迎提交新的 Skill！格式很简单：

1. 在仓库里新建一个文件夹，如 `my-new-skill/`
2. 在里面创建 `SKILL.md`
3. 提交 Pull Request

---

## 📄 License

MIT License — 随意使用和修改。
