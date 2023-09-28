from tasks import reverse_string, add

print(add.delay(5, 9).get())
