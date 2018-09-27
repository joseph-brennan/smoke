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

  describe('before login the user', () => {
    it('should not be authenticated', () => {
      auth.checkAuth()
      expect(auth.user.authenticated).to.equal(false)
    })

    it('should not have a username', () => {
      expect(auth.user.username).to.equal(null)
    })

    it('should not have an email', () => {
      expect(auth.user.email).to.equal('')
    })

    it('should not have a permission', () => {
      expect(auth.user.permission).to.equal('')
    })
  })

  describe('after login the user', () => {
    it('should be authenticated', done => {
      auth.login({}, { username: 'admin', password: 'password' })
      expectAsync(
        {
          status: 200,
          response: {
            access_token: 'Hooray!',
            user: {
              active: true,
              email: 'admin@mail.com',
              id: 1,
              username: 'admin',
              permission: 'Admin'
            }
          }
        },
        () => {
          auth.checkAuth()
          expect(auth.user.authenticated).to.equal(true)
          done()
        }
      )
    })

    it('should have set the authenticated user to the username', () => {
      expect(auth.user.username).to.equal('admin')
    })

    it("should have set the authenticated user's email", () => {
      expect(auth.user.email).to.equal('admin@mail.com')
    })

    it("should have set the authenticated user's permission", () => {
      expect(auth.user.permission).to.equal('Admin')
    })
  })
})
