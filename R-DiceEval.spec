%global packname  DiceEval
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Construction and evaluation of metamodels

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DiceKriging 

BuildRequires:    R-devel tex(latex) R-DiceKriging 

%description
Estimation, validation and prediction of metamodels (linear models,
additive models, MARS,PolyMARS and Kriging)

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
%doc %{rlibdir}/DiceEval/html
%doc %{rlibdir}/DiceEval/DESCRIPTION
%{rlibdir}/DiceEval/INDEX
%{rlibdir}/DiceEval/data
%{rlibdir}/DiceEval/NAMESPACE
%{rlibdir}/DiceEval/help
%{rlibdir}/DiceEval/R
%{rlibdir}/DiceEval/Meta
%{rlibdir}/DiceEval/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora