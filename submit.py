import re
import os.path as osp
import argparse
import socket
import traceback

import yaml
import requests
from getch import getch
from rich.style import Style
from rich.console import Console

from bdcc.utils import read_config
from bdcc.utils import to_json
from bdcc.utils import use_logging, write_log, finish_logging
from bdcc.utils import flush_input
from bdcc.utils import uformat


yaml.reader.Reader.NON_PRINTABLE = re.compile('[^\t\n\r -�-\U0010ffff]')


style_input = Style(color="green", bold=True)
style_menu = Style(color="white")


def menu_start(console):
    
    console.print(" [green]1[/]. Sign [green]I[/]n", highlight=False)
    console.print(" [green]2[/]. [green]Q[/]uit", highlight=False)    
    console.print("Select: ", end="", highlight=False)   

    while True:
        try:
            input = getch()

            if isinstance(input, bytes):
                input = input.decode()
                
            input = input.strip().lower()

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
       
    # Check course ID.
    err_msg = "\n[red][ERROR][/] You must define course ID!"
    if "COURSE" in config:
        COURSE = config["COURSE"]
        if not COURSE or not isinstance(COURSE, str):
            console.print(err_msg)
            return False
    else:
        console.print(err_msg)
        return False

    response = requests.post(uformat(config, b"c2lnbmlu"), json=student)
    res = to_json(response)
    if "error" in res and "result" not in res:
        console.print("\n[red][ERROR][/] {}".format(res["error"]))
        return False

    if res["result"] != student_id:
        raise RuntimeError("\n[red][SYSTEM ERROR][/] Report this error to system manager!")

    config["ID"] = student_id
    config["PW"] = pw

    return student_id


def menu_update_pw(console, config):
    console.print("\n[red][[/] [#00C9FF]Update Password[/] [red]][/]")
    
    pw_old = console.input("- Current password: ", password=True)
    pw_new = console.input("- New password: ", password=True)
    pw_new_confirm = console.input("- Retype new password: ", password=True)

    if len(pw_new) < 4:
        console.print("\n[red][ERROR][/] {}".format("The length of new password should be greater than 3!"))
        return

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

    response = requests.post(uformat(config, b"dXBkYXRl"), json=student)
    res = to_json(response)
    
    if "error" in res and "result" not in res:
        console.print("\n[red][ERROR][/] {}".format(res["error"]))
        return

    if res["result"] != student_id:
        raise RuntimeError("\n[red][SYSTEM ERROR][/] Report this error to system manager!")

    
    console.print("\n[#00FF00]Password updated successfully![/]")    
    config["PW"] = pw_new
    return student_id

def menu_show_stats(console, config):
    student_id = str(config["ID"])
    
    # Process show the results.
    student = {
        "student_id": student_id,
    }
    response = requests.get(uformat(config, b"cmVzdWx0cw=="), params=student)
    res = to_json(response)

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

        console.print(" [green]0[/]. [green]R[/]eload Configuration", highlight=False)
        console.print(" [green]1[/]. Submit [green]A[/]ssignment", highlight=False)
        console.print(" [green]2[/]. [green]S[/]how Results", highlight=False)
        console.print(" [green]3[/]. [green]C[/]hange Password", highlight=False)
        console.print(" [green]4[/]. [green]Q[/]uit", highlight=False)
        console.print("Select: ", end="", highlight=False)

        while True:
            try:         
                
                input = getch()
                if isinstance(input, bytes):
                    input = input.decode()

                input = input.strip().lower()

                if input in ["0", "1", "2", "3", "4", "r", "a", "s", "c", "q"]:
                    break
            except UnicodeDecodeError as err:
                flush_input()
                continue
        # end of while
            
        console.print(input, end="\n\n", style=style_input)

        if input == "0" or input =="r":
            try:
                pw = config["PW"]
                
                try:
                    config = read_config(args.fpath_config)
                except yaml.scanner.ScannerError:
                    err_msg = "The configuration file contains some invalid characters."
                    
                    console.print(traceback.format_exc())
                    console.print("\n[red][ERROR][/] {}".format(err_msg), end="\n\n")
                    break
                    
                if "ID" in config and student_id != config["ID"]:
                    raise RuntimeError("Student ID has been changed! Please sign in again.")
                
                if "PW" in config and pw != config["PW"]:
                    raise RuntimeError("Password has been changed! Please sign in again.")

                config["PW"] = pw
            except yaml.scanner.ScannerError as err:
                err_msg = "The configuration file contains some invalid characters."                
                console.print(traceback.format_exc())
                console.print("\n[red][ERROR][/] {}".format(err_msg), end="\n\n")
                raise err
            
            console.print("\n[#00FF00]Configuration reloaded successfully![/]")    


        elif input == "1" or input == "a":
            submit(console, config)
        elif input == "2" or input == "s":
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
    print(["SYSTEM LOG"], log)
    log = re.sub(r'\[Problem (.+)\] (.+)\n', r'[#ffff96][Problem \1] \2\n[/]', log)
    
    log = re.sub(r'All tests have been passed! \[(.+)pts]\n',
                 r'[#00FF00]All tests have been passed! [\\1pts][/]\n',
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

    try:
        ip_address = socket.gethostbyname(socket.gethostname())
    except Exception as err:
        ip_address = ""
        
    try:
        hostname = socket.gethostname()
    except Exception as err:
        hostname = ""

    submission = {
        "student_id": config["ID"],
        "password": config["PW"],
        "course_id": config["COURSE"],
        "assignment_id": config["ASSIGNMENT"],
        "problems": config["PROBLEMS"],
        "ip_address": ip_address,
        "hostname": hostname
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

        if not osp.isfile(fpath):
            console.print("\n[red][ERROR][/] File not found:\n ▶ {}".format(fpath))
            return

        _, ext = osp.splitext(fname)
        if ext not in [".py", ".cpp", ".c", ".h", ".csv"]:            
            console.print("\n[red][ERROR][/] Invalid file format:\n ▶ {}".format(fpath))
            return

        files.append(
            ('files', (fname, open(fpath, 'rb'), 'text/plain'))
        )
    # end of for

    # Submit the files with the meta-information.
    response = requests.post(uformat(config, b"c3VibWl0"), data=submission, files=files)    
    res = to_json(response)

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
                
                if not osp.isfile(args.fpath_config):                    
                    err_msg = "No such file: %s"%(args.fpath_config)
                    console.print("\n[red][ERROR][/] {}".format(err_msg), end="\n\n")
                    break
                                
                try:
                    config = read_config(args.fpath_config)
                except yaml.scanner.ScannerError:
                    err_msg = "The configuration file contains some invalid characters."
                    
                    console.print(traceback.format_exc())
                    console.print("\n[red][ERROR][/] {}".format(err_msg), end="\n\n")
                    break
                
                student_id = menu_signin(console, config)
                if student_id:
                    console.print()
                    menu_main(console, config)
            else:                
                raise RuntimeError("[SYSTEM ERROR][/] Report this error to system manager!")
        
            console.print()   
    
    finally:
        finish_logging()
