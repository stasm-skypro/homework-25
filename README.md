# 25 FBV и CBV

-- Changelog -- 22-01-2025 --
1. Добалены тесты для приложения Каталог.
2. Добавлены тесты для приложения Блог.
Тесты проверяют корректность работы CRUD-операций, а также фильтрации и увеличения счётчика просмотров.

-- Changelog -- 18-01-2025 --
1. Полностью переработаны шаблоны приложений Каталог и Блог. В частности подверглись рефакторингу шаблоны product_list
и product_detail приложения Каталог, а также шаблоны blog_list и blog_detail приложения Блог.
2. Учтено замечание наставника и проверка publicated из шаблона перенесена в контроллер.
3. Также проведён рефакторинг кода с целью оптимизации и приведения к единому стилю.


## Что сделано?
1.  Имеющиеся в проекте контроллеры переведены с FBV на CBV.
2. Создано новое приложение Блог (blog).
3. Для приложений Каталог (catalog) и Блог (blog) реализовано увеличение счётчика просмотров.
4. Для приложения Блог реализована фильтрация опубликованных статей: в список выводятся только те статьи, которые
имеют положительный признак публикации.
5. Для приложения Блог реализовано перенаправление после успешного редактирования записи на просмотр только что
отредактированной статьи.
6. Для приложений Каталог и Блог реализовано отправление административного оповещения при достижении 100 просмотров
карточки товара в приложении Каталог или статьи в приложении Блог.
7. Для приложений Каталог и Блог реализовано логирование CRUD-операций.

## Что можно переделать?
1. Можно изменить логику редактирования карточек товаров и статей. Для этого нужно добавить регистрацию пользователей,
чтобы редактировать и удалять соответствующий объект мог только автор.
2. Создать отдельную логику просмотра карточек товаров и статей в режиме редактирования и/или удаления. В режиме
обычного просмотра карточки товаров и статьи должны быть доступны только для чтения. Кнопки "Редактировать" и "Удалить"
не должны быть видны. Только после регистрации и перехода в режим редактирования соответствующие кнопки должны
появиться на форме.
3. Для фалов логов нужно предусмотреть их обновление. Например, стирание части записей по определённому алгоритму -
либо при достижении заданного размера файла лога, либо при достижении заданного числа записей.
