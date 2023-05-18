import pkgutil

def main():
    data = pkgutil.get_data("git_debranch", "assets/bpmn/git-debranch/git-debranch.bpmn")
    print(f"git-debranch")
