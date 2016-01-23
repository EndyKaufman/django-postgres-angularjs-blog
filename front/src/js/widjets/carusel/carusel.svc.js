app.factory('CaruselSvc', function () {
    var service={};
    service.prev=function(target){
        $(target).carousel('prev');
    }
    service.next=function(target){
        $(target).carousel('next');
    }
    service.init=function(reload){
    }
    service.init();    
    return service;
  });