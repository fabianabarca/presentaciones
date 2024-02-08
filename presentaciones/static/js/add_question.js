let choiceInputCount = 0;
let checkboxes = [];

function addChoiceInput() {
  choiceInputCount++;

  let selectionType = document.getElementById("selection-type").value;

  console.log(selectionType);

  let container = document.getElementById("choices-container");

  let formGroup = document.createElement("div");
  formGroup.classList.add("form-group");

  let inputDeleteContainer = document.createElement("div");
  inputDeleteContainer.style.display = "flex";
  inputDeleteContainer.style.alignItems = "center";

  let label = document.createElement("label");
  label.setAttribute("for", "choice_" + choiceInputCount);
  label.textContent = "Opción " + choiceInputCount + ":";
  label.classList.add("label-opcion");

  let inputText = document.createElement("input");
  inputText.setAttribute("type", "text");
  inputText.setAttribute("id", "choice_" + choiceInputCount);
  inputText.setAttribute("name", "choices__" + choiceInputCount);
  inputText.classList.add("form-control");
  inputText.style.marginRight = "10px";

  let inputCheckbox = document.createElement("input");
  inputCheckbox.setAttribute("type", "checkbox");
  inputCheckbox.setAttribute("id", "is_correct_" + choiceInputCount);
  inputCheckbox.setAttribute("name", "is_correct_" + choiceInputCount);
  inputCheckbox.classList.add("form-check-input", "my-2");

  checkboxes.push(inputCheckbox);

  inputCheckbox.addEventListener("change", function () {
    if (selectionType === "single") {
      uncheckOtherCheckboxes(inputCheckbox);
    }
  });

  let labelCheckbox = document.createElement("label");
  labelCheckbox.setAttribute("for", "is_correct_" + choiceInputCount);
  labelCheckbox.classList.add(
    "form-check-label",
    "text-secondary",
    "mx-1",
    "my-1"
  );
  labelCheckbox.textContent = "Correcta";

  let deleteButton = document.createElement("button");
  deleteButton.classList.add("btn", "p-0");
  deleteButton.addEventListener("click", function () {
    container.removeChild(formGroup);
    choiceInputCount--;
    updateLabels();
  });

  let deleteIcon = document.createElement("img");
  deleteIcon.setAttribute(
    "src",
    "../../static/front/svg/icons/delete-choice.svg"
  );
  deleteIcon.setAttribute("alt", "Eliminar");
  deleteIcon.style.width = "30px";
  deleteIcon.style.height = "30px";
  deleteIcon.style.margin = "0px";

  deleteButton.appendChild(deleteIcon);

  formGroup.appendChild(label);
  formGroup.appendChild(inputDeleteContainer);
  inputDeleteContainer.appendChild(inputText);
  inputDeleteContainer.appendChild(deleteButton);
  formGroup.appendChild(inputCheckbox);
  formGroup.appendChild(labelCheckbox);

  container.appendChild(formGroup);

  inputText.focus();
}

function uncheckOtherCheckboxes(currentCheckbox) {
  checkboxes.forEach(function (checkbox) {
    if (checkbox !== currentCheckbox) {
      checkbox.checked = false;
    }
  });
}

function updateLabels() {
  let choiceLabels = document.querySelectorAll(".form-group .label-opcion");
  choiceLabels.forEach(function (label, index) {
    label.textContent = "Opción " + (index + 1) + ":";
  });
}

function uncheckOtherCheckboxes(currentCheckbox) {
  checkboxes.forEach(function (checkbox) {
    if (checkbox !== currentCheckbox) {
      checkbox.checked = false;
    }
  });
}

function updateLabels() {
  let choiceLabels = document.querySelectorAll(".form-group .label-opcion");
  let inputs = document.querySelectorAll(".form-group input[type='text']");
  let checkboxes = document.querySelectorAll(
    ".form-group input[type='checkbox']"
  );

  choiceLabels.forEach(function (label, index) {
    label.textContent = "Opción " + (index + 1) + ":";
  });

  inputs.forEach(function (input, index) {
    input.setAttribute("id", "choice_" + (index + 1));
    input.setAttribute("name", "choices__" + (index + 1));
  });

  checkboxes.forEach(function (checkbox, index) {
    checkbox.setAttribute("id", "is_correct_" + (index + 1));
    checkbox.setAttribute("name", "is_correct_" + (index + 1));
  });
}
