import Vue from 'vue'
import Router from 'vue-router'
import AllArticle from '@/components/all-article'
import CreateArticle from '@/components/create-article'
import EditArticle from '@/components/edit-article'
import DeleteArticle from '@/components/delete-article'
Vue.use(Router)
Vue.use(VueResource);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'AllArticle',
      component: AllArticle
    },
    {
      path: '/create-article',
      name: 'CreateArticle',
      component: CreateArticle
    },
    {
      path: '/edit-article',
      name: 'EditArticle',
      component: EditArticle
    },
    {
      path: '/delete-article',
      name: 'DeleteArticle',
      component: DeleteArticle
    }
  ]
})
