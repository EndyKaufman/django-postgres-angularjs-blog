module.exports ={
  executeAndReturnJson: function (code, callback){
    code =
        'var callbackArg = arguments[arguments.length - 1];' +
        'var callback = function(data){callbackArg(JSON.stringify(data));};' + code;
    browser.driver.executeAsyncScript(code).then(function(data){
        callback(JSON.parse(data));
    });
  },
  getJson: function(uri, callback){
    this.executeAndReturnJson(
        '$.get( "'+uri+'")'+
        '.done(function(data){callback(data)})'+
        '.fail(function(data){callback(data)});',
        callback
    )
  },
  postJson: function(uri, data, callback){
    this.executeAndReturnJson(
        'var postData='+JSON.stringify(data)+';'+
        'postData.csrfmiddlewaretoken=window.AppConfig.csrf_token;'+
        '$.ajaxSetup({headers:{"X-CSRFToken":window.AppConfig.csrf_token}});'+
        '$.ajax({'+
        '    type: "POST",'+
        '    url: "'+uri+'",'+
        '    contentType: "application/json",'+
        '    dataType: "json",'+
        '    data: JSON.stringify(postData)'+
        '})'+
        '.done(function(data){callback(data)})'+
        '.fail(function(data){callback(data)});',
        callback
    )
  }
}