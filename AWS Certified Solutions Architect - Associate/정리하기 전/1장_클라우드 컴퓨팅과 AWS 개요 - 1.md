 # 클라우드 컴퓨팅과 가상화

모든 클라우드 컴퓨팅 서비스 핵심 기술은 **가상화**  

**가상화란?**
하나의 물리적 서버 형태로 존재하는 HW 리소스를 여러 개의 작은 유닛으로 나누는 것.
가상의 작은 유닛으로 분활된 물리적 서버는 자체 운영 체제와 함께, 
유닛별 메모리, 스토리지, 네트워크를 할당 받은 가상 머신이 돼 완벽하게 작동.

가상화 기술  
사용자가 가상 서버를 몇초만에 배포하고, 프로젝트 요구 사항에 맞춰 실행 후 즉시 삭제할 수 있을 정도로 높은 유연성 제공.

→ 생성된 리소스는 다른 워크로드 HW 성능 및 가치를 최대치로 ↑  
상용화 테스트 환경 및 실험 환경을 쉽게 만들 수 있게된다.

## 클라우드 컴퓨팅 아키텍처

AWS 같은 주요 클라우드 서비스 제공사는 수십만 대의 서버,   
디스크 드라이브러를 네트워크 케이블로 연결한 방대한 규모의 서버 팜을 운영. 
 
정비된 가상환경은 스토리지, 메모리, 컴퓨트 사이클을 이용한 가상 서버를 제공,  
활용 간으 리소스의 최적이 이용이 가능하도록 네트워크 서비스를 제공.

클라우드 컴퓨팅 플랫폼, → 사용자는 워크로드 처리를 위해 온디맨드 및 셀프 서비스 기반의 컴퓨트 리소스 풀에 접속,   
→ 사용 내역은 정확하게 측정돼. 사용량에 따라 과금된다.   
클라우드 컴퓨팅 시스템은 시간에 따른 사용량을 매우 세분화된 수준에서 정확하게 측정하는 과금 모델을 제공.

## 클라우드 컴퓨팅 최적화

클라우드 확장성 및 탄력성을 지니고 있고, 전통적인 시스템에 비해 ↓비용이 소요므로 변동성 높은 워크로드 처리를 위한 탁우러한 선택  
사용자는 효과적인 클라우드 리소스 배포를 위해  세 가지 속성에 대한 나름의 감각 또는 인사이트를 지니고 있다.

- **확장성(Scalability)**
    
    인프라의 확장성이 ↑ 의미.   
    사용자의 애플리케이션에 예측하지 못한 트래픽이 몰렸을 때  
    → 해소하기 위한 리소스를 자동으로 추가.  
    처리 용량의 증가에 맞춰 가상 머신 또는 인스턴스의 수를 동적 ↑ 시키는 방법을 보여준다  
    (AWS 가상머신은 인스턴스라는 이름으로…)
    
    AWS 사전 정의된 요구 수준에 맞춰 필요한 즉시 자동으로 머신 이미지를 복제해 론칭할 수 있는 오토스케일링 서비를 제공.
    
- **탄력성(Elastcity)**
    
    원칙 또는 확장성과 같이 요구 수준 변화에 대해 시스템이 어떻게 반응하도록 할 것인지 하는 문제를 다룸.  
    탄력성이 확정성과 다른 부분.   
    **확장성**은 수요 ↑에 따라 리소스를 증대 시키는 개념.  
    **탄성력**은 수요  ↓시키는 개념을 포함.  
    → 사용자는 꼭 필요할 떄만 리소스를 실행하면 되므로 클라우드 비용을 효과적으로 통제.
    
