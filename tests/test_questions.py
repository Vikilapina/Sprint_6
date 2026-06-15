import pytest

from pages.main_page import MainPage
from data.faq_data import FAQ_DATA


class TestQuestions:

    @pytest.mark.parametrize(
        "question_index, expected_text",
        FAQ_DATA
    )
    def test_faq_answers(
        self,
        driver,
        question_index,
        expected_text
    ):
        main_page = MainPage(driver)

        main_page.accept_cookies()

        main_page.click_question(question_index)
        main_page.wait_for_answer(question_index)

        actual_text = main_page.get_answer_text(question_index)

        assert actual_text == expected_text