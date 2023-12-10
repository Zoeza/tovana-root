// This is your test publishable API key.
const stripe = Stripe("pk_test_51Novf3FuL8GWnTLgurepIYrfdoeaOa3UbM65EFIBeax2okYW4QpVSUBprkTn1MxnEDGlF7ICvZsDxtN4QhK8mbRc00rwApk8kd");

const elements = stripe.elements();

// Options for card number Element.
const cardNumberOptions = {
  iconStyle: 'default',
  showIcon: true,
  placeholder: '1111 1111 1111 1111',
  style: {
    base: {
        fontSize: '16px',
    }
  },
};

// Create an instance of the card number Element.
var cardNumberElement = elements.create('cardNumber',cardNumberOptions);
// Add an instance of the card Element into the `card-number-element` <div>.
cardNumberElement.mount('#card-number-element');

// Options for card expiry Element.
const cardExpiryOptions = {
  placeholder: 'MM/YY',
  style: {
    base: {
        fontSize: '16px',
    }
  },
};

// Create an instance of the card expiry Element.
var cardExpiryElement = elements.create('cardExpiry' ,cardExpiryOptions);
// Add an instance of the card Element into the `card-expiry-element` <div>.
cardExpiryElement.mount('#card-expiry-element');

// Options for card cvc Element.
const cardCvcOptions = {
  placeholder: '123',
  style: {
    base: {
        fontSize: '16px',
    }
  },
};

// Create an instance of the card cvc Element.
var cardCvcElement = elements.create('cardCvc' ,cardCvcOptions);
// Add an instance of the card Element into the `card-cvc-element` <div>.
cardCvcElement.mount('#card-cvc-element');



// Create a token or display an error when the form is submitted.
const form = document.getElementById('payment-form');
form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {token, error} = await stripe.createToken(cardNumberElement);

  if (error) {
    // Inform the customer that there was an error.
    const errorElement = document.getElementById('card-errors');
    errorElement.textContent = error.message;
  } else {
    // Send the token to your server.
    stripeTokenHandler(token);
  }
});

const stripeTokenHandler = (token) => {
  // Insert the token ID into the form so it gets submitted to the server
  const form = document.getElementById('payment-form');
  const hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}