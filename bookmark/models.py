from django.db import models

# 내가 데이터베이스에 어떤 데이터를 어떻게 저장할 것이냐?
# O.R.M

# Create your models here.

# Models.py -> Views.py -> Urls.py -> Template

# 하나의 테이블을 하나의 모델로 묘사한다.
# 모델은 class로 구현한다.

class Bookmark(models.Model):
    # 하나의 필드를 만든다.
    # 컬럼 이름 = 컬럼 종류(제약조건)
    site_name = models.CharField(max_length = 100)
    url = models.URLField('url')

    # 모델의 옵션
    class Meta:
        ordering = ['site_name']

    def __str__(self):
        return self.site_name

