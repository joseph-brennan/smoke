<template>
  <div id = "editor">
    <div class="dropdown is-active">
      <div class="dropdown-trigger">
        <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
          <span>Editor Mode</span>
          <span class="icon is-small">
        <i class="fas fa-angle-down" aria-hidden="true"></i>
      </span>
        </button>
      </div>
      <div class="dropdown-menu" id="dropdown-menu" role="menu">
        <div class="dropdown-content">
          <a href="#" class="dropdown-item">
            Python 2
          </a>
          <a class="dropdown-item">
            Python 3
          </a>
          <a href="#" class="dropdown-item">
            Ruby
          </a>
          <a href="#" class="dropdown-item">
            Javascript
          </a>
        </div>
      </div>
    </div>
  <div>
    <brace style="height: 500px"
      :fontsize="'12px'"
      :theme="'github'"
      :mode="'python'"
      :codefolding="'markbegin'"
      :softwrap="'free'"
      :selectionstyle="'text'"
      :highlightline="true">
    </brace>
  </div>
  </div>
</template>

<script>
import Brace from 'vue-bulma-brace'

export default {
  components: {
    Brace
  },
  methods: {
    myFunction: function () {
      document.getElementById('myDropdown').classList.toggle('show')
    }
  }
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName('dropdown-content')
    var i
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i]
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show')
      }
    }
  }
}
</script>
