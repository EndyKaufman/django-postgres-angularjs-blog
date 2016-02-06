app.factory('AccountRes', function ($http, AppConst) {
    var service={};

    service.actionLogin=function(email, password){
        return $http.post(AppConst.account.login.action, {
            email: email,
            password: password,
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionLogout=function(){
        return $http.post(AppConst.account.logout.action,{
            csrfmiddlewaretoken: AppConfig.csrf_token
        });
    };

    service.actionUpdate=function(item){
        var item=angular.copy(item);
        item['csrfmiddlewaretoken']=AppConfig.csrf_token;
        return $http.post(AppConst.account.update.action, item);
    }

    return service;
  });