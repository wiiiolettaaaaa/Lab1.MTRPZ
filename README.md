# Lab1.MTRPZ

### Quadratic Equation Solver

Цей застосунок розв’язує квадратні рівняння виду:

ax<sup>2</sup> + bx + c = 0, a &ne; 0

Підтримуються два режими роботи:
- Інтерактивний режим – користувач вводить коефіцієнти вручну.
- Неінтерактивний режим – коефіцієнти зчитуються з файлу.

### Інструкція зі збирання та запуску

- Запуск у інтерактивному режимі:

<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <pre><code>python3 interactive.py</code></pre>
</body>
</html>

Додаток запросить введення коефіцієнтів a, b, c та виведе рівняння з розв’язками.

- Запуск у неінтерактивному режимі (з файлу):

<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <pre><code>python non-interactive.py path/to/input.txt</code></pre>
</body>
</html>

Де input.txt – файл з коефіцієнтами.

#### <p style="font-style: italic;">Формат файлу для неінтерактивного режиму.</p>

Файл містить три числа, розділені пробілами, з десятковою крапкою:

<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <pre><code>1.0 0.0 -4.0</code></pre>
</body>
</html>


Обов’язково має бути новий рядок після останнього числа.

### Revert-коміт

Був виконаний revert коміту fef98bce через порушення узгодженості виводу.

Команда для перегляду:

<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <pre><code>git log --grep="Revert"</code></pre>
</body>
</html>


