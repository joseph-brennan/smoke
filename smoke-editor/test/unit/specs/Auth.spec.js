import { expectAsync } from './utils'
import moxios from 'moxios'
import auth from '@/auth'

describe('auth', () => {
  beforeEach(() => {
    moxios.install()
  })

  afterEach(() => {
    moxios.uninstall()
  })

  it('should only be authenticated aftter successful login', done => {
    auth.checkAuth()
    expect(auth.user.authenticated).to.equal(false)
    auth.login({}, { username: 'bogus', password: 'password' })
    expectAsync({
      status: 200,
      response: {
        access_token: 'Hooray!'
      }
    }, () => {
      auth.checkAuth()
      expect(auth.user.authenticated).to.equal(true)
      done()
    })
  })
})
