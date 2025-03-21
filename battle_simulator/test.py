from InquirerPy import inquirer

def googoogaga(attributes):
    prompt = inquirer.select(
        message="Select item:",
        choices=[f"Speed [{attributes[0]}]", f"Strength [{attributes[1]}]"],
        long_instruction="ENTER=view, D=Add",
        keybindings={"answer": []}
    )

    @prompt.register_kb("d")
    def _handle_delete(event):
        choice_name = prompt.result_name
        choice_value= prompt.result_value
        attributes = 'GOOGOO GAGA'
        event.app.exit(result=[['Speed','Strength'].index(choice_value.split()[0]),int(choice_value[-2])+1])

    @prompt.register_kb("a")
    def _handle_delete(event):
        choice_name = prompt.result_name
        choice_value= prompt.result_value
        attributes = 'GOOGOO GAGA'
        event.app.exit(result=[['Speed','Strength'].index(choice_value.split()[0]),int(choice_value[-2])-1])

    result = prompt.execute()
    attributes[result[0]] = result[1] 
    print('\033c')
    googoogaga(attributes)
googoogaga([0,0])