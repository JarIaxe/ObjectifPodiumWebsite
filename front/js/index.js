let baseUrl = "http://127.0.0.1:5000"

$(document).ready(function() {
    fetch(baseUrl + '/api/getTodaySession') // Remplace par l'URL de l'API
    .then(data => {
        // Afficher les données de l'API
        $('#session-display').html(`Session chargée`);
    })
    .catch(error => {
        // Gérer les erreurs
        $('#session-display').html(`Pas de session`);
    });
  });



function updateResults(data) {
    const $resultsList = $('#resultsList');
    $resultsList.empty(); // Vider la liste précédente

    if (data.length === 0) {
        $resultsList.append('<li class="list-group-item">Aucun résultat trouvé</li>');
    } else {
        data.forEach(item => {
            let artists = '';
            item.artists.forEach((artist, i) => {
                if (i != 0){ artists += ', ' }
                artists += artist.name;
            });
        $resultsList.append(`<li class="list-group-item">${item.name} - ${artists}</li>`);
        });
    }
    }

// Écouter les changements dans la zone de recherche
$(document).ready(function() {
    $('#searchInput').on('input', function() {
      const query = $(this).val();
      
      // Appeler l'API seulement si la recherche n'est pas vide
      if (query.trim().length > 0) {
        fetch(baseUrl + `/api/searchSong`,
            {method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ title: query })})
          .then(response => {
            if (!response.ok) {
              throw new Error('Erreur de réseau');
            }
            return response.json();
          })
          .then(data => {
            console.log(data);
            updateResults(data); // Mettre à jour la liste avec les données reçues
          })
          .catch(error => {
            console.error('Erreur :', error);
          });
      } else {
        // Vider la liste si le champ de recherche est vide
        updateResults([]);
      }
    });
  });
