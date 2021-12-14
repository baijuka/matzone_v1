document.addEventListener("DOMContentLoaded", function(event) { 
    
    document.getElementById('id_product_size').addEventListener('change', function(){
<<<<<<< HEAD
        document.getElementById('p_price').innerText = '£'+this.value;
    });
});
=======
        console.log('Current value ' + this.value);
        document.getElementById('p_price').innerText = '£'+this.value;
    });



});
  
>>>>>>> a6659350daad7aa977d1ffee7caff789a1ffc7cc
