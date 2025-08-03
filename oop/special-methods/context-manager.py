
class FileOpen:

    # it only work 'with' keyword
    def __enter__(self) -> str:
        return f"file has open by 'open('test.txt', 'w')'"
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        print(f"file has closed")
    

object1 = FileOpen()

with object1 as file:
    print(file)