// ----------------------------
// Choices inputs
// ----------------------------

var choiceInputCount = 0;

var forloopCounter = 0;
var checkboxes = [];

function addChoiceInput() {
    forloopCounter++;

    // Get the container where you want to append the form group
    var container = document.getElementById('choices-container');

    // Create the form group element
    var formGroup = document.createElement('div');
    formGroup.classList.add('form-group');

    // Create the label element
    var label = document.createElement('label');
    label.setAttribute('for', 'choice_' + forloopCounter);
    label.textContent = 'Opción ' + forloopCounter + ':';

    // Create the input element for the text
    var inputText = document.createElement('input');
    inputText.setAttribute('type', 'text');
    inputText.setAttribute('id', 'choice_' + forloopCounter);
    inputText.setAttribute('name', 'choices__' + forloopCounter);
    inputText.setAttribute('placeholder', 'Opción ' + forloopCounter);
    inputText.classList.add('form-control', 'my-2');

    // Create the checkbox input for "Opción Correcta"
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

    // Create the label for the checkbox
    var labelCheckbox = document.createElement('label');
    labelCheckbox.setAttribute('for', 'is_correct_' + forloopCounter);
    labelCheckbox.classList.add('form-check-label', 'my-2');
    labelCheckbox.textContent = 'Opción Correcta';
    

    // Append elements to the form group
    formGroup.appendChild(label);
    formGroup.appendChild(inputText);
    formGroup.appendChild(inputCheckbox);
    formGroup.appendChild(labelCheckbox);

    // Append the form group to the container
    container.appendChild(formGroup);

    // Focus on the new input
    inputText.focus();
}


// Create button to delete last choice input
function deleteChoiceInput() {
    if (choiceInputCount > 0) {
        choiceInputCount--;
        
        // Get the input container
        var inputContainer = document.getElementById('choices');

        // Remove the last child
        inputContainer.removeChild(inputContainer.lastChild);
    }
}

function uncheckOtherCheckboxes(currentCheckbox) {
    // Desmarca todas las casillas de verificación excepto la actual
    checkboxes.forEach(function (checkbox) {
        if (checkbox !== currentCheckbox) {
            checkbox.checked = false;
        }
    });
}
