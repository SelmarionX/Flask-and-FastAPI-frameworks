**Task1**

Создать RESTful API для управления списком задач. Приложение должно
использовать FastAPI и поддерживать следующие функции:

○ Получение списка всех задач.

○ Получение информации о задаче по её ID.

○ Добавление новой задачи.

○ Обновление информации о задаче по её ID.

○ Удаление задачи по её ID.

Каждая задача должна содержать следующие поля: ID (целое число),
Название (строка), Описание (строка), Статус (строка): "todo", "in progress",
"done".


**Task2**

Необходимо создать API для управления списком задач. Каждая задача должна
содержать заголовок и описание. Для каждой задачи должна быть возможность
указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:

○ GET /tasks - возвращает список всех задач.

○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.

○ POST /tasks - добавляет новую задачу.

○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.

○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и
ответа. Для этого использовать библиотеку Pydantic.