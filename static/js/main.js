/**
 * Validating a input email
 * @param idField: the id field of the element to validate
 * @param fieldError: the id field where to show the error
 */
function validationEmail(idField, fieldError) {
    let id_email = document.getElementById(idField); // the input text to validate
    let email = document.getElementById(fieldError); // div to show the error
    let regex = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{1,4}$/;

    let textError;

    let button = document.getElementById('button');

    // if the email is valid, hide the div error field
    if (regex.test(id_email.value)) {
        textError = document.createTextNode('');
        email.replaceChild(textError, email.firstChild);
        button.disabled = false;
    } else {
        // show the error to the user and disable the button
        textError = document.createTextNode('Invalid email. Please enter a valid email address');
        if (!email.hasChildNodes()) {
            email.appendChild(textError);
        } else {
            email.replaceChild(textError, email.firstChild);
        }
        button.disabled = true;
    }
}

/**
 * Validating a input field
 * @param idField: the id field of the element to validate
 * @param fieldError: the id field where to show the error
 */
function validationField(idField, fieldError) {
    let id_field = document.getElementById(idField); // the input text to validate
    let email = document.getElementById(fieldError); // div to show the error
    let regex = /(?=^.{3,255}$)^[a-zA-Z|\s][a-zA-Z0-9|\s]*[._-]?[a-zA-Z0-9]+$/;

    let textError;

    let button = document.getElementById('button');

    // if the email is valid, hide the div error field
    if (regex.test(id_field.value)) {
        textError = document.createTextNode('');
        email.replaceChild(textError, email.firstChild);
        button.disabled = false;
    } else {
        // show the error to the user and disable the button
        textError = document.createTextNode('Invalid field.');
        if (!email.hasChildNodes()) {
            email.appendChild(textError);
        } else {
            email.replaceChild(textError, email.firstChild);
        }
        button.disabled = true;
    }
}