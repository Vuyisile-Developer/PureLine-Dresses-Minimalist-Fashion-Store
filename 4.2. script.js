async function loadProducts() {

    let response = await fetch("http://localhost:5000/products")

    let products = await response.json()

    let container = document.getElementById("product-list")

    products.forEach(p => {

        let card = document.createElement("div")

        card.className = "product"

        card.innerHTML = `
<h3>${p.name}</h3>
<p>${p.description}</p>
<p>$${p.price}</p>
<button>Add to Cart</button>
`

        container.appendChild(card)

    })

}

loadProducts()