from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.http.response import JsonResponse

from nlang.processor.tokenizer import Tokenizer
from nlang.corpus.chasen.chasen_type import ChasenInvertTable

from sakuya.accounts.models import Child
from sakuya.photos.models import Photo, Stamp
from sakuya.voice.models import Word
from sakuya.utils import get_active_user, get_owner_child


tokenizer = Tokenizer()

@csrf_exempt
@require_POST
def record(request):
#    import pdb; pdb.set_trace()
    user = get_active_user(request)

    if 'speech_text' not in request.GET:
        raise Http404
    
    if 'speech_file' not in request.FILES:
        raise Http404

    child = get_owner_child(request, user)
    all_child = Child.objects.get(name='allofthem')
    
    speech = request.GET['speech_text']
    words = tokenizer.tag(speech)

    new_words = []
    for word in words:
        if word.lemma != ' ' and word.lemma != '　':
            try:
                vocab_word = child.word_set.get(lemma=word.lemma, tag=word.tag)
            except Word.DoesNotExist:
                pos_size = len(word.pos)
                pos1 = ChasenInvertTable[word.pos[0]] if pos_size > 0 else ''
                pos2 = ChasenInvertTable[word.pos[1]] if pos_size > 1 else ''
                pos3 = ChasenInvertTable[word.pos[2]] if pos_size > 2 else ''
                vocab_word = Word.objects.create(
                    lemma=word.lemma,
                    pron=word.pron,
                    base=word.base,
                    pos1=pos1, pos2=pos2, pos3=pos3,
                    conj_type=word.conj_type,
                    conj_form=word.conj_form,
                    tag= word.tag,
                    date=now(),
                    owner=child)

                try:
                    all_child.word_set.get(lemma=vocab_word.lemma, tag=vocab_word.tag)
                except:
                    all_child.word_set.create(
                        lemma=vocab_word.lemma,
                        pron=vocab_word.pron,
                        base=vocab_word.base,
                        pos1=vocab_word.pos1,
                        pos2=vocab_word.pos2,
                        pos3=vocab_word.pos3,
                        conj_type=vocab_word.conj_type,
                        conj_form=vocab_word.conj_form,
                        tag=vocab_word.tag,
                        date=now())
                
                new_words.append('「' + vocab_word.__str__() + '」')

    if not new_words:
        return JsonResponse({})

    speech_file = request.FILES['speech_file']
    date = now()
    age = child.detail_age()
    footer = 'Voiceからの投稿'
    comment = '、'.join(new_words) + 'をおぼえました。'
    
    try:
        photo = Photo.objects.create(title=speech, image=None, audio=speech_file, movie=None, comment=comment, date=date, age=age, owner=child, footer=footer)
        try:
            stamp = Stamp.objects.get(title='VeryGood')
            photo.stamp = stamp
            photo.save()
        except:
            pass
    except IntegrityError:
        raise Http404
    
    res = {}
    res['new_words'] = new_words

    return JsonResponse(res)
