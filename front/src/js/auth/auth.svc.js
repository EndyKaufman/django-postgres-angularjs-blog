app.factory('AuthSvc', function ($http, AppConst, AuthRes, MessageSvc, $rootScope, $routeParams, NavbarSvc) {
    var service={};

    $rootScope.$on('auth.login',function(event, data){
        MessageSvc.info('auth/login/success');
        NavbarSvc.init();
        NavbarSvc.goBack();
    });

    $rootScope.$on('auth.logout',function(event, data){
        MessageSvc.info('auth/logout/success');
        NavbarSvc.init();
        NavbarSvc.goHome();
    });

    $rootScope.$on('navbar.change',function(event, eventRoute, current, previous){
        if (current.params!=undefined && current.params.navId==AppConst.auth.logout.name && service.isLogged()){
            eventRoute.preventDefault();
            service.doLogout();
        }
    });

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
                    MessageSvc.error(response.data.code, {
                        values:
                            [
                                email
                            ]
                    });
            }
        );
	}
	service.doLogout=function(){
         MessageSvc.confirm('auth/logout/confirm', {},
         function(){
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
                        MessageSvc.error(response.data.code);
                }
            );
        });
    }

    service.isLogged=function(){
        return AppConfig.userId!=false;
    }

    service.isAdmin=function(){
        return AppConfig.userId!=false && AppConfig.userData.roles!=undefined && AppConfig.userData.roles.indexOf('admin')!=-1
    }

    service.isAuthor=function(){
        return AppConfig.userId!=false && AppConfig.userData.roles!=undefined && AppConfig.userData.roles.indexOf('author')!=-1
    }

    service.isUser=function(){
        return AppConfig.userId!=false && AppConfig.userData.roles!=undefined && AppConfig.userData.roles.indexOf('user')!=-1
    }

    return service;
  });