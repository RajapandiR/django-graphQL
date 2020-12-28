import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload


from studapp import models

class StudType(DjangoObjectType):
	class Meta:
		model = models.Stud

class Query(graphene.ObjectType):
    studs = graphene.List(StudType)
    edit = graphene.Field(StudType, id=graphene.Int())
    delete = graphene.Field(StudType, id=graphene.Int())
    def resolve_studs(self, info):
        return models.Stud.objects.all()
    def resolve_edit(self, info,id):
        return models.Stud.objects.get(pk=id)
    def resolve_delete(self, info,id):
        return models.Stud.objects.get(pk=id)


class CreateStud(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    file = graphene.String()
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

class EditStud(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    file = graphene.String()
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        age = graphene.Int()
        graphene.types.datetime.Date()
        file = Upload()

    stud = graphene.Field(StudType)
    @staticmethod
    def mutate(root, info,id,file = None, name=None, age=None):
        stud = models.Stud.objects.get(pk=id)
        if name != None :
            stud.name = name
        if age != None :
            stud.age = age
        if file != None :
            print(file)
            stud.file = file
            print(stud.file)
        stud.save()
        return EditStud(stud=stud)

class DeleteStud(graphene.Mutation):
    id = graphene.ID()
    class Arguments:
        id = graphene.ID(required=True)

    stud = graphene.Field(StudType)
    @staticmethod
    def mutate(root, info,id):
        stud = models.Stud.objects.get(pk=id)
        print(stud)
        stud.delete()
        return DeleteStud(stud=stud)

class Mutation(graphene.ObjectType):
    create_Stud = CreateStud.Field()
    edit_Stud = EditStud.Field()
    delete_Stud = DeleteStud.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)