- **비용 관리(Cost Management)**
    
    사용하는 리소스의 양과 관련된 비용을 통제하는 것과 별개로 클라우드 컴퓨팅은 IT 인프라 도입 및 운영을 기존의 자본 비용(capex) 관점에서 운영 비용(opex) 관점으로 변화.
    
    전산 업무 개념에서 설명하면  
    클라우드 컴퓨팅 환경에선 새 서버 한 대를 도입하기 위해 자본적 지출에 해당하는 고정비 $10,000와 그에 수반되는 전기료, 냉각장치비, 보안 유지비, 서버 공간 비용 등을 지불할 필요가 없다는 것.  
    대신 사용자는 자신이 실행하는 애플리케이션 실행과 관련된 훨씬 적은 수준의 운영 비용만 지불.  
    사용자는 변화하는 수요에 대응하기 위해 클라우드를 통해 좀더 간단하게 배포 → 리소스 용량을 늘이거나 줄일 수 있게 됨.  
    ex.  커머스 비즈니스의 경우,  
    수요 금증 기간 동안에는 리소스를 추가로 배포하고 수요가 감소하면 자동으로 리소스를 줄일 수 있다.
    
    → 클라우드 기반의 총 운영 비용이 전통적인 data 센터 구축 및 운영 비용보단 낮다는 것은 X,  
    사용자가 장기적인 수요의 관점에서 불필요한 자본적 지출의 리스크를 줄일 수 있다는 것은 분명함.  
    즉, 신규 사업을 위해 IT 인프라에 대규모 투자를 했찌만 수요 감소로 해당 사업에서 철수해야 할 수도 있고,  
    도입 당시엔 최신 기술이였으나 기술 트렌드의 급격한 변화로 불과 수년 내에 서버를 교체하거나 업그레이드해야 하는 리스크가 존재.
    
    - +
        
        클라우드 컴퓨팅 비용 계산을 위해   
        AWS - Pricing Calculator  제공
        
        AWS Pricing Calculator는 형행 data 센터의 비용과 AWS 기반 클라우드 리소스 활용 비용을 일대일 방식으로 비교 계산
        

# AWS 클라우드

AWS는 늘 혁신을 추구, 새로운 서비스를 추가하고 있으며, 누군가 최신의 AWS 서비스를 지속적으로 파악하고 활용하는 일을 결코 쉬운 일이 아니다.  
but. 솔루션 아키텍트로서, 핵심적인 AWS 서비스를 잘 파악하고 있어야한다.

핵심적이 AWS 서비스를 카테고리별 구분, 카테고리별 주요 서비스를 간략 정리.  
AWS 전박적인 서비스의 개요 파악, 해당 서비스와 다른 서비스와의 관계, AWS 생태계에 해당 요소의 상대적인 위치. 알 수 있다

### AWS 서비스 카테고리

| 카테고리 | 기능 |
| --- | --- |
| 컴퓨트 | 전통적인 물리적 서버를 클라우드에 복제한 개념의 서비스로서 오토스케일링, 로드밸런싱은 물론 서버리스 아키텍처와 같은 고급 환경설정 기능을 제공. |
| 네트워킹 | 애플리케이션 연결성, 액세스 컨트롤, 강화된 원격 연결성 제공. |
| 스토리지 | 다양한 객체 저장 목적에 활용, 즉각적인 접근성 및 장기적인 백어 기능 제공하는 스토리지 플랫폼. |
| 데이터베이스 | 관계형, NoSQL, 캐싱 등 다양한 데이터를 포맷을 지원하는 관리형 데이터 솔루션. |
| 애플리케이션 관리 | AWS 리소스에 대한 모니터링, 감사, 환경설정 기능을 제공. |
| 보안 및 권한 증명 | 권한 인증, 권한 부여, 데이터 및 연결 암호화, 서드 파티 인증 관리 시스템과 통합 기능을 제공. |

### 핵심 AWS 서비스

