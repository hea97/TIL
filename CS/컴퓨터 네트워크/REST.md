# REST란

**REST는 Representational State Tansfer** 의 약자, HTTP 통신을 활용하기 위해 고안된 아키텍처.  
Representational은 인터넷상의 자원을 **URI(Uniform Resoure Idntifier)** 로 나타냄.  
클라이언트는 URI로 표현된 자원을 HTTP 메서드를 이용해 **CRUD(Create, Read, Update, Delete)** 연산을 할 수 있음. State Transfer는 자원의 상태를 주고받는 것,  
즉 요청 받은 자원의 상태를 전달하는 것을 의미. 결국 REST는 자원을 명시해 연산을 수행하고 상태를 주고 받는 것.

**REST 특징**

- **일관된 인터페이스**  
자원을 나타내는 URI를 HTTP 메서드로 조작하는 일관된 인터페이스를 사용.  
따라서 HTTP를 따르는 모든 플랫폼에서 REST를 사용
- **클라이언트-서버 구조**  
클라이언트와 서버 간에 요청-응답의 독립적인 구조를 갖는다. 클라이언트는 서버에 요청을 보내고 응답을 대기. 서버는 자원을 가지고 있으며 클라이언트의 요청에 응답
- **무상태성**  
서버에서는 클라이언트의 요청을 저장하거나 관리하지 않는다. 서버는 클라이언트의 요청에 대한 처리와 응답만 한다. 사용자 인증, 로그인 정보 등은 클라이언트에서 직접 관리.
- **캐싱 가능**  
HTTP 표준을 사용하므로 클라이언트는 이전에 서버로부터 받은 응답을 저장 및 재사용하는 캐싱(caching)을 할 수 있다. 캐싱은 클라이언트의 많은 요청으로부터 서버 부하를 줄여 주고, 클라이언트는 비교적 빨리 응답을 받을 수 있게 한다.
- **자체 표현 구조**  
REST API는 자원, 행위, 표현으로 구성 REST API 메시지를 보고 어떤 요청을 하는지 알 수 있다.
- **계층형 구조**  
REST 서버는 다중 계층으로 구성될 수 있어서 보안, 암호화와 같은 계층을 추가해 서버에 대한 기능을 유연하게 확장

REST는 이런 특징과 함께 HTTP 기반으로 하기 때문에 별도의 인프라를 구축할 필요가 없다는 장점.  
그래서 HTTP 표준을 따르면 REST를 쉽게 사용할 수 있다. 하지만 HTTP 메서드를 사용해 자원에 대한 연산을 처리하므로 동작이 한정적이라는 단점

---

- **URI(Uniform Reseource Identifier)**  
인터넷에 있는 자원을 나타내는 주소.  
URI 인터넷에서 요구하는 기본 조건으로 인터넷 프로토콜에 항상 붙어 다닌다. URI 하위 개념으로 URL, URN이 있다
- **URL(Uniform Resource Locator)**  
인터넷에서 자원의 위치를 알 수 잇는 규약.  
웹 사이트 주소와 인터넷의 모든 자원을 나타낼 수 있다.
- **URN(Uniform Resource Name)**  
자원의 위치 정보가 아닌 실제 자원을 특정

---

# REST API

REST API는 REST를 기반으로 한 API를 뜻한다. **API(Application Programming Interface)** 는 다른 소프트 웨어에 서비스를 제공하기 위한 소프트웨어 인터페이스다.  
**REST API는 REST를 기반으로 한 인터페이스**라고 할 수 있다. 여러 기업에서 자체 서비스를 제공하기 위해 REST API를 활용하고 있다

REST API 구성

REST API에서 자원의 식별은 URI로 하고, 자원에 대한 행위(처리)는 HTTP 메서드로 나타남.  
전달되는 데이터는 JSON  또는 XML 등으로 표현

1. 클라이언트가 URI 요청 메시지에 실려 서버에 전달.
2. REST API가 HTTP 요청 메시지에 실려 서버에 전달.
3. 서버에서는 수신한 HTTP 요청 메시지를 바탕으로 요청 사항을 확인해 처리하고 HTTP 응답을 반환한다. 응답에는 요청에 대한 처리 성공 여부와 정보 포함
4. 응답 메시지는 자원에 대한 정보를 JSON 또는 XML 등의 형태로 포함.  
클라이언트는 해당 형태의 정보 수신

---

REST 규칙을 지키며 API 제공하는 서비스를 **RESTful** 하다고 함.  
REST API를 최대한 RESTful하게 사용하려면 규칙 준수.

- 자원에 대한 행위는 HTTP 메서드로 나타내며, HTTP 메서드나 행위에 대한 표현이 URI에 들어가면 안 된다
- HTTP 메서드는 명시적이어야한다.   
즉, 요청하려는 목적에 맞게 HTTP 메서드를 사용해야 한다. POST 메서드로 Create뿐 아니라 Update 같은 연산을 하면 명시적이라고 할 수 없다.
- URI 경로는 슬래시(/)로 계층 관계를 표현, URI 마지막에 슬래시가 들어가면 안된다
- URI 경로에는 언더바(_)를 사용하면 안되고, 소문자 사용을 지향.

# HTTP 메서드

클라이언트가 요청을 보낼 때 요청에 포함된 HTTP 메서드는 요청의 종류와 목적을 나타냄.  
주요 HTTP 메서드

- **POST**  
데이터를 생성할 때 사용
- **GET**  
데이터를 조회할 때 사용
- **PUT**  
데이터를 갱신할 때 사용
- **DELETE**  
데이터를 제거할 때 사용

HTTP 메서드는 다음과 같이 CRUD 연산과 매칭.  
CRUD 연산은 각각 Create(생성), Read(조회), Update(갱신), Delete(삭제) 연산 나타냄’

HTTP 메서드와 CRUD 연산

| C | Create | POST |
| --- | --- | --- |
| R | Read | GET |
| U | Update | PUT |
| D | Delete | DELETE |
|  |  | HTTP 메서드 |

---

HTTP 메서드

- **PATCH**  
데이터를 일부 갱신할 때 사용
- **HEAD**  
GET과 동일하게 데이터를 조회할 때 사용, HTTP 메시지에 바디를 포함핮 않고 헤더로만 응답
- **TRACE**  
클라이언트의 요청 메시지를 그대로 반환(루프백 메시지)하면서 쿠키 및 세션 값을 포함해 응답
- **CONNECT**  
요청한 자원을 양방향으로 연결하는 데 사용, SSL 사용하는 웹 사이트에 접속할 수 있음
- **OPTION**   
서버가 지원하는 HTTP 메서드를 메시지 헤더에 포함해 응답