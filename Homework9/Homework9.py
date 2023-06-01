#������ 40


import csv

with open('sample_data/california_housing_train.csv', 'r') as file:
    reader = csv.reader(file)

    header = next(reader)

    total_price = 0
    count = 0

    for row in reader:
        population = int(row[0])
        price = float(row[-1])

        if 0 <= population <= 500:
            total_price += price
            count += 1

    average_price = total_price / count if count > 0 else 0

    print(f"������� ��������� ���� (���-�� ����� �� 0 �� 500): {average_price}")





    #������ 42

    import csv

with open('sample_data/california_housing_train.csv', 'r') as file:
    reader = csv.reader(file)

    header = next(reader)

    min_population = float('inf')
    max_households = 0

    for row in reader:
        population = int(row[0])
        households = int(row[4])

        if population < min_population:
            min_population = population

    file.seek(0)
    next(reader)  

    for row in reader:
        population = int(row[0])
        households = int(row[4])

        if population == min_population and households > max_households:
            max_households = households

    print(f"������������ ���������� households � ���� ������������ �������� population: {max_households}")