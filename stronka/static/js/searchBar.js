const addInputButton = document.getElementById("add-button");
const inputContainer = document.getElementById("input-container");

document.getElementById('search-button').addEventListener('click', search);
// event.preventDefault(); // zapobiega przeładowaniu strony po kliknięciu przycisku
  // var searchInput = document.getElementById('search-input').value; // pobieramy wartość pola tekstowego
  // alert(searchInput)

addInputButton.addEventListener("click", function() {
  const newInput = document.createElement("input");
  newInput.type = "text";
  newInput.className = "search-input";
  inputContainer.appendChild(newInput);
});

function search() {
  const searchInput =document.getElementsByClassName("search-input");
  const itemsArray = [];

  for(let i = 0; i < searchInput.length; i++) {
      const item = {
          name: searchInput.item(i).value
      };
      itemsArray.push(item);
  }
  // alert(JSON.stringify(itemsArray));

  let temp = typeof searchInput;
  $.ajax({
      type: 'POST',
      url: '/search',
      data: JSON.stringify(itemsArray),
      contentType: 'application/json',
      success: function(response) {
          // kod do wykonania po pomyślnym zakończeniu żądania
      },
      error: function(xhr, status, error) {
      }
  });
}

//TODO: limit do 10 elementów
//TODO: Pobłogosławić CSSem
//TODO: Jakieś komentarze