# 轻量级文档阅读器

一个简洁高效的文档展示工具，专为技术文档和项目说明设计。

## 功能特性

- **多格式支持**：支持 TXT 纯文本和 Markdown 文档自动渲染
- **智能目录**：树形结构展示，支持无限层级嵌套
- **搜索功能**：快速定位目标文档
- **暗色模式**：保护眼睛，主题偏好自动保存
- **Mermaid 图表**：支持流程图、甘特图、关系图等
- **自动同步**：GitHub Actions 自动部署，保持文档同步

## 快速开始

### 本地运行

```bash
# 进入项目目录
cd your-project

# 启动本地服务器
python -m http.server 8080
```

访问 http://localhost:8080

### 添加文档

将文档放入 `txt/` 目录即可：

```
txt/
├── 01-项目简介.txt
├── 02-安装部署.txt
├── 03-配置指南.txt
└── 04-使用说明.txt
```

## 配置说明

编辑 `reader/config.json` 自定义网站：

```json
{
  "site_title": "文档阅读器",
  "sidebar_title": "文档目录",
  "theme": "light",
  "enable_search": true,
  "home_page": "01-项目简介.txt"
}
```

## 部署

### Gitee Pages

1. 进入仓库 → 服务 → Gitee Pages
2. 选择分支 `main`，目录 `/reader`
3. 点击启动

### GitHub Pages

推送到 GitHub 仓库后，自动触发 Actions 部署。

## 文档规范

- 文件名使用 UTF-8 编码
- Markdown 支持标题、列表、代码块、表格
- Mermaid 图表使用 ```mermaid 代码块

## 开源协议

MIT License
