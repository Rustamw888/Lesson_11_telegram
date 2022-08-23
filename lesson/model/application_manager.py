from selene import have, command
from selene.support.shared import browser

from lesson.model.pages.student_registration_page import StudentRegistrationForm, ModalDialogSubmittingForm

form = StudentRegistrationForm()
result = ModalDialogSubmittingForm()


def opened_practice_form():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)\
        .should(have.size_less_than_or_equal(4))\
        .perform(command.js.remove)
