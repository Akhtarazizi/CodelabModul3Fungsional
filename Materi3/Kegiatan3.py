# Data list
data = [5.5, 3.1, 7, 2.7, 'Hello', 'world', 1, 'AI', 105]

# Filter untuk memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), data))
int_values = list(filter(lambda x: isinstance(x, int), data))
string_values = list(filter(lambda x: isinstance(x, str), data))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int(value):
    return {
        'ratusan': (value // 100) % 10,
        'puluhan': (value // 10) % 10,
        'satuan': value % 10
    }

int_mapped = list(map(map_int, int_values))

# Output
print("Data Float:", (float_values))
print("Data Int:")
for value in int_mapped:
    print(value)
print("Data String :", string_values)