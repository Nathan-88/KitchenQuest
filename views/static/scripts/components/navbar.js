export default {
  props: {
    showsearch: false
  },
  template: /*html*/ `
    <nav class="navbar">
      <a href="/"><img class="logo" src="/static/images/Logo.svg" alt="kitchen Quest"></a>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="#trending">Trending</a></li>
        <li><a href="/saved_recipes">Favourites</a></li>
      </ul>
      <div v-if="showsearch" class="nav-search">
          <input type="text" name="nav_search" id="nav-search" placeholder="Search for Recipes">
          <button type="submit"><img class="icon" src="/static/images/search.svg" alt="search"></button>
      </div>
    </nav>
  `
};
