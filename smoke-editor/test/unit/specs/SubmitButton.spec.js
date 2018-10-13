import SubmitButton from '@/components/SubmitButton'
import moxios from 'moxios'
import { expectAsync, mount } from './utils'

describe('SubmitButton', () => {
  beforeEach(() => {
    window.onbeforeunload = () => {}
    moxios.install()
  })

  afterEach(() => {
    moxios.uninstall()
  })

  it('should send a proper JSON payload when clicked', done => {
    const vm = mount(SubmitButton, { propsData: { editorCode: '' } })
    vm.clicked()

    expectAsync(
      {
        status: 200,
        request: { data: '' }
      },
      () => {
        done()
      }
    )
  })

  it('should send a proper base64 payload', done => {
    const vm = mount(SubmitButton, { propsData: { editorCode: 'Hello World' } })
    vm.clicked()

    expectAsync(
      {
        status: 200,
        request: { data: 'SGVsbG8gV29ybGQ=' }
      },
      () => {
        done()
      }
    )
  })
})
