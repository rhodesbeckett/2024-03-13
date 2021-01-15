<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/editor">Highlights</router-link> |
      <router-link to="/testing">Testing data</router-link> |
      <router-link to="/cut-and-render">Cut and render</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  methods: {
    test() {
      console.log("something ffrom appp vue");
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
