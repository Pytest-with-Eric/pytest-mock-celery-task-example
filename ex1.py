from tasks import add, return_hello

result = add.delay(4, 4)

# result = return_hello.delay()
print(result.ready())
