# Bad word scanner of music

# How to use ?

## Firstly install depencies
```
pip install flask && pip install lyricsgenius
```
## Secondly
### Enter your lyrics genius api key 
```py
genius = lyricsgenius.Genius("xxxxxxx")
```
## Finaly run the "index.py" file and open 9000 port on your browser

### For example
```url
http://192.168.1.<host-ip>:9000/check_song/<song_name>