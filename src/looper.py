import os
import time
from subprocess import Popen


def read_AD():
    """ADを読み込み"""
    params = {}
    params["dur"]   = 8.2
    params["f"]     = 400
    params["fbeat"] = 2
    params["ntri"]  = 30
    params["amp"]   = 0.5
    params["tempo_dur"] = 2.2

    return params


def main():
    """コントローラから状態を取得して、プレーヤへ引数経由で渡して再生"""
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    try:

        handles = []

        for i in range(999):
            
            params = read_AD()

            cmd = [
                "pipenv", "run", "python", "b.py",
                    "--fs", "44100",
                    "--nbit", "16",
                    "--dur",    str(params["dur"]),
                    "--f",      str(params["f"]),
                    "--fbeat",  str(params["fbeat"]),
                    "--ntri",   str(params["ntri"]),
                    "--amp",    str(params["amp"]),
            ]

            h = Popen(cmd)
            handles.append(h)
            
            time.sleep(params["tempo_dur"])

    except KeyboardInterrupt:
        while len(handles) > 0:
            for proc in handles:
                retcode = proc.poll()
                if retcode is not None:
                    handles.remove(proc)
                else:
                    time.sleep(0.1)


if __name__ == "__main__":
    main()




