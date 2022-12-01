import re
import os.path as osp
import argparse
import socket

import yaml
import requests
from getch import getch
from rich.style import Style
from rich.console import Console

import utils
from utils import use_logging, write_log, finish_logging
from utils import flush_input
from utils import uformat


raw = b"aHR0cDovLzE2NS4xOTQuMTY0Ljg2OjEwMDAxL3t9"
style_input = Style(color="green", bold=True)
style_menu = Style(color="white")

def menu_start(console):
    
    console.print(" [green]1[/]. Sign [green]I[/]n", highlight=False)
    console.print(" [green]2[/]. [green]Q[/]uit", highlight=False)    
    console.print("Select: ", end="", highlight=False)   

    while True:
        try:
            input = getch()
            input = input.decode().strip()
            input = input.lower()

            if input in ["1", "2", "q", "i"]:
                break
        except UnicodeDecodeError as err:
            flush_input()
            continue
    
    console.print(input, end="", style=style_input)

    return input


def menu_signin(console, config):
    console.print("\n[red][[/] [#00C9FF]Sign In[/] [red]][/]")

    if "ID" in config and config["ID"].strip():
        student_id = config["ID"]
        console.print("- Student ID: {}".format(student_id))
    else:
        student_id = console.input("- Student ID: ")
    # end of if-else    
        
    student_id = str(student_id)    
    student_id = student_id.strip()

    pw = console.input("- Password: ", password=True)
    
    # Process sign-in
    student = {
        "id": student_id,
        "pw": pw,
        "name": "",
        "group": 0
    }

    response = requests.post(uformat(raw, b"c2lnbmlu"), json=student)
    res = utils.to_json(response)
    if "error" in res and "result" not in res:
        console.print("\n[red][ERROR][/] {}".format(res["error"]))
        return False

    if res["result"] != student_id:
        raise RuntimeError("\n[red][SYSTEM ERROR][/] Report this error to system manager!")

    config["ID"] = student_id
    config["PW"] = pw
    #console.print()

    return student_id


def menu_update_pw(console, config):
    console.print("\n[red][[/] [#00C9FF]Update Password[/] [red]][/]")
    
    pw_old = console.input("- Current password: ", password=True)
    pw_new = console.input("- New password: ", password=True)
    pw_new_confirm = console.input("- Retype new password: ", password=True)

    if pw_new != pw_new_confirm:
        console.print("\n[red][ERROR][/] {}".format("The inputs for new password do not match!"))
        return

    # Process update the password.
    student = {
        "id": student_id,
        "pw": pw_old,
        "pw_new": pw_new,
        "name": "",
        "group": 0
    }

    response = requests.post(uformat(raw, b"dXBkYXRl"), json=student)
    res = utils.to_json(response)
    
    if "error" in res and "result" not in res:
        console.print("\n[red][ERROR][/] {}".format(res["error"]))
        return

    if res["result"] != student_id:
        raise RuntimeError("\n[red][SYSTEM ERROR][/] Report this error to system manager!")

    
    console.print("\n[#00FF00]Password updated successfully![/]")    
    
    return student_id

def menu_show_stats(console, config):
    student_id = str(config["ID"])
    
    # Process show the results.
    student = {
        "student_id": student_id,
    }
    response = requests.get(uformat(raw, b"cmVzdWx0cw=="), params=student)
    res = utils.to_json(response)

    if "error" in res and "result" not in res:
        console.print("\n[red][ERROR][/] {}".format(res["error"]))
        return

    console.print("\n[red][[/] [#00C9FF]Current Results[/] [red]][/]")

    fstr = "- [[#ffff96]{}[/]] Total Score: [#00FF00]{} / 100[/]"
    for assignment_id, total_score in res["result"].items():
        console.print(fstr.format(assignment_id, total_score))

    # end of for
    return student_id

def menu_main(console, config):
    student_id = config["ID"]
    while True:
        console.print(f"[red][[/] [#00C9FF]Blue Dragon Club[/] [#00FF00](ID: {student_id})[/] [red]][/]")

        console.print(" [green]1[/]. Submit [green]A[/]ssignment", highlight=False)
        console.print(" [green]2[/]. Show [green]R[/]esults", highlight=False)
        console.print(" [green]3[/]. [green]C[/]hange Password", highlight=False)
        console.print(" [green]4[/]. [green]Q[/]uit", highlight=False)
        console.print("Select: ", end="", highlight=False)

        while True:
            try:         
                
                input = getch()
                input = input.decode().strip()
                input = input.lower()

                if input in ["1", "2", "3", "4", "a", "r", "c", "q"]:
                    break
            except UnicodeDecodeError as err:
                flush_input()
                continue
        # end of while
            
        console.print(input, end="\n\n", style=style_input)

        if input == "1" or input == "a":
            submit(console, config)
        elif input == "2" or input == "r":
            menu_show_stats(console, config)
        elif input == "3" or input == "c":
            menu_update_pw(console, config)
        elif input == "4" or input == "q":
            config["ID"] = ""
            config["PW"] = None
            break

        console.print()
    # end of while

    return input