| 카테고리 | 서비스 | 기능 |
| --- | --- | --- |
| 컴퓨트 | Elastic Compute Cloud(EC2) | EC2 서버 인스턴스는 전통적인 data 센터에선 실행되던 서버의 가상화 버전이라 할 수 있음. EC2 인스턴스는 CPU, 메모리, 스토리지, 네트워크 인터페이스 프로필 등과 함께 프로비저닝되며, 간단한 웹 서버부터 통합 멀티 티어 아키텍처 기반의 클러스터용 인스턴스까지 구현.
EC2 인스턴스는 가상화된 리소스이므로, 효율성은 높고 배포는 즉각 이루어짐 |
|  | Lambda | 실행 중인 EC2 인스턴스 이미지 템플릿으로 저장. 
트래픽 급증 등 요구 조건이 증가하면 해당 템플릿을 이용해 자동으로 인스턴스를 추가, 확정. 요구 조건이 감소하면 미사용 인스턴스 폐쇄. |
|  | Auto Scaling | 하나의 웹 서버로 처리할 수 없는 수준의 네트워크 트래픽을 사용량이 적거나 미사용중인 다수의 웹 서버로 분산. |
|  | Elastic Load Balancer | AWS 컴퓨트 및 네트워킹 인프라 프로비저닝을 추상화한 관리형 서비스.
사용자가 애플리케이션 코드를 업로드하면, 애플리케이션을 자동으로 론칭, 실행에 필요한 각종 서비스를 제공 |
|  | Elastic Container Service | Docker 또는 Kubernetes 등과 같은 컨테이너 기술을 이용해 다른 AWS 계정 소유 리소스와 완벽하게 통합할 수 있는 컴퓨트 워크로드를 프로비전, 자동화, 배포, 관리 업무를 수행할 수 있다. Kubemetes의 경우. 전용의 컴퓨트 워크로드인 Amazon Elastic Kubernetes SErvice (EKS)사용. |
|  | Elastic Beandstalk | Beanstalk는 AWS 컴퓨트와 네트워크 인프라의 프로비저닝을 추상화한 관리형 서비스, 개발자가 애플리케이션 코드 작성에만 집중 할 수 있도록 해줌. Beanstalk는 애플리케이션 서비스 구현에 피요한 제반 요소 자동으로 시작 및 관리 |
| 네트워킹 | Virtual Private Cloud(VPC) | EC2 (및 RDS) 인스턴스 호스팅을 위해 만들어진, 고도의 환경설정이 가능한 네트워크 환경. 사용자는 VPC 기반 도구를 이용해 인스턴스의 네트워크 보안을 유지, 외부 환경과 격리해서 인바운드 및 아웃바운드 네트워크 트래픽을 긴밀하게 제어. |
|  | Direct Connect | 속도 및 보안 수준이 높은 전용의 네트워크 연결 서비스를 통해 서드파티 공급자와 AWS를 연결해 로컬 데이터 센터 또는 AWS VPC 전용 네트워크를 구현 |
|  | Route 53 | 도메인 등록, 레코드 어드민, 라우팅 프로토콜 관리, 헬스 체크 등의 기능을 제공하는 AWS DNS 서비스, 다른 AWS 리소스와 완벽한 통합성 제공. |
|  | CloudFront | 아마존의 글로벌 분산화 CDN(Content Delivery Network) 서비스. → 사용자는 글로벌 차원의 엣지 로케이션에 사이트 콘텐츠의 캐시 버전을 저장할 수 있고 고객의 요청시 매우 신속하며 효율적으로 콘텐츠 제공. |
| 스토리지 | simple Storage Service(S3) | 다목적성, 신뢰성을 갖춘 저렴한 객체 저장 서비스로서 data 스토리지 및 백업 용도로 널리 활용. S3는 AWS 기반 사용화 서비스 구현시 보편적으로 사용, 상용화 버전과 관련된 스크립트, 템플릿, 로그 파일 스토리지 활용 |
|  | S3 Glacier | 장기간, 저렴하게 대량의 data 아카이브를 저장할 수 있도록 해주는 서비스로서 일정 시간의 인출 지연 시간이 존재. Glacier 생애 주기는 S3와 긴밀하게 통합돼 관리. |
|  | Elastic Block Store(EBS) | EC2 인스턴스의 운영 체제 및 각종 실행 data호스팅하기 위한 지속형 가상 스토리지 드라이브. 물리적 서버에 부착하는 스토리지 드라이브의 기능 및 파티션 속성을 가상 환경에서도 사용 |
|  | Storage Gateway | AWS 클라우드 스토리지를 로컬, 온프레미스 환경과 연결해서 사용할 수 있또록 해주는 하이브리드 스토리지 시스템. 데이터 마이그레이션 및 데이터 백업, 재난 복구 작업의 일부 활용. |
| 데이터베이스 | Relational Database Service(RDS) | 안정성, 보안성 신뢰성을 갖춘 관리형 SQL  데이터베이스 서비스. 사용자는 MySQL, Microsoft SQL Server, Oracle, Amazon이 만든 Aurora등 다양한 SQL 엔진 사용. |
|  | DynamoDB | 신속성, 유연성, 고확장성을 지닌 관리형 NoSQL 데이터베이스 서비스. |
| 애플리케이션 | CloudWatch | 프로세스 성능 및 리소스 사용량 모니터링 서비스로서, 사용자가 미리 정한 기준치에 도달, 메시지를 전송하거나 자동화된 응답 실행. |
|  | CloudFormation | AWS 리소스 배포를 위한 완벽하면서도 복잡적인 요구 사항 정의 템플릿 제공. 사용자는 AWS 인프라에 대한 스크립트를 작성해 자동화된 리소스 관리가 가능, 애플리케이션 론칭 프로세스를 표준화 간소화 |
|  | ColudTrail | API 이벤트와 관련된 모든 사용자 계정의 기록을 수집해서 감사 업무 및 시스템 문제 해결에 활용. |
|  | Config | AWS 계정과 관련된 변경 사항 관리 및 규정 준수 업무를 지원. 사용자가 바람직한 형태의 환경설정 상태를 정의, Config는 정의된 내용과 다른 변경 사항을 감지 및 평가하게됨. 변경 사항과 미리 정된 내용관의 격차가 일정 수준 이상인 경우, 알림 메시지를 발송 |
| 보안 및 권한 관리 | ldentily and Access Management(IAM) | AWS 계정에 대한 특정 사용자 또는 프로그래밍 차원의 접근을 관리하기 위한 서비스. 유저, 그룹, 역할, 정책 등 개념을 통해 AWS 리소스에 누가. 어떤 작업을 위해 접근하게 할지 매우 상세하게 지정. |
|  | Key Management Service(KMS) | AWS 리소스와 관련된 보안 data의 암호화 키 생성 및 관리를 위한 어드민 서비스. |
|  | Directory Service | AWS 리소스의 활용을 위해, Amazon Cognito 및 Microsoft AD 도멘인 등 내외부의 신원 인증 제공 서비스와 통합 관리. |
| 애플리케이션 통합 | Simple Notification Service(SNS) | SQS, Lambda 등 다른 서비스나 모바일 기기에게 자동으로 알림 또는 경고 메시지를 보내거나 다른 수신자에게 이메일 또는 SMS를 전송하는 서비스. |
|  | Simple Workflow(SWF) | 일련의 AWS 서비스 또는 디지털화할 수 없는 (사람의 특정 동작이 관련된) 이벤트를 포함, 연속적인 작업 관리 서비스.  |
|  | Simple Aueue Service(SQS) | 분산 시스템 등 대규모 프로세스에 포함된 다수의 업무 단계를 느슨하게 연결해 유연한 처리를 돕는, 이벤트 기반 메시징 서비스. SQS 메시지에 담긴 데이터는 신회할 수 있는 방식으로 전달돼. 애플리케이션의 내오류성 높일 수 있음. |
|  | API  Gateway | AWS 기반 애플리케이션을 위한 안전, 신뢰할 수 있는 API 생성하고 관리하기 위한 서비스. |

