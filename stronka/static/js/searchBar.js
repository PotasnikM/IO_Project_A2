document.getElementById('search-button').addEventListener('click', search);
  // event.preventDefault(); // zapobiega przeładowaniu strony po kliknięciu przycisku
  // var searchInput = document.getElementById('search-input').value; // pobieramy wartość pola tekstowego
  // alert(searchInput)

function search() {
  let searchInput = document.getElementById('search-input').value;
  // let searchInput =document.querySelectorAll(".search-input").values()
  let temp = typeof searchInput;
  $.ajax({
      type: 'POST',
      url: '/search',
      data: JSON.stringify({"name":searchInput}),
      contentType: 'application/json',
      success: function(response) {
          // kod do wykonania po pomyślnym zakończeniu żądania
      },
      error: function(xhr, status, error) {
      }
  });
}
// document.getElementById("add-button").addEventListener("click", function () {
// // document.getElementById("innerdiv").innerHTML += "<h5><input type=\"text\" class=\"search-input\" " +
// //                                                             "placeholder=\"Wpisz frazę wyszukiwania\"></h5>";});
// document.getElementById("innerdiv").append(<h5><input type=\"text\" class=\"search-input\" " +
//                                                             "placeholder=\"Wpisz frazę wyszukiwania\"></h5>)});