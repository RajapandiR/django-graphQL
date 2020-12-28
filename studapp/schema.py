import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload


from studapp import models

class StudType(DjangoObjectType):
	class Meta:
		model = models.Stud

class Query(graphene.ObjectType):

	studs = graphene.List(StudType)
	def resolve_studs(self, info):
		return models.Stud.objects.all()


class CreateStud(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    file = graphene.String()
    # file = graphene.String()
    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        graphene.types.datetime.Date()
        file = Upload(required=True)

    stud = graphene.Field(StudType)

    @staticmethod
    def mutate(root, info, name, age,file):
        stud = models.Stud(name=name, age=age,file=file)
        stud.save()
        return CreateStud(stud=stud)

   
# class UploadFile(graphene.ClientIDMutation):
#     class Input:
#         pass
#         # nothing needed for uploading file

#     # your return fields
#     file = graphene.String()
#     success = graphene.String()
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, **input):
#         # When using it in Django, context will be the request
#         files = info.context.FILES
#         # Or, if used in Flask, context will be the flask global request
#         # files = context.files

#         # do something with files

#         return UploadFile(success=True)
class Mutation(graphene.ObjectType):
    create_Stud = CreateStud.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)