# AWS 플랫폼 아키텍처

AWS는 전세계에 산재한 자사의 물리적 서버를 관리하기 위해 자체 data 센터를 운영중.  
→ data 센터는 고도로 분산화돼 운영, 사용자는 자신과 좀더 가까운 data 센터에서 워크로드를 처리함으로써 네트워크 전송 지연을 줄일수 있다.  
또한 사용자 데이터와 같이 국가별 법령에 의해 이동이 불가능한 data도 있으므로, 법령에 저촉되지 않도록 data 센터 위치를 선정하는 것 또한 중요.

(집필 시점)글로벌 AWS 리전의 수는 21개(미국 정부 전용 제),  
(현재) 글로벌 AWS 리전의 수는 30개 (미국 정부 전용 제외) 그리고 새로운 리전 예정인 곳 3개

사용자는 새로운 AWS 리소스를 론칭할 때 어떤 리전에서 할 것인지 신중하게 결정, → 부과되는 요금 및 서비스 내용이 달라질 수 있기 때문이다.

**공식적으로 접근 가능한 AWS 리전**

https://aws.amazon.com/ko/about-aws/global-infrastructure/

---

++

엔드포인트 주소는 애플리케이션 코드 또는 스크립트를 이용해 원격으로 AWS 리소스에 접근할 때 사용, 엔드포인트에 ec2, apigateway 또는 cloudformation과 같은 전치사를 추가해 해당 AWS 서비스를 가리키도록 할 수 있음.  

---

