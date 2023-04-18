from selene import browser, have
import os


def test_filling_form(web_browser):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Dmitii')
    browser.element('#lastName').type('Larin')
    browser.element('#userEmail').type('Dmitrii@mail.ru')

    browser.element('[value="Male"]').double_click()
    browser.element('#userNumber').type('79290423322')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1991"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="0"]').click()
    browser.element('[aria-label="Choose Wednesday, January 9th, 1991"]').click()

    browser.element('#subjectsInput').type('Arts')
    browser.element('#react-select-2-option-0').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd()+"/cat.png")
    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').double_click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').execute_script('element.click()')
    #browser.element('#submit').click()

    browser.all('tbody tr')\
        .should(have.exact_texts('Student Name Dmitii Larin', 'Student Email Dmitrii@mail.ru', 'Gender Male',
                                 'Mobile 7929042332', 'Date of Birth 09 January,1991',
                                 'Subjects Arts', 'Hobbies Sports', 'Picture cat.png',
                                 'Address Moscow', 'State and City Uttar Pradesh Lucknow'))
