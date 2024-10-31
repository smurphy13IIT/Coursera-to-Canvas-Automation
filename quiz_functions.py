import yaml
import json

quiz_yaml_file = "auto_graded_questions.yml"
json_file = 'output.json'


## def yaml_to_json(yaml_file):
    # Open and read the YAML file
with open(quiz_yaml_file, 'r') as file:
    yaml_content = yaml.safe_load(file)

## COURSERA TO RESPONDUS FORMATTING FUNCTIONS
quiz_contents = ""

def multiple_choice(question_data, question_index):

    question_number = question_index
    question_wording = question_data['prompt']

    answer_letter_list = [f"{chr(97 + j)}." for j, item in enumerate(question_data['options'])]

    answers = ""

    for k in question_data['options']:
        answer_letter = answer_letter_list[question_data['options'].index(k)]

        if k['isCorrect'] == True:
            answer_letter = "*" + answer_letter

        answer_text = k['answer']
        answer_feedback = f"@ {k['feedback']}"

        complete_answer = f"{answer_letter} {answer_text}\n{answer_feedback}"

        answers = f"{answers}\n{complete_answer}\n"

    complete_question = f"{question_number} {question_wording}\n{answers}"

    return complete_question

for i in yaml_content:

    question_index = str(yaml_content.index(i) + 1) + ") "
    question_data = i['variations'][0]

    if question_data['typeName'] == "multipleChoice":
        question_contents = multiple_choice(question_data, question_index)

    if yaml_content.index(i) != 0:
        quiz_contents = f"{quiz_contents}\n{question_contents}"

    else:
        quiz_contents = f"{quiz_contents}{question_contents}"


open a CSV

For every row in the CSV:
    run the respondus transform function

    export the results



with open('respondus_quiz.txt', 'w') as file:
    file.write(quiz_contents)






## COURSERA TO CANVAS API FUNCTIONS

## Get course ID from Canvas or from a CSV file
course_id = "COURSE_ID_HERE"

## Build a quiz dictionary object

## Create a loop to build an array of Quiz Question dictionary objects