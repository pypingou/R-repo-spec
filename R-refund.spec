%global packname  refund
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Regression with Functional Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mgcv R-fda 

BuildRequires:    R-devel tex(latex) R-mgcv R-fda 

%description
Functions for regression with functional data.  The principal methods
currently implemented regress (i) scalar responses on functional
predictors; (ii) functional responses on scalar predictors; and (iii)
functional responses on functional predictors.

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
%doc %{rlibdir}/refund/html
%doc %{rlibdir}/refund/DESCRIPTION
%{rlibdir}/refund/data
%{rlibdir}/refund/NAMESPACE
%{rlibdir}/refund/Meta
%{rlibdir}/refund/help
%{rlibdir}/refund/INDEX
%{rlibdir}/refund/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora