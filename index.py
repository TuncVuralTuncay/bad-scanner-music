import flask
import subprocess
def check(song_name):
    process = subprocess.Popen(["python", "lyrics.py",song_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    print(stdout.decode())
    return stdout.decode()
app = flask.Flask(__name__)
@app.route('/check_song/<song>')
def check_song(song):
    c = check(song)
    return c


if __name__ == "__main__":
    app.run(host='192.168.1.54',port=9000,debug=False)