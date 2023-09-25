# bdc-client

## 소개
- 중앙대학교 예술공학대학의 블루드래곤클럽(BlueDragonClub, BDC)을 이용하기 위한 클라이언트입니다.
- Python으로 구현된 본 클라이언트를 이용하여 프로그래밍 과제를 제출할 수 있습니다.

## 설치 방법

### 저장소 다운로드
- `git` 명령어를 이용하여 저장소를 로컬 저장소에 복제합니다.
- `git` 사용이 어려우신 분은 저장소를 `*.zip` 파일로 다운로드 받으실 수 있습니다.

```
git clone https://github.com/bluedragonclub/bdc-client.git
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


가상환경을 활성화 시키면 아래와 같이 프롬프트에 가상환경 이름이 나타나게 됩니다.

```
(bdc) 
```


### 의존 패키지 설치

`bdc-client`의 의존 패키지를 설치하기 위해 아래와 같이 `pip`를 설치합니다.

```
(bdc) conda install pip
```

CLI 클라이언트를 이용하기 위해 다음과 같이 `pip` 명령어의 `-r` 옵션을 이용하여 의존 패키지를 일괄적으로 설치할 수 있습니다. 의존 패키지가 궁금하신 분은 `requirements.txt`에서 참고하시기 바랍니다. `requirements.txt`가 존재하는 `bdc-client` 저장소 디렉토리로 이동한 후 다음 명령어를 실행하여 의존 패키지를 설치합니다.

```
(bdc) cd bdc-client
(bdc) pip install -r requirements.txt
```

GUI 클라이언트를 이용하고자 하는 경우 아래와 같이 `requirements_gui.txt`에 정의된 의존 패키지를 설치합니다.

```
(bdc) cd bdc-client
(bdc) pip install -r requirements_gui.txt
```


## 클라이언트 실행

제출하고자 하는 과제의 `config.yml` 파일을 수정한 후 아래와 같은 명령어를 입력하여 CLI 클라이언트를 실행할 수 있습니다.
설정 파일 경로를 잘못 입력하면 오류가 발생하게 됩니다.

```bash
(bdc) python submit.py --config "설정 파일(*.yml) 경로"
```

예를 들어, 본 저장소 디렉토리 구조에서 아래와 같이 명령어를 실행할 수 있습니다.

```bash
(bdc) python submit.py --config path-to-your-course/assignment_01/config.yml
```

GUI 클라이언트를 이용하고자 하는 경우 아래와 같이 커맨드를 입력합니다.

```bash
(bdc) python submit_gui.py
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
    - "path-to-your-course/cau_oop_2022/assignment_01/mathlib.cpp"
    - "path-to-your-course/cau_oop_2022/assignment_01/mathlib.h"
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


## 자주 발생하는 오류 유형


**오류 상황**)
- 의존 패키지 설치 과정에서 `requirements.txt` 파일을 찾을 수 없다는 오류를 만나게 되는 경우.

```bash
(bdc) pip install -r requirements.txt
Could not open requirements file
No such file or directory: 'requirements.txt'
```

**해결 방법**)
- `requirements.txt`가 들어있는 `bdc-client` 디렉토리 내로 진입 후 설치.

```bash
(bdc) cd bdc-client
(bdc) pip install -r requirements.txt
```


------------------------------------------------------------------------

**오류 상황**)
- `Sign In` 과정에서 `config.yml` 파일을 찾지 못하는 경우.

```bash
(bdc) python submit.py --config "/Users/oop/cau_oop_2022/assignment01/config.yml

[ERROR] No such file: "/Users/oop/cau_oop_2022/assignment_01/config.yml

```

**해결 방법**)
- `config.yml`의 경로를 정확하게 기입.

```bash
(bdc) python submit.py --config cau_oop_2022/assignment_01/config.yml
```

- `config.yml`의 경로를 절대 경로로 기입.

```bash
(bdc) python submit.py --config "D:/repos/bdc-client/cau_oop_2022/assignment_01/config.yml"
```


------------------------------------------------------------------------

**오류 상황**)
- 들여쓰기(indentation)가 제대로 되지 않은 경우.
- 들여쓰기가 망가지면 `yaml` 파일 형식이 제대로 인식되지 않음.

```yaml

"FILES":
    - "/Users/oop/cau_oop_2022/assignment_01/mathlib.h"
            - "/Users/oop/cau_oop_2022/assignment_01/mathlib.cpp"

```

**해결 방법**)
- 들여쓰기를 제대로 수정.

```yaml

"FILES":
    - "/Users/oop/cau_oop_2022/assignment_01/mathlib.h"
    - "/Users/oop/cau_oop_2022/assignment_01/mathlib.cpp"

```


------------------------------------------------------------------------


**오류 상황**)
- Windows에서 실행 시 파일 경로 구분자로 `\` 를 사용하는 경우.
- 아래 예시에서처럼 `\a`나 `\n`이 예외 문자(escape character)로 인식될 수 있음.
- 참고로 파일 경로 내 `\n`은 개행 문자로 인식됨.


```yaml
"FILES":
    - "C:\Users\dwlee\oop\assignment_01\network.h"
    - "C:\Users\dwlee\oop\assignment_01\network.cpp"

```

**해결 방법**)
- 파일 경로 구분자 `\`를 `/`로 교체 (역슬래시 대신 슬래시 사용).

```yaml
"FILES":
    - "C:/Users/dwlee/oop/assignment_01/network.h"
    - "C:/Users/dwlee/oop/assignment_01/network.cpp"

```

------------------------------------------------------------------------


**오류 상황**)
- Windows에서 실행 후 단축키가 제대로 동작하지 경우.
- 단축키를 입력하면 바로 실행되어야 하는데 엔터를 입력해야 하는 경우.

**해결 방법**)
- 한컴 입력기가 입력기로 선택되어 있는 경우 입력이 원활하지 않을 수 있음.
- 한컴 입력기를 삭제하거나, 한컴 입력기 대신 Microsoft 입력기를 사용.
