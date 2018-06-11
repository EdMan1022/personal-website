<template>
  <div id="navbar">
    <b-navbar toggleable type="light" variant="info">
      <b-navbar-toggle target="nav_text_collapse"></b-navbar-toggle>
      <b-navbar-brand>MyWebsite</b-navbar-brand>
      <b-collapse is-nav id="nav_text_collapse">
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
  #navbar {
    margin-bottom: 30px
  }

</style>
