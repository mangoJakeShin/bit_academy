

### Multi Process? 

core 개별적으로 각각 프로세스를 돌리게 만듦.
terminal 을 여러개 띄워서 사용할 수도 있음. 
terminal 안에서 여러가지 프로세스를 돌리는 방법? a & b 
-> a는 background에서 실행됨

프로세스에는 부모-자식 관계가 존재할 수 있음.
* 1 -- 2 : 1과 2는 부자 관계
* | -- 3 : 2와 3은 형제 관계


* 부모 프로세스는 자식 프로세스가 끝날때까지 끝나지 않는게 일반적인 rule

보통의 경우 부모 프로세스가 죽을 결우 자식 프로세스도 끝나야 함. 
그 때 자식프로세스가 안 죽고 살아있는 경우를 좀비 프로세스라고 함.   

* 프로세스에서 프로세스로 보내는 명령 : signal(kill, ctrl c, ...) 
    * c를 통해서 모든 명령이 제어 가능 - 리눅스가 c로 만들어졌기 때문 

--- 
### file system? 
자료를 저장하는 과정에서 어떻게 저장하는가? 어떻게 끄집어내는가?
eg 블랙박스 회사 : 충돌로 인해 사고가 났을 때 일반적인 프로그램은 깨짐 
그러나 블랙박스 회사는 파일시스템을 연구해서 최대한 손실이 없도록 저장하게 만듦

프레임웤 : 굉장히 자주 사용하는 코드의 집합(?)

### 작업 관리자? 
어떻게 여러가지 프로그램을 동시에 실행시킬 수 있는가?

#### 프로그램의 실행 
1. HDD : test 라는 프로그램을 저장 / gcc -o test test.c 로 실행 -> 코드 내부에 memory에 복사해주는 코드 생성(loader)
1. memory : 메모리에서 test를 받아서 컨텍스트를 붙여줌 -> test structer 로 만들어줌 : 이런 프로그램이 메모리 내부에 여러개가 존재
    * 그렇다면 이 프로그램을 어떻게 관리하나? OS 내부의 스케쥴러에 test가 마지막에 등록되고 순서대로 실행 / cpu의 개수에 따라 스케쥴러가 대기 큐를 조정함
    * test 프로그램이 돌 때 하나의 cpu가 아니라 여러개를 사용하게 만들수도 있음. 그 때 쓰는게 보통 fork()
    * 코드를 작성할 때 부모일때와 자식일때 조건을 지정하여 만듦. 그렇지만 이 방식을 쓸 경우 
1. cpu :  

* fork()
>```c
>int main(void){
>pid_t pid;
>int x = 0;
>
>pid = fork;    
># 자식 프로세스 pid를 생성
>
>if (pid == 0) #부모 프로세스일 때 실행
>
>else           #자식 프로세스일 떄 실행
>{ ...
>return 1 
>}
>
>{ return 0 }
>
># 일방적으로 위의 코드 방식으로 사용하지 않음 
># (pid == 0 일 때 리턴을 하고 종료되므로 자식 프로세스가 좀비 프로세스가 되고 부모없이 돌아가게 됨)
>}```
---
### Thread

                fork
    * stack 0     --     stack 1
    * xxx 0        --     xxx 1
    * heap 0      --     heap 1
    * data 0      --     data 1
    * code 0      --     code 1
    
            multi-thread
    * stack 0     --     stack 1
                * xxx 0
                * heap 0
                * data 0
                * code 0
    
* fork() 는 위의 메모리를 통채로 복사를 함. 그래서 프로세스 용량이 클수록 부담
멀티스레드를 할 경우 다른건 그대로 둔 채 stack부분에서 분리를 진행 

* fork()를 통해 복사 된 프로세스간 통신을 하게 만드려면 복잡한 과정이 필요함
그러나 멀티스레드로 진행할 시 변수공유가 굉장히 간편

 


---
### AWS
1. aws 인스턴스 생성
1. filezilla install
1. 편집 - 설정
1. SFTP -
    1. 키 추가
    1. ppk 파일 추가
1. 파일 - 사이트 관리자
    1. host에 탄력적 ip 할당받은 것 추가
    1. 사용자 ubuntu 
    1. 암호는 그대로
1. 연결 시도
    * 성공 시 파일 업로드하기


PATH=D:\VMware\VMware Player\bin\;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\
Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine C
omponents\IPT;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\dotnet\;C:\Program Files\Git\cmd;C:\Program Files\PuTTY\;C:\Users\bit\AppData\Local\Programs\Python\Python38-32\Scripts\;C:\Users\bit\AppData\Local\Programs\Python\Python38-32
\;C:\Users\bit\AppData\Local\Microsoft\WindowsApps;C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.1\bin;;C:\Users\bit\.dotnet\tools;C:\Users\bit\AppData\Local\Programs\Microsoft VS Code\bin;C:\Program Files\Bandizip\;C:\Us
ers\bit\AppData\Local\GitHubDesktop\bin










