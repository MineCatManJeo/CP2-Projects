# TEST FILE. NOT USED IN CODE. MAY NEVER BE USED IN CODE. NOT SURE YET.
from InquirerPy import inquirer

def googoogaga(attributes):
    prompt = inquirer.select(
        message="Select item:",
        choices=[f"Speed [{attributes[0]}]", f"Strength [{attributes[1]}]"],
        long_instruction="ENTER=view, D=Add",
        keybindings={"answer": []}
    )

    @prompt.register_kb("right")
    @prompt.register_kb("d")
    def _add_skill(event):
        choice_value= prompt.result_value
        event.app.exit(result=[['Speed','Strength'].index(choice_value.split()[0]),int(choice_value[choice_value.find('[')+1:-1])+1])

    @prompt.register_kb('left')
    @prompt.register_kb('a')
    def _subtract_skill(event):
        choice_value= prompt.result_value
        event.app.exit(result=[['Speed','Strength'].index(choice_value.split()[0]),int(choice_value[choice_value.find('[')+1:-1])-1])

    @prompt.register_kb('enter')
    def _enter(event):
        event.app.exit(result=[0,100])

    result = prompt.execute()
    attributes[result[0]] = result[1] 
    print('\033c')
    googoogaga(attributes)
googoogaga([0,0])