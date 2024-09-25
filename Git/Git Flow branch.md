git-flow 사용되는 브랜치 총 5개

1. main (= master)
2. develop
3. feature
4. release
5. hotifx

# flow

사용자 케이스 별 flow 순으로 요약

## case1. 처음 프로젝트 셋팅부터 구현, 배포 하는 앱팀

1. `mkdir 앱_이름` or `flutter create 앱_이름`  
팀 리더가 new project 생성
2. 팀 리더가 git 공유 repository 올림
3. 나머지 팀원 고용 repository 올라 온 project 로컬 가져옴
4. 전 팀원 git flow 도구 사용 init(초기화) 해줌
5. 폭풍 엔터로 브랜치 명명규칙 기본값 따라줌
6. 모든 팀원 로컬 환경에서 처음에 main 브랜치 뿐 있었는데 develop 브랜치가 로컬에 생겨남
7. 각자 맡은 작업 시작 하기 위해 git flow 도구 사용 feature 브랜치 생성
8. (feature 폭풍 작업)
9. 작업 완료 후 feature 브랜치 push → pr
10. pr 타이틀, 설명 등 작성 후 리뷰어 팀원들 등록
11. pr 승인 되면 Squash and Merge 버튼 통해 압출 된 하나의 commit develop에 머지
12. 그리고 기존 feature 브랜치 삭제
13. 또 다른 feature 작업 위해 가장 마지막 업데이트 된 develop 브랜치 pull
14. (7 ~ 13번 무한 반복)
15. 어느정도 팀 원하는 작업 다 완료 해서 릴리즈 배포할 때가 됐다면 릴리즈 담당할 한명 정함
16. 현 버전 릴리즈 담당 1명 / 나머지는 그 다음 버전 릴리즈르 위한 feature 무한 작업
17. 릴리즈 담당자는 git flow 도구 사용 release 브랜치 생성
18. (버저닝 작업)
19. relase 브랜치 기반 배포 파일
20. 배포 한다 = 심사 요청
21. 심사 요청 후 이상이 있다? 릴리즈 브랜치 내 수정해줌
22. 심사를 모두 무사히 통과해 정상적으로 배포 완료
23. git flow 도구 사용 relase 브랜치 finish 해줌
24. 릴리즈 브랜치 이름 태그도 추가
25. git flow 도구 인해 자동으로 릴리즈 브랜치 삭제, main 체크아웃됨
26. main 브랜치 + 버저닝 태그와 함께 푸시
27. develop 브랜치 체크아웃하고 main 브랜치 내용으 백머지 함
28. develop 브랜치 푸시
29. (7 ~ 28번 무한 반복)

## case2. 기존 프로젝트에 합류 후 첫 feature 구현하게된 앱 개발자

1. 이미 기존 올라가 있는 git 공용 repository에서 project 확인
2. 공용 repository 올라온 project 로컬 가져옴
3. git flow 도구 사용 init 해줌
4. 브랜치 명명규칙은 이미 등록 된 기본값을 따라줌, 하나하나 잘 보면서 엔터 누르기
5. develop 브랜치 체크아웃
6. 맡은 작업 시작하기 위해 git flow 도구 사용 feature 브랜치 생성
7. (feature 폭풍 작업)
8. 작업 완료 후 feature 브랜치 push해서 pr 올림
9. pr 타이틀, 설명 등 작성 후 리뷰어 팀원들 등록
10. pr 승인 되면 squash and merge 버튼 통해 압축 된 하나의 commit develop에 머지
11. 기존 feature 브랜치 삭제
12. 또 다른 feature 작업 위해 가장 마지막 업데이트 된 develop 브랜치 pull
13. (7 ~ 12번 무한 반복)

## case3. 프로덕션에 올라가있는 앱에서 버그 발견한 앱 개발자

(내 로컬 프로젝트 git flow init 되어있는 가정)

1. 호들짝 놀래며 자책, 참단한 현 상황 디코 채널을 통해 슬픈 소식 침착하게 알리기
2. 기존 작업 중단
3. main 브랜치 체크아웃
4. pull 받아 최신 main 브랜치 바라봄
5. git flow 도구 사용 hotfix 브랜치 생성
6. (버그 수정 침착하게 뚝딱)
7. (버저닝 작업)
8. hotfix 브랜치 기반 배포 파일 만듬
9. 배포 한다. = 심사 요청
10. 심사 요청 후 이상? 릴리즈 브랜치 내 수정
11. 심사 모두 무사히 통과해 정상적 배포 완료
12. git flow 도구 사용 hotfix 브랜치 finish 해줌
13. hotfix 브랜치 이름 태그도 추가
14. git flow 도구 인해 자동 hotfix 브랜치 했던 작업 main 브랜치와 develop 브랜치 머지 해주고 develop 브랜치로 체크아웃 해줌
15. develop 브랜치 최종사항 버저닝 태그와 함께 푸시
16. main 브랜치도 체크아웃해서 푸시
17. develop 브랜치 체크아웃하고 main 브랜치 내용 백머지
18. develop 브랜치 psuh
19. 다시 develop 브랜치 체크아웃하고 멈췄던 작업 다시

## QA 해야하는 앱 서비스팀

1. 팀은 “새 기능 작업”과 “bugfix 해야하는 작업” 우선순위와 함께 나열
2. 플래닝 미팅 갖고 이번 스프린트 내에 할 수 있는 작업만 가져감
3. 새 기능 작업을 위해 feature 브랜치 생성 작업 pr하고 qa함
4. bugfix 작업 or feature 브랜치 생성 작업 pr하고 qa함
5. dev 환경 qa develop 브랜치 feature 브랜치 머지 되었을 때 항시
6. dev 환경 qa 나온 버그들도 feature 브랜치 생성 작업 pr qa
7. develop 브랜치 버그 없는 기능 완성 된 당장 출시 가능한 상태로 유지   
(진행중인 작업 머지되거나 불안전한 작업 머지되지 않도록 함)
8. 릴리즈 앞둔 시점 충분히 dev 환경 qa 이뤄지고 문제가 없는걸 확인
9. 현 버전 릴리즈 담당 1명 / 나머지 그 다음 버전 릴리즈 위한 feature 무한 작업
10. 릴리즈 담당자는 git flow 도구 사용 release 브랜치 생성
11. 나머지 그 다음 버전 릴리즈 위한 feature 무한 작업
12. (버저닝 작업)
13. release 브랜치 기반 배포 파일 만듬
14. prod 환경 qa 진행
15. prod 환경 qa에서 나온 소소한 버그들은 relase 브랜치내 에서 작업 or qa 함
16. 버저닝 작업 prod환경 qa 무사히 끝남 배포 준비
17. 배포 = 심사 요청
18. 심사 요청 후 이상? 릴리즈 브랜치 내 수정
19. 심사 모두 무사히 통과 정상적 배포완료
20. git flow 도구 사용 release 브랜ㅊ finish 해줌
21. 릴리즈 브랜치 이름 태그도 추가
22. git flow 도구 인해 자동 릴리즈 브랜치 삭제, main 체크아웃됨
23. main 브랜치 + 버저닝 태그와 함께 푸시
24. develop 브랜치 체크아웃 main 브랜치 내용 백머지
25. develop 브랜치 push