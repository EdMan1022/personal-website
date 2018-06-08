<template>
  <b-card id="pageCard" class="text-justify"
          :header="page.id">
    <div>
      <p class="card-text text-justify">{{ page.page_type}}</p>
    </div>
    <div>
      {{ page.block[0].content }}
    </div>
  </b-card>
</template>

<script>
export default {
  name: 'PageCard',
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
