%global packname  scaRabee
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Optimization Toolkit for Pharmacokinetic-Pharmacodynamic Models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-neldermead R-optimsimplex R-optimbase R-lattice R-grid R-deSolve R-PBSddesolve R-utils 


BuildRequires:    R-devel tex(latex) R-neldermead R-optimsimplex R-optimbase R-lattice R-grid R-deSolve R-PBSddesolve R-utils



%description
scaRabee is a port of the Scarabee toolkit originally written as a
Matlab-based application. It provides a framework for simulation and
optimization of pharmacokinetic-pharmacodynamic models at the individual
and population level. It is built on top of the neldermead package, which
provides the direct search algorithm proposed by Nelder and Mead for model

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora