module.exports ={
  debug: false,
  executeAndReturnJson: function (code, callback){
    code =
        "function getCookie(name) {\n"+
        "var cookieValue = null;\n"+
        "if (document.cookie && document.cookie != '') {\n"+
        "    var cookies = document.cookie.split(';');\n"+
        "    for (var i = 0; i < cookies.length; i++) {\n"+
        "        var cookie = jQuery.trim(cookies[i]);\n"+
        "        if (cookie.substring(0, name.length + 1) == (name + '=')) {\n"+
        "            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));\n"+
        "            break;\n"+
        "        }\n"+
        "    }\n"+
        "}\n"+
        "return cookieValue;\n"+
        "}\n"+
        "if (getCookie('csrftoken')!==null && window.AppConfig!==undefined)\n"+
        "window.AppConfig.csrf_token=getCookie('csrftoken');\n"+
        'var callbackArg = arguments[arguments.length - 1];\n' +
        'var callback = function(data){callbackArg(JSON.stringify(data));};\n' + code;
    browser.driver.executeAsyncScript(code).then(function(data){
        callback(JSON.parse(data));
    });
  },
  getJson: function(uri, callback){
    var $this=this;
    this.executeAndReturnJson(
        '$.get( "'+uri+'")'+
        '.done(function(){callback.apply(this, arguments)})'+
        '.fail(function(){callback.apply(this, arguments)});',
        function(){
                if ($this.debug===true){
                    console.log('\nGET: '+uri);
                    console.log('DATA:');
                    console.log(data);
                    console.log('RESPONSE:');
                    if (arguments[0]!=undefined)
                        console.log(arguments[0]);
                    else
                        console.log(arguments);
                    console.log('\n');
                    $this.debug=false;
                }
                callback.apply(this, arguments);
        }
    )
  },
  postJson: function(uri, data, callback){
    var $this=this;
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
        '.done(function(){callback.apply(this, arguments)})'+
        '.fail(function(){callback.apply(this, arguments)});',
        function(){
                if ($this.debug===true){
                    console.log('\nPOST: '+uri);
                    console.log('DATA:');
                    console.log(data);
                    console.log('RESPONSE:');
                    if (arguments[0]!=undefined)
                        console.log(arguments[0]);
                    else
                        console.log(arguments);
                    console.log('\n');
                    $this.debug=false;
                }
                callback.apply(this, arguments)
        }
    )
  }
}