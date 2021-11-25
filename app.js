const Products = {
    data() {
        return {
            products: []
        }
    },
    methods: {
        async getProducts(){
            try {
                const res = await fetch("http://127.0.0.1:5000/products")
                const { products } = await res.json()
                this.products = products
            }
            catch (error) {
                console.log(error);
            }
        }
    },
    created() {
        this.getProducts();
    }
}
  
const productsApp = Vue.createApp(Products)
  
productsApp.component('product-item', {
    props: ['product'],
    template: `<div class="product-card col-md-4">
                    <img
                        :src="product.imageUrl"
                        :alt="product.name"
                        class="product-img"
                    />
                    <p class="product-title">{{ product.name }} | \${{product.price}}</p>
                    <p class="product-description">
                        {{ product.description }}
                    </p>
                    <div class="star">
                        <div class="rating" v-bind:style="{ width: product.rating + '%' }">
                            <span>&#x2605;&#x2605;&#x2605;&#x2605;&#x2605;</span>
                        </div>
                    </div>
                </div>`
})
  
productsApp.mount('#product-list')