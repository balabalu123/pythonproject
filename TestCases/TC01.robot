****** settings ***
Library      SeleniumLibrary
Library      ../../../py/google.py

****** variables ***
${browser}      chrome
${url}          https://www.google.co.in/
${textbox}      googletxtbox
${text value}   textvalue
${search}       googlesearch
${link}         flipkartlink

****** Test Cases ***
Navigate Test

    Start test cases
#
#    Navigation to Home page

    Close Browser
    
addition


   

****** keywords ***
Start test cases
    open browser          ${url}     ${browser}
    Maximize Browser Window

#Navigation to Home page
    sleep  3
    Input Text          ${textbox}    ${text value}
    click element       ${search}
    click element       ${link}