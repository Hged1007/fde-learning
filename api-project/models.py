#model 模型
from tabnanny import verbose
from tortoise import fields
from tortoise.models import Model   # pyright: ignore[reportMissingImports]

class Publish(Model):
    name=fields.CharField(max_length=32,verbose="出版社名称")
    email=fields.CharField(max_length=32,verbose="出版社邮箱")

class Author(Model):
    name=fields.CharField(max_length=32,verbose="作者")
    age=fields.CharField(max_length=32,verbose="年龄")

class Book(Model):
    title=fields.CharField(max_length=32,verbose="书名") 
    price=fields.CharField(max_length=32,verbose="价格") 
    img_url=fields.CharField(max_length=255,null=True,blank=True,verbose="") 
    bread=fields.IntField(verbose="阅读量")
    bcomment=fields.IntField(verbose="评论量")
    publish=fields.ForeignKeyField('models.Publish',related_name='books')
    authors=fields.ManyToManyField('models.Author',related_name='books',description="作者")


      

