가상환경 생성/실행

.gitignore

git init

django 설치

```bash
$ pip freeze > requirement.txt
# requirement.txt 설정
$ pip install -r 
# 추후에 requirement.txt 설치

$ django-admin startprject crud .
# . 띄어쓰기 필수(현재 디렉토리에 생성)
```

app 만들고 등록

model 정의

	- models.py (스키마)
	- makemigrations (마이그레이션 파일 생성)
	- migrate (db 반영)

sqlite 설치

```bash
$ pip install ipython
$ python manage.py shell
```

```shell
from articles.models import Article
article = Article()
article.title = '1번글'
article.content = '1번 내용'
article.save()
Article.objects.create(title='제목2', content='내용2')
article = Article(title='제목3', content='내용3')
article.save()

Article.objects.all()[0]

Article.objects.get(title='test1111')
# 찾는 값이 하나일 때만 오브젝트를 띄움. 
Article.objects.filter(title='test1111')
# 찾는 값이 없어도 리스트로 반환
```

