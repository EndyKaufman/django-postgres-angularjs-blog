$(document).ready(function(){
  $('[data-toggle="offcanvas"]').click(function () {
    $('.row-offcanvas').toggleClass('active')
  });
  $('input').iCheck({
    checkboxClass: 'icheckbox_custom-blue',
    radioClass: 'iradio_custom-blue',
    increaseArea: '20%'
  });
});