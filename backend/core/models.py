from django.db import models


# Create your models here.
class QuestLongDescription(models.Model):
    header = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    image = models.ImageField()
    keyPoints = models.CharField(max_length=100)
    startPoint = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    formats = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)

    def __str__(self):
        return self.header

    def __iter__(self):
        yield "id", self.pk
        yield "header", self.header
        yield "time", self.time
        yield "keyPoints", self.keyPoints
        yield "startPoint", self.startPoint
        yield "difficulty", self.difficulty
        yield "formats", self.formats
        yield "keyPoints", self.keyPoints
        yield "link", self.link
        yield "authors", self.authors
        yield "imageUrl", "/media/" + self.image.name
        yield "description", self.description

class QuestDescription(models.Model):
    header = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    places = models.CharField(max_length=100)
    startPoint = models.CharField(max_length=100)
    fires = models.IntegerField()
    image = models.ImageField()
    quest_long_description = models.ForeignKey(on_delete=models.SET_NULL, default=1, to=QuestLongDescription, null=True)


    def __str__(self):
        return self.header

    def __iter__(self):
        yield "id", self.pk
        yield "header", self.header
        yield "time", self.time
        yield "places", self.places
        yield "startPoint", self.startPoint
        yield "fires", self.fires
        yield "imageUrl", "/media/" + self.image.name
        yield "questId", self.quest_long_description.pk





# header: "Станция метро «Озерки»",
# question: "Внимательно рассмотрите масштабное панно на стене в конце зала. Что оно символизирует?",
# trueAnswer: ["времена года"],
# hints: "Обратите внимание на число деревьев",
# historicalText: "Станция была открыта в 1988 году. Её название обусловлено находящимися рядом Суздальскими озёрами. Это единственная станция, на которой можно наблюдать напольные мозаичные панно, сделанные в мозаичной мастерской Академии Художеств СССР. Напольная мозаика показала себя непрактичной в местах массового скопления людей. Панно стало довольно быстро портиться из-за воздействия на него в том числе каблуков от женской обуви. Кусочки смальты стали раскалываться и крошиться.",
# nextText: "Отправляйтесь на место легендарной дуэли самого известного поэта Золотого века русской литературы."

class Quest(models.Model):
    startInstructions = models.CharField(max_length=100)
    finalText = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default="Quest")

    def __str__(self):
        return f"{self.pk}"

    def __iter__(self):
        yield "id", self.pk
        yield "startInstructions", self.startInstructions
        yield "finalText", self.finalText


class Question(models.Model):
    order = models.IntegerField()
    header = models.CharField(max_length=100)
    question = models.TextField()
    trueAnswers = models.CharField(max_length=100)
    hints = models.CharField(max_length=100, blank=True, null=True)
    historicalText = models.TextField(blank=True, null=True)
    nextText = models.TextField(blank=True, null=True)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)

    def __str__(self):
        return self.header

    def __iter__(self):
        yield "order", self.order
        yield "header", self.header
        yield "question", self.question
        yield "trueAnswers", self.trueAnswers
        yield "hints", self.hints
        yield "historicalText", self.historicalText
        yield "nextText", self.nextText
