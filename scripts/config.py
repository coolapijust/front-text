import json
from pathlib import Path

CONFIG_FILE = Path(__file__).parent.parent / 'config.json'

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def get_source_dir():
    return load_config().get('source_dir', 'txt')

def get_site_title():
    return load_config().get('site_title', '文档阅读器')

def get_sidebar_title():
    return load_config().get('sidebar_title', '文档目录')

def get_theme():
    return load_config().get('theme', 'light')

def get_max_content_width():
    return load_config().get('max_content_width', 900)

def get_enable_search():
    return load_config().get('enable_search', False)

def get_enable_back_to_top():
    return load_config().get('enable_back_to_top', True)

def get_exclude_patterns():
    return load_config().get('exclude_patterns', [])

def get_exclude_files():
    return load_config().get('exclude_files', [])

def get_docs_dir():
    return Path(__file__).parent.parent / 'reader' / 'docs'
