def read_content(path: str) -> list:
    try:
        file = open(path, encoding="utf-8")
    except FileNotFoundError:
        return(f"File {path} does not exist!")
    content = file.read()
    file.close()
    return(content.split("\n"))

print(read_content("C:/Users/minos/Documents/ŠKOLA/Prog/2022-2023/Python/Projekty/test.txt"))
print(read_content("C:/Users/minos/Documents/ŠKOLA/Prog/2022-2023/Python/Projekty/poem.txt"))
print(read_content("Projekty/poem.txt"))