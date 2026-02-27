import yaml

try:
    with open('.github/workflows/python-package.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    print('YAML file is valid')
except Exception as e:
    print(f'YAML error: {e}')
