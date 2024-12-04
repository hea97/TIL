리포지토리 설정 후 Docker 설치

```bash
sudo apt-get update
```

먼저 위와 같이 apt 패키지 인덱스를 업데이트.  
한 번 더 업데이트하는 이유는 다음 단계에서 Docker를 정상적으로 설치하기 위해서이다. 만약, 이 단ㄴ계에서 업데이트하지 않고 넘어가면 패키지의 최신 버전을 찾지 못해 설치 과정에서 에러가 발생할 수 있다

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

1. Docker 설치 중 Yes or No에서 Y

설치가 되었따면 성공적으로 설치되었는지 확인

1. Docker 명령어를 입력했을 때 **active (running) (초록색)**

```bash
systemctl status docker
```

docker 원활히 작동되고 있는 확인 위해 명령어 입력.

```bash
sudo usermod -aG docker $USER
```

설치가 완료되면 위와 같은 코드를 실행해서 docker 명령어를 사용자 모드에서도 사용할 수 있도록 한다.  
위 명령어를 입력한 후 실제 사용자 모드에서 사용하기 위해 로그아웃을 한 후 로그인을 다시 한다.

```bash
docker version
```

docker 버전 확인.