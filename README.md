# Project - Crawler 
승부예측 프로젝트 진행에 필요한 데이터 크롤링소스
연구용으로만 사용하였음

## 소스설명
사용 설명서
1. crawl_core는 크롤링을 위한 기본적인 함수들이 구현되어 있다.
Beautifulsoup을 활용해서 웹으로부터 데이터를 얻어온다.
goal.com 함수는 json url 태그를 가져오며, get_data는 json 값을 가져와 텍스트 형식으로 리턴한다.
참고로 json을 사용하려면 리턴값에 json모듈을 이용한다.
eg) json.loads(return_value)

2. mariaDB는 mariaDB에 접속하여 명령어를 수행하는 함수로 구성되어 있으며
create함수 load함수의 차이는 db로 부터 값을 가져오는가으 차이가 있다.

3. crawl_source는 크롤링 진행할 때 필요한 함수들이 있으며,
goal.com Json파일로 부터 얻을 수 있는 태그를 불러오는 load_key_value와
기간을 월단위로 일정하게 나눠주는 time_calc
mariaDB에 데이터를 넣는 mariaDB_json으로 구성되어 있다.

4. main_script는 실제 수행하는 함수를 직접 작성하였으며,
multiprocessing을 활용하여, 병렬처리로 크롤링의 속도를 높였다.

5. 데이터가 양이 많고 크기 때문에, 데이터를 가진 페이지 url을 먼저 크롤링 하여 DB에 저장하고
추가적으로 DB에 저장된 url을 불러와 각각의 데이터를 크롤링함. (main_script.py)
