# 데이터베이스와 DBMS

데이터베이스아 이를 관리하는 SW인 DBMS 관계.

## DBMS 정의

데이터베이스를 ‘데이터 집합’이라고 정의.  
DB를 관리하고 운영하는 SW **DBMS(Database Management System)**.  
다양한 데이터 저장되어 이쓴ㄴ DB는 여러 명의 사용자나 응용 프로그램과 공유 동시 접근 가능해야함.

마이크로소프트 사의 엑셀과 같은 프로그램은 ‘데이터의 집합’을 관리하고 운영한다는 차원에서는 DBMS로 오해할 수 있지만 대용량 데이터를 관리하거나 여러 사용자와 공유하는 개념과는 거리가 있어 DBMS라고 부르지 않는다

e.g. 은행

여러 명의 예금 계좌 정보 모아 놓은 것이 DB.  
은행이 가지고 있는 가지고 있는 예금 계좌 DB에는 여러 명이 동시에 접근. 예금 계좌 주인, 은행 직원, 인터넷 뱅킹, ATM 기기 등 모두 접근 가능함. → DBMS의 존재 이유 덕분.

## DBMS의 종류

DBMS와 같은 SW는 특정 목정 처리 위한 프로그램.  

e.g.

문서를 작성하기 위해 아래아한글(HWP)이나 워드(Wrod), 표 계산 위한 엑셀(Excel)이나 캘크(Calc), 포토샵(Photoshop) 등과 같은 SW를 설치

마찬가지로 DB를 사용하기 위해 SW, DBMS를 설치해야 함   
대표적으로 MySQL, Oracle, SQL Server, MariaDB.  
SW 사용 방법 특징 다르지만 특정 목적 위해 어떤 것을 사용해도 무방

**DBMS 종류**

| DBMS | 제작사 | 작동 운영체제 | 최신 버전 (2024년 기준) | 기타 |
| --- | --- | --- | --- | --- |
| **MySQL** | Oracle Corporation | Windows, Linux, macOS | 8.0.34 | 오픈 소스, LAMP 스택의 기본 구성 요소 |
| **MariaDB** | MariaDB Foundation | Windows, Linux, macOS | 10.11.4 | MySQL 포크, 오픈 소스, 커뮤니티 지원 |
| **PostgreSQL** | PostgreSQL Global Development Group | Windows, Linux, macOS | 16.0 | 오픈 소스, ACID 준수, 확장성 및 호환성 높은 SQL 지원 |
| **Oracle** | Oracle Corporation | Windows, Linux, Solaris, AIX | 23c (2024년) | 상용 DBMS, 클라우드 및 대규모 기업용 DBMS |
| **SQL Server** | Microsoft | Windows, Linux, Docker | 2022 (16.x) | 상용 DBMS, .NET 및 Microsoft 생태계와 높은 호환성 |
| **DB2** | IBM | Windows, Linux, AIX, z/OS | 11.5.x | 상용 DBMS, 대기업용, AI 및 머신러닝 기능 강화 |
| **Access** | Microsoft | Windows | Office 365 (계속 업데이트) | 데스크톱 데이터베이스, 소규모 응용 프로그램에 적합 |
| **SQLite** | D. Richard Hipp | Windows, Linux, macOS, Android, iOS | 3.43.0 | 오픈 소스, 경량형, 서버리스, 내장형 데이터베이스 시스템 |

# DBMS의 발전 과정

컴퓨터 존재하기 전부터 사람들은 데이터를 관리해 왔음.  
종이에 정보를 기록하고 관리하던 때부터 시작해서 지금의 DBMS까지의 발전 과정

## 종이, 펜

아주 오래 전부터 정보는 관리되어 왔음.  
컴퓨터가 없던 시기에는 종이에 펜으로 기록.

## 컴퓨터에 파일로 저장

