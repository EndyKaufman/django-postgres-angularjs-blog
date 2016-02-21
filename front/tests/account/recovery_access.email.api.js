describe('Create, reset password with email and delete user', function() {
    var helpers = require('./../helpers.js');
    var cheerio = require('cheerio');

    var appConfigResponse = undefined, createResponse = undefined, logoutResponse = undefined,
    logoutNewPasswordResponse = undefined, loginNewPasswordResponse = undefined,
    loginResponse = undefined, recoveryResponse = undefined, resetCode = undefined,
    resetpasswordResponse = undefined, deleteResponse = undefined;

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
            email: process.env.EMAIL_HOST_USER,
            password: process.env.EMAIL_HOST_USER
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

        describe('Logout from site', function() {

            beforeEach(function(done){
                if (logoutResponse!==undefined){
                    done();
                    return;
                }
                //helpers.debug=true;
                helpers.postJson('/account/logout', {
                }, function(response){
                    logoutResponse = response;
                    done()

                });
            });

            it('response structure must be correct', function() {
                expect(typeof logoutResponse).toEqual('object');
                expect(logoutResponse.code).toEqual('ok');
            });

            describe('Sent password reset code to email', function() {

                beforeEach(function(done){
                    if (recoveryResponse!==undefined){
                        done();
                        return;
                    }
                    //helpers.debug=true;
                    helpers.postJson('/account/recovery', {
                        email: process.env.EMAIL_HOST_USER
                    }, function(response){
                        setTimeout(function(){
                            recoveryResponse = response;
                            done()
                        },10000);
                    });
                });

                it('response structure must be correct', function() {
                    expect(typeof recoveryResponse).toEqual('object');
                    expect(recoveryResponse.code).toEqual('ok');
                });

                describe('Check email over IMAP and try find message with code for reset', function() {

                    beforeEach(function(done){
                        if (resetCode!==undefined){
                            done();
                            return;
                        }
                        //helpers.debug=true;
                        helpers.checkMail(function(msg){
                            if (msg.html != undefined && msg.headers['return-path'] == process.env.EMAIL_HOST_USER){
                                $ = cheerio.load(msg.html);
                                if ($('strong.code').text()!='')
                                    resetCode = $('strong.code').text();
                            }
                        },done);
                    });

                    it('response structure must be correct', function() {
                        expect(resetCode).toBeDefined();
                    });


                    describe('Sent code for reset password and new password', function() {

                        beforeEach(function(done){
                            if (resetpasswordResponse!==undefined){
                                done();
                                return;
                            }
                            //helpers.debug=true;
                            helpers.postJson('/account/resetpassword', {
                                code:resetCode,
                                password:'password'
                            }, function(response){
                                resetpasswordResponse = response;
                                done();
                            });
                        });

                        it('response structure must be correct', function() {
                            expect(typeof resetpasswordResponse).toEqual('object');
                            expect(resetpasswordResponse.data).toBeDefined();
                            if (resetpasswordResponse.data){
                                var userData = resetpasswordResponse.data[0];
                                var fields = ['id', 'username', 'email', 'firstname', 'lastname', 'roles'];
                                for (var i=0; i<fields.length; i++)
                                    expect(userData[fields[i]]).toBeDefined();
                                if (userData.roles.length>0)
                                    expect(userData.roles[0]).toEqual('user');
                            }
                        });

                        describe('Logout from site', function() {

                            beforeEach(function(done){
                                if (logoutNewPasswordResponse!==undefined){
                                    done();
                                    return;
                                }
                                //helpers.debug=true;
                                helpers.postJson('/account/logout', {
                                }, function(response){
                                    logoutNewPasswordResponse = response;
                                    done()

                                });
                            });

                            it('response structure must be correct', function() {
                                expect(typeof logoutNewPasswordResponse).toEqual('object');
                                expect(logoutNewPasswordResponse.code).toEqual('ok');
                            });
                            describe('Login on site', function() {

                                  beforeEach(function(done){
                                    if (loginNewPasswordResponse!==undefined){
                                        done();
                                        return;
                                    }
                                    //helpers.debug=true;
                                    helpers.postJson('/account/login', {
                                        email:process.env.EMAIL_HOST_USER,
                                        password:'password'
                                    }, function(response){
                                        loginNewPasswordResponse = response;
                                        done();
                                    });
                                  });

                                  it('response structure must be correct', function() {
                                    expect(typeof loginNewPasswordResponse).toEqual('object');
                                    expect(loginNewPasswordResponse.data).toBeDefined();
                                    if (loginNewPasswordResponse.data){
                                        var userData = loginNewPasswordResponse.data[0];
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
                    });
                });
            });
        });
    });
});