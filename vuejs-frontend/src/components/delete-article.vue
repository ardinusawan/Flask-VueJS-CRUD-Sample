<template>
    <div id="delete-product">
        <h1>Delete Article {{ article.title }}</h1>

        <p><router-link :to="{ name: 'AllArticle' }">Return to articles</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="deleteArticle">
            <p><button class="btn btn-danger">Delete Article</button></p>
        </form>
    </div>
</template>

<script>
    import Notification from './notifications.vue';

    export default{
        data(){
            return{
                article:{},
                notifications:[]
            }
        },

        created: function(){
            this.getArticle();
        },

        methods: {
            getArticle: function()
            {
                this.$http.get('http://localhost:5000/article/' + this.$route.params.id).then((response) => {
                    this.article = response.body;
                }, (response) => {

                });
            },

            deleteArticle: function()
            {
                if(this.notifications) this.notifications = [];
                this.$http.delete('http://localhost:5000/article/' + this.$route.params.id, this.article, {
                    headers : {
                        'Content-Type' : 'application/json'
                    }
                }).then((response) => {
                    this.$router.push({name: 'AllArticle'})
                }, (response) => {
                    this.notifications.push({
                        type: 'danger',
                        message: 'Article could not deleted'
                    });
                });
            }
        },

        components: {
            'notification' : Notification
        }
    }
</script>