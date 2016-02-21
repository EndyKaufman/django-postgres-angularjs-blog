describe('Create and delete user', function() {
    var helpers = require('./../helpers.js');
    var appConfigResponse = undefined, createResponse = undefined, deleteResponse = undefined;

    beforeEach(function(done){
        if (appConfigResponse!==undefined){
            done();
            return;
        }
        browser.driver.manage().window().setSize(1280, 1024);
        browser.get(browser.baseUrl).then(function(){
            helpers.executeAndReturnJson(
                'if (window.AppConfig!==undefined)callback(window.AppConfig);else callback({});',
                function(response){
                    appConfigResponse = response;
                    done();
                });
            }
        );
    });

    it('response structure must be correct', function() {
        expect(appConfigResponse).toBeDefined();
        expect(typeof appConfigResponse).toEqual('object');
    });

    describe('Create new user', function() {

      beforeEach(function(done){
        if (createResponse!==undefined){
            done();
            return;
        }
        //helpers.debug=true;
        helpers.postJson('/account/reg', {
            email:'newuser@email.com',
            password:'newuser@email.com'
        }, function(response){
            createResponse = response;
            done();
        });
      });

      it('response structure must be correct', function() {
        expect(typeof createResponse).toEqual('object');
        expect(createResponse.data).toBeDefined();
        if (createResponse.data){
            var userData = createResponse.data[0];
            var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
            for (var i=0; i<fields.length; i++)
                expect(userData[fields[i]]).toBeDefined();
            if (userData.roles.length>0)
                expect(userData.roles[0]).toEqual('user');
        }
      });

        describe('Delete created user', function() {

            beforeEach(function(done){
                if (deleteResponse!==undefined){
                    done();
                    return;
                }
                //helpers.debug=true;
                helpers.postJson('/account/delete', {
                }, function(response){
                    deleteResponse = response;
                    done()

                });
            });

            it('response structure must be correct', function() {
                expect(typeof deleteResponse).toEqual('object');
                expect(deleteResponse.code).toEqual('ok');
            });
        });
    });
});