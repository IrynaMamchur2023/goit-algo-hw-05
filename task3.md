Звіт з вимірювання швидкості алгоритмів пошуку шаблону в тексті

Під час виконання експериментів було проведено вимірювання часу роботи трьох алгоритмів пошуку шаблону: Boyer-Moore, Knuth-Morris-Pratt і Rabin-Karp.  

Стаття 1
Пошук існуючого шаблону "структури даних"
Boyer-Moore: 5.76e-05 секунд
Knuth-Morris-Pratt: 6.99e-05 секунд
Rabin-Karp: 0.00033 секунд

Пошук відсутнього шаблону "структури всіх даних"
Boyer-Moore: 0.0004 секунд (шаблон не знайдено)
Knuth-Morris-Pratt: 0.00126 секунд (шаблон не знайдено)
Rabin-Karp: 0.00759 секунд (шаблон не знайдено)


Стаття 2
Пошук існуючого шаблону "структури даних"
Boyer-Moore: 1.46e-05 секунд
Knuth-Morris-Pratt: 1.09e-05 секунд
Rabin-Karp: 1.73e-05 секунд

Пошук відсутнього шаблону "структури всіх даних"
Boyer-Moore: 0.00052 секунд (шаблон не знайдено)
Knuth-Morris-Pratt: 0.00282 секунд (шаблон не знайдено)
Rabin-Karp: 0.01216 секунд (шаблон не знайдено)


Висновок:
У цьому експерименті алгоритми Boyer-Moore та Rabin-Karp показали найкращі результати в пошуку шаблону. У першій статті алгоритм Rabin-Karp виявився найшвидшим при пошуку існуючого шаблону, а в другій статті Knuth-Morris-Pratt виявився найшвидшим при пошуку існуючого шаблону. Проте алгоритм Boyer-Moore вивявися самим швидким, якщо в статті відсутній шаблон, який ми шукаємо. Це може бути пояснено тим, що алгоритм Boyer-Moore виявився більш ефективним у конкретних умовах даної задачі. Проте, варто враховувати, що ефективність алгоритмів може залежати від конкретних умов задачі та характеристик текстів.