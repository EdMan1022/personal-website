<template>
  <div class="page_index">
    <b-container>
      <b-row class="justify-content-center">
        <b-cols>
          <page-card
          v-for="page in pages" :key="page.id"
          v-bind:id="page.id"
          ></page-card>
        </b-cols>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import PageCard from './PageCard'

export default {
  name: 'PageIndex',
  components: {PageCard},
  computed: mapState({
    pages: state => state.pages
  }),
  beforeMount () {
    this.$store.dispatch('loadPages')
  }
}
</script>

<style scoped>

</style>
