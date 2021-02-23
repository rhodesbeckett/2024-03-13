<template>
    <section class="section">
        <div class="container">
          <nav class="navbar navbar--routing" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
                <a class="navbar-item" href="/">
                  <img src="@/assets/pyfootball.png" width="112" height="28">
                </a>
            
                <a role="button" class="navbar-burger" @click="toggleHamburger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                  <span aria-hidden="true"></span>
                  <span aria-hidden="true"></span>
                  <span aria-hidden="true"></span>
                </a>
            </div>

            <div class="navbar-menu" ref="navbarMenu">
                <div class="navbar-start">
                  <!-- navbar items -->
                </div>
              
                <div class="navbar-end">
                  <div class="navbar-item">
                    <router-link to="/matchCompInfo" class="button">
                        <span class="icon">
                            <i class="fas fa-info-circle" aria-hidden="true"></i>
                        </span>
                        <span>Match information</span>
                    </router-link>
                  </div>
                  <div class="navbar-item">
                    <router-link to="/editor" class="button">
                        <span class="icon">
                            <i class="fas fa-chalkboard-teacher" aria-hidden="true"></i>
                        </span>
                        <span>Highlights</span>
                    </router-link>
                  </div>
                  <div class="navbar-item">
                    <router-link to="/testing" class="button">
                        <span class="icon">
                            <i class="fas fa-border-style" aria-hidden="true"></i>
                        </span>
                        <span>Testing</span>
                    </router-link>
                  </div>
                  <div class="navbar-item">
                    <router-link to="/cut-and-render" class="button">
                        <span class="icon">
                            <i class="fas fa-video" aria-hidden="true"></i>
                        </span>
                        <span>Cut and render</span>
                    </router-link>
                  </div>
                </div>
            </div>
          </nav>
          <transition
            name="zoom"
            mode="out-in">
              <router-view/>
          </transition>
      </div>
  </section>
</template>

<script>
export default {
  methods: {
    toggleHamburger() {
      this.$refs.navbarMenu.classList.toggle('visible-hamburger')
    }
  }
}
</script>

<style>
@import "./assets/bulma.min.css";
@import "./assets/main.css";

.visible-hamburger {
  display: initial;
}

.zoom-enter-active,

.zoom-leave-active {
  animation-duration: 0.3s;
  animation-fill-mode: both;
  animation-name: zoom;
}

.zoom-leave-active {
  animation-direction: reverse;
}

@keyframes zoom {

  from {
    opacity: 0;
    transform: scale3d(0.4, 0.4, 0.4);
}
100% {
    opacity: 1;
  }
}


</style>
