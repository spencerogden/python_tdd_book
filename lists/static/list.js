window.Superlists = {};


window.Superlists.initialize = function() {
  console.log('initialization called')
  $('input[name="text"]').on('keypress',function(){
    $('.has-error').hide();
  });
};