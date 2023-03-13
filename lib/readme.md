# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def reading_time():
    """estimates time in minutes it will take to read the whole text

    Parameters: 
        reader_speed: = 200 words per minute
        given_text: a string of text

    Returns:
        a number, the time it takes to read the text

    Side effects:
        This function does not do anything else

    pass 

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Given text of 200 words
It returns 1 

"""
reading_time(200words) => [1]

"""
Given a word count of 400
It returns 2

"""
reading_time(400) => [2]

"""
Given a word count of 2000
It returns 10

"""
reading_time(2000) => [10]

"""
Given a word count of < 200
It returns 1

"""
reading_time(100) => [1]

"""
Given a word count of 0
It returns 0

"""
reading_time(0) => [0]

```python


# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!





<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->


dummy text:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris accumsan pharetra tellus, et vulputate eros aliquam vitae. Phasellus sagittis sagittis purus in scelerisque. Praesent et ligula quis nunc lobortis aliquam eget non odio. Nunc vel consequat lorem, cursus convallis enim. Nam finibus venenatis elit, a sagittis justo euismod vitae. Nulla eleifend lobortis lacus. Suspendisse potenti.

Aliquam erat volutpat. Pellentesque eu mauris porttitor, sagittis ipsum eget, consectetur lectus. Cras nisi purus, eleifend lacinia nisl id, tempor gravida lacus. In hac habitasse platea dictumst. Nunc sodales sodales erat et dictum. Pellentesque quis ligula ut nisl sagittis commodo. Cras suscipit felis consequat venenatis rhoncus. Nunc in mi quis tortor ornare pellentesque non id metus. Morbi blandit molestie nisl vitae egestas.

Sed semper lobortis nulla eget mollis. Mauris tristique, tortor vel pharetra ultrices, ante diam lacinia risus, at tempor tortor tortor sit amet eros. Aenean imperdiet finibus luctus. Nulla vel tincidunt lectus. Nunc venenatis tellus dolor, quis condimentum sem vestibulum at. Duis vel justo aliquet, imperdiet elit nec, volutpat metus. Sed dictum velit nec interdum vehicula. Nam dictum diam a felis tincidunt cursus. In interdum, mauris at vulputate pulvinar, quam elit luctus mi, et semper enim nibh mattis purus. Etiam quis felis mollis, venenatis metus ac, facilisis mauris. Quisque cursus felis ac semper venenatis. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Nunc non diam posuere, tempus urna sit amet, facilisis velit. Cras faucibus eros ut mattis semper. Praesent quis turpis pulvinar, scelerisque velit ac, gravida diam. Nam sollicitudin maximus lacus eu imperdiet. Nunc tincidunt sapien non magna lacinia maximus. Cras lobortis augue et quam pharetra convallis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce at nisl mattis turpis pharetra gravida. Phasellus non metus lorem. Morbi non libero cursus, consectetur metus et, euismod dui. Quisque condimentum consequat neque, sed imperdiet metus aliquam at. Sed sollicitudin diam facilisis erat tincidunt dignissim. Sed et eros nec magna aliquam lobortis sed quis nulla. Morbi dictum congue dolor, et lacinia lacus dignissim id. Maecenas hendrerit odio vitae metus rutrum auctor.

Suspendisse eu porttitor dolor. Quisque eros leo, scelerisque sed gravida ac, tempor eu lorem. Fusce at augue pretium, semper sapien ac, semper nulla. Pellentesque vel tempor dolor. Nunc risus tortor, congue sed est sed, pharetra sollicitudin massa. Praesent euismod convallis viverra. Pellentesque eu leo finibus, dapibus lacus in, dictum est. Suspendisse potenti. Aliquam interdum urna a odio ullamcorper bibendum. In hac habitasse platea dictumst.

Morbi a finibus augue, a semper nibh. Aenean vel risus nisl. Cras dui lectus, commodo id mauris hendrerit, feugiat egestas purus. Proin posuere lacus quam, vel varius arcu rutrum in. Ut consectetur varius purus eu tincidunt. Sed rutrum ligula finibus malesuada accumsan. Praesent sit amet volutpat felis. Quisque porta felis id nisl accumsan, consequat congue purus pretium. Integer auctor pulvinar aliquet. Vivamus mauris urna, condimentum vel tincidunt sit amet, ultricies sed turpis.

Nunc in auctor elit, non porttitor eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In pretium libero mauris, et cursus leo dictum nec. Aenean molestie dui in sapien interdum, quis ultricies tortor volutpat. Maecenas quis porttitor erat. Phasellus blandit aliquam rhoncus. Nullam diam nisi, scelerisque vitae felis sed, imperdiet vehicula mauris. Duis egestas scelerisque nisl a tempus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Integer tristique metus vitae fringilla vulputate. Aenean vel urna sapien. Phasellus gravida tempus aliquam. Nunc in mi vel orci tempor convallis. Maecenas rutrum felis in bibendum aliquet.

Suspendisse ullamcorper turpis hendrerit dapibus condimentum. Nam luctus erat ut mi consequat, id volutpat dolor luctus. Aliquam erat volutpat. Nunc dolor erat, semper eget ante eu, vulputate vehicula ante. Sed ipsum leo, aliquam ac risus at, faucibus mattis mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc nec risus vel sem fermentum bibendum vel volutpat quam.

Suspendisse tincidunt massa enim, quis efficitur urna sagittis eu. Maecenas a placerat leo. Nunc at semper sem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas posuere neque vulputate metus luctus gravida. Nulla viverra interdum dui quis vestibulum. Cras tincidunt, odio id faucibus laoreet, odio nunc vulputate erat, volutpat viverra risus dui in ligula. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi in dolor at enim tristique tempor ut vel nunc. Mauris id accumsan ipsum, id elementum turpis.

Maecenas lacinia laoreet venenatis. Sed vel mollis leo. Vivamus eget bibendum augue. Aliquam sagittis purus quis metus porttitor faucibus. Praesent quis sapien turpis. Nullam pharetra arcu ligula, sit amet mattis nulla euismod non. Integer tortor dolor, aliquam sed sodales ut, scelerisque et nulla. Maecenas id nunc at turpis aliquet auctor. Phasellus viverra lacinia interdum.

Mauris elit leo, facilisis sed varius sed, sagittis a mauris. Pellentesque pulvinar, mi a pretium commodo, felis enim malesuada ligula, at auctor eros erat ac urna. Donec ornare, odio non tristique porta, sem felis pulvinar justo, sed efficitur nunc neque vel purus. Aliquam luctus, leo in consequat lobortis, orci est rhoncus justo, vitae dignissim quam risus a ante. Phasellus sodales at lorem vel semper. Duis nisi magna, euismod non sollicitudin non, luctus at sapien. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean non ligula finibus, sodales tellus eu, iaculis purus. Nunc vel semper elit. Nulla sit amet leo quis leo molestie accumsan quis ac metus.

Aliquam vel bibendum turpis, ut pretium purus. Nulla massa erat, bibendum ut semper sit amet, tincidunt et sapien. Ut iaculis neque nec hendrerit luctus. Vivamus vel mi sollicitudin, condimentum massa non, ultrices nisi. Nullam at dignissim lectus, vitae varius ex. Nunc a ante mi. Vivamus vulputate tortor eu risus facilisis rutrum vel nec odio. Proin diam magna, scelerisque ut laoreet in, aliquam sed risus. Cras vitae lacinia sem, quis euismod lorem. Integer malesuada nibh a tellus rhoncus vehicula. Proin sit amet felis varius, tristique magna eget, blandit mi.

Ut imperdiet tortor ut convallis pulvinar. Praesent mattis venenatis ex at facilisis. Praesent aliquam augue purus, bibendum scelerisque libero aliquet sit amet. Cras ornare eros sit amet ipsum malesuada, vitae vehicula velit feugiat. Sed dapibus velit in nulla suscipit, tincidunt dictum nulla luctus. Nulla semper aliquam dui, quis pulvinar nunc porta eget. Suspendisse viverra, augue ut consequat convallis, urna sapien pellentesque justo, a eleifend orci sapien et quam. Donec ullamcorper lorem urna, eget malesuada mi rutrum nec.

Quisque bibendum placerat turpis, a vehicula diam tempus sed. Morbi vel imperdiet nulla. Vivamus metus metus, feugiat vitae tincidunt ac, malesuada vel metus. In hac habitasse platea dictumst. Quisque velit lorem, aliquam vel quam non, placerat mollis enim. Ut eu purus mattis, imperdiet velit in, tempus nibh. Nulla enim quam, tincidunt vel convallis at, vehicula at lectus. Integer interdum volutpat enim sit amet vehicula. Nulla fringilla, dolor sed pellentesque vehicula, mauris odio sagittis ante, non sodales lorem felis et tellus. Sed interdum fermentum est eu finibus. Mauris egestas, nibh a venenatis sagittis, metus purus tristique lorem, id porttitor eros odio at purus. Proin nec tellus eu sem lacinia pharetra quis vitae eros.

Nunc porttitor libero sit amet massa porta, eget commodo augue tincidunt. Nulla placerat sapien luctus, fermentum nibh nec, auctor magna. Duis auctor lectus metus, dictum sodales diam luctus a. Aenean malesuada magna ac elit convallis, et luctus velit varius. Nullam fermentum congue lacus, quis consequat quam vulputate eget. Aliquam sit amet magna ullamcorper, blandit mi at, maximus ex. Sed nec pretium lacus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus placerat quis diam eget accumsan. Vivamus scelerisque rutrum justo quis tempor. In sodales tempus magna, eu varius turpis consectetur a. Vivamus condimentum sollicitudin arcu nec euismod. Sed pellentesque ex velit, sit amet ultricies nulla congue quis. Nam sed elit at metus efficitur interdum.

Duis nec maximus arcu. Morbi convallis vestibulum enim, ac placerat elit convallis pellentesque. Phasellus sed pharetra risus. In ut nisl vitae enim tempor feugiat. Pellentesque cursus sagittis tortor, nec ultricies dolor rutrum vitae. Aenean ac condimentum purus, in ultricies ex. Curabitur non euismod nibh. Quisque eleifend erat aliquam maximus sagittis. Proin laoreet cursus egestas. Aenean fringilla ipsum eu imperdiet aliquet. Aenean iaculis sit amet nulla eu luctus. Aenean vel auctor est, a interdum justo. Etiam tortor arcu, luctus vitae augue id, consequat volutpat enim. Phasellus lorem mauris, vulputate vitae hendrerit et, dictum nec est.

Etiam ex erat, fringilla eget gravida in, fringilla sit amet ante. Morbi cursus viverra semper. Maecenas quis aliquam mauris. Suspendisse pretium lacus sapien, at consequat justo ullamcorper a. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis egestas a nulla ac ultricies. Duis vel lacus erat. Fusce elementum libero tellus.

In laoreet sapien a felis tempus, sed ullamcorper felis accumsan. Ut tincidunt odio iaculis, venenatis sapien id, pulvinar felis. Fusce vitae pellentesque lorem. Praesent ac viverra orci. Maecenas quam velit, porttitor in molestie non, venenatis vehicula ante. Sed quis nisi nec elit luctus fermentum sit amet et est. Nunc sem felis, scelerisque in tincidunt a, tincidunt non est. Cras interdum purus velit, id eleifend diam commodo aliquam.

Duis eget pellentesque quam. Donec sit amet velit metus. Suspendisse est ipsum, mollis non suscipit vitae, luctus sit amet quam. Suspendisse id luctus dolor, luctus scelerisque ligula. In turpis leo, imperdiet imperdiet odio ut, rhoncus fringilla sem. Sed egestas leo lorem, non sollicitudin leo egestas eget. Ut vel fringilla enim. Quisque ac volutpat erat, et euismod orci. Nulla facilisi. Cras posuere sed odio quis molestie.

Vestibulum tempor nulla ut pulvinar tincidunt. Donec elementum vitae nisl vitae auctor. Etiam facilisis nulla et dolor maximus, vel gravida metus accumsan. Etiam egestas nibh sed arcu tempor, a tincidunt arcu faucibus. Quisque eu metus vel metus commodo vestibulum ac ac metus. Ut tortor justo, vestibulum quis lacinia eget, dictum sit amet eros. Donec malesuada justo nisi.

Aenean sagittis gravida magna, non iaculis tortor vestibulum ac. Donec non suscipit dolor, sed faucibus felis. Nulla fermentum ullamcorper erat ac congue. Vestibulum non lacus malesuada libero dapibus tincidunt ut eu metus. Morbi quis dui faucibus, feugiat neque in, venenatis nibh. Phasellus mauris urna, vestibulum in leo in, pharetra sollicitudin leo. Vivamus et maximus felis. Proin nec arcu non augue commodo consequat sit amet non orci. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent non nulla varius, laoreet augue sed, elementum purus. Nunc ut nibh sapien.

Donec mauris metus, volutpat et velit in, ullamcorper fringilla neque. Nunc lobortis justo et nulla aliquet, sit amet venenatis ex gravida. Maecenas et congue eros, vel interdum tortor. Suspendisse quis venenatis nunc. Vestibulum ornare maximus gravida. Fusce lacus dui, fringilla ut rhoncus id, pretium id mauris. Duis malesuada auctor rutrum. In hac habitasse platea dictumst. Etiam vitae fringilla ex, quis eleifend enim. Vestibulum mi lectus, ultricies eget augue dapibus, dignissim pharetra felis. Morbi dictum pharetra dui nec mollis. Cras porttitor magna eu massa pharetra, nec tincidunt dui tempus. Curabitur consectetur mattis vestibulum.

Nulla facilisi. Aenean nec quam est. Nullam risus sapien, imperdiet sit amet consequat et, semper nec justo. Vestibulum porta eros eu dictum blandit. Morbi semper sapien vel volutpat interdum. Aenean auctor vulputate fringilla. In tempus, magna quis hendrerit sodales, eros nunc viverra libero, ut condimentum felis erat rutrum mauris. Curabitur eros magna, ullamcorper quis posuere vitae, venenatis id nisi. Phasellus et lacus tellus. In pretium mi sit amet dapibus tincidunt. Mauris lectus mauris, sodales nec eros at, fringilla lobortis nisl. Aliquam porttitor blandit arcu, finibus consequat libero pulvinar eget.

Aenean malesuada erat augue, sit amet vulputate libero mattis quis. Maecenas dictum in justo sed tincidunt. Nulla non nunc leo. Praesent et ornare odio, vel vehicula felis. Cras ut interdum urna. Praesent non aliquam dui. Suspendisse ornare turpis nisi, quis suscipit tortor tristique et. Phasellus commodo, nunc sed suscipit bibendum, nibh nisi egestas sapien, ut sagittis turpis massa eget mi.

Nunc non augue vitae massa elementum ornare. Quisque nec dui sed nulla condimentum tincidunt. Phasellus sit amet sodales mauris, a pharetra augue. Aenean nibh neque, egestas id maximus quis, ullamcorper at ante. Nunc a nulla elementum, lacinia nulla in, tempor erat. Praesent et tempor quam. Mauris vel bibendum metus, dignissim ullamcorper libero. Nam cursus orci id rhoncus tristique. Nullam a luctus velit.

Sed rhoncus magna luctus, pharetra neque eget, faucibus mauris. Fusce auctor dui ligula, id mollis mi venenatis a. Suspendisse quis ipsum elit. Sed accumsan eros mauris, nec lacinia orci condimentum a. Morbi viverra in arcu eu semper. Suspendisse sollicitudin eros nec orci suscipit, quis tempor diam tincidunt. Nunc venenatis gravida imperdiet. In at lorem eleifend, ullamcorper risus eget, convallis est. Curabitur semper euismod dignissim. Vestibulum risus est, dapibus nec ligula eu, eleifend dapibus dui.

Aliquam neque mi, vehicula ac augue sit amet, tincidunt commodo ex. Praesent lacinia diam ac urna suscipit congue. Nulla a erat sed libero ornare posuere ac ut sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec aliquam efficitur convallis. Morbi dictum porta justo ac tristique. Aenean sed tristique nisi, et porta augue. In eget ex lectus. Pellentesque vitae tortor ac justo porta blandit eu vitae nisi. Donec pretium, elit maximus viverra malesuada, odio enim condimentum erat, sed tempus sem elit rutrum tellus. Nam non augue at metus pretium blandit. Ut vitae dolor lacus.

Maecenas vel ex sapien. Nullam sed elementum nunc, quis euismod ante. Donec euismod finibus urna sit amet dignissim. Donec orci dolor, rhoncus et accumsan non, molestie vitae urna. Donec vitae tristique nulla, quis fermentum quam. Ut nec pulvinar justo. Maecenas turpis nulla, rhoncus et dolor vel, tincidunt sodales leo.

Duis semper volutpat euismod. Praesent sit amet lectus velit. Mauris eleifend diam id lectus cursus, vel condimentum nunc luctus. Nam mauris purus, tempus sed semper et, posuere interdum leo. Praesent semper justo justo, in vestibulum urna fermentum ornare. Praesent ac tortor a turpis egestas lobortis. Vestibulum eu porttitor ante. Donec non auctor ipsum, eget rutrum ligula. Nunc non tristique odio. Maecenas suscipit ultrices semper. Morbi et ipsum tortor. Sed blandit massa quis ante convallis, ornare elementum felis tincidunt. Phasellus porta feugiat turpis, et iaculis ligula commodo tincidunt. Pellentesque sed sem at nisi sagittis volutpat mollis vel metus. Mauris porttitor felis neque, eu aliquet nunc sagittis at. Phasellus luctus mauris ut nisi finibus, sed accumsan nibh porttitor.

Suspendisse nunc nisi, tincidunt lobortis pellentesque non, maximus quis leo. Aenean nec dui erat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean auctor condimentum nisl quis placerat. Cras magna erat, dictum rutrum diam vitae, rhoncus laoreet sapien. Aliquam erat volutpat. Morbi dapibus pharetra libero quis mollis. Sed accumsan mi sed dolor ultrices viverra.

Nam placerat rhoncus ex. Etiam maximus auctor condimentum. Pellentesque ultricies, augue nec aliquet vestibulum, nunc ligula varius leo, id eleifend eros metus vitae mi. Cras eget vestibulum justo, ut pharetra nulla. Maecenas feugiat vel dui vitae vestibulum. Proin nec rutrum erat. Fusce euismod ligula vel massa convallis imperdiet.

Nunc tellus diam, lobortis eget eros vitae, luctus condimentum nulla. Mauris semper sodales faucibus. Mauris id metus eleifend, imperdiet lorem sit amet, egestas purus. Donec ultricies, mauris nec pulvinar faucibus, nisi mi volutpat ligula, hendrerit elementum elit enim a orci. In diam diam, maximus vitae fringilla in, porttitor et arcu. Vivamus luctus nibh a efficitur egestas. Quisque vitae ex at augue venenatis ornare ut non arcu. Vivamus in mollis tellus, nec feugiat turpis. Maecenas vitae blandit lorem. Praesent at nisl quis nulla rutrum euismod. Praesent fermentum ipsum elit, sit amet malesuada neque consequat at. Duis tincidunt bibendum augue, eu facilisis arcu vulputate porta. Aliquam sagittis, lectus ac vestibulum vestibulum, dolor eros tempor erat, at sagittis elit enim ac tortor. Vivamus tincidunt nunc nisi, in tincidunt est congue non. Nam mi elit, maximus eu ante mattis, tristique commodo dui.

Sed viverra in mi eget ornare. Nunc maximus lacus laoreet magna congue, et auctor dolor auctor. Curabitur vitae porttitor lectus. Nam at malesuada lacus, id porttitor nibh. Aenean vel tellus et neque fringilla vulputate ut nec metus. Aliquam quis tellus sit amet magna elementum hendrerit at a lacus. In eget posuere mi, at pharetra augue. Aliquam gravida, elit nec tempor vehicula, arcu mi congue leo, quis ultricies sem nisi non sem. Morbi ut nisl eget odio aliquet interdum. Pellentesque sed arcu non nibh tincidunt tincidunt. Aliquam scelerisque massa ut diam interdum blandit. Phasellus nec enim id diam mattis finibus ac in tortor. Mauris non rutrum velit. Aliquam imperdiet risus ex, non consequat orci semper quis. Vestibulum placerat erat neque, condimentum suscipit odio pulvinar at. Proin feugiat, sem eget sodales dapibus, ante magna malesuada lacus, at fringilla enim velit sit amet nunc.

Aliquam sed blandit augue, vel malesuada ipsum. Proin porttitor dolor urna, quis vestibulum magna sagittis eu. Quisque egestas tempor ornare. Sed tincidunt varius ante eget tincidunt. Morbi consectetur ex orci, at sodales urna laoreet vel. Morbi mollis blandit lorem eu mattis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Fusce nisi mauris, aliquet dapibus turpis eu, blandit lacinia orci. Nulla sollicitudin, ante nec scelerisque dignissim, turpis massa elementum mauris, nec pellentesque dui nunc sit amet purus. Morbi sed orci mauris. Fusce tempus arcu vel dui posuere imperdiet. Curabitur mattis, ipsum eu sagittis consectetur, quam justo varius lectus, vitae ultricies felis ligula nec mauris. Mauris varius metus pretium maximus elementum. Nunc congue convallis risus, in consectetur purus tincidunt efficitur. Morbi pharetra vulputate ipsum, vitae sollicitudin magna ornare vitae.

Curabitur ac facilisis massa. Maecenas quis feugiat dolor. Suspendisse ipsum nunc, rutrum eget semper a, ornare nec urna. Ut massa velit, rutrum a vestibulum non, pretium a nunc. Aliquam erat volutpat. Nam ultrices massa sed turpis sagittis accumsan. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque non sapien nisi. Sed ut gravida orci. Aliquam feugiat sem at diam interdum lobortis nec sit amet arcu. Maecenas varius enim arcu, ac fringilla diam condimentum sit amet. Suspendisse et tellus sem.

In nibh purus, placerat in lectus sit amet, dictum facilisis arcu. Sed ultricies rutrum mollis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras bibendum elit sed enim commodo dapibus. Vestibulum nibh justo, finibus ac diam at, pulvinar luctus nibh. Sed sit amet tristique urna. Praesent hendrerit bibendum velit, id ultrices ligula luctus id. Sed rhoncus non massa id cursus. Suspendisse eleifend risus et gravida lacinia. Phasellus varius velit sed mauris dapibus eleifend. Phasellus nisi eros, pretium id porta nec, hendrerit aliquet lacus. Phasellus commodo felis ac dui tempus, non scelerisque ante tincidunt. Praesent ligula tortor, mattis vitae diam vel, pharetra pharetra lorem. Curabitur commodo ligula risus, in rutrum magna rutrum vitae. Donec ut odio nec mauris imperdiet porta. Fusce sagittis, elit ac pretium ullamcorper, tellus libero bibendum lorem, eu eleifend nulla est sit amet sapien.

Nam ac dapibus ante. Suspendisse eleifend, augue vel ultricies pharetra, libero magna vestibulum elit, et porttitor massa magna sit amet ante. Aliquam tristique ex in bibendum volutpat. Praesent nisi sem, rutrum non erat ut, volutpat hendrerit quam. Cras lectus enim, ornare in purus quis, egestas pretium nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras pretium ut dui in pretium. Nulla semper suscipit vestibulum. Nullam eu ex leo. Mauris euismod neque quis ligula rhoncus pellentesque. Maecenas elementum orci in malesuada condimentum.

Integer accumsan ipsum eget congue laoreet. Duis mollis suscipit risus eu facilisis. Phasellus sed tempus felis. Aliquam elit odio, tempor at dolor non, congue vestibulum leo. Fusce ultricies orci vel lorem aliquet, nec auctor elit varius. Aenean pretium leo eget ultricies venenatis. Vivamus quam massa, volutpat at erat a, rhoncus vehicula neque.

Vivamus hendrerit, neque vitae vulputate rhoncus, quam eros aliquam tellus, ac auctor lectus dolor vel urna. Sed at lacinia nibh. In sed mauris non augue placerat tristique. Sed id aliquet lacus. Nunc sit amet fermentum eros. Pellentesque aliquet id neque non porta. Etiam ut sapien sollicitudin, faucibus lectus nec, viverra metus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean et magna quis tortor lacinia ullamcorper. Nam sed rhoncus ligula, id porta velit. Mauris vehicula leo metus, imperdiet aliquet purus lacinia at. Mauris faucibus neque tempus suscipit ornare. Maecenas in commodo lacus. Pellentesque quis tristique arcu, ut vehicula diam.

Nam at vulputate lorem. Maecenas ultricies eget odio mollis tristique. Quisque ac tortor dictum, commodo dui at, congue dui. Sed id est vitae nunc aliquam pretium. Nullam euismod enim tellus, vitae commodo magna dictum eget. Vivamus eget ipsum odio. Sed eu massa finibus, imperdiet quam a, tristique enim. Proin id neque fringilla, accumsan turpis at, rhoncus eros. Donec nec orci erat. Pellentesque non congue leo. Vivamus vulputate quis orci nec scelerisque.

Fusce a quam felis. In vestibulum eleifend lectus ut placerat. Duis placerat, turpis in tempus pharetra, nibh libero fringilla orci, vitae pellentesque lacus erat vel felis. Nulla at massa nibh. Integer leo purus, faucibus eu libero non, elementum mattis erat. Ut sollicitudin consectetur metus at ultricies. Etiam placerat risus vel turpis efficitur, nec vulputate ante pulvinar. Etiam pulvinar auctor mi. Vestibulum quis ipsum quis diam blandit dapibus non in est.

In sit amet congue sem. Morbi odio magna, interdum sed congue egestas, pretium vitae ex. Praesent lacinia purus risus, ut feugiat dui venenatis vitae. Nullam molestie, dui sit amet venenatis accumsan, dui turpis porttitor ante, eget luctus tellus erat quis risus. In laoreet enim ullamcorper est malesuada consequat. Mauris viverra nulla a porta lacinia. Sed bibendum, purus ut vestibulum interdum, tortor libero rutrum lorem, et faucibus risus tellus id neque. Mauris eu ipsum sapien. Fusce eu justo lobortis, aliquam tortor ac, vestibulum odio. Fusce eu ante et nisi viverra viverra. Aliquam vulputate scelerisque tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse quis augue quis erat porttitor congue. Cras pretium sodales libero nec placerat. Aenean quam dolor, malesuada a enim non, auctor scelerisque enim. Cras quis nibh fringilla, rutrum eros ac, elementum nisi.

Nulla pharetra at diam nec iaculis. Praesent maximus at diam quis mollis. Suspendisse dapibus efficitur ultrices. Pellentesque hendrerit elementum felis non iaculis. Vestibulum gravida consectetur ipsum, quis imperdiet augue tristique quis. Morbi eu sapien et neque suscipit ullamcorper. Nulla id euismod massa.

Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla fringilla sapien nibh, a condimentum risus posuere a. Curabitur ultricies mollis quam eu tristique. Proin felis lectus, feugiat a posuere sed, iaculis at lorem. Nam sed eros eget turpis sodales interdum eget eget lacus. Fusce sed orci ullamcorper, posuere libero vitae, porta dolor. Ut ultrices accumsan magna, nec accumsan odio consequat vel. Aliquam arcu metus, fermentum nec ultricies vitae, dapibus et turpis. Ut vitae nisl nec ligula gravida aliquam et vitae turpis. Aliquam et ipsum dolor. Integer cursus faucibus quam maximus facilisis. Suspendisse tincidunt, odio eget consectetur dignissim, eros diam venenatis tellus, sed ullamcorper turpis ipsum quis lectus. Sed facilisis semper varius.

Integer bibendum, ligula sed aliquam efficitur, nibh ligula varius velit, sed fringilla ligula est eget tortor. Etiam lacus eros, faucibus id turpis semper, feugiat aliquet leo. Nullam volutpat consectetur magna sed imperdiet. Vivamus sit amet elit sit amet tortor semper dapibus. Integer in erat fringilla, iaculis ante et, vestibulum ante. Aenean at congue risus. Quisque malesuada, magna sit amet ultrices posuere, nulla metus maximus lacus, in rhoncus ante massa pulvinar libero. Vivamus non felis sit amet urna fringilla auctor.

Integer facilisis tellus ac metus dictum facilisis ut vitae purus. Mauris pellentesque quam turpis, in convallis nibh egestas in. Pellentesque ultrices condimentum placerat. Integer facilisis ultricies neque et porta. Morbi in lorem vestibulum magna elementum pharetra id vel turpis. Duis vel mattis enim. Phasellus nec ex posuere, auctor est eget, placerat nibh. In molestie tempus blandit. Nullam facilisis lacinia sem, et condimentum orci tristique et. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam egestas ex ligula, sit amet ultrices odio tincidunt sed.

Nulla facilisi. Mauris sem mauris, tincidunt eu risus non, scelerisque interdum urna. Aliquam et dui sit amet dolor egestas dignissim sit amet vel lacus. Aliquam convallis ex sit amet odio auctor semper. Pellentesque egestas ante ligula, eu gravida lacus gravida sed. Integer bibendum quam sed bibendum consectetur. Praesent massa erat, accumsan sit amet scelerisque vitae, pellentesque eu enim. Aliquam vitae nunc tristique, fermentum velit non, imperdiet turpis. Etiam eget bibendum turpis. Aliquam erat volutpat.

Aliquam semper, mi ut sollicitudin vulputate, mi dolor sagittis massa, vel rutrum lorem justo ut purus. Vestibulum et ante vitae turpis congue fermentum. Maecenas imperdiet, magna quis auctor finibus, dui turpis venenatis est, vitae ultricies neque mauris a quam. Curabitur dolor turpis, ullamcorper quis ex in, ornare pretium dui. Aliquam et risus risus. Nulla eu fringilla eros. Curabitur eu condimentum tortor. Phasellus iaculis purus risus, et volutpat risus sodales ac. Nam a imperdiet augue, tincidunt vehicula orci. In et elementum nisi. Fusce quam turpis, imperdiet a dictum sed, ultricies sit amet sapien. Duis mattis ipsum eu sem eleifend euismod. Fusce sed nisi sit amet ligula fermentum laoreet vitae et dolor.

Duis sit amet sem quam. Donec dictum luctus urna nec tempus. Nullam sed dui vulputate, malesuada nisl vitae, facilisis ex. Maecenas eleifend fringilla tellus eu feugiat. Integer eleifend interdum feugiat. Aenean tempor commodo orci et dapibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi porta nunc nec magna auctor mattis. Proin ut tincidunt lorem. Aliquam id quam quis neque suscipit volutpat id a erat. Duis eu ipsum dui. Maecenas porta lectus sit amet sapien fermentum, sodales lacinia urna gravida. Pellentesque at sapien scelerisque, sagittis elit vel, egestas libero. Curabitur diam velit, rhoncus vel imperdiet at, convallis id nulla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce dolor sapien, fringilla et dolor et, bibendum maximus nisl.


