# bdc-client

## 소개
- 중앙대학교 예술공학대학의 블루드래곤클럽(BlueDragonClub, BDC)을 이용하기 위한 클라이언트입니다.
- Python으로 구현된 본 클라이언트를 이용하여 프로그래밍 과제를 제출할 수 있습니다.

## 설치

:snake: [Anaconda](https://www.anaconda.com) 및 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 사용을 권합니다.


### Anaconda & Miniconda 가상환경 설정

Anaconda 또는 Miniconda 설치 후 다음 명령어를 실행하여 가상환경을 만듭니다. 아래 명령어 예시에서 가상환경 이름을 `bdc`로 정의하였지만, 사용자가 원하는 이름으로 변경할 수 있습니다. Python 버전은 `3.7` 이상을 사용하시기를 바랍니다.

```
conda create -n bdc python=3.10
```

가상환경 설치가 완료되면 아래와 같이 `conda` 명령어를 통해 가상환경을 활성화 시킬 수 있습니다.

```
conda activate bdc
```

`bdc-client`의 의존 패키지를 설치하기 위해 아래와 같이 `pip`를 설치합니다.

```
conda install pip
```

의존 패키지는 다음과 같이 `pip` 명령어의 `-r` 옵션을 이용하여 다음과 같이 설치할 수 있습니다. `requirements.txt`에서 의존 패키지를 참고하실 수 있습니다.

```
pip install -r requirements.txt
```


## 사용



