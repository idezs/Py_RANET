from pprint import pprint
import inquirer

def main_menu():

    banner = """  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    MAIN MENU FUNCTIONs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    print(banner)

    questions = [
        inquirer.List(
            "YOU SELECTED : ",
            message="WHAT YOU NEED TO DO?",
            choices=["CGH_LLK_PM_AUTOMATION", "CGH_SAIMAI_PM_AUTOMATION",
             "CGH_PAHOLYOTHIN_PM_AUTOMATION", "SCIPRK_PM_AUTOMATION",
              "RMUTTO_PM_AUTOMATION", "TU_TAPRACHAN_PM_AUTOMATION"],
        ),
    ]

    answers = inquirer.prompt(questions)
    pprint(answers)