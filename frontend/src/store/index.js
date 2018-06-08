import Vue from 'vue'
import Vuex from 'vuex'
import 'es6-promise/auto'
import { fetchPages } from '@/api'

Vue.use(Vuex)

const state = {
  pages: []
}

const actions = {
  loadPages (context) {
    return fetchPages()
      .then((response) => context.commit('setPages', {pages: response}))
  }
}

const mutations = {
  setPages (state, payload) {
    state.luigiErrors = payload.luigiErrors
  }
}

const getters = {}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store
