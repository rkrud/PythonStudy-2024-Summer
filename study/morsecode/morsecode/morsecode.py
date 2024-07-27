def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code
# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()
    counter = 0
    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"
    return message

def is_help_command(user_input):
    if user_input.upper() in ["H", "HELP"]:
        return True
    else:
        return False
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정

    # ==================================
def is_validated_english_sentence(user_input):
    
    num = list(map(str, (0,1,2,3,4,5,6,7,8,9)))
    special_chars = list("_@#$%^&*()-+=[]{}\"';:\\|`~")

    for i in user_input:
        if i in num:
            return False
        if i in special_chars:
            return False
        
    for i in ".,!?":
        user_input = user_input.replace(i, "")

    if user_input.strip() == "":
        return False
    
    return True
    
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
          3) 영어와 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_english_sentence("Hello 123")
        False
        >>> mc.is_validated_english_sentence("Hi!")
        True
        >>> mc.is_validated_english_sentence(".!.")
        False
        >>> mc.is_validated_english_sentence("!.!")
        False
        >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
# print(is_validated_english_sentence(" "))
    # ==================================
def is_validated_morse_code(user_input):

    use = ["-", ".", " "]
    morsecodedict = get_morse_code_dict()

    for i in user_input:
        if i not in use:
            return False
    
    user_input_split = user_input.split()
    for i in user_input_split:
        if i not in morsecodedict.values():
            return False
    
    return True

    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_morse_code("..")
        True
        >>> mc.is_validated_morse_code("..-")
        True
        >>> mc.is_validated_morse_code("..-..")
        False
        >>> mc.is_validated_morse_code(". . . .")
        True
        >>> mc.is_validated_morse_code("-- -- -- --")
        True
        >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """

    # ==================================
def get_cleaned_english_sentence(raw_english_sentence):

    for i in ".,!?":
        raw_english_sentence = raw_english_sentence.replace(i, "")
    
    raw_english_sentence = raw_english_sentence.strip()
    
    return raw_english_sentence

    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        >>> import morsecode as mc
        >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """

def decoding_character(morse_character):

    morsecodedict = get_morse_code_dict()

    reversed_morse_code = {value :key for key, value in morsecodedict.items()}

    return reversed_morse_code.get(morse_character)
    
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_character("-")
        'T'
        >>> mc.decoding_character(".")
        'E'
        >>> mc.decoding_character(".-")
        'A'
        >>> mc.decoding_character("...")
        'S'
        >>> mc.decoding_character("....")
        'H'
        >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정

    # ==================================
def encoding_character(english_character):

    morsecodedict = get_morse_code_dict()

    return morsecodedict.get(english_character)

    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_character("G")
        '--.'
        >>> mc.encoding_character("A")
        '.-'
        >>> mc.encoding_character("C")
        '-.-.'
        >>> mc.encoding_character("H")
        '....'
        >>> mc.encoding_character("O")
        '---'
        >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정

    # ==================================
def decoding_sentence(morse_sentence):

    morse_sentence_split = morse_sentence.strip().split("  ") #단어별로 나눈 뒤 리스트

    decoding_word = []
    for i in morse_sentence_split: # 나눈 각 리스트의 단어에 대해 반복할거다
        alphabet = i.split(" ") #단어를 알파벳 단위로 나눈 뒤 리스트
        alphabet = "".join(decoding_character(j) for j in alphabet)# 알파벳들 디코딩해서 디코딩된 각 단어로 완성
        #각 단어들을 모아야함
        decoding_word.append(alphabet)
        
    return " ".join(decoding_word)


    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    # ==================================
def encoding_sentence(english_sentence):

    english_sentence = get_cleaned_english_sentence(english_sentence)

    english_sentence_split = english_sentence.upper().split() #단어별로 나눠 리스트에 넣음
    
    encoding_word = []
    for i in english_sentence_split: #각 단어에 대해 반복
        alphabet = list(i) #각 단어를 알파벳으로 나눠 리스트에 넣음
        
        alphabet = " ".join(encoding_character(j) for j in alphabet)  # 각 알파벳을 모스 부호로 변환
        encoding_word.append(alphabet)
       #각 알파벳을 인코딩하여 합쳐서 한 단어로 만든다
    return "  ".join(encoding_word)
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
         .... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
         .... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
         .-- .  .- .-. .  --. .- -.-. .... --- -.
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
         .... ..  .... ..
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정

    # ==================================
def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    continue_number = 1
    sentence_strings = '.,!?'
    while continue_number == 1:
        input_message = input("Input your message(H - Help, 0 - Exit): ")
        if input_message == '0':
            continue_number = 0
        elif continue_number == 1: 
            if is_help_command(input_message) == True: 
                print(get_help_message()) 
                
            elif is_help_command(input_message) == False: 
                
                if is_validated_english_sentence(input_message) == True:
                    
                    print(encoding_sentence(input_message))
                elif is_validated_morse_code(input_message) == True:
                    
                    print(decoding_sentence(input_message))
                else:
                    print("Wrong Input")
                    
            else:
                print("Wrong Input")
                
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")
if __name__ == "__main__":
    main()

