// Obtener elementos del DOM
const commentInput = document.getElementById('comment');
const submitButton = document.getElementById('submit-comment');
const starRating = document.getElementById('star-rating');

// Asignar evento al botón de enviar comentario
submitButton.addEventListener('click', function() {
  const comment = commentInput.value;
  // Realizar acción con el comentario, como enviarlo a un servidor
  console.log('Comentario:', comment);
});

// Asignar evento a las estrellas para asignar calificación
starRating.addEventListener('click', function(event) {
  const selectedStar = event.target;
  if (selectedStar.classList.contains('star')) {
    // Realizar acción con la calificación seleccionada, como enviarla a un servidor
    console.log('Calificación:', selectedStar.innerText);
  }
});
