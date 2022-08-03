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
            choices=["CGH_LLK_PM_AUTOMATION_JUNIPER", "CGH_SAIMAI_PM_AUTOMATION_JUNIPER",
             "CGH_PAHOLYOTHIN_PM_AUTOMATION_JUNIPER", "SCIPRK_PM_AUTOMATION_CISCO",
              "RMUTTO_PM_AUTOMATION_CISCO", "TU_TAPRACHAN_PM_AUTOMATION_CISCO"],
        ),
    ]
    
    answers = inquirer.prompt(questions)
    menu_selector.json_selector(answers['YOU SELECTED'])