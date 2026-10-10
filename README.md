# Flask CI/CD Demo

Учебное Flask-приложение с одной главной страницей и CI/CD-конвейером
на GitHub Actions (Build → Test). СРОП по дисциплине «Прикладные аспекты DevOps».

## Запуск локально
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Открыть: http://127.0.0.1:5000

## Тесты
```bash
pytest -v
```

## CI/CD
Файл `.github/workflows/ci.yml`: при каждом push и pull request запускаются
job `build` (установка зависимостей и проверка сборки) и job `test` (pytest).

Повторный запуск CI после изменения.
