import random
from random import randint

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

cardPullFacing = randint(0,1)

if cardPullFacing == 0:
    cardMeaningNormNum = randint(0,21)
    cardMeaningNormPull = cardMeaningNorm[cardMeaningNormNum]
    cardMeaningNormFace = allCardFaces[cardMeaningNormNum]
    card1 = card(cardMeaningNormPull,cardMeaningNormFace,False)
    print(card1)
elif cardPullFacing == 1:
    cardMeaningRevNum = randint(0,21)
    cardMeaningRevPull = cardMeaningRev[cardMeaningRevNum]
    cardMeaningRevFace = allCardFaces[cardMeaningRevNum]
    card1 = card(cardMeaningRevPull,cardMeaningRevFace,True)
    print(card1)
else:
    print('error')
