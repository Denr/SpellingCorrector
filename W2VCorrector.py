import time
import nltk
import re
import Candidates
import logging
from gensim.models.keyedvectors import KeyedVectors

def reduce_repeating_letters(words, i):
    words[i] = re.sub('у{3,}', 'у', words[i])
    words[i] = re.sub('б{3,}', 'б', words[i])
    words[i] = re.sub('а{3,}', 'а', words[i])
    words[i] = re.sub('о{3,}', 'о', words[i])
    words[i] = re.sub('е{3,}', 'е', words[i])
    words[i] = re.sub('цц', 'дс', words[i])
    words[i] = re.sub('^писят$', 'пятьдесят', words[i])
    words[i] = re.sub('^птом$', 'потом', words[i])
    words[i] = re.sub('^лутче$', 'лучше', words[i])
    words[i] = re.sub('^енто$', 'это', words[i])
    words[i] = re.sub('^енти$', 'эти', words[i])
    words[i] = re.sub('^чтоже$', 'что же', words[i])
    words[i] = re.sub('^ниче$', 'ничего', words[i])
    words[i] = re.sub('^впринципе$', 'в принципе', words[i])
    words[i] = re.sub('^чесно$', 'честно', words[i])
    words[i] = re.sub('^в тупую$', 'в втупую', words[i])
    words[i] = re.sub('^оч$', 'очень', words[i])
    words[i] = re.sub('^незря$', 'не зря', words[i])
    words[i] = re.sub('^помойму$', 'по-моему', words[i])
    words[i] = re.sub('^как-то$', 'как то', words[i])
    words[i] = re.sub('^в правду$', 'вправду', words[i])
    words[i] = re.sub('^хотябы$', 'хотя бы', words[i])
    words[i] = re.sub('^не правильно$', 'неправильно', words[i])
    words[i] = re.sub('^мож$', 'может', words[i])
    words[i] = re.sub('^изретко$', 'изредка', words[i])
    words[i] = re.sub('^собсно$', 'собственно', words[i])
    words[i] = re.sub('^в общем$', 'вообщем', words[i])
    words[i] = re.sub('^нада$', 'надо', words[i])
    words[i] = re.sub('^выпеть$', 'выпить', words[i])
    words[i] = re.sub('^што$', 'что', words[i])
    words[i] = re.sub('^что-бы$', 'чтобы', words[i])
    words[i] = re.sub('^манхеттоне$', 'манхэттене', words[i])
    words[i] = re.sub('^шо$', 'что', words[i])
    words[i] = re.sub('^экзам$', 'экзамен', words[i])
    words[i] = re.sub('^буит$', 'будет', words[i])
    words[i] = re.sub('^ченить$', 'что-нибудь', words[i])
    words[i] = re.sub('^какую-нить$', 'какую-нибудь', words[i])
    words[i] = re.sub('^заффтра$', 'завтра', words[i])
    words[i] = re.sub('^знаеш$', 'знаешь', words[i])
    words[i] = re.sub('^на последок$', 'напоследок', words[i])
    words[i] = re.sub('^врядли$', 'вряд ли', words[i])
    words[i] = re.sub('^какбэ$', 'как бы', words[i])
    words[i] = re.sub('^болше$', 'больше', words[i])
    words[i] = re.sub('^чота$', 'что-то', words[i])
    words[i] = re.sub('^какую-нить$', 'какую-нибудь', words[i])


def w2v_correct(source_file, answer_file):
    for line in source_file:
        words = nltk.word_tokenize(line)
        for i in range(len(words)):
            reduce_repeating_letters(words, i)
            if len(words[i]) > 2:
                if words[i] in model:
                    value = 0
                    correct_word = ''
                    candidates = get_candidates.known(get_candidates.edits1(words[i]))
                    if len(candidates) == 0:
                        answer_file.write(words[i] + ' ')
                    else:
                        for j in range(len(candidates)):
                            candidate_word = list(candidates)[j]
                            if candidate_word in model:
                                if value < model.similarity(words[i], candidate_word):
                                    value = model.similarity(words[i], candidate_word)
                                    correct_word = candidate_word
                                elif value > model.similarity(words[i], candidate_word):
                                    correct_word = get_candidates.correct(words[i])
                            elif value == 0:
                                correct_word = words[i]
                    if len(correct_word) != 0:
                        answer_file.write(correct_word + ' ')
                else:
                    answer_file.write(words[i] + ' ')
            else:
                answer_file.write(words[i] + ' ')
        answer_file.write('\n')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    get_candidates = Candidates
    model = KeyedVectors.load('model')
    model.init_sims(replace=True)
    source_file = open('txt/source_file.txt', 'r', encoding='utf8')
    answer_file = open('txt/answer_file.txt', 'w', encoding='utf8')
    start_time = time.time()
    w2v_correct(source_file, answer_file)
    print('Времени прошло: ' + str(time.time() - start_time))
