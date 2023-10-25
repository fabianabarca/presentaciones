// ----------------------------
// Choices inputs
// ----------------------------

var choiceInputCount = 0;

var forloopCounter = 0;
var checkboxes = [];

function addChoiceInput() {
    forloopCounter++;

    var container = document.getElementById('choices-container');

    var formGroup = document.createElement('div');
    formGroup.classList.add('form-group');

    var label = document.createElement('label');
    label.setAttribute('for', 'choice_' + forloopCounter);
    label.textContent = 'Opción ' + forloopCounter + ':';

    var inputText = document.createElement('input');
    inputText.setAttribute('type', 'text');
    inputText.setAttribute('id', 'choice_' + forloopCounter);
    inputText.setAttribute('name', 'choices__' + forloopCounter);
    inputText.classList.add('form-control');

    var inputCheckbox = document.createElement('input');
    inputCheckbox.setAttribute('type', 'checkbox');
    inputCheckbox.setAttribute('id', 'is_correct_' + forloopCounter);
    inputCheckbox.setAttribute('name', 'is_correct_' + forloopCounter);
    inputCheckbox.classList.add('form-check-input', 'my-2');

    // Agrega la casilla de verificación al array
    checkboxes.push(inputCheckbox);

    inputCheckbox.addEventListener('change', function () {
        uncheckOtherCheckboxes(inputCheckbox);
    });

    var labelCheckbox = document.createElement('label');
    labelCheckbox.setAttribute('for', 'is_correct_' + forloopCounter);
    labelCheckbox.classList.add('form-check-label', 'text-secondary', 'mx-1', 'my-1');
    labelCheckbox.textContent = 'Correcta';

    formGroup.appendChild(label);
    formGroup.appendChild(inputText);
    formGroup.appendChild(inputCheckbox);
    formGroup.appendChild(labelCheckbox);

    container.appendChild(formGroup);

    inputText.focus();
}


function devareChoiceInput() {
    if (choiceInputCount > 0) {
        choiceInputCount--;
        
        var inputContainer = document.getElementById('choices');

        inputContainer.removeChild(inputContainer.lastChild);
    }
}

function uncheckOtherCheckboxes(currentCheckbox) {
    checkboxes.forEach(function (checkbox) {
        if (checkbox !== currentCheckbox) {
            checkbox.checked = false;
        }
    });
}
