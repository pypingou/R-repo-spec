%global packname  PKfit
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          A Data Analysis Tool for Pharmacokinetics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats4 R-odesolve R-rgenoud 

BuildRequires:    R-devel tex(latex) R-stats4 R-odesolve R-rgenoud 

%description
PKfit is a nonlinear regression (including a genetic algorithm) program
which was designed to perform model/curve fitting and model simulations
for pharmacokinetics.

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
%doc %{rlibdir}/PKfit/DESCRIPTION
%doc %{rlibdir}/PKfit/html
%{rlibdir}/PKfit/Meta
%{rlibdir}/PKfit/help
%{rlibdir}/PKfit/INDEX
%{rlibdir}/PKfit/R
%{rlibdir}/PKfit/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8-1
- initial package for Fedora