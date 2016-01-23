app.controller('NavbarCtrl', function ($scope, $rootScope, NavbarSvc) {
	$scope.NavbarSvc=NavbarSvc;

	$rootScope.$on('$routeChangeSuccess',function(event, current, previous){
	    NavbarSvc.init();
	    $rootScope.$broadcast('routeChangeSuccess', current, previous);
	});

	$rootScope.$on('login',function(data){
	    NavbarSvc.init();
	    NavbarSvc.goHome();
	});

	$rootScope.$on('logout',function(data){
	    NavbarSvc.init();
	    NavbarSvc.goHome();
	});

    NavbarSvc.init();
});