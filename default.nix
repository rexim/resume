with import <nixpkgs> {}; {
  resumeEnv = stdenv.mkDerivation {
    name = "resume";
    buildInputs = [ stdenv python27Full python27Packages.virtualenv texLiveFull ];
    shellHook = ''
      if [ ! -d venv ]; then
        virtualenv --python=python2.7 venv
        ./venv/bin/pip install -r requirements.txt
      fi
    '';
  };
}
