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
        $resultsList.append(`<li class="list-group-item d-flex justify-content-between align-items-center">
            ${item.name} - ${artists}
            <div class="d-flex align-items-center">
            <span class="info-label me-2">${item.bd_num} occurences en BD</span><button class="btn btn-primary btn-sm action-btn" data-name="${item.id}">Enregistrer en BD</button>
            </div>
          </li>
          `);
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

  // Écouter les clics sur les boutons avec la classe 'action-btn'
  $('#resultsList').on('click', '.action-btn', function() {
    const itemName = $(this).data('name'); // Récupérer le nom de l'item
    
    // Faire un appel API pour cet item
    fetch(baseUrl + '/api/saveSong', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ id: itemName })
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erreur de réseau');
        }
        return response.json();
      })
      .then(data => {
        alert(`Action réalisée pour ${itemName} : ${data.message}`);
      })
      .catch(error => {
        console.error('Erreur :', error);
      });
  });
