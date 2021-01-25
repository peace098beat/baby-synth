# Baby Synth

Baby のための Simple シンセ

# Environments

- Raspberry Pi Zero - Raspbian StrechのデフォルトPython3のヴァージョンに合わせる.
	- python 3.5.3


# On Raspberry Pi


## Setup Pipenv

- nstall `numpy` and `simpleaudio`.
- Don't use `pipenv`

```
$ pip3 install simpleaudio==1.0.4
```



## v0.1

- 感想

- 追っかけ並列再生しているので、想像とちょっと違った。
    - pyaudio?
- chip音が入っている。
    - フェードアウトした方が良い.