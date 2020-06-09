

$("#buttonsubmit").on("click", function(){

    var casa_en_c, casa, depto, nuevo, remate;
         
    var inputroom = $("#selRooms").val();
    
    var inputbathroom = $("#selBathrooms").val();
    
    var inputtype = $("#selTypeofProperty").val();
        if (inputtype === '1') {
            casa = 1;
            casa_en_c = 0;
            depto = 0;
        }
        else if (inputtype === '2') {
            casa = 0;
            casa_en_c = 1;
            depto = 0;
        }
        else if (inputtype === '3'){
            casa = 0;
            casa_en_c = 0;
            depto = 1;  
        }
        else {
            casa = 1;
            casa_en_c = 0;
            depto = 0;

        }

     var inputtype2 = $("#selnuevoremate").val();
        if (inputtype2 === '1') {
            nuevo = 1;
            remate = 0;
            
        }
        else if (inputtype2 === '2') {
            nuevo = 0;
            remate = 1;
        }
        else {
            nuevo = 1;
            remate = 0;
        }

    var inputterrain = $("#inputterrain").val();
        if (parseFloat(inputterrain) > 1491 ) {
            inputterrain = 1491; 
        }
        else if (parseFloat(inputterrain) < 12) {
            inputterrain = 12; 
        }
   
    var inputhousem2 = $("#inputhousem2").val();
        if (parseFloat(inputhousem2) > 1199 ) {
            inputhousem2 = 1199; 
        }
        else if (parseFloat(inputhousem2) < 12) {
            inputhousem2 = 12; 
        }
    var inputcity = $("#inputcity").val();
   
    console.log(inputroom);
    console.log(inputbathroom);
    console.log(inputhousem2);
    console.log(inputterrain);
    console.log(inputcity);
    console.log(casa);
    console.log(casa_en_c);
    console.log(depto);
    console.log(nuevo);
    console.log(remate);

    console.log(`/predict/${inputroom}/${inputbathroom}/${inputhousem2}/${inputterrain}/${inputcity}/${casa}/${casa_en_c}/${depto}/${nuevo}/${remate}`) 
    d3.json(`/predict/${inputroom}/${inputbathroom}/${inputhousem2}/${inputterrain}/${inputcity}/${casa}/${casa_en_c}/${depto}/${nuevo}/${remate}`).then(data => {
        // $("#output").text(data);

        $("#paragraph-price").html("<h1>"+new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(data)+"</h1>");
        console.log( new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(data) );
        
    })

    
});


