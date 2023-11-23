document.getElementById('deleteButton1').addEventListener('click', function() {
    delAlert();
  });
  document.getElementById('deleteButton2').addEventListener('click', function() {
    delAlert();
  });
  document.getElementById('deleteButton3').addEventListener('click', function() {
    delAlert();
  });

  function  delAlert() {
   if (confirm("Do you want to Delete?")===true) {
     alert("delete confirmed")
   }else{
    alert("delete cancelled")
   }
    
  }