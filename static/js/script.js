//search bar
function filmSearch(userSearcBar) {
    console.log(userSearcBar);
    document.getElementById('userSearchBar').value;
    fetch('https://www.omdbapi.com/?apikey=fe2afef6&s='+userSearchBar+'&type=movie')
    .then(res => res.json())
    .then(data => {
console.log(data.Search);
      data.Search.forEach(movie => {
console.log(movie.Title)
        let movieInfo =
        `<div class="col-md-3 film-card">
        <div class="card border-0 shadow">
        <a href="/view/movies/${movie.imdbID}">
            <img src="${movie.Poster}" class="card-img-top" alt="movie-poster"></a>
            <p>${movie.Title}</p>
            </div>`;
        $('#moviesDIV').append(movieInfo);
      });
    });
}
const userSearchBar = $("#filmSearchBar");


