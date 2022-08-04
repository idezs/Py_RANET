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
            choices=["SERIAL_INITIAL_SWITCH_IOS_DEVICES", "PM_CGH_LLK_AUTOMATION_JUNIPER", "PM_CGH_SAIMAI_AUTOMATION_JUNIPER",
             "PM_CGH_PAHOLYOTHIN_AUTOMATION_JUNIPER", "PM_SCIPRK_AUTOMATION_CISCO",
              "PM_RMUTTO_AUTOMATION_CISCO", "PM_TU_TAPRACHAN_AUTOMATION_CISCO"],
        ),
    ]
    
    answers = inquirer.prompt(questions)
    menu_selector.icon_selector(answers['YOU SELECTED'])