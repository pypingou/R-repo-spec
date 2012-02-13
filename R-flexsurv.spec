%global packname  flexsurv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{dist}
Summary:          Flexible parametric survival models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival R-muhaz 

BuildRequires:    R-devel tex(latex) R-survival R-muhaz 

%description
Flexible parametric models for time-to-event data, including the
Royston-Parmar spline model, generalized gamma and generalized F
distributions.  Easily extensible to fit user-defined parametric

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
%doc %{rlibdir}/flexsurv/html
%doc %{rlibdir}/flexsurv/NEWS
%doc %{rlibdir}/flexsurv/DESCRIPTION
%{rlibdir}/flexsurv/data
%{rlibdir}/flexsurv/R
%{rlibdir}/flexsurv/Meta
%{rlibdir}/flexsurv/NAMESPACE
%{rlibdir}/flexsurv/help
%{rlibdir}/flexsurv/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- Update to version 0.1.3

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora