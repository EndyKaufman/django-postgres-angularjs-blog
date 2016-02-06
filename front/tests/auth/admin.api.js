describe('Update user profile with admin role', function() {
    var helpers = require('./../helpers.js');

    var appConfigResponse = undefined, adminResponse = undefined, logoutResponse = undefined, profileResponse = undefined, restoreProfileResponse = undefined;

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

    describe('Login on site', function() {

      beforeEach(function(done){
        if (adminResponse!==undefined){
            done();
            return;
        }
        helpers.postJson('/auth/login', {
            email:'admin@email.com',
            password:'admin@email.com'
        }, function(response){
            adminResponse = response;
            done();
        });
      });

      it('response structure must be correct', function() {
        expect(typeof adminResponse).toEqual('object');
        var userData = adminResponse.data[0];
        var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
        for (var i=0; i<fields.length; i++)
            expect(userData[fields[i]]).toBeDefined();
        if (userData.roles.length>0)
            expect(userData.roles[0]).toEqual('admin');
      });

      describe('Update first name', function() {

        beforeEach(function(done){
            if (profileResponse!==undefined){
                done();
                return;
            }
            helpers.postJson('/auth/profile/update', {
                firstname:'New Name',
                email:'admin@email.com'
            }, function(response){
                profileResponse = response;
                done();
            });
        });

        it('response structure must be correct', function() {
            expect(typeof profileResponse).toEqual('object');
            var userData = profileResponse.data[0];
            var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
            for (var i=0; i<fields.length; i++)
                expect(userData[fields[i]]).toBeDefined();
            if (userData.roles.length>0)
                expect(userData.roles[0]).toEqual('admin');
            expect(userData.firstname).toEqual('New Name');
        });

        describe('Cancel modify first name', function() {

            beforeEach(function(done){
                if (restoreProfileResponse!==undefined){
                    done();
                    return;
                }
                helpers.postJson('/auth/profile/update', {
                    firstname:adminResponse.data[0].firstname,
                    email:'admin@email.com'
                }, function(response){
                    restoreProfileResponse=response;
                    done();
                });
            });

            it('response structure must be correct', function() {
                expect(typeof restoreProfileResponse).toEqual('object');
                var oldData = restoreProfileResponse.data[0];
                var userData = restoreProfileResponse.data[0];
                expect(oldData.firstname).toEqual(userData.firstname);
            });

            describe('Logout from site', function() {

                beforeEach(function(done){
                    if (logoutResponse!==undefined){
                        done();
                        return;
                    }
                    helpers.postJson('/auth/logout', {
                    }, function(response){
                        logoutResponse = response;
                        done()

                    });
                });

                it('response structure must be correct', function() {
                    expect(typeof logoutResponse).toEqual('object');
                    expect(logoutResponse.code).toEqual('ok');
                });

            });

        });

      });

    });

});