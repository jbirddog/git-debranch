import pkgutil

def main():
    data = pkgutil.get_data("git_debranch", "bpmn/git-debranch/git-debranch.bpmn")
    print(f"git-debranch: {data}")
