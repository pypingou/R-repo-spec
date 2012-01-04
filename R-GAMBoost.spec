%global packname  GAMBoost
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Generalized linear and additive models by likelihood based boosting

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
This package provides routines for fitting generalized linear and and
generalized additive models by likelihood based boosting, using penalized

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
%doc %{rlibdir}/GAMBoost/html
%doc %{rlibdir}/GAMBoost/DESCRIPTION
%doc %{rlibdir}/GAMBoost/CITATION
%{rlibdir}/GAMBoost/libs
%{rlibdir}/GAMBoost/Meta
%{rlibdir}/GAMBoost/R
%{rlibdir}/GAMBoost/NAMESPACE
%{rlibdir}/GAMBoost/help
%{rlibdir}/GAMBoost/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora