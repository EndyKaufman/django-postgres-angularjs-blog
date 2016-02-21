app.factory('ProjectSvc', function ($routeParams, $rootScope, $http, $q, $timeout, $location, AppConst, ProjectRes, TagSvc, NavbarSvc, MessageSvc) {
    var service={};

    $rootScope.$on('project.delete',function(event, item){
        MessageSvc.info('project/delete/success', {values:item});
        service.goList();
    });

    $rootScope.$on('project.create',function(event, item){
        MessageSvc.info('project/create/success', {values:item});
        service.goItem(item.name);
    });

    $rootScope.$on('project.update',function(event, item){
        MessageSvc.info('project/update/success', {values:item});
        service.goItem(item.name);
    });

    service.item={};
    service.list=false;

    service.countItemsOnRow=2;

    service.title=AppConst.project.strings.title;

    service.init=function(reload){
        NavbarSvc.init('project');

        $q.all([
            TagSvc.load(),
            service.load()
        ]).then(function(responseList) {

        });
    }

    service.goList=function(){
        $location.path('/project');
    }

    service.goItem=function(projectName){
        $location.path('/project/'+projectName);
    }

    service.updateItemOnList=function(item){
        for (var i=0;i<service.list.length;i++){
            if (item.id===service.list[i].id){
                service.list[i]=angular.copy(item);
            }
        }
    }

	service.doCreate=function(item){
	    $rootScope.$broadcast('show-errors-check-validity');
		 ProjectRes.actionCreate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    if (response.data.reload_source.tag==true)
                        TagSvc.load(true);
                    service.item=angular.copy(response.data.data[0]);
                    service.list.push(service.item);
                    $rootScope.$broadcast('project.create', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
    }
	service.doUpdate=function(item){
	    $rootScope.$broadcast('show-errors-check-validity');
		 ProjectRes.actionUpdate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    if (response.data.reload_source.tag==true)
                        TagSvc.load(true);
                    service.item=angular.copy(response.data.data[0]);
                    service.updateItemOnList(service.item);

                    $rootScope.$broadcast('project.update', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
            }
        );
    }
	service.doDelete=function(item){
         MessageSvc.confirm('project/remove/confirm', {values:[item.title]},
         function(){
             ProjectRes.actionDelete(item).then(
                function (response) {
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                        for (var i=0;i<service.list.length;i++){
                            if (service.list[i].id==item.id){
                                service.list.splice(i, 1);
                                break;
                            }
                        }
                        service.item={};
                        $rootScope.$broadcast('project.delete', item);
                    }
                },
                function (response) {
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                        MessageSvc.error(response.data.code, response.data);
                }
            );
         });
    }

    service.doDeleteImage=function(index){
        service.item.images.splice(index, 1);
    }
    service.doAddImage=function(text){
        if (text===undefined)
            text='';
        if (service.item.images===undefined)
            service.item.images=[];
        service.item.images.push({
            id: chance.guid(),
            title: text
        });
    }
    service.initEmptyItem=function(){
        service.item = {};
        /*service.title = '';
        service.name = '';
        service.description = '';
        service.url = '';
        service.text = '';
        service.html = '';
        service.markdown = '';*/
        service.item.type = 1;
        service.item.tags = [];
        service.item.images = [];
    }
    service.load=function(){
        var deferred = $q.defer();
        if ($routeParams.projectName!=undefined){
            if (service.item.name!==$routeParams.projectName)
                ProjectRes.getItem($routeParams.projectName).then(
                    function (response) {
                        service.item=angular.copy(response.data.data[0]);
                        deferred.resolve(service.item);
                        $rootScope.$broadcast('project.item.load', service.item);
                    },
                    function (response) {
                        service.item={};
                        if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                            MessageSvc.error(response.data.code, response.data);
                        deferred.resolve(service.item);
                    }
                );
        }else{
            if (service.list===false){
                ProjectRes.getList().then(function (response) {
                    service.list=angular.copy(response.data.data);
                    deferred.resolve(service.list);
                    $rootScope.$broadcast('project.load', service.list);
                }, function (response) {
                    service.list=[];
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                        MessageSvc.error(response.data.code, response.data);
                    deferred.resolve(service.list);
                });
            }else
                deferred.resolve(service.list);
        }
        return deferred.promise;
    }
    return service;
  });