컴퓨터 등장하는 일반 사람들도 컴퓨터를 사용하게 되면서 종이에 기록하던 내용을 컴퓨터 파일에 기록, 저장.  
컴퓨터 판매/구매 이력 저장하는 방법은 단순하게 메모장 사용, 컴퓨터 어느 정도 할용하게 되면서 엑셀과 같은 스프레드시트 프로그램을 사용 표 형태로 내용 기록하고 자동으로 계산하는 등 한층 더 효율적으로 정보를 관리. 

기록된 내용은 **파일(file)** 형태로 저장 필요할 때마다 열어서 사용.

엑셀 사용 아주 편리, 저장한 파일은 한 번에 한 명의 사용자만 열어서 작업할 수 있음.  
규모가 작은 경우 한 명으 ㅣ사용자가 하나의 파일에 작업한는 것이 문제 되지 않음.  
하지만, 규모가 큰 경우 데이터의 양이 많아 한 명의 사용자가 모두 처리할 수 없기 때문에 여러 명이 각자 파일을 만들어서 작업.

## DBMS의 대두와 보급

파일의 단점을 보완하고자 대량의 데이터를 효율적으로 관리하고 운영하기 위해 등장한 것이 **DBMS**.  
사용하고 있는 MySQL과 같은 DBMS 개념은 1973년 최초로 에드거 프랭크커드라는 학자가 이론을 정립.    
이후 많은 DBMS 제품 만들어졌고, 지금과 같이 안정적인 SW 자리 잡게 됨

DBMS 데이터 집합인 **DB**를 잘 관리하고 운영하기 위한 사용하기 위해 사용되는 언어 S**QL(Structured Query Languager)**. SQL을 이용 DBMS 통해 중요한 정보 입력, 관리 추출.

SQL 문 잘 이해해야 DBMS 원활히 활용.

# DBMS의 분류

DBMS의 유형은 계층형(Hierarchical), 망형(Network), 관계형(Relational), 객체지향형(Object-Oriented), 객체관계형(Object-Relational)

## 계층형 DBMS

**계층형 DBMS(Hierarchical DBMS)** 처음으로 등장 DBMS 개념 1960년대 시작.  
같이 각 계층은 트리(tree)형태.

## 망형 DBMS

망형 DBMS는 계층형  DBMS 문제점 개선 위해 1970년대 등장.  
망형 DBMS를 잘 활용하려면 프로그래머가 모든 구조 이해해야만 프로그램 작성 가능 단점 존재.  
지금 거의 사용하지 않는 형태

## 관계형 DBMS

**관계형 DBMS(Reational DBMS, RDBMS)**.  
사용할 MySQL뿐 아니라, 대부분의 DBMS가 RDBMS 형태로 사용. RDBMS의 DB는 **테이블(table)**이라는 최소 단위로 구성, 이 테이블은 하나 이상의 **열(column)**과 **행(row)**으로 이루어짐.

RDBMS에서는 모든 데이터가 테이블에 저장.  
구조가 가장 기본적이고 중요한 구성이기 때문에 테이블만 제대호 파악하면 RDBMS를 어느 정도 이해.

테이블은 열과 행으로 이루어진 2차원 구조.  
세로는 열, 가로는 행.

# DBMS 언어 SQL

SQL(Structured Query langauge)은 RDB에서 사용되는 언어로, ‘에스큐엘’ 또는 ‘시퀄’로 읽습니다. 공부하고자 하는 RDB를 배우려면 SQL을 필수로 익혀야함.   
SQL이 데이터베이스를 조작하는 ‘언어’지만 프로그래밍 언어와는 조금 다른 특성.

SQL은 특정 회사가 아닌 국제표준화긱구에서 SQL에 대한 표준을 저해서 발표.  
이를 표준 SQL. 문제는 SQL을 사용 DBMS 만드는 회사가 여러 곳 때문에 표준 SQL이 각 회사 제품을 특성을 모두 포용하지 못한다는 점이 있다.  
그래서 DBMS를 만드는 회사에서는 되도록 표준 SQL 준수, 각 제품의 특성을 반영한 SQL 사용함.

결론 표준 SQL을 익히면 여러 DBMS의 공통적인 부분 배우는 것.  
(MySQL 기준으로 작성 예정)