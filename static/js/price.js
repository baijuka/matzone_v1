document.addEventListener("DOMContentLoaded", function(event) { 
    
    document.getElementById('id_product_size').addEventListener('change', function(){
        document.getElementById('p_price').innerText = '£'+this.value;
    });
});
