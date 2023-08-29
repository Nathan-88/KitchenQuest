export default {
  props: {
    showsearch: false
  },
  template: /*html*/ `
    <nav class="navbar">
      <a href="home.html"><img class="logo" src="images/Logo.svg" alt="kitchen Quest"></a>
      <ul>
        <li><a href="home.html">Home</a></li>
        <li><a href="recipe_details.html">Recipes</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Trending</a></li>
      </ul>
      <div v-if="showsearch" class="nav-search">
          <input type="text" name="nav_search" id="nav-search" placeholder="Search for Recipes">
          <button type="submit"><img class="icon" src="images/search.svg" alt="search"></button>
      </div>
    </nav>
  `
};
