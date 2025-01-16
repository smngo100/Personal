# A Class to Test 
survey.py 
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and preprare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results: ")
        for response in self.responses:
            print(f" -{response}")


# Proving that the AnonymousSurvey class works 
language_survey.py 
from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()


# Testing the AnonoymmousSurvey Class
test_survey.py 
from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
