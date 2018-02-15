<template>
    <div id="update-article">
        <h1>Update Article</h1>

        <p><router-link :to="{ name: 'AllArticle' }">Return to articles</router-link></p>

        <notification v-bind:notifications="notifications"></notification>

        <form v-on:submit.prevent="editArticle">
            <div class="form-group">
                <label name="article_title">Title</label>
                <input type="text" class="form-control" v-model="article.title" id="article_title">
            </div>

            <div class="form-group">
                <label name="article.content">Content</label>
                <input type="text" class="form-control" v-model="article.content" id="article.content" required>
            </div>

            <div class="form-group">
                <label name="article_thumbnail">Thumbnail</label>
                <div v-if="!image">
                Select an image
                        <input type="file" class="form-control" @change="onFileChange">
                </div>
                <div v-else>
                    <img :src="image" />
                    <button @click="removeImage">Remove image</button>
                </div>
            </div>

            <div class="form-group">
                <button class="btn btn-primary">Update</button>
            </div>
        </form>
    </div>
</template>

<script>
    import Notification from './notifications.vue';
    export default{
        data(){
            return{
                article:{},
                notifications:[],
                image: ''
            }
        },
        created: function(){
            this.getArticle();
        },
        methods: {
            onFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            this.article.file = files[0]; 
            this.createImage(files[0]);
            },
            createImage(file) {
                var image = new Image();
                var reader = new FileReader();
                var vm = this;

                reader.onload = (e) => {
                    vm.image = e.target.result;
            };
                reader.readAsDataURL(file);
            },
                removeImage: function (e) {
                this.image = '';
            },
            getArticle: function()
            {
                this.$http.get('http://localhost:5000/article/' + this.$route.params.id).then((response) => {
                    this.article = response.body;
                    this.image = this.article.thumbnail;
                }, (response) => {
                });
            },
            editArticle: function()
            {
                var formData = new FormData();
                formData.append('title', this.article.title);
                formData.append('content', this.article.content);
                formData.append('file', this.article.file);
                if(this.notifications) this.notifications = [];
                if(this.image) this.$http.put('http://localhost:5000/article/' + this.$route.params.id, formData, {
                    headers : {
                        // 'Content-Type' : 'multipart/form-data'
                        'enctype' : 'multipart/form-data'
                    }
                }).then((response) => {
                    this.notifications.push({
                        type: 'success',
                        message: 'Article updated successfully'
                    });
                }, (response) => {
                    this.notifications.push({
                        type: 'error',
                        message: 'Article not updated'
                    });
                });
            }
        },
        components: {
            'notification' : Notification
        }
    }
</script>

<style scoped>
img {
  width: 30%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
button {
  
}
</style>