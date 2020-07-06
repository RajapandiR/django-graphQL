import graphene
from graphene_django.types import DjangoObjectType

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
    
    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        graphene.types.datetime.Date()

    stud = graphene.Field(StudType)

    @staticmethod
    def mutate(root, info, name, age ):
        stud = models.Stud(name=name, age=age)
        stud.save()
        return CreateStud(stud=stud)

class Mutation(graphene.ObjectType):
    create_Stud = CreateStud.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)