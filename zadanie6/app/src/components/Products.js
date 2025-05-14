import React, { useEffect, useState, useContext } from 'react';
import { CartContext } from '../context/CartContext';

const Products = () => {
  const [products, setProducts] = useState([]);
  const { addToCart } = useContext(CartContext);

  useEffect(() => {
    fetch('http://localhost:4000/products')
      .then(response => {
        if (!response.ok) {
          throw new Error('Błąd podczas pobierania danych');
        }
        return response.json();
      })
      .then(data => setProducts(data))
      .catch(error => console.error('Błąd:', error));
  }, []);

  return (
    <div>
      <h2>Produkty</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            {product.name} - {product.price} zł
            <button onClick={() => addToCart(product)}>Dodaj do koszyka</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Products;

