# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

longitud = len(it_companies)
print(longitud)

agree = it_companies.add('Twitter')
print(it_companies)


it_latam = {'Uala','Mercadolibre','Globant','Despegar','OLX'}
it_conjunto = it_companies.union(it_latam)
print(it_conjunto)

it_companies.clear()
print(it_companies)
