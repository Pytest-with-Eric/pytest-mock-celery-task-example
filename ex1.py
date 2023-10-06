from tasks import reverse_string, add

print(reverse_string.delay("hello"))

print(add.delay(5, 9).get())
