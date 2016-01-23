app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/login', {
        templateUrl: 'views/auth/login.html',
        controller: 'AuthCtrl',
        navId: 'login'
      });
});