import Editor from '@/components/Editor'
import { mount } from './utils'

describe('Editor.vue', () => {
  it('should set editorCodeString to null', () => {
    const vm = mount(Editor)
    expect(vm.$data.editorCodeString).to.equal(null)
  })

  it('should set editorCodeString when editorCodeChanged is called', () => {
    const vm = mount(Editor)
    vm.editorCodeChanged('some clever code')
    expect(vm.$data.editorCodeString).to.equal('some clever code')
  })
})
