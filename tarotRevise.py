import random
from random import randint
from PIL import Image, ImageFont, ImageDraw

class card:
    def __init__(self,meaning,cardFace,rev):
        self.meaning = meaning
        self.cardFace =cardFace
        self.rev = rev

    def __str__(self):
        if self.rev == True:
            return f"Card face: {self.cardFace} meaning: {self.meaning}"
        elif self.rev == False:
            return f"Revsere card face: {self.cardFace} meaning: {self.meaning}"


allCardMeaning = [("Beginnings, innocence, spontaneity, a free spirit"),("Holding back, recklessness, risk-taking"),("Manifestation, resourcefulness, power, inspired action"),
                    ("Manipulation, poor planning, untapped talents"),("Intuition, sacred knowledge, divine feminine, the subconscious mind"),("REVERSED: Secrets, disconnected from intuition, withdrawal and silence"),
                    ("Femininity, beauty, nature, nurturing, abundance"),("Creative block, dependence on others"),("Authority, establishment, structure, a father figure"),("Domination, excessive control, lack of discipline, inflexibility"),
                    ("Spiritual wisdom, religious beliefs, conformity, tradition,institutions"),("Personal beliefs, freedom, challenging the status quo"),("Love, harmony, relationships, values alignment, choices"),
                    ("Self-love, disharmony, imbalance, misalignment of values"),("Control, willpower, success, action, determination"),("Self-discipline, opposition, lack of direction"),("Strength, courage, persuasion, influence, compassion"),
                    ("Inner strength, self-doubt, low energy, raw emotion"),("Soul-searching, introspection, being alone, inner guidance"),("Isolation, loneliness, withdrawal"),("Good luck, karma, life cycles, destiny, a turning point"),("Bad luck, resistance to change, breaking cycles"),
                    ("Justice, fairness, truth, cause and effect, law"),("Unfairness, lack of accountability, dishonesty"),("Pause, surrender, letting go, new perspectives"),("Delays, resistance, stalling, indecision"),
                    ("Shadow self, attachment, addiction, restriction, sexuality"),("Releasing limiting beliefs, exploring dark thoughts, detachment"),("Sudden change, upheaval, chaos, revelation, awakening"),("Personal transformation, fear of change, averting disaster"),
                    ("Hope, faith, purpose, renewal, spirituality"),("Lack of faith, despair, self-trust, disconnection"),("Illusion, fear, anxiety, subconscious, intuition"),("Release of fear, repressed emotion, inner confusion"),("Positivity, fun, warmth, success, vitality"),
                    ("Inner child, feeling down, overly optimistic"),("Judgement, rebirth, inner calling, absolution"),("Self-doubt, inner critic, ignoring the call"),("Completion, integration, accomplishment, travel"),("Seeking personal closure, short-cuts, delays"),
                    ("Endings, change, transformation, transition "),("Resistance to change, personal transformation, inner purging"),("Balance, moderation, patience, purpose"),("Imbalance, excess, self-healing, re-alignment")]
allCardFaces = [('fool'),('magician'),('highpriestess'),('empress'),('emperor'),('hierophant'),('lovers'),('chariot'),('strength'),('hermit'),('wheeloffortune'),
                ('justice'),('hangedman'),('death'),('tower'),('star'),('moon'),('sun'),('judgement'),('world'),('devil'),('temperance')]

cardMeaningNorm = allCardMeaning[::2]
cardMeaningRev = allCardMeaning[1::2]

cardPullFacing1 = randint(0,1)

if cardPullFacing1 == 0:
    cardMeaningNormNum = randint(0,21)
    cardMeaningNormPull = cardMeaningNorm[cardMeaningNormNum]
    cardMeaningNormFace = allCardFaces[cardMeaningNormNum]
    card1 = card(cardMeaningNormPull,cardMeaningNormFace,False)
    cardImg1 = Image.open("tarot-{cardMeaningNormFace}.jpg")
    print(card1)
elif cardPullFacing1 == 1:
    cardMeaningRevNum = randint(0,21)
    cardMeaningRevPull = cardMeaningRev[cardMeaningRevNum]
    cardMeaningRevFace = allCardFaces[cardMeaningRevNum]
    card1 = card(cardMeaningRevPull,cardMeaningRevFace,True)
    cardImg1 = Image.open("tarot-{cardMeaningRevFace}.jpg")
    cardImg1_Rev = cardImg1.rotate(180)
    cardImg1 = cardImg1_Rev
    print(card1)
else:
    print('error')

cardPullFacing2 = randint(0,1)

if cardPullFacing2 == 0:
    cardMeaningNormNum = randint(0,21)
    cardMeaningNormPull = cardMeaningNorm[cardMeaningNormNum]
    cardMeaningNormFace = allCardFaces[cardMeaningNormNum]
    card2 = card(cardMeaningNormPull,cardMeaningNormFace,False)
    cardImg2 = Image.open("tarot-{cardMeaningNormFace}.jpg")
    print(card2)
elif cardPullFacing2 == 1:
    cardMeaningRevNum = randint(0,21)
    cardMeaningRevPull = cardMeaningRev[cardMeaningRevNum]
    cardMeaningRevFace = allCardFaces[cardMeaningRevNum]
    card2 = card(cardMeaningRevPull,cardMeaningRevFace,True)
    cardImg2 = Image.open("tarot-{cardMeaningRevFace}.jpg")
    cardImg2_Rev = cardImg2.rotate(180)
    cardImg2 = cardImg2_Rev
    print(card2)
else:
    print('error')

cardPullFacing3 = randint(0,1)

if cardPullFacing3 == 0:
    cardMeaningNormNum = randint(0,21)
    cardMeaningNormPull = cardMeaningNorm[cardMeaningNormNum]
    cardMeaningNormFace = allCardFaces[cardMeaningNormNum]
    card3 = card(cardMeaningNormPull,cardMeaningNormFace,False)
    cardImg3 = Image.open("tarot-{cardMeaningNormFace}.jpg")
    print(card3)
elif cardPullFacing3 == 1:
    cardMeaningRevNum = randint(0,21)
    cardMeaningRevPull = cardMeaningRev[cardMeaningRevNum]
    cardMeaningRevFace = allCardFaces[cardMeaningRevNum]
    card3 = card(cardMeaningRevPull,cardMeaningRevFace,True)
    cardImg3 = Image.open("tarot-{cardMeaningRevFace}.jpg")
    cardImg3_Rev = cardImg3.rotate(180)
    cardImg3 = cardImg3_Rev
    print(card3)
else:
    print('error')

results = Image.open("picture.jpg")
results.paste(cardImg1, (50,100))
results.paste(cardImg2, (350,100))
results.paste(cardImg3, (650,100))
results.save('final.jpg')
results.show()
