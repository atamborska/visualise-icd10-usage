import streamlit
import pandas
import matplotlib.pyplot
import streamlit.web.cli as stcli
import os, sys


def resolve_path(path):
    file_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return file_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("icd10_app.py"),
        "--global.developmentMode=false",
    ]
sys.exit(stcli.main())
