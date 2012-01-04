%global packname  Sim.DiffProc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Simulation of Diffusion Processes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-tcltk2 R-stats4 R-rgl R-xlsx 


BuildRequires:    R-devel tex(latex) R-tcltk R-tcltk2 R-stats4 R-rgl R-xlsx



%description
Simulation of diffusion processes and numerical solution of stochastic
differential equations. Analysis of discrete-time approximations for
stochastic differential equations (SDE) driven by Wiener processes,in
financial and actuarial modeling and other areas of application for
example modelling and simulation of dispersion in shallow water using the
attractive center (K.BOUKHETALA, 1996). Approximated the evolution of
conditional law a diffusion process with three methods Euler, Kessler and
Shoji-Ozaki. Simulation and statistical analysis of the first passage time
(FPT) and M-samples of the random variable X(v) given by a simulated
diffusion process.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora