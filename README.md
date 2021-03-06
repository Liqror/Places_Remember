# Places-Remember
## Цель
Создать веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещаемых местах.
 
## Описание задачи
Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает кнопки “Войти с помощью Facebook/VK”, нажимая на которую FB/VK предлагает ему разрешить доступ к его базовой информации.

Он разрешает доступ, после чего должна открыться страница. В ее шапке будет имя и фотография (информация взята из профиля FB/VK), по центру страницы надпись “У вас нет ни одного воспоминания”, кнопка “Добавить воспоминание” (ее расположение на ваше усмотрение), при нажатии на которую должна открываться форма с возможностью указания места на карте, а также поле для ввода названия и поле для ввода комментария об этом месте.

Далее пользователь может нажать на кнопку “Сохранить”, после чего он снова попадает на домашнюю страницу со списком из этого элемента и возможностью добавлять новые места. Весь добавленный список мест будет отображаться на домашней странице.

На домашней странице пользователя также есть кнопка, позволяющая ему выйти из своего аккаунта. После выхода он должен попасть на приветственную страницу сервиса без возможности видеть список посещаемых мест. При повторной авторизации через FB/VK пользователь снова видит все свои добавленные места.
 
## Требования к реализации
- Приложение должно быть реализовано на базе фреймворка Django.
- Оформление кода должно соответствовать стандартам (PEP8, Django coding style)
- Все используемые зависимости должны быть актуальными на момент создания проекта.
- С самого начала разработки необходимо использовать git, а также следовать стилю коммитов: https://chris.beams.io/posts/git-commit/. Исходный код приложения должен быть размещён на github.
- Основной функционал (создание впечатлений о посещаемых местах и получение их списка) должен быть покрыт юнит-тестами.
- Возможно использование любых сторонних пакетов, для стилей рекомендуется использовать bootstrap.
