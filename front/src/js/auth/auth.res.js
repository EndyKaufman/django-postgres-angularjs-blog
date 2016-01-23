app.factory('AuthRes', function ($http, AppConst) {
    var service={};

    service.actionLogin=function(email, password){
        return $http.post(AppConst.auth.login.action, {
            email: email,
            password: password,
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionLogout=function(){
        return $http.post(AppConst.auth.logout.action,{
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    return service;
  });