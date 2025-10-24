## Интерактивная карта Москвы
Проект создан для отображения интерактивной карты Москвы с местами активного отдыха, с подробными описаниями и комментариями.
В отличие от массовых агрегаторов, карта показывает уникальные и интересные точки, которые не всегда попадают в стандартные подборки.
## Особенности
- Админ-панель для загрузки и редактирования мест
- Загрузка фотографий и сортировка изображений перетаскиванием
- Поддержка WYSIWYG-редактора для длинного описания (description_long)
- API-эндпоинт:
   - ```GET /places/<int:place_id>``` — подробности конкретного места
 
### Установка
1. Клонируем репозиторий
   ```bash
   git clone https://github.com/AKamysheva/The-map.git
   cd The-map/interactive_map
   ```
2. Клонируем frontend
   ```bash
   git clone https://github.com/devmanorg/where-to-go-frontend.git frontend
   ```
3. Создаем виртуальное окружение и устанавливаем все зависимости
   ```bash
   python -m venv venv
   source venv/bin/activate  # или venv\Scripts\activate на Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Создаем .env и добавляем следующее:
   ```python
   SECRET_KEY=ваш secret_key
   ```
4. Создаем папку для медиа-файлов
   ```bash
   mkdir media
   ```
5. Делаем миграции:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Создаём суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
7. Запускаем сервер:
   ```bash
   python manage.py runserver
   ```

Сайт доступен по ссылке: https://akamysheva.pythonanywhere.com/
