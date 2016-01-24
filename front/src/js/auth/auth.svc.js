app.factory('AuthSvc', function ($http, AppConst, AuthRes, $rootScope, $routeParams, NavbarSvc) {
    var service={};
    service.init=function(reload){
        NavbarSvc.init();
    }

	service.doLogin=function(email,password){
	    AuthRes.actionLogin(email,password).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    var data=angular.copy(response.data.data);
                    AppConfig=angular.extend(AppConfig, data);
                	$rootScope.$broadcast('auth.login', data);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
            }
        );
	}
	service.doLogout=function(){
		 AuthRes.actionLogout().then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    var data={
                      "userId": false,
                      "userData": {}
                    }
                    AppConfig=angular.extend(AppConfig, data);
                    $rootScope.$broadcast('auth.logout', data);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
            }
        );
    }

    service.isLogged=function(){
        return AppConfig.userId!=false;
    }

    service.isAdmin=function(){
        return AppConfig.userId!=false && AppConfig.userData.roles!=undefined && AppConfig.userData.roles.indexOf('admin')
    }

    service.isAuthor=function(){
        return AppConfig.userId!=false && AppConfig.userData.roles!=undefined && AppConfig.userData.roles.indexOf('author')
    }

    service.isUser=function(){
        return AppConfig.userId!=false && AppConfig.userData.roles!=undefined && AppConfig.userData.roles.indexOf('user')
    }

    return service;
  });