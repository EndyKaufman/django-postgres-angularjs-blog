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

    service.actionUpdate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post(AppConst.auth.update.action, item);
    }

    return service;
  });