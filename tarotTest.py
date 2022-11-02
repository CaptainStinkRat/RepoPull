from PIL import Image


def tarot(card):
    if card == 'The Fool':
        card_meaning=("UPRIGHT: Beginnings, innocence, spontaneity, a free spirit REVERSED: Holding back, recklessness, risk-taking")
    elif card == 'The Magician':
        card_meaning=("UPRIGHT: Manifestation, resourcefulness, power, inspired action REVERSED: Manipulation, poor planning, untapped talents")
    elif card == 'The High Priestess':
        card_meaning=("UPRIGHT: Intuition, sacred knowledge, divine feminine, the subconscious mind REVERSED: Secrets, disconnected from intuition, withdrawal and silence")
    elif card == 'The Empress':
        card_meaning=("UPRIGHT: Femininity, beauty, nature, nurturing, abundance REVERSED: Creative block, dependence on others")
    elif card == 'The Emperor':
       card_meaning=("UPRIGHT: Authority, establishment, structure, a father figure REVERSED: Domination, excessive control, lack of discipline, inflexibility")
    elif card == 'The Hierophant':
        card_meaning=("UPRIGHT: Spiritual wisdom, religious beliefs, conformity, tradition,institutions REVERSED: Personal beliefs, freedom, challenging the status quo")
    elif card == 'The Lovers':
        card_meaning=("UPRIGHT: Love, harmony, relationships, values alignment, choices REVERSED: Self-love, disharmony, imbalance, misalignment of values")
    elif card == 'The Chariot':
        card_meaning=("UPRIGHT: Control, willpower, success, action, determination REVERSED: Self-discipline, opposition, lack of direction")
    elif card == 'Strength':
        card_meaning=("UPRIGHT: Strength, courage, persuasion, influence, compassion REVERSED: Inner strength, self-doubt, low energy, raw emotion")
    elif card == 'Hermit':
        card_meaning=("UPRIGHT: Soul-searching, introspection, being alone, inner guidance REVERSED: Isolation, loneliness, withdrawal")
    elif card == 'Wheel Of Fortune':
        card_meaning=("UPRIGHT: Good luck, karma, life cycles, destiny, a turning point REVERSED: Bad luck, resistance to change, breaking cycles")
    elif card == 'Justice':
        card_meaning=("UPRIGHT: Justice, fairness, truth, cause and effect, law REVERSED: Unfairness, lack of accountability, dishonesty") 
    elif card == 'Hanged Man':
        card_meaning=("UPRIGHT: Pause, surrender, letting go, new perspectives REVERSED: Delays, resistance, stalling, indecision")         
    elif card == 'Death':
        card_meaning=("UPRIGHT: Endings, change, transformation, transition REVERSED: Resistance to change, personal transformation, inner purging")
    elif card == 'Temperance':
        card_meaning=("UPRIGHT: Balance, moderation, patience, purpose REVERSED: Imbalance, excess, self-healing, re-alignment") 
    elif card == 'Devil':
        card_meaning=("UPRIGHT: Shadow self, attachment, addiction, restriction, sexuality REVERSED: Releasing limiting beliefs, exploring dark thoughts, detachment")
    elif card == 'Tower':
        card_meaning=("UPRIGHT: Sudden change, upheaval, chaos, revelation, awakening REVERSED: Personal transformation, fear of change, averting disaster")
    elif card == 'Star':
        card_meaning=("UPRIGHT: Hope, faith, purpose, renewal, spirituality REVERSED: Lack of faith, despair, self-trust, disconnection")
    elif card == 'Moon':
        card_meaning=("UPRIGHT: Illusion, fear, anxiety, subconscious, intuition REVERSED: Release of fear, repressed emotion, inner confusion")
    elif card == 'Sun':
        card_meaning=("UPRIGHT: Positivity, fun, warmth, success, vitality REVERSED: Inner child, feeling down, overly optimistic")
    elif card == 'Judgement':
        card_meaning=("UPRIGHT: Judgement, rebirth, inner calling, absolution REVERSED: Self-doubt, inner critic, ignoring the call")
    elif card == 'World':
        card_meaning=("UPRIGHT: Completion, integration, accomplishment, travel REVERSED: Seeking personal closure, short-cuts, delays") 
    else:
        card_meaning=("Make sure to capitalize the card name.")
    return card_meaning
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)
def image_pull(card_title):
    if card_title == 'The Fool':
        card_image= Image.open("tarot-fool.jpg")
    elif card_title == 'The Magician':
        card_image= Image.open("tarot-magician.jpg")
    elif card_title == 'The High Priestess':
        card_image = Image.open("tarot-highpriestess.jpg")
    elif card_title == 'The Empress':
        card_image = Image.open("tarot-empress.jpg")
    elif card_title == 'The Emperor':
        card_image = Image.open("tarot-emperor.jpg")
    elif card_title == 'The Hierophant':
        card_image = Image.open("tarot-hierophant.jpg")
    elif card_title == 'The Lovers':
        card_image = Image.open("tarot-lovers.jpg")
    elif card_title == 'The Chariot':
        card_image = Image.open("tarot-chariot.jpg")
    elif card_title == 'Strength':
        card_image = Image.open("tarot-strength.jpg")
    elif card_title == 'Hermit':
        card_image = Image.open("tarot-hermit.jpg")
    elif card_title == 'Wheel Of Fortune':
        card_image = Image.open("tarot-wheeloffortune.jpg")
    elif card_title == 'Justice':
        card_image = Image.open("tarot-justice.jpg")
    elif card_title == 'Hanged Man':
        card_image = Image.open("tarot-hangedman.jpg")
    elif card_title == 'Death':
        card_image = Image.open("tarot-death.jpg")
    elif card_title == 'Tower':
        card_image = Image.open("tarot-tower.jpg")
    elif card_title == 'Star':
        card_image = Image.open("tarot-star.jpg")
    elif card_title == 'Moon':
        card_image = Image.open("tarot-moon.jpg")
    elif card_title == 'Sun':
        card_image = Image.open("tarot-sun.jpg")
    elif card_title == 'Judgement':
        card_image = Image.open("tarot-judgement.jpg")
    elif card_title == 'World':
        card_image = Image.open("tarot-world.jpg")
    else:
        print("error.")
    return card_image

card_name=input("Hello enter the card name you want to look up. Make sure to capitalize each letter of the card name:")
card_print=tarot(card_name)
image=image_pull(card_name)
print_msg_box(card_print)
image.show()
