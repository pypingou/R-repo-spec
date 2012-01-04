%global packname  saws
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.3.3
Release:          1%{?dist}
Summary:          Small-Sample Adjustments for Wald tests Using Sandwich Estimators

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gee R-survival R-stats 

BuildRequires:    R-devel tex(latex) R-gee R-survival R-stats 

%description
Tests coefficients with sandwich estimator of variance and with small
samples. Regression types supported are gee, cox regression, and
conditional logistic regression.

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
%doc %{rlibdir}/saws/CITATION
%doc %{rlibdir}/saws/doc
%doc %{rlibdir}/saws/html
%doc %{rlibdir}/saws/NEWS
%doc %{rlibdir}/saws/DESCRIPTION
%{rlibdir}/saws/Meta
%{rlibdir}/saws/data
%{rlibdir}/saws/R
%{rlibdir}/saws/NAMESPACE
%{rlibdir}/saws/help
%{rlibdir}/saws/INDEX
%{rlibdir}/saws/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3.3-1
- initial package for Fedora