%global packname  mkin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.11
Release:          1%{?dist}
Summary:          Routines for fitting kinetic models with one or more state variables to chemical degradation data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-FME R-deSolve R-kinfit 


BuildRequires:    R-devel tex(latex) R-FME R-deSolve R-kinfit



%description
Calculation routines based on the FOCUS Kinetics Report (2006).  Includes
a function for conveniently defining differential equation models, model
solution based on eigenvalues if possible or using numerical solvers and a
choice of the optimisation methods made available by the FME package
(default is a Levenberg-Marquardt variant).  Please note that no warranty
is implied for correctness of results or fitness for a particular purpose.

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
%doc %{rlibdir}/mkin/doc
%doc %{rlibdir}/mkin/html
%doc %{rlibdir}/mkin/DESCRIPTION
%{rlibdir}/mkin/data
%{rlibdir}/mkin/NAMESPACE
%{rlibdir}/mkin/INDEX
%{rlibdir}/mkin/help
%{rlibdir}/mkin/GUI
%{rlibdir}/mkin/Meta
%{rlibdir}/mkin/unitTests
%{rlibdir}/mkin/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.11-1
- initial package for Fedora