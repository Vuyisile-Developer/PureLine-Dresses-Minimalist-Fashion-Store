using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

[ApiController]
[Route("api/products")]
public class ProductsController : ControllerBase
{

    static List<Product> products = new List<Product>()
    {
        new Product{
            Id=1,
            Name="Ocean Breeze Maxi Dress",
            Price=89.99,
            Description="Blue tropical maxi dress with crisscross back",
            Image="/images/ocean.jpg"
        },

        new Product{
            Id=2,
            Name="Sky Blossom",
            Price=79.99,
            Description="Light blue puff sleeve floral dress",
            Image="/images/sky.jpg"
        }
    };

    [HttpGet]
    public IEnumerable<Product> Get()
    {
        return products;
    }

    [HttpPost]
    public IActionResult Post(Product product)
    {
        products.Add(product);
        return Ok(product);
    }

}