def colorize_log(log):
    log = re.sub('\[Problem (.+)\] (.+)\n', '[#ffff96][Problem \\1] \\2\n[/]', log)
    
    log = re.sub('All tests have been passed! \[(.+)pts]\n',
                 '[#00FF00]All tests have been passed! [\\1pts][/]\n',
                 log)

    log = log.replace("[ERROR]", "[red][ERROR][/]")
    log = log.replace("[FAILED]", "[red][FAILED][/]")
    log = log.replace("[MEMORY LEAK]", "[red][MEMORY LEAK][/]") 
    log = log.replace("100 / 100", "[#00FF00]100 / 100[/]")     
    return log

def submit(console, config):

    console.print("[Assignment: [#ffff96]{}[/]]".format(config["ASSIGNMENT"]))


    # Check course ID.
    err_msg = "\n[red][ERROR][/] You must define course ID!"
    if "COURSE" in config:
        COURSE = config["COURSE"]
        if not COURSE or not isinstance(COURSE, str):
            console.print(err_msg)
            return
    else:
        console.print(err_msg)
        return

    # Check assignment ID.
    err_msg = "\n[red][ERROR][/] You must define assignment ID!"
    if "ASSIGNMENT" in config:
        ASSIGNMENT = config["ASSIGNMENT"]
        if not ASSIGNMENT or not isinstance(ASSIGNMENT, str):
            console.print(err_msg)
            return
    else:
        console.print(err_msg)
        return

    # Check problem ID.
    err_msg = "\n[red][ERROR][/] You must define at least one problem ID!"
    if "PROBLEMS" in config:
        PROBLEMS = config["PROBLEMS"]
        if not PROBLEMS or not isinstance(PROBLEMS, list) or len(PROBLEMS) < 1:
            console.print(err_msg)
            return
    else:
        console.print(err_msg)
        return


    submission = {
        "student_id": config["ID"],
        "password": config["PW"],
        "course_id": config["COURSE"],
        "assignment_id": config["ASSIGNMENT"],
        "problems": config["PROBLEMS"],
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "hostname": socket.gethostname()
    }

    # Check and collect files.
    err_msg = "\n[red][ERROR][/] You must define file paths!"
    if "FILES" in config:
        FILES = config["FILES"] 
        if not FILES  or len(FILES) < 1:
            console.print(err_msg)
            return
    else:
        console.print(err_msg)
        return  

    files = []
    for fpath in FILES:
        fname = osp.basename(fpath)
        fpath = osp.abspath(osp.join(droot, fpath))

        if not osp.isfile(fpath):
            # raise FileNotFoundError(fpath)             
            console.print("\n[red][ERROR][/] File not found:\n ▶ {}".format(fpath))
            return

        files.append(
            ('files', (fname, open(fpath, 'rb'), 'text/plain'))
        )
    # end of for

    # Submit the files with the meta-information.
    response = requests.post(uformat(raw, b"c3VibWl0"), data=submission, files=files)    
    res = utils.to_json(response)

    if "error" in res:
        write_log("\n[ERROR] {}".format(res["error"]))
        console.print("\n[red][ERROR][/] {}".format(res["error"]), end="\n\n")
    elif "result" in res:
        result = res["result"]
        log = result["log"]
        write_log("\n{}".format(log))
        log = colorize_log(log) 
        console.print("\n{}".format(log), highlight=False)
    else:
        raise RuntimeError("[SYSTEM ERROR]", response)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Blue Dragon Club Arguments")
    argparser.add_argument('-c', '--config',
                           action='store',
                           dest='fpath_config',                           
                           help="Designate the file path of a configuration file.")


    droot = osp.dirname(__file__)

    use_logging("bluedragonclub-logging",
                mode='a',
                stdout=False,
                fout=True,
                fpath=osp.join(droot, "log.txt"))

    console = Console()

    try:
        while True:
            console.print("[red][[/] [#00C9FF]Blue Dragon Club[/] [red]][/]")

            input = menu_start(console)
            console.print()
            if input == "2" or input == "q":
                break
            elif input == "1" or input == "i":    
                args = argparser.parse_args()       
                with open(args.fpath_config, "rt") as fin:
                    config = yaml.safe_load(fin)

                student_id = menu_signin(console, config)
                if student_id:
                    console.print()
                    menu_main(console, config)
            else:                
                raise RuntimeError("[SYSTEM ERROR][/] Report this error to system manager!")
                # console.print("\n[red][ERROR][/] Wrong input: %s"%(input))
        
            console.print()
    finally:
        finish_logging()
