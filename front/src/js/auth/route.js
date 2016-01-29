app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
      .when('/login', {
        templateUrl: 'views/auth/login.html',
        controller: 'AuthCtrl',
        navId: 'login'
      })
      .when('/profile', {
        templateUrl: 'views/auth/profile.html',
        controller: 'AuthCtrl',
        navId: 'profile'
      });
});