#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Syntax extension for writing in-line tests in OCaml code
Summary(pl.UTF-8):	Rozszerzenie składni do pisania testów wewnątrz kodu w OCamlu
Name:		ocaml-ppx_inline_test
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_inline_test/tags
Source0:	https://github.com/janestreet/ppx_inline_test/archive/v%{version}/ppx_inline_test-%{version}.tar.gz
# Source0-md5:	132754f0757188c3b700a2c5b6a2fb3f
URL:		https://github.com/janestreet/ppx_inline_test
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.14.0
BuildRequires:	ocaml-time_now-devel >= 0.14
BuildRequires:	ocaml-time_now-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Syntax extension for writing in-line tests in OCaml code.

This package contains files needed to run bytecode executables using
ppx_inline_test library.

%description -l pl.UTF-8
Rozszerzenie składni do pisania testów wewnątrz kodu w OCamlu.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_inline_test.

%package devel
Summary:	Syntax extension for writing in-line tests in OCaml code - development part
Summary(pl.UTF-8):	Rozszerzenie składni do pisania testów wewnątrz kodu w OCamlu - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.14.0
Requires:	ocaml-time_now-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_inline_test library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_inline_test.

%prep
%setup -q -n ppx_inline_test-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_inline_test/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_inline_test/*/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_inline_test/*/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_inline_test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_inline_test
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/ppx.exe
%{_libdir}/ocaml/ppx_inline_test/META
%{_libdir}/ocaml/ppx_inline_test/*.cma
%dir %{_libdir}/ocaml/ppx_inline_test/config
%{_libdir}/ocaml/ppx_inline_test/config/*.cma
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/drop/ppx.exe
%dir %{_libdir}/ocaml/ppx_inline_test/drop
%{_libdir}/ocaml/ppx_inline_test/drop/*.cma
%dir %{_libdir}/ocaml/ppx_inline_test/libname
%{_libdir}/ocaml/ppx_inline_test/libname/*.cma
%dir %{_libdir}/ocaml/ppx_inline_test/runner
%{_libdir}/ocaml/ppx_inline_test/runner/*.cma
%dir %{_libdir}/ocaml/ppx_inline_test/runner/lib
%{_libdir}/ocaml/ppx_inline_test/runner/lib/runtime.js
%{_libdir}/ocaml/ppx_inline_test/runner/lib/*.cma
%dir %{_libdir}/ocaml/ppx_inline_test/runtime-lib
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/config/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/drop/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/libname/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/runner/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/runner/lib/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllppx_inline_test_runner_lib_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_inline_test/*.cmi
%{_libdir}/ocaml/ppx_inline_test/*.cmt
%{_libdir}/ocaml/ppx_inline_test/*.cmti
%{_libdir}/ocaml/ppx_inline_test/*.mli
%{_libdir}/ocaml/ppx_inline_test/config/*.cmi
%{_libdir}/ocaml/ppx_inline_test/config/*.cmt
%{_libdir}/ocaml/ppx_inline_test/config/*.cmti
%{_libdir}/ocaml/ppx_inline_test/config/*.mli
%{_libdir}/ocaml/ppx_inline_test/drop/*.cmi
%{_libdir}/ocaml/ppx_inline_test/drop/*.cmt
%{_libdir}/ocaml/ppx_inline_test/libname/*.cmi
%{_libdir}/ocaml/ppx_inline_test/libname/*.cmt
%{_libdir}/ocaml/ppx_inline_test/libname/*.cmti
%{_libdir}/ocaml/ppx_inline_test/libname/*.mli
%{_libdir}/ocaml/ppx_inline_test/runner/*.cmi
%{_libdir}/ocaml/ppx_inline_test/runner/*.cmt
%{_libdir}/ocaml/ppx_inline_test/runner/lib/libppx_inline_test_runner_lib_stubs.a
%{_libdir}/ocaml/ppx_inline_test/runner/lib/*.cmi
%{_libdir}/ocaml/ppx_inline_test/runner/lib/*.cmt
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cmt
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cmti
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_inline_test/ppx_inline_test.a
%{_libdir}/ocaml/ppx_inline_test/*.cmx
%{_libdir}/ocaml/ppx_inline_test/*.cmxa
%{_libdir}/ocaml/ppx_inline_test/config/inline_test_config.a
%{_libdir}/ocaml/ppx_inline_test/config/*.cmx
%{_libdir}/ocaml/ppx_inline_test/config/*.cmxa
%{_libdir}/ocaml/ppx_inline_test/drop/ppx_inline_test_drop.a
%{_libdir}/ocaml/ppx_inline_test/drop/*.cmx
%{_libdir}/ocaml/ppx_inline_test/drop/*.cmxa
%{_libdir}/ocaml/ppx_inline_test/libname/ppx_inline_test_libname.a
%{_libdir}/ocaml/ppx_inline_test/libname/*.cmx
%{_libdir}/ocaml/ppx_inline_test/libname/*.cmxa
%{_libdir}/ocaml/ppx_inline_test/runner/ppx_inline_test_runner.a
%{_libdir}/ocaml/ppx_inline_test/runner/*.cmx
%{_libdir}/ocaml/ppx_inline_test/runner/*.cmxa
%{_libdir}/ocaml/ppx_inline_test/runner/lib/ppx_inline_test_runner_lib.a
%{_libdir}/ocaml/ppx_inline_test/runner/lib/*.cmx
%{_libdir}/ocaml/ppx_inline_test/runner/lib/*.cmxa
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/ppx_inline_test_lib.a
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_inline_test/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_inline_test/dune-package
%{_libdir}/ocaml/ppx_inline_test/opam
%{_examplesdir}/%{name}-%{version}
