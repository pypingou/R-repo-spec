%global packname  car
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.11
Release:          1%{?dist}
Summary:          Companion to Applied Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-graphics R-MASS R-nnet R-survival 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-MASS R-nnet R-survival 

%description
This package accompanies J. Fox and S. Weisberg, An R Companion to Applied
Regression, Second Edition, Sage, 2011.

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
%doc %{rlibdir}/car/DESCRIPTION
%doc %{rlibdir}/car/CITATION
%doc %{rlibdir}/car/NEWS
%doc %{rlibdir}/car/html
%{rlibdir}/car/NAMESPACE
%{rlibdir}/car/Meta
%{rlibdir}/car/R
%{rlibdir}/car/help
%{rlibdir}/car/INDEX
%{rlibdir}/car/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.11-1
- initial package for Fedora