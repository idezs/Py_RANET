from pprint import pprint
import inquirer
import menu_selector

def main_menu():

    banner = """  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    MAIN MENU FUNCTIONs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    print(banner)

    questions = [
        inquirer.List(
            "YOU SELECTED",
            message="WHAT YOU NEED TO DO?",
            choices=["PM_AUTOMATION_CISCO_1", "PM_AUTOMATION_CISCO_2"],
        ),
    ]
    
    answers = inquirer.prompt(questions)
    menu_selector.icon_selector(answers['YOU SELECTED'])
