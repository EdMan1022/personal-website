<template>
  <b-card id="pageCard" class="text-justify"
          :header="page.title">
    <vue-markdown>
      {{ page.block[0].content }}
    </vue-markdown>
  </b-card>
</template>

<script>
import VueMarkdown from 'vue-markdown'
export default {
  name: 'PageCard',
  components: {VueMarkdown},
  props: ['id'],
  computed: {
    page () {
      return this.$store.getters.getPageById(this.$props.id)
    }
  }
}
</script>

<style scoped>
  #pageCard {
    margin-bottom: 20px
  }
</style>