전송 속도가 중요 일부 AWS 서비스의 경우,   
전용 엣지 네트워크 로케이션을 이용하기도 하며, Amazon CloudFront, Amazon Route 53, AWS Firewall Manager, AWS shield, AWS WAF 등 해당된다.

**최신 사용가능 로케이션 목록**

https://aws.amazon.com/ko/about-aws/global-infrastructure/regions_az/#Edge_Locations

AWS 계정으로 접속 가능한 물리적인 AWS data 센터를 가용성 지역 또는 AZ라 부름.  하나의 리전 내에 5 ~ 6개의 AZ존재.  
us-east-la 및 us-east-1b 각각 하나 혹은 그 이상의 data 센터를 구성.

리전 내 리소스는 하나 또는 그 이상의 가상 프라이빗 클라우드 또는 VPC에 포함시켜 사용.  
VPC는 사용자별 보안이 유지, 네트워크 주소 공간이며 사용자는 여기에 네트워크 서브넷을 만들거나 AZ를 연결해 사용.  
VPC 대한 적절한 환경설정을 통해, 사용자는 효과적으로 자신의 리솟를 다른 네트워크와 격리해서 안정성, 지속성이 확보된 복제 공간 활용. 

# AWS 신뢰성 및 서비스 규약

AWS 계정을 생성 직후 새 인스턴스를 생성하기까지 많은 기본 규약과 지침, 보안 규정을 제시.  

AWS는 글로벌 클라우드 서비스를 제공하기 위해, 인프라 어드민과 관련된 리소스 개발 및 전무성 확보에 엄청난 양의 인적, 물적 투자를 해옴, data 센터 보안, 반복 구현 레이어, 위법한 복제를 방지하기 위한 검증된 프로토콜 구현 등 당양한 어드민 지원 체계를 확보 개선.

AWS 플랫폼 상 존재하는 리소스는 ISO 9001, FedRAMP, NIST, GDPR 등 수십여가지의 글로벌 표준 국가별 표준, 공통 규약, 조건 준수. 

https://aws.amazon.com/ko/compliance/programs/

## AWS 공유 책임 모델

안정장치 및 편의성 요소는 모두 AWS 플랫폼에 제공.  
but. AWS에 업로드한 data, AWS 구현한 애플리케이션은 사용자 또는 사용자라면 누구라도 AWS 공유 책임 모델을 명확하게 이해할 필요O.

AWS는 클라우드 자체의 보안 유지 및 원활한 운영 책임.  
즉, AWS 물리적 서버, 스토리지, 네트워킹 인프라, 각종 관리형 서비스에 대해 책임.

반면, 곡개 또는 사용자는 클라우드 안에 있는 것에 대해 책임을 진다.  
즉, 사용자가 설치한 운영 체제에 대한 보안 및 운영, 클라이언트 측 데이터, 네트워크에서 유입 및 유출되는 data, 사용자 인증 및 접근 권한 부여, data 관리 책임 있다.

## AWS 서비스 수준 합의서

AWS 서비스 수준 합의서에서의 
**보증**이란
단어는 클라우드 사용자가 일시적 서비스 중단 또는 보안 위험 노출 문제를 절대 격지 않다는 의미? == X

클라우드 인프라를 구성하는 하드 드라이브가 멈출 수 있고, 자연 재해가 일어날 수 있기 때문이다.

실제로 발생했을 때, AWS 합의서는 통해 미리 약정한 시간 내에 관련 문제를 해소하고 정상적으로 서비스를 제공할 것임을 약속.  
→ AWS 약속이 모든 고객에게 만족스럽지 않을수도?, 장애 등으로 인한 손실이 보상되지 않을 수도..

AWS는 서비스 수준 합의서  
즉, SLA를 통해 보증 비율을 명시. 보증 비율은 서비스마다 다르다.  
ex. EC2 경우 99% 사용성을 보장.  
→ EC2 인스턴스, ECS 컨테이너, EBS 스토리지 사용자가 30ㅇ리 중 대략 4분을 제외하고 언제나 정상적으로 서비스를 이용할 수 있는 수준.

중요한 요소 ‘실패 가능성이 낮다’는 점보다는 ‘언제 실패할 수 있는가’의 문제일 것이다.  
→ 애플링케이션 서비스 제공자는 내오류성 및 글로벌 리전에 대한 반복 구현 전략을 통해 실패 가능성을 최소한하는 것이 중요.
