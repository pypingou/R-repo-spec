%global packname  DiceKriging
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Kriging methods for computer experiments

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Estimation, validation and prediction of kriging models. Important
functions : km, print.km, plot.km, predict.km.

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
%doc %{rlibdir}/DiceKriging/DESCRIPTION
%doc %{rlibdir}/DiceKriging/html
%{rlibdir}/DiceKriging/R
%{rlibdir}/DiceKriging/Meta
%{rlibdir}/DiceKriging/libs
%{rlibdir}/DiceKriging/NAMESPACE
%{rlibdir}/DiceKriging/INDEX
%{rlibdir}/DiceKriging/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora