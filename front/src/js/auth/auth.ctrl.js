app.controller('AuthCtrl', function ($scope, $rootScope, AuthSvc, AppConst) {
	$scope.AuthSvc=AuthSvc;

    $rootScope.$on('navbar.change',function(event, current, previous){
        if (current.params!=undefined && current.params.navId==AppConst.auth.logout.name)
            AuthSvc.doLogout();
	});

	AuthSvc.init();
});