from flask import Flask, request
from flask_cors import CORS
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import matplotlib.pyplot as plt
from flask import Flask
from googletrans import Translator
import random

app = Flask(__name__)
CORS(app)

nltk.download('stopwords')
nltk.download('punkt')
# text = "I am really sad to see you! "
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words and word.isalpha()]
    return ' '.join(filtered_text)


def analyze_sentiment(text):
    # 示例文本
    processed_text = preprocess_text(text)
    # print("Processed Text:", processed_text)
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

@app.route('/analyze_sent', methods=['POST'])
def analyze_sent():
    positive_responses = [
"积极的心态让你更有动力和热情去追求自己的目标和梦想。当你拥有积极的心态时，你会感受到内心的喜悦和满足。这种积极的心态会激发你的内在动力，让你更加专注和努力地朝着自己的目标前进。无论遇到多大的困难和挑战，你都会坚持不懈地努力，因为你相信自己能够克服一切困难。"
,"保持积极心态可以帮助你更好地应对生活中的挑战和困难。当你面对困难时，积极的心态会让你更加乐观和自信。你会相信自己有能力找到解决问题的方法，并且相信一切都会变得更好。积极的心态还能帮助你更好地应对压力，保持冷静和理智的思考，从而做出更明智的决策。"
, "积极的心态让你更加乐观和自信，从而更好地面对各种情况。当你拥有积极的心态时，你会更加相信自己的能力和价值。你会对自己充满信心，相信自己可以应对任何挑战和困难。这种自信会让你更加勇敢地面对生活中的各种情况，无论是工作上的压力还是人际关系的挑战，你都能够从容应对。"
, "积极的心态可以提高你的创造力和解决问题的能力。当你拥有积极的心态时，你会更加开放和灵活地思考问题，从而找到更多的解决方案。你会更加有创意地思考，找到新的方法和途径来解决问题。同时，积极的心态也会让你更加坚持不懈地去解决问题，不轻易放弃，直到找到最佳的解决方案。"
, "你的积极心态会影响周围的人，传递积极的能量和影响。当你拥有积极的心态时，你会成为身边人的榜样和鼓舞。你的积极能量会感染他人，让他们也变得更加积极和乐观。你的积极心态会在你的家庭、工作场所和社交圈中产生积极的影响，创造出更加和谐、积极的氛围。"
, "保持积极心态可以增强你的身体健康，提高免疫力和抵抗力。研究表明，积极的心态与身体健康之间存在着密切的关联。当你拥有积极的心态时，你的身体会释放出更多的免疫细胞和抗体，从而增强你的免疫力。同时，积极的心态还能降低患病的风险，减少慢性疾病的发生。所以，保持积极心态不仅有助于你的心理健康，也对你的身体健康有着积极的影响。"
, "积极的心态让你更有耐心和坚韧，不轻易放弃。当你拥有积极的心态时，你会相信自己的努力和坚持一定会有回报。你会更加有耐心地等待结果的到来，不会轻易放弃。即使遇到挫折和失败，你也会从中吸取经验教训，继续努力前行。这种坚韧和毅力会让你在人生的道路上走得更远，取得更大的成就。"
, "你的积极心态有助于建立更好的人际关系，增进彼此之间的理解和信任。当你拥有积极的心态时，你会更加善于倾听和理解他人。你会更加关注他人的需求和感受，从而建立起更加深入和真诚的人际关系。同时，积极的心态也会让你更加乐于分享和支持他人，增进彼此之间的信任和亲近感。"
, "保持积极心态可以提升你的幸福感和生活满意度。积极的心态让你更加关注和珍惜生活中的美好事物。你会更加感恩和满足于自己所拥有的，而不是过分追求外在的物质和成就。这种积极心态会让你更加快乐和满足，享受当下的每一刻。同时，积极的心态也会让你更加乐观地面对未来，相信未来会带来更多的幸福和成功。"
, "积极的心态让你更加乐观面对未来，看到更多的机会和可能性。当你拥有积极的心态时，你会相信未来会带来更多的机会和发展。你会更加积极主动地寻找机会，抓住每一个机会来实现自己的目标和梦想。你会相信自己的能力和价值，相信自己可以创造出更美好的未来。"
, "你的积极心态将帮助你更好地管理压力和情绪，保持内心的平静和稳定。当你拥有积极的心态时，你会更加冷静和理智地应对压力和挑战。你会学会放松自己，寻找平衡和调节自己的情绪。这种内心的平静和稳定会让你更加从容地面对生活中的各种情况，不被外界的压力和困扰所影响。"
, "保持积极心态可以帮助你更好地应对变化和适应环境。当你拥有积极的心态时，你会更加灵活和适应变化。你会相信自己有能力适应新的环境和情况，找到适合自己的方式和方法。这种积极的心态会让你更加勇敢地面对变化，不被变化所困扰，而是积极主动地去适应和应对变化。"
, "积极的心态让你更有动力去追求个人成长和进步。当你拥有积极的心态时，你会不断地寻求个人成长和进步的机会。你会相信自己有无限的潜力和可能性，相信自己可以不断地成长和进步。这种积极的心态会激发你的内在动力，让你更加努力地学习和成长，不断提升自己的能力和素质。"
, "积极的心态有助于发展自己的潜力和才能。当你拥有积极的心态时，你会更加相信自己的能力和价值。你会更加积极地发掘和发展自己的潜力和才能。你会相信自己可以做到更多，实现更大的成就。这种积极的心态会激发你的内在激情和动力，让你更加专注和努力地发展自己的潜力和才能。"
, "保持积极心态可以让你更加专注和集中注意力，提高工作和学习的效率。当你拥有积极的心态时，你会更加专注和投入地去完成工作和学习任务。你会更加有耐心和毅力地坚持下去，不被外界的干扰所影响。这种专注和集中注意力的能力会让你更加高效地完成任务，取得更好的成果。"
, "积极的心态让你更有勇气去面对生活中的挑战和困难。当你拥有积极的心态时，你会相信自己有能力克服一切困难和挑战。你会更加勇敢地面对困难，不退缩不放弃。这种勇气和坚持会让你在面对困难时更加坚强和有信心，找到解决问题的方法和途径。"
, "积极的心态有助于培养乐观和开朗的个性，给自己和他人带来更多的快乐和幸福。当你拥有积极的心态时，你会更加乐观和开朗。你会积极地面对生活中的各种情况，不被消极的情绪所困扰。这种乐观和开朗的个性会让你更加快乐和幸福，同时也会影响他人，给他人带来快乐和幸福。"
, "你的积极心态将帮助你更好地发展自己的人际交往能力，建立更好的人际关系。当你拥有积极的心态时，你会更加关注他人的需求和感受。你会更加善于倾听和理解他人，从而建立起更加深入和真诚的人际关系。这种积极心态会让你更加乐于分享和支持他人，增进彼此之间的信任和亲近感。"
, "保持积极心态可以让你更加感恩和满足于自己所拥有的，从而提升幸福感和生活满意度。当你拥有积极的心态时，你会更加关注和珍惜生活中的美好事物。你会感恩于自己所拥有的，而不是过分追求外在的物质和成就。这种积极心态会让你更加快乐和满足，享受当下的每一刻。同时，积极的心态也会让你更加乐观地面对未来，相信未来会带来更多的幸福和成功。"
, "积极的心态让你更加乐观面对未来，看到更多的机会和可能性。当你拥有积极的心态时，你会相信未来会带来更多的机会和发展。你会更加积极主动地寻找机会，抓住每一个机会来实现自己的目标和梦想。你会相信自己的能力和价值，相信自己可以创造出更美好的未来。"
, "你的积极心态将帮助你更好地管理压力和情绪，保持内心的平静和稳定。当你拥有积极的心态时，你会更加冷静和理智地应对压力和挑战。你会学会放松自己，寻找平衡和调节自己的情绪。这种内心的平静和稳定会让你更加从容地面对生活中的各种情况，不被外界的压力和困扰所影响。"
, "保持积极心态可以帮助你更好地应对变化和适应环境。当你拥有积极的心态时，你会更加灵活和适应变化。你会相信自己有能力适应新的环境和情况，找到适合自己的方式和方法。这种积极的心态会让你更加勇敢地面对变化，不被变化所困扰，而是积极主动地去适应和应对变化。"
, "积极的心态让你更有动力去追求个人成长和进步。当你拥有积极的心态时，你会不断地寻求个人成长和进步的机会。你会相信自己有无限的潜力和可能性，相信自己可以不断地成长和进步。这种积极的心态会激发你的内在激情和动力，让你更加专注和努力地发展自己的潜力和才能。"
, "积极的心态有助于发展自己的潜力和才能。当你拥有积极的心态时，你会更加相信自己的能力和价值。你会更加积极地发掘和发展自己的潜力和才能。你会相信自己可以做到更多，实现更大的成就。这种积极的心态会激发你的内在激情和动力，让你更加专注和努力地发展自己的潜力和才能。"
]
    negative_responses = [
"当心情是消极的时候，你可能会感到沮丧和无助。消极的心态会影响你的情绪和思维，使你更容易陷入负面的情绪循环中。但是，请记住，消极的情绪并不是永恒的，它们是暂时的。"
, "在消极的心态下，你可能会对自己和周围的事物持有负面的看法。然而，要意识到消极的情绪并不代表现实，它们只是你当前的感受。"
, "当你感到消极时，尝试停下来，深呼吸并观察自己的情绪。接受这些情绪的存在，并尝试理解它们的原因。"
, "消极的心态可能会导致你对自己的能力和价值产生怀疑。但请记住，每个人都有自己的优点和价值，你也不例外。"
, "与他人分享你的感受可以帮助你减轻消极情绪的负担。找一个信任的朋友或专业的心理咨询师倾诉，他们可以提供支持和理解。"
, "尝试寻找积极的事物和经历，即使它们可能很小。这些积极的元素可以帮助你改变消极的心态，并逐渐提升你的情绪。"
, "给自己一些时间和空间来处理消极情绪。不要强迫自己立刻改变心态，接受情绪的存在，并相信你有能力逐渐走出消极的情绪状态。"
, "尝试寻找一些能够带给你快乐和满足感的活动。这些活动可以是你喜欢的爱好、运动、阅读或与朋友相聚等。这些积极的体验可以帮助你转移注意力，减轻消极情绪的影响。"
, "消极的心态可能会导致你对未来感到绝望和无望。但请记住，未来是充满无限可能性的。尝试设定一些小目标，并逐步朝着它们前进，这将帮助你重建对未来的信心。"
, "寻求专业的心理咨询师的帮助是一个明智的选择。他们可以提供专业的指导和支持，帮助你更好地应对消极情绪，并找到积极的解决方案。"
, "消极的心态可能会让你对自己的过去产生后悔和自责。但请记住，过去的经历是无法改变的，重要的是从中学习，并向前看。"
, "尝试关注自己的成长和进步，而不是过于关注自己的不足和失败。每一次挫折都是一个学习的机会，它们可以帮助你变得更加坚强和成熟。"
, "消极的心态可能会让你对他人产生怀疑和不信任。然而，要意识到每个人都有自己的故事和背景，他们的行为可能受到各种因素的影响。试着保持开放的心态，给予他人一些理解和宽容。"
, "尝试寻找一些积极的灵感和激励。这可以是一本激励人心的书籍、一部励志电影或一位你敬佩的人的故事。这些积极的影响可以帮助你改变消极的心态，并重新点燃内心的激情和动力。"
, "消极的心态可能会让你对生活失去兴趣和热情。但请记住，生活中有很多美好的事物和经历等待着你去发现和体验。尝试寻找一些能够带给你快乐和满足感的事物，并将它们融入到你的日常生活中。"
, "与消极情绪作斗争并不容易，但请相信你有能力克服它们。尝试采取积极的行动，如积极思考、培养健康的生活习惯和寻求支持等。这些行动可以帮助你逐渐改变消极的心态，并走向积极的生活。"
, "消极的心态可能会让你对自己的能力和价值产生怀疑。但请记住，每个人都有自己的优点和价值，你也不例外。尝试关注自己的优点和成就，肯定自己的价值和能力。"
, "与他人分享你的感受可以帮助你减轻消极情绪的负担。找一个信任的朋友或专业的心理咨询师倾诉，他们可以提供支持和理解，并帮助你找到应对消极情绪的方法。"
, "尝试寻找积极的事物和经历，即使它们可能很小。这些积极的元素可以帮助你改变消极的心态，并逐渐提升你的情绪。试着关注生活中的美好事物，如阳光、花朵、笑声等，它们可以带给你一些积极的感受。"
, "给自己一些时间和空间来处理消极情绪。不要强迫自己立刻改变心态，接受情绪的存在，并相信你有能力逐渐走出消极的情绪状态。尝试寻找一些放松和舒缓情绪的方法，如冥想、运动、艺术创作等。"
, "消极的心态可能会导致你对未来感到绝望和无望。但请记住，未来是充满无限可能性的。尝试设定一些小目标，并逐步朝着它们前进，这将帮助你重建对未来的信心。同时，寻找一些能够激发你激情和兴趣的事物，让你对未来充满期待。"
, "寻求专业的心理咨询师的帮助是一个明智的选择。他们可以提供专业的指导和支持，帮助你更好地应对消极情绪，并找到积极的解决方案。他们可以帮助你探索消极情绪背后的原因，并提供有效的应对策略。"
, "消极的心态可能会让你对自己的过去产生后悔和自责。但请记住，过去的经历是无法改变的，重要的是从中学习，并向前看。尝试接受过去的错误和失败，并将它们视为成长和学习的机会。"
, "尝试关注自己的成长和进步，而不是过于关注自己的不足和失败。每一次挫折都是一个学习的机会，它们可以帮助你变得更加坚强和成熟。试着设定一些小目标，并逐步实现它们，这将帮助你重建对自己的信心。"
, "消极的心态可能会让你对他人产生怀疑和不信任。然而，请记住每个人都有自己的故事和背景，他们的行为可能受到各种因素的影响。试着保持开放的心态，给予他人一些理解和宽容，建立起更加健康和积极的人际关系。"
, "尝试寻找一些积极的灵感和激励。这可以是一本激励人心的书籍、一部励志电影或一位你敬佩的人的故事。这些积极的影响可以帮助你改变消极的心态，并重新点燃内心的激情和动力。"
, "消极的心态可能会让你对生活失去兴趣和热情。但请记住，生活中有很多美好的事物和经历等待着你去发现和体验。尝试寻找一些能够带给你快乐和满足感的事物，并将它们融入到你的日常生活中。"
, "与消极情绪作斗争并不容易，但请相信你有能力克服它们。尝试采取积极的行动，如积极思考、培养健康的生活习惯和寻求支持等。这些行动可以帮助你逐渐改变消极的心态，并走向积极的生活。"
, "消极的心态可能会让你对自己的能力和价值产生怀疑。但请记住，每个人都有自己的优点和价值，你也不例外。尝试关注自己的优点和成就，肯定自己的价值和能力。"
, "与他人分享你的感受可以帮助你减轻消极情绪的负担。找一个信任的朋友或专业的心理咨询师倾诉，他们可以提供支持和理解，并帮助你找到应对消极情绪的方法。"
, "尝试寻找积极的事物和经历，即使它们可能很小。这些积极的元素可以帮助你改变消极的心态，并逐渐提升你的情绪。试着关注生活中的美好事物，如阳光、花朵、笑声等，它们可以带给你一些积极的感受。"
, "给自己一些时间和空间来处理消极情绪。不要强迫自己立刻改变心态，接受情绪的存在，并相信你有能力逐渐走出消极的情绪状态。尝试寻找一些放松和舒缓情绪的方法，如冥想、运动、艺术创作等。"
, "消极的心态可能会导致你对未来感到绝望和无望。但请记住，未来是充满无限可能性的。尝试设定一些小目标，并逐步朝着它们前进，这将帮助你重建对未来的信心。同时，寻找一些能够激发你激情和兴趣的事物，让你对未来充满期待。"
, "寻求专业的心理咨询师的帮助是一个明智的选择。他们可以提供专业的指导和支持，帮助你更好地应对消极情绪，并找到积极的解决方案。他们可以帮助你探索消极情绪背后的原因，并提供有效的应对策略。"
, "消极的心态可能会让你对自己的过去产生后悔和自责。但请记住，过去的经历是无法改变的，重要的是从中学习，并向前看。尝试接受过去的错误和失败，并将它们视为成长和学习的机会。"
, "尝试关注自己的成长和进步，而不是过于关注自己的不足和失败。每一次挫折都是一个学习的机会，它们可以帮助你变得更加坚强和成熟。试着设定一些小目标，并逐步实现它们，这将帮助你重建对自己的信心。"
, "消极的心态可能会让你对他人产生怀疑和不信任。然而，请记住每个人都有自己的故事和背景，他们的行为可能受到各种因素的影响。试着保持开放的心态，给予他人一些理解和宽容，建立起更加健康和积极的人际关系。"
, "尝试寻找一些积极的灵感和激励。这可以是一本激励人心的书籍、一部励志电影或一位你敬佩的人的故事。这些积极的影响可以帮助你改变消极的心态，并重新点燃内心的激情和动力。"
, "消极的心态可能会让你对生活失去兴趣和热情。但请记住，生活中有很多美好的事物和经历等待着你去发现和体验。尝试寻找一些能够带给你快乐和满足感的事物，并将它们融入到你的日常生活中。"
    ]
    neutral_responses = [
"当心情是中立的时候，你可能感觉既不特别开心也不特别沮丧。这种中立的心态可以让你更加冷静和客观地看待事物，不受情绪的影响。"
, "中立的心态可以帮助你保持平衡和稳定，不被情绪的波动所左右。这种平衡的心态可以让你更好地应对生活中的各种挑战和困难。"
, "当你处于中立的心态时，你可以更加客观地评估自己和他人的行为和决策。这种客观的观察和分析能力可以帮助你做出更明智和理性的决策。"
, "中立的心态可以让你更加客观地看待自己的优点和不足。你可以更加客观地评估自己的能力和价值，并制定合理的目标和计划来提升自己。"
, "中立的心态可以帮助你更好地处理人际关系。你可以更加客观地看待他人的行为和动机，从而建立起更加健康和积极的人际关系。"
, "中立的心态可以让你更加客观地看待自己的过去和未来。你可以从过去的经验中吸取教训，同时对未来保持一定的期待和希望。"
, "中立的心态可以帮助你更好地应对压力和挑战。你可以更加冷静和理智地面对困难和挫折，从而找到解决问题的方法和途径。"
, "中立的心态可以让你更加客观地评估自己的情绪和情感。你可以更好地理解自己的情绪，并采取适当的方式来管理和调节情绪。"
, "中立的心态可以帮助你更好地应对变化和适应环境。你可以更加灵活和适应变化，从而更好地应对生活中的各种情况。"
, "中立的心态可以让你更加客观地看待成功和失败。你可以从成功中获得启示和动力，同时从失败中吸取教训和经验。"
, "中立的心态可以帮助你更好地管理时间和资源。你可以更加客观地评估自己的能力和资源，并合理地分配它们来实现自己的目标和梦想。"
, "中立的心态可以让你更加客观地看待自己的身体和外貌。你可以更好地接受自己的外貌和身体，并关注自己的健康和内在美。"
, "中立的心态可以帮助你更好地应对他人的批评和评价。你可以更加客观地评估他人的意见，并从中找到有益的建议和反馈。"
, "中立的心态可以让你更加客观地看待自己的成功和成就。你可以更好地认识到自己的努力和付出，并对自己的成就感到满意和自豪。"
, "中立的心态可以帮助你更好地应对不确定性和变化。你可以更加冷静和理智地面对不确定的情况，并找到适合自己的方式来应对和适应。"
, "中立的心态可以让你更加客观地看待自己的情绪和情感。你可以更好地理解自己的情绪，并采取适当的方式来管理和调节情绪。"
, "中立的心态可以帮助你更好地应对压力和挑战。你可以更加冷静和理智地面对困难和挫折，从而找到解决问题的方法和途径。"
, "中立的心态可以让你更加客观地评估自己的能力和价值。你可以更好地认识到自己的优点和不足，并制定合理的目标和计划来提升自己。"
, "中立的心态可以帮助你更好地处理人际关系。你可以更加客观地看待他人的行为和动机，从而建立起更加健康和积极的人际关系。"
, "中立的心态可以让你更加客观地看待自己的过去和未来。你可以从过去的经验中吸取教训，同时对未来保持一定的期待和希望。"
, "中立的心态可以帮助你更好地应对压力和挑战。你可以更加冷静和理智地面对困难和挫折，从而找到解决问题的方法和途径。"
, "中立的心态可以让你更加客观地评估自己的情绪和情感。你可以更好地理解自己的情绪，并采取适当的方式来管理和调节情绪。"
, "中立的心态可以帮助你更好地应对变化和适应环境。你可以更加灵活和适应变化，从而更好地应对生活中的各种情况。"
, "中立的心态可以让你更加客观地看待自己的身体和外貌。你可以更好地接受自己的外貌和身体，并关注自己的健康和内在美。"
, "中立的心态可以帮助你更好地应对他人的批评和评价。你可以更加客观地评估他人的意见，并从中找到有益的建议和反馈。"
, "中立的心态可以让你更加客观地看待自己的成功和成就。你可以更好地认识到自己的努力和付出，并对自己的成就感到满意和自豪。"
, "中立的心态可以帮助你更好地应对不确定性和变化。你可以更加冷静和理智地面对不确定的情况，并找到适合自己的方式来应对和适应。"
, "中立的心态可以让你更加客观地看待自己的情绪和情感。你可以更好地理解自己的情绪，并采取适当的方式来管理和调节情绪。"
, "中立的心态可以帮助你更好地应对压力和挑战。你可以更加冷静和理智地面对困难和挫折，从而找到解决问题的方法和途径。"
, "中立的心态可以让你更加客观地评估自己的能力和价值。你可以更好地认识到自己的优点和不足，并制定合理的目标和计划来提升自己。"
, "中立的心态可以帮助你更好地处理人际关系。你可以更加客观地看待他人的行为和动机，从而建立起更加健康和积极的人际关系。"
, "中立的心态可以让你更加客观地看待自己的过去和未来。你可以从过去的经验中吸取教训，同时对未来保持一定的期待和希望。"
, "中立的心态可以帮助你更好地应对压力和挑战。你可以更加冷静和理智地面对困难和挫折，从而找到解决问题的方法和途径。"
, "中立的心态可以让你更加客观地评估自己的情绪和情感。你可以更好地理解自己的情绪，并采取适当的方式来管理和调节情绪。"
, "中立的心态可以帮助你更好地应对变化和适应环境。你可以更加灵活和适应变化，从而更好地应对生活中的各种情况。"
, "中立的心态可以让你更加客观地看待自己的身体和外貌。你可以更好地接受自己的外貌和身体，并关注自己的健康和内在美。"
, "中立的心态可以帮助你更好地应对他人的批评和评价。你可以更加客观地评估他人的意见，并从中找到有益的建议和反馈。"
, "中立的心态可以让你更加客观地看待自己的成功和成就。你可以更好地认识到自己的努力和付出，并对自己的成就感到满意和自豪。"
, "中立的心态可以帮助你更好地应对不确定性和变化。你可以更加冷静和理智地面对不确定的情况，并找到适合自己的方式来应对和适应。"
, "中立的心态可以让你更加客观地看待自己的情绪和情感。你可以更好地理解自己的情绪，并采取适当的方式来管理和调节情绪。"
    ]
    data = request.get_json()
    text = data.get('text', '')
    translator = Translator()
    result = translator.translate(text, dest='en')
    print(result.text)
    # text = "我有点感兴趣"
    processed_text = preprocess_text(result.text)
    sentiment_score = analyze_sentiment(processed_text)
    # print("Sentiment Score:", sentiment_score)    
    if sentiment_score>0:
        answer="今天你是积极的。"+random.choice(positive_responses)
        return answer
    if sentiment_score<0:
        answer="今天你是消极的。"+random.choice(negative_responses)
        return answer
    if sentiment_score==0:
        answer="今天你心情是中立的。"+random.choice(neutral_responses)
        return answer

if __name__ == '__main__':
    app.run()

