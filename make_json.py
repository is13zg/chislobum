import json
from generate_quiz_combinations import generate_combinations as gc


def get_weight(spec_quest_count):
    return spec_quest_count // 2


def get_voices(text):
    # Здесь должна быть реализация функции, которая генерирует аудиофайл из текста
    # и возвращает путь к файлу. Для примера вернем заглушку.
    print(text)
    return "path_to_audio.mp3"


def get_audio(questions_list):
    for question_type in questions_list:
        for formulation in question_type["formulations"]:
            for specific_question in formulation["specific_questions"]:
                # Предполагаем, что get_voices возвращает путь к аудиофайлу для текста вопроса
                audio_path = get_voices(specific_question["text"])
                specific_question["audio"] = audio_path


def create_question_type(base_text, specific_questions_count, difficulty, topics, formulations):
    question_type = {
        "base_text": base_text,
        "specific_questions_count": specific_questions_count,
        "weight": get_weight(specific_questions_count),
        "topics": topics,
        "difficulty": difficulty,
        "formulations": []
    }
    print(formulations)
    for x in formulations:
        print("     ",x)
        formulation = {
            "formulation_text": x,
            "specific_questions": []
        }
        specific_questions = gc(x)
        for xx in specific_questions:
            print("         ", xx)
            specific_question = {
                "text": xx,
                "audio": "lol.mp3"
            }
            formulation["specific_questions"].append(specific_question)
        question_type["formulations"].append(formulation)
        print(question_type)
    return question_type





def load_questions_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        questions_list = json.load(file)
    return questions_list


def save_questions_to_file(questions_list, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(questions_list, file, ensure_ascii=False, indent=4)


def preload(mstr):
    ls = mstr.split("	")
    tls = [ls[0]] + ls[4:]
    return create_question_type(ls[0],int(ls[1]),int(ls[2]),ls[3],tls)




# Пример использования
filename = 'questions.json'

# Загрузка вопросов из файла
questions_list = load_questions_from_file(filename)

#questions_list = questions["questions"]


#mstr= input()
#preload(mstr)

# Добавление нового типа вопроса
#new_question_type = preload(mstr)
#questions_list.append(new_question_type)
get_audio(questions_list)


# Сохранение обновленных вопросов в файл
save_questions_to_file(questions_list, filename)
