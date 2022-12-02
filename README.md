# bdc-client

## 소개
- 중앙대학교 예술공학대학의 블루드래곤클럽(BlueDragonClub, BDC)을 이용하기 위한 클라이언트입니다.
- Python으로 구현된 본 클라이언트를 이용하여 프로그래밍 과제를 제출할 수 있습니다.

## 설치 방법

### 저장소 다운로드
- `git` 명령어를 이용하여 저장소를 로컬 저장소에 복제합니다.
- `git` 사용이 어려우신 분은 저장소를 `*.zip` 파일로 다운로드 받으실 수 있습니다.

```
https://github.com/bluedragonclub/bdc-client.git
```


### 가상환경 생성
- :snake: [Anaconda](https://www.anaconda.com) 및 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 사용을 권합니다.

- Anaconda 또는 Miniconda 설치 후 다음 명령어를 실행하여 가상환경을 만듭니다. 
- 아래 명령어 예시에서 가상환경 이름을 `bdc`로 정의하였지만, 사용자가 원하는 이름으로 변경할 수 있습니다.
- Python 버전은 `3.7` 이상을 사용하시기를 바랍니다.

```
conda create -n bdc python=3.10
```

가상환경 생성이 완료되면 아래와 같이 `conda` 명령어를 통해 가상환경을 활성화 시킬 수 있습니다.

```
conda activate bdc
```

### 의존 패키지 설치

`bdc-client`의 의존 패키지를 설치하기 위해 아래와 같이 `pip`를 설치합니다.

```
(bdc) conda install pip
```

의존 패키지는 다음과 같이 `pip` 명령어의 `-r` 옵션을 이용하여 일괄적으로 설치할 수 있습니다. 의존 패키지가 궁금하신 분은 `requirements.txt`에서 참고하시기 바랍니다. `requirements.txt`가 존재하는 `bdc-client` 저장소 내에서 다음 명령어를 실행하여 의존 패키지를 설치합니다.

```
(bdc) pip install -r requirements.txt
```


## 클라이언트 실행

제출하고자 하는 과제의 `config.yml` 파일을 수정한 후 아래와 같은 명령어를 입력하여 클라이언트를 실행할 수 있습니다.
설정 파일 경로를 잘못 입력하면 오류가 발생하게 됩니다.

```bash
(bdc) python submit.py --config "설정 파일(*.yml) 경로"
```

예를 들어, 본 저장소 디렉토리 구조에서 아래와 같이 명령어를 실행할 수 있습니다.

```bash
(bdc) python --config cau_oop_2022/assignment_01/config.yml
```


## 설정 파일 수정

- 설정(configuration, config) 파일에서 `ID`와 `FILES`를 적절하게 수정하시기 바랍니다.
- `ID`에는 본인의 **학번**(예: 20221234)을 기입하고 `FILES`에는 제출하고자 하는 파일의 경로를 입력해 주시면 됩니다.
- 아래 예시에서는 클라이언트가 실행된 디렉토리를 기준으로 제출하고자 하는 파일의 **상대 경로**를 기입하였습니다. 그러나 사용자의 개발 환경에 따라 상대 경로 보다는 **절대 경로**를 기입하시기 바랍니다.
- `PROBLEMS`에는 제출하고자 하는 문제의 번호를 기입할 수 있습니다. 특정 문제만 평가 받기 위해 `PROBLEMS`에 일부 문제만 기입하실 수 있습니다.

```yaml
---

"COURSE": "CAU_OOP_2022"  # 과목 아이디
"ASSIGNMENT": "ASSIGNMENT_01"  # 과제 아이디

"ID": "20221234"  # 학번
"FILES":  # 제출 파일의 경로 기입 (절대 경로 권장)
    - "cau_oop_2022/assignment_01/mathlib.cpp"
    - "cau_oop_2022/assignment_01/mathlib.h"
"PROBLEMS":  # 채점 받고자 하는 문제 번호
    - "PROBLEM_01A"
    - "PROBLEM_01B"
    - "PROBLEM_02A"
    - "PROBLEM_02B"
    - "PROBLEM_03A"
    - "PROBLEM_03B"
    - "PROBLEM_04A"
    - "PROBLEM_04B"
    - "PROBLEM_04C"
    # - "PROBLEM_05B"
    # - "PROBLEM_05C"
    # - "PROBLEM_05D"
    # - "PROBLEM_05E"
    # - "PROBLEM_06C"
```

