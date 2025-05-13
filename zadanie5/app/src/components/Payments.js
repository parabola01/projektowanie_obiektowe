import React, { useContext } from 'react';
import { CartContext } from '../context/CartContext';

const Payments = () => {
  const { cartItems, setCartItems } = useContext(CartContext);

  const handlePayment = async () => {
    if (cartItems.length === 0) {
      alert('Koszyk jest pusty.');
      return;
    }

    const paymentData = {
      items: cartItems,
      totalAmount: cartItems.reduce((sum, item) => sum + item.price, 0),
      timestamp: new Date().toISOString()
    };

    try {
      const response = await fetch('http://localhost:4000/payment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(paymentData)
      });

      if (!response.ok) {
        throw new Error('Błąd serwera');
      }

      const result = await response.json();
      console.log('Odpowiedź serwera:', result);
      alert('Płatność została wysłana do serwera.');

      // Opcjonalnie: wyczyść koszyk po płatności
      setCartItems([]);

    } catch (error) {
      console.error('Błąd podczas płatności:', error);
      alert('Nie udało się zrealizować płatności.');
    }
  };

  return (
    <div>
      <h2>Płatności</h2>
      <p>Liczba produktów w koszyku: {cartItems.length}</p>
      <p>Suma: {cartItems.reduce((sum, item) => sum + item.price, 0)} zł</p>
      <button onClick={handlePayment}>Wyślij płatność</button>
    </div>
  );
};

export default Payments;
