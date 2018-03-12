import sys, warnings
if sys.version_info[0] < 2:
    warnings.warn("Для выполнения этой программы необходима как минимум \
    версия Python 3.0",
    RuntimeWarning)
else:
    print('Нормальное продолжение')