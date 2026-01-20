# 配置文件说明

## 文件位置

```
仓库根目录/
├── config.json              ← 配置文件
├── scripts/
│   ├── config.py            ← 配置读取模块
│   └── sync.py              ← 同步脚本
```

## 完整配置示例

```json
{
  "source_dir": "txt",
  "site_title": "文档阅读器",
  "sidebar_title": "文档目录",
  "theme": "light",
  "max_content_width": 900,
  "enable_search": false,
  "enable_back_to_top": true,
  "exclude_patterns": [
    "drafts/*",
    "private/**",
    "*.bak"
  ],
  "exclude_files": [
    "notes/secret.md",
    "temp.docx"
  ]
}
```

## 变量说明

### 源目录配置

| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `source_dir` | string | `"txt"` | 源文档目录（支持 .txt/.md/.docx） |

### 显示配置

| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `site_title` | string | `"文档阅读器"` | 浏览器标签页标题 |
| `sidebar_title` | string | `"文档目录"` | 侧边栏标题 |
| `theme` | string | `"light"` | 主题：`light` 或 `dark` |
| `max_content_width` | number | `900` | 内容区最大宽度（像素） |
| `enable_search` | boolean | `false` | 是否启用搜索功能 |
| `enable_back_to_top` | boolean | `true` | 是否显示返回顶部按钮 |

### 排除规则

| 变量名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `exclude_patterns` | array | `[]` | 通配符匹配模式 |
| `exclude_files` | array | `[]` | 精确路径匹配 |

## 通配符语法

| 模式 | 匹配范围 | 示例 |
|------|----------|------|
| `*.txt` | 当前目录 | `guide.txt` ✓, `sub/guide.txt` ✗ |
| `**/*.txt` | 任意目录 | `guide.txt` ✓, `sub/guide.txt` ✓ |
| `drafts/*` | 指定文件夹 | `drafts/notes.txt` ✓ |
| `private/**` | 文件夹及子文件 | `private/secret.txt` ✓, `private/sub/secret.txt` ✓ |

## 支持的文件格式

| 源文件 | 输出格式 | 处理方式 |
|--------|----------|----------|
| `.txt` | `.txt` | 直接复制 |
| `.md` | `.html` | Markdown 转换 |
| `.docx` | `.html` | 文本提取+HTML |

## Markdown 支持

- `# 标题1` → `<h1>`
- `## 标题2` → `<h2>`
- `### 标题3` → `<h3>`
- `- 列表项` → `<li>`
- `**粗体**` → `<strong>`
- `| 表格 |` → `<p>`（简单支持）

## DOCX 转换

需要安装依赖：
```bash
pip install python-docx
```

转换规则：
- 大字号粗体 → `<h1>` 或 `<h2>`
- 普通段落 → `<p>`
- 列表项 → `<li>`

## 示例

### 目录结构

```
项目根目录/
├── config.json
├── txt/                      ← source_dir
│   ├── guide.md
│   ├── notes.txt
│   ├── drafts/
│   │   └── draft.txt         ← 被排除
│   └── private/              ← 被排除
└── reader/
    └── docs/
        ├── guide.html        ← 已转换
        ├── notes.txt
        └── ...
```

### 配置

```json
{
  "source_dir": "txt",
  "exclude_patterns": ["drafts/*", "private/**"]
}
```

### 同步输出

```
[Sync] 开始同步...
[Sync] 源目录: /txt/
[Sync] 复制: notes.txt
[Sync] 转换: guide.md → guide.html
[Sync] 排除: drafts/draft.txt
[Sync] 排除: private/secret.md
[Sync] 完成！共同步 2 个文